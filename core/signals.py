from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import About, Project, Skill, Experience
from .utils import compress_image
import os

@receiver(post_save, sender=About)
@receiver(post_save, sender=Project)
@receiver(post_save, sender=Skill)
@receiver(post_save, sender=Experience)
def clear_cache(sender, instance, **kwargs):
    cache.delete('portfolio_data')

@receiver(pre_save, sender=Project)
def compress_project_image(sender, instance, **kwargs):
    if instance.image and hasattr(instance.image, 'file'):
        compressed_image = compress_image(instance.image)
        compressed_image.save(instance.image.path, quality=85, optimize=True)

@receiver(post_delete, sender=Project)
def delete_project_files(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path) 