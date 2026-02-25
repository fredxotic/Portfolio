from django.test import TestCase, Client
from django.urls import reverse
from portfolio.models import Project, Profile, ContactMessage

class PortfolioTests(TestCase):
    def setUp(self):
        # Setup runs before every test. We need some dummy data.
        self.client = Client()
        self.profile = Profile.objects.create(
            name="Test User",
            email="test@example.com",
            bio="Test Bio"
        )
        self.project = Project.objects.create(
            title="Test Project",
            slug="test-project",
            category="Web",
            short_description="Short desc",
            description="Long desc",
            detailed_content="Detailed content here",
            tech_stack="Django, Python",
            project_date="2025",
            featured=True
        )

    def test_homepage_loads(self):
        """Test that the homepage loads with status code 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test User") # Check if profile name renders
        self.assertContains(response, "Test Project") # Check if project renders

    def test_portfolio_detail_loads(self):
        """Test that a specific project page loads"""
        response = self.client.get(reverse('portfolio-details', args=[self.project.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")

    def test_contact_form_valid_submission(self):
        """Test that a valid form submission saves to DB and redirects"""
        form_data = {
            'name': 'Recruiter',
            'email': 'job@company.com',
            'subject': 'Job Offer',
            'message': 'We want to hire you.'
        }
        response = self.client.post(reverse('home'), data=form_data)
        
        # Should redirect after success
        self.assertEqual(response.status_code, 302) 
        
        # Check if it was saved to the database
        self.assertTrue(ContactMessage.objects.filter(email='job@company.com').exists())

    def test_contact_form_invalid_submission(self):
        """Test that an invalid form (missing email) does NOT save"""
        form_data = {
            'name': 'Spammer',
            'message': 'I have no email'
        }
        response = self.client.post(reverse('home'), data=form_data)
        
        # Should return 200 (stay on page to show errors), not redirect
        self.assertEqual(response.status_code, 200)
        self.assertFalse(ContactMessage.objects.filter(name='Spammer').exists())