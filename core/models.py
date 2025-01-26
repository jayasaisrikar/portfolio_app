from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    resume = models.FileField(upload_to='resume/', blank=True)
    email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    
    def __str__(self):
        return self.title

def project_image_path(instance, filename):
    return f'projects/{filename}'

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to=project_image_path)
    url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_live = models.BooleanField(default=False)
    technologies = models.ManyToManyField('Technology')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='technologies/', blank=True)
    
    class Meta:
        verbose_name_plural = 'Technologies'
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    category = models.ForeignKey(
        'SkillCategory',
        on_delete=models.CASCADE,
        related_name='skills'
    )
    
    def __str__(self):
        return self.name

    def clean(self):
        if self.percentage < 0 or self.percentage > 100:
            raise ValidationError("Percentage must be between 0 and 100")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)  # For FontAwesome icons
    
    class Meta:
        verbose_name_plural = 'Skill categories'
    
    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.position} at {self.company}" 

    def clean(self):
        if self.current and self.end_date:
            raise ValidationError("Current job cannot have an end date")
        if not self.current and not self.end_date:
            raise ValidationError("Past jobs must have an end date")
        if self.end_date and self.start_date and self.end_date < self.start_date:
            raise ValidationError("End date cannot be before start date")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs) 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}" 