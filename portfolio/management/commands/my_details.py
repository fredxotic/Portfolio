from django.core.management.base import BaseCommand
from portfolio.models import (
    Profile, Skill, Education, Certification, Interest,
    Project, ProjectTag, CareerGoal
)

class Command(BaseCommand):
    help = 'Populate portfolio with my real data (BCom student profile)'

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
            title="BCom Student | Aspiring Finance Professional",
            bio="""I am Fred Kaloki, a Bachelor of Commerce student at Egerton University with a focus on Accounting and Finance. I am passionate about using data and technology to enhance financial decision‑making and business efficiency.

My academic training provides a solid foundation in financial accounting, management accounting, and business law. Complementing this, I have pursued practical training in Python, data analysis, and AI literacy—skills I apply to build tools that solve real‑world financial problems. I believe the future of finance lies at the intersection of deep domain knowledge and technological fluency, and I am committed to developing expertise in both.""",
            location="Nairobi, Kenya",
            phone="+254706367840",
            email="charlesfred285@gmail.com",
            github_url="https://github.com/fredxotic",
            linkedin_url="https://linkedin.com/in/fred-kaloki",
            instagram_url="https://instagram.com/xotic.py"
        )
        
        # Create Skills (updated to reflect actual first-year knowledge)
        self.stdout.write('Creating skills...')
        skills_data = [
            ("Financial Accounting", 75, 1),
            ("Financial Analysis", 65, 2),
            ("Microsoft Office Suite", 85, 3),
            ("Python for Data Analysis", 80, 4),
            ("Data Visualization", 70, 5),
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
        
        # Create Certifications (actual completed trainings)
        self.stdout.write('Creating certifications...')
        Certification.objects.create(
            title="AI for Software Engineering",
            issuer="Power Learn Project",
            description="A 16‑week intensive program covering Python programming, web technologies, database management, and software engineering essentials with a specialization in AI for Software Engineering. This training equipped me with practical skills to develop data‑driven applications and leverage AI in business contexts.",
            is_current=False,
            order=1
        )
        
        Certification.objects.create(
            title="Data Science Essentials",
            issuer="Ivy Code Academy",
            description="A 3‑day hands‑on workshop covering core data science concepts: data cleaning, exploratory analysis, basic machine learning, and visualization. The skills gained are directly applicable to financial data analysis and business intelligence.",
            is_current=False,
            order=2
        )
        
        Certification.objects.create(
            title="AI Literacy",
            issuer="Otermans Institute",
            description="A foundational course on artificial intelligence, its applications, and ethical considerations. This certification demonstrates my understanding of how AI can be applied in finance and business to improve decision‑making and efficiency.",
            is_current=False,
            order=3
        )
        
        # Create Interests (more personal and specific)
        self.stdout.write('Creating interests...')
        interests_data = [
            ("Building Financial Tools with Python", 
             "I enjoy creating small applications that automate financial calculations and help make sense of data.", 
             "bi-code-square", 1),
            ("Data‑Driven Investment Analysis", 
             "Exploring how data science can uncover investment opportunities and improve portfolio decisions.", 
             "bi-graph-up", 2),
            ("Tech Solutions for Small Business Accounting", 
             "Passionate about developing simple, affordable tools that help entrepreneurs manage their finances.", 
             "bi-calculator", 3),
            ("AI Applications in Finance", 
             "Fascinated by how artificial intelligence is transforming risk assessment, fraud detection, and financial advisory.", 
             "bi-cpu", 4),
        ]
        
        for title, desc, icon, order in interests_data:
            Interest.objects.create(title=title, description=desc, icon=icon, order=order)
        
        # Create Career Goals (more tailored to your unique path)
        self.stdout.write('Creating career goals...')
        CareerGoal.objects.create(
            timeframe='short',
            title='Foundation Building (1‑2 Years)',
            goals="""Complete second year of BCom with strong grades in Accounting and Finance modules.
Build 3 practical finance‑focused projects (financial statement analyzer, portfolio tool, accounting app) to demonstrate my ability to combine finance and tech.
Secure an internship where I can apply both my accounting knowledge and data analysis skills (in audit, financial analysis, or FinTech).
Deepen proficiency in Python for financial data analysis and explore Power BI or Tableau.""",
            order=1
        )
        
        CareerGoal.objects.create(
            timeframe='medium',
            title='Professional Growth (3‑4 Years)',
            goals="""Graduate with BCom and pursue professional certification (e.g., CPA, CFA) while working in a finance role.
Gain experience in financial analysis, reporting, or audit, using data tools to add value.
Specialize in a niche that blends finance and technology – e.g., financial data analyst, FinTech product analyst.
Build a network of mentors and peers in the finance and tech communities.""",
            order=2
        )
        
        CareerGoal.objects.create(
            timeframe='long',
            title='Leadership & Innovation (5+ Years)',
            goals="""Hold a position where I influence financial strategy using data‑driven insights.
Potentially lead a team or project that develops innovative financial solutions (e.g., a FinTech product for underserved markets).
Mentor students who want to bridge finance and technology.
Continuously learn and adapt as the financial landscape evolves with AI and automation.""",
            order=3
        )
        
        # Create Finance / Accounting Projects (Placeholders - unchanged)
        self.stdout.write('Creating projects...')
        
        # Project 1: FinSight - Financial Statement Analyzer
        project1 = Project.objects.create(
            title="FinSight – Financial Statement Analyzer",
            slug="finsight-financial-statement-analyzer",
            category="Finance",
            short_description="A web application that computes key financial ratios and generates insightful reports from income statements and balance sheets.",
            description="""FinSight helps business owners, students, and analysts quickly interpret financial health. By simply entering or uploading financial data, users receive a comprehensive analysis with liquidity, profitability, and leverage ratios, trend graphs, and a DuPont decomposition.""",
            detailed_content="""The Problem:
Many small business owners and students struggle to interpret raw financial statements. Manual ratio calculation is time‑consuming and error‑prone, and insights often remain buried in spreadsheets.

Technical Solution:
A Django‑based web app that automates ratio analysis and presents results in an intuitive dashboard.

Core Features:
• Input forms for income statement and balance sheet data
• CSV/Excel upload for batch processing
• Automatic calculation of 15+ financial ratios (current ratio, ROE, debt‑to‑equity, etc.)
• Historical comparison with visual trend lines
• DuPont analysis breakdown
• Export professional PDF reports
• User accounts to save and track multiple companies

Tech Stack:
Django, Python (pandas, numpy), Chart.js, Bootstrap 5, PostgreSQL, WeasyPrint for PDF generation.

Impact:
Enables faster, more accurate financial analysis for entrepreneurs and students, bridging the gap between raw data and actionable insights.""",
            tech_stack="Django, Python, pandas, numpy, Chart.js, Bootstrap, PostgreSQL",
            project_date="Planned – March 2026",
            live_url="#",
            github_url="https://github.com/fredkaloki/finsight",
            featured=True,
            order=1
        )
        ProjectTag.objects.create(project=project1, name="Django")
        ProjectTag.objects.create(project=project1, name="Financial Analysis")
        ProjectTag.objects.create(project=project1, name="Python")
        ProjectTag.objects.create(project=project1, name="Data Visualization")
        
        # Project 2: OptiPort - Portfolio Optimization Tool
        project2 = Project.objects.create(
            title="OptiPort – Portfolio Optimization & Backtesting",
            slug="optiport-portfolio-optimization",
            category="Investment",
            short_description="Interactive tool that applies Modern Portfolio Theory to help investors build efficient portfolios and backtest strategies.",
            description="""OptiPort allows users to select stocks, define constraints, and instantly see the optimal asset allocation that maximizes return for a given risk level. The efficient frontier is plotted, and historical backtesting shows how the portfolio would have performed.""",
            detailed_content="""The Problem:
Individual investors often lack access to quantitative tools for portfolio construction. Spreadsheet‑based optimization is complex and prone to error.

Technical Solution:
A web application built with Python and Flask (or Django) that fetches real‑time market data and performs portfolio optimization using scipy.

Core Features:
• Search and select stocks (via Yahoo Finance API)
• Choose date range and optimization objective (max Sharpe, min volatility)
• Generate efficient frontier with interactive Plotly charts
• Display optimal weights and portfolio metrics (expected return, volatility, Sharpe ratio)
• Backtest the optimized portfolio against a benchmark (e.g., S&P 500)
• Download report with weights and performance statistics

Tech Stack:
Python, Flask/Django, pandas, numpy, scipy, yfinance, Plotly, Bootstrap.

Impact:
Democratizes access to quantitative investment tools, enabling informed decision‑making for student investors and DIY portfolio managers.""",
            tech_stack="Python, Flask, pandas, numpy, scipy, yfinance, Plotly, Bootstrap",
            project_date="Planned – April 2026",
            live_url="#",
            github_url="https://github.com/fredkaloki/optiport",
            featured=True,
            order=2
        )
        ProjectTag.objects.create(project=project2, name="Python")
        ProjectTag.objects.create(project=project2, name="Finance")
        ProjectTag.objects.create(project=project2, name="Investment")
        ProjectTag.objects.create(project=project2, name="Data Analysis")
        
        # Project 3: LedgerFlow - Double‑Entry Accounting System
        project3 = Project.objects.create(
            title="LedgerFlow – Double‑Entry Accounting for Small Business",
            slug="ledgerflow-accounting-system",
            category="Accounting",
            short_description="A full‑featured web application that implements double‑entry bookkeeping, enabling small businesses to manage their finances accurately.",
            description="""LedgerFlow provides an intuitive interface for recording journal entries, maintaining ledgers, and generating financial statements. It follows GAAP principles and includes an audit trail.""",
            detailed_content="""The Problem:
Many small businesses rely on spreadsheets that are prone to errors and lack internal controls. Affordable, user‑friendly accounting software is often out of reach.

Technical Solution:
A Django‑based accounting system that enforces double‑entry rules and produces real‑time financial reports.

Core Features:
• Chart of accounts with account types (asset, liability, equity, revenue, expense)
• Journal entry form with automatic debit/credit balancing
• General ledger view with running balances
• Trial balance, income statement, and balance sheet generation
• User roles: admin (full access) vs. accountant (entry only)
• Audit log of all changes
• Export statements to PDF/Excel

Tech Stack:
Django, PostgreSQL, Bootstrap, JavaScript (vanilla), ReportLab for PDF generation.

Impact:
Provides an affordable, transparent accounting solution for micro‑enterprises and serves as a practical learning tool for accounting students to see double‑entry in action.""",
            tech_stack="Django, PostgreSQL, Bootstrap, JavaScript, ReportLab",
            project_date="Planned – May 2026",
            live_url="#",
            github_url="https://github.com/fredkaloki/ledgerflow",
            featured=True,
            order=3
        )
        ProjectTag.objects.create(project=project3, name="Django")
        ProjectTag.objects.create(project=project3, name="Accounting")
        ProjectTag.objects.create(project=project3, name="Python")
        ProjectTag.objects.create(project=project3, name="Business")
        
        self.stdout.write(self.style.SUCCESS('Successfully populated portfolio with BCom‑focused data'))