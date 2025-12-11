from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, Skill, Education, Certification, Interest,
    Project, ProjectImage, ProjectTag, CareerGoal
)

class Command(BaseCommand):
    help = 'Populate portfolio with my real data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Profile.objects.all().delete()
        Skill.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Interest.objects.all().delete()
        Project.objects.all().delete()
        CareerGoal.objects.all().delete()

        # Create Profile
        self.stdout.write('Creating profile...')
        profile = Profile.objects.create(
            name="Fred Kaloki",
            title="BCom Student, CPA Candidate, Full Stack Developer",
            bio="""I am Fred Kaloki, a Bachelor of Commerce student at Egerton University with a strong passion for merging financial expertise with cutting-edge technology. As a CPA candidate and aspiring full-stack developer, I am dedicated to leveraging analytical skills and innovative solutions to drive business growth and efficiency.

My journey spans accounting, finance, and technology, where I've developed proficiency in Python, Django, data analysis, and web development. I'm committed to continuous learning and applying my knowledge to solve real-world problems through data-driven insights and robust applications.""",
            location="Nairobi, Kenya",
            phone="+254706367840",
            email="charlesfred285@gmail.com",
            github_url="https://github.com/fredxotic",
            linkedin_url="https://linkedin.com/in/fred-kaloki",
            instagram_url="https://instagram.com/xotic.py"
        )
        
        # Create Skills
        self.stdout.write('Creating skills...')
        skills_data = [
            ("Financial Accounting", 85, 1),
            ("Python Programming", 90, 2),
            ("Django Framework", 85, 3),
            ("React & Next.js", 80, 4),
            ("FastAPI & REST APIs", 80, 6),
            ("Data Analysis & AI Integration", 75, 7),
        ]
        
        for name, percentage, order in skills_data:
            Skill.objects.create(name=name, percentage=percentage, order=order)
        
        # Create Education
        self.stdout.write('Creating education...')
        Education.objects.create(
            degree="Bachelor of Commerce (BCom)",
            institution="Egerton University",
            description="Pursuing a comprehensive business education with focus on Accounting, Finance, and Business Management. Developing strong analytical and strategic thinking skills while exploring the intersection of business and technology.",
            start_year=2025,
            is_current=True,
            degree_level="Undergraduate",
            order=1
        )
        
        Education.objects.create(
            degree="Kenya Certificate of Secondary Education (KCSE)",
            institution="Upperhill School",
            description="Completed secondary education with strong performance in Mathematics, Business Studies, and Sciences. Developed foundational analytical and problem-solving skills that form the basis of my current pursuits.",
            start_year=2021,
            end_year=2024,
            is_current=False,
            degree_level="High School",
            order=2
        )
        
        # Create Certifications
        self.stdout.write('Creating certifications...')
        Certification.objects.create(
            title="CPA Part I",
            issuer="KASNEB (Kenya Accountants and Secretaries National Examinations Board)",
            description="Currently undertaking CPA Section 1, covering Financial Accounting, Economics, and Business Law. Building strong foundation in accounting principles and business regulations.",
            is_current=True,
            order=1
        )
        
        Certification.objects.create(
            title="AI for Software Engineering",
            issuer="Power Learn Project (PLP Academy)",
            description="Comprehensive training in Python programming, software engineering principles, and AI fundamentals. Gained hands-on experience in building applications and solving problems with code.",
            is_current=False,
            order=2
        )
        
        Certification.objects.create(
            title="Web Development with Django",
            issuer="EMobilis Technology Institute",
            description="Intensive training in full-stack web development using Django framework. Learned MVT architecture, database design, RESTful APIs, and deployment strategies for production-ready applications.",
            is_current=False,
            order=3
        )
        
        # Create Interests
        self.stdout.write('Creating interests...')
        interests_data = [
            ("AI & Machine Learning", "Building intelligent systems that solve real-world problems using LLMs and data science.", "bi-cpu", 1),
            ("Full Stack Development", "Creating end-to-end web applications with modern frameworks like Django, React, and Next.js.", "bi-code-slash", 2),
            ("Financial Technology", "Exploring how technology transforms financial services and business operations.", "bi-graph-up-arrow", 3),
            ("Social Impact Tech", "Developing solutions that address environmental and social challenges through technology.", "bi-globe", 4),
        ]
        
        for title, desc, icon, order in interests_data:
            Interest.objects.create(title=title, description=desc, icon=icon, order=order)
        
        # Create Career Goals
        self.stdout.write('Creating career goals...')
        CareerGoal.objects.create(
            timeframe='short',
            title='Foundation Building (1-2 Years)',
            goals="""Complete CPA qualification
Master full-stack development (Django, React, Next.js)
Build and deploy 15+ production projects
Contribute to open-source AI/ML projects
Secure software development internship""",
            order=1
        )
        
        CareerGoal.objects.create(
            timeframe='medium',
            title='Professional Growth (3-4 Years)',
            goals="""Position as Full Stack Developer or AI Engineer
Lead development of enterprise-scale applications
Specialize in AI integration and FinTech solutions
Build professional network in tech ecosystem
Pursue advanced certifications (AWS/Azure, ML)""",
            order=2
        )
        
        CareerGoal.objects.create(
            timeframe='long',
            title='Leadership & Innovation (5+ Years)',
            goals="""Technical leadership in innovative tech companies
Develop AI-powered financial solutions at scale
Become recognized expert in AI + Finance intersection
Mentor emerging developers and contribute to tech education
Launch tech venture addressing real-world challenges""",
            order=3
        )
        
        # Create Real Projects
        self.stdout.write('Creating projects...')
        
        # Project 1: PathFinder
        project1 = Project.objects.create(
            title="PathFinder - AI Decision Intelligence Platform",
            slug="pathfinder-ai-decision-platform",
            category="AI",
            short_description="AI-powered decision-making platform that transforms analysis paralysis into confident action using priority-weighted scoring and LLM reasoning.",
            description="""PathFinder is a sophisticated AI platform that revolutionizes how professionals make critical life and career decisions. By combining large language models with structured decision frameworks, it provides quantitative analysis that goes far beyond generic chatbot responses.

Every day, people face decisions that can shape their entire careers - job offers, career transitions, relocation choices. PathFinder transforms this daunting process into a structured, data-driven experience.""",
            detailed_content="""The Problem:
Traditional decision-making tools are either too simplistic (pros/cons lists) or too complex (decision matrices requiring extensive setup). People need intelligent guidance that respects their unique priorities while providing objective analysis.

Technical Architecture:
• Next.js 14 frontend with server-side rendering for optimal performance
• FastAPI backend providing RESTful endpoints for decision processing
• Groq LLM integration for rapid AI inference and reasoning
• Supabase for user authentication and decision history storage
• Real-time streaming responses for enhanced user experience

Core Innovation - Priority Weighting System:
Unlike generic AI assistants, PathFinder implements a mathematical scoring engine:
1. Users define their priorities (Career Growth, Work-Life Balance, Financial Security, etc.)
2. AI evaluates each option against these specific criteria
3. Weighted scores are calculated based on user-defined importance
4. Comprehensive reports include risk assessment and long-term projections

Key Features:
• Intelligent option comparison with quantitative scoring (0-100 scale)
• Priority-based weighting that reflects individual values
• Risk analysis identifying potential challenges for each choice
• Professional PDF report generation for stakeholder communication
• Decision history tracking with revision capabilities
• Mobile-responsive design for on-the-go decision making

Technical Highlights:
• Implemented streaming LLM responses for real-time feedback
• Custom prompt engineering for decision-specific reasoning
• Optimized API architecture handling concurrent decision analyses
• Secure authentication with row-level security in Supabase
• PDF generation with charts and formatted analysis

Impact:
PathFinder has helped users make confident decisions about job offers, career pivots, and life-changing opportunities by providing structured analysis that combines AI intelligence with personal values.

Live Demo: https://pathfinder-eight-sable.vercel.app""",
            tech_stack="Next.js 14, FastAPI, Python, Groq LLM, Supabase, PostgreSQL, TailwindCSS",
            project_date="October 2024",
            live_url="https://pathfinder-eight-sable.vercel.app",
            github_url="https://github.com/fredkaloki/pathfinder",
            featured=True,
            order=1
        )
        ProjectTag.objects.create(project=project1, name="Next.js")
        ProjectTag.objects.create(project=project1, name="FastAPI")
        ProjectTag.objects.create(project=project1, name="AI/LLM")
        ProjectTag.objects.create(project=project1, name="Python")
        ProjectTag.objects.create(project=project1, name="Supabase")
        ProjectTag.objects.create(project=project1, name="TailwindCSS")
        
        # Project 2: ReForester
        project2 = Project.objects.create(
            title="ReForester - AI-Powered Reforestation Intelligence",
            slug="reforester-ai-reforestation",
            category="AI",
            short_description="Comprehensive platform empowering environmental teams to plan and manage reforestation projects worldwide using AI and real-world environmental data.",
            description="""ReForester is an end-to-end solution for ecosystem restoration that combines cutting-edge AI with environmental science. It transforms complex reforestation planning into an intuitive, data-driven process accessible to environmental teams globally.

By integrating real-time soil data, climate information, and AI-powered ecological reasoning, ReForester enables informed decisions about where and how to plant for maximum environmental impact.""",
            detailed_content="""Environmental Challenge:
Reforestation projects often fail due to poor species selection, inadequate site analysis, or lack of long-term planning. Teams need intelligent tools that understand local ecosystems and predict project outcomes.

Technical Architecture:
• React frontend with modular component architecture
• Node.js/Express backend handling complex environmental calculations
• MongoDB for flexible project data and geospatial storage
• Leaflet.js for interactive global mapping capabilities
• Claude AI integration for context-aware ecological reasoning
• External APIs: SoilGrids, OpenWeatherMap for real-world data

Core Features:

1. Interactive Global Analysis:
• Click anywhere on the map to instantly retrieve:
  - Soil composition and pH levels (via SoilGrids API)
  - Climate data including rainfall and temperature patterns
  - Elevation and terrain characteristics
• Real-time data visualization with color-coded indicators

2. AI-Powered Recommendations:
• Claude AI analyzes site-specific conditions
• Generates species recommendations based on:
  - Local ecosystem requirements
  - Soil and climate compatibility
  - Native vs. adaptive species considerations
• Provides planting strategies and maintenance guidelines

3. Project Planning Tools:
• Create detailed reforestation project proposals
• Define project areas, species mix, and planting density
• Set timelines and track implementation milestones
• Collaborative features for team coordination

4. Impact Projections:
• 20-year growth forecasts for carbon sequestration
• Biodiversity impact predictions
• Cost-benefit analysis for different approaches
• Success probability based on historical data

5. Project Management:
• Dashboard for tracking multiple projects
• Progress monitoring with photo documentation
• Team collaboration and task assignment
• Reporting tools for stakeholders

Technical Implementation:
• Implemented GeoJSON for efficient map data handling
• Custom algorithms for carbon calculation based on species and growth rates
• Real-time API integration with error handling and caching
• Responsive design optimized for field use on mobile devices
• RESTful API design for extensibility

Environmental Impact:
ReForester democratizes access to professional-grade reforestation planning tools, enabling organizations of any size to execute scientifically-sound restoration projects.

Live Demo: https://reforester.vercel.app""",
            tech_stack="React, Node.js, Express, MongoDB, Leaflet.js, Claude AI, SoilGrids API, OpenWeatherMap",
            project_date="August - September 2024",
            live_url="https://reforester.vercel.app",
            github_url="https://github.com/fredkaloki/reforester",
            featured=True,
            order=2
        )
        ProjectTag.objects.create(project=project2, name="React")
        ProjectTag.objects.create(project=project2, name="Node.js")
        ProjectTag.objects.create(project=project2, name="MongoDB")
        ProjectTag.objects.create(project=project2, name="AI/LLM")
        ProjectTag.objects.create(project=project2, name="GeoSpatial")
        ProjectTag.objects.create(project=project2, name="Environmental Tech")
        
        # Project 3: FoodLoop
        project3 = Project.objects.create(
            title="FoodLoop - Food Waste & Hunger Solution Platform",
            slug="foodloop-food-sharing-platform",
            category="Web",
            short_description="Community-driven web platform that bridges food donors and recipients, combating both food waste and hunger through smart donation management.",
            description="""FoodLoop addresses the dual crisis of food waste and hunger by creating a seamless ecosystem where surplus food can be easily shared with those in need. This full-stack Django application demonstrates how technology can drive social impact at scale.

The platform features intelligent donation management, real-time tracking, geolocation services, and a trust-building rating system that ensures quality and reliability.""",
            detailed_content="""Social Problem:
Over 1.3 billion tons of food is wasted annually while millions face hunger. The disconnect between those with surplus food and those in need represents both a logistical and social coordination challenge.

Technical Solution - Full Stack Django Application:

Backend Architecture:
• Django MVT (Model-View-Template) framework
• PostgreSQL database with optimized relationships
• Custom user model extending Django AbstractUser
• RESTful API design for mobile-ready architecture
• Celery for asynchronous task processing (notifications)
• Redis for caching and session management

Core Features:

1. Smart Donation Management:
• Create donations with details (quantity, expiry, dietary info)
• Upload photos with automatic image optimization
• Set pickup locations with address autocomplete
• Define availability windows and pickup instructions
• Real-time status updates (Available, Claimed, Completed)

2. Intelligent Discovery:
• Search and filter by location, food type, dietary restrictions
• Interactive map showing nearby donations (Leaflet.js)
• Distance calculation and route planning
• Email/SMS notifications for new donations in user's area
• Favorites and watchlist functionality

3. Trust & Safety System:
• Mutual rating system (donors rate recipients, vice versa)
• Profile verification with photo ID
• Report and flag inappropriate behavior
• Admin moderation dashboard
• History tracking for accountability

4. User Dashboards:
• Donor Dashboard:
  - Track active/completed donations
  - Analytics on food saved and impact
  - Recipient ratings and feedback
• Recipient Dashboard:
  - Claimed donations tracking
  - Pickup reminders and navigation
  - Donation history and statistics

5. Impact Analytics:
• Calculate total food waste prevented (in kg)
• Meals provided to community members
• CO2 emissions saved through waste reduction
• Community leaderboards for motivation

Technical Implementation:

Security & Authentication:
• Django authentication with custom permissions
• Role-based access control (Donor/Recipient/Admin)
• CSRF protection and secure password hashing
• Email verification for account activation

Database Design:
• Optimized models for donations, users, ratings, and messages
• Efficient queries using select_related and prefetch_related
• Database indexing for search performance
• Soft deletes for data integrity

Frontend:
• Bootstrap 5 for responsive design
• Vanilla JavaScript for interactivity
• AJAX for seamless user experience
• Progressive Web App (PWA) capabilities

Deployment:
• Hosted on PythonAnywhere with production settings
• Static files served via WhiteNoise
• Environment variables for sensitive data
• Automated backup system for database

Real-World Impact:
FoodLoop has facilitated thousands of food donations, preventing waste while addressing hunger in local communities. The platform proves that thoughtful technology can drive meaningful social change.

Live Platform: https://foodloop.pythonanywhere.com""",
            tech_stack="Django, Python, PostgreSQL, Bootstrap 5, JavaScript, Leaflet.js, Celery, Redis",
            project_date="August 2024 - Ongoing",
            live_url="https://foodloop.pythonanywhere.com",
            github_url="https://github.com/fredkaloki/foodloop",
            featured=True,
            order=3
        )
        ProjectTag.objects.create(project=project3, name="Django")
        ProjectTag.objects.create(project=project3, name="Python")
        ProjectTag.objects.create(project=project3, name="PostgreSQL")
        ProjectTag.objects.create(project=project3, name="Bootstrap")
        ProjectTag.objects.create(project=project3, name="GeoLocation")
        ProjectTag.objects.create(project=project3, name="Social Impact")
        
        self.stdout.write(self.style.SUCCESS('Successfully populated portfolio with your real projects!'))