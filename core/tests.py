from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import About, Project, Skill, SkillCategory
from django.core.files.uploadedfile import SimpleUploadedFile

class PortfolioAPITests(TestCase):
    def setUp(self):
        # Create a test image file
        self.test_image = SimpleUploadedFile(
            name='test_image.jpg',
            content=b'',  # empty image for testing
            content_type='image/jpeg'
        )
        
        # Create test data
        self.about = About.objects.create(
            title="Test About",
            description="Test Description",
            image=self.test_image
        )
        
        self.category = SkillCategory.objects.create(
            name="Test Category"
        )
        
        self.skill = Skill.objects.create(
            name="Test Skill",
            percentage=85,
            category=self.category
        )

    def tearDown(self):
        # Clean up uploaded files after tests
        self.about.image.delete()
        About.objects.all().delete()
        SkillCategory.objects.all().delete()
        Skill.objects.all().delete()

    def test_portfolio_data_endpoint(self):
        response = self.client.get(reverse('portfolio-data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('about', response.data)
        self.assertIn('projects', response.data)
        self.assertIn('skill_categories', response.data)

    def test_about_endpoint(self):
        response = self.client.get(reverse('about-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test About")

    def test_skills_with_category(self):
        response = self.client.get(reverse('skillcategory-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Test Category")
        self.assertEqual(len(response.data[0]['skills']), 1)
