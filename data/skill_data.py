
import pandas as pd

# Synthetic data for skills and learning resources

SKILL_CATEGORIES = {
    "Python": "general",
    "Data Analysis": "general",
    "Machine Learning": "general",
    "Cloud Computing (AWS/Azure)": "general",
    "Project Management (Agile/Scrum)": "general",
    "Financial Modeling": "general",
    "Digital Marketing": "general",
    "Proprietary CRM Software": "firm-specific",
    "Internal Compliance Procedures": "firm-specific",
    "Company-specific HR Software": "firm-specific",
    "Legacy System Maintenance": "firm-specific",
    "Legal Case Management Software": "firm-specific",
    "Specific Accounting Standards (Internal)": "firm-specific",
}

LEARNING_RESOURCES = pd.DataFrame([
    {"Skill": "Python", "Type": "general", "Course Name": "Python for Data Science", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/python-data-science"},
    {"Skill": "Data Analysis", "Type": "general", "Course Name": "Data Analysis with Python", "Platform": "edX", "Link": "https://www.edx.org/course/data-analysis-with-python"},
    {"Skill": "Machine Learning", "Type": "general", "Course Name": "Machine Learning Specialization", "Platform": "Coursera", "Link": "https://www.coursera.org/specializations/machine-learning-engineering-for-production-mlops"},
    {"Skill": "Cloud Computing (AWS/Azure)", "Type": "general", "Course Name": "AWS Certified Cloud Practitioner", "Platform": "Udemy", "Link": "https://www.udemy.com/course/aws-certified-cloud-practitioner-clf-c01/"},
    {"Skill": "Project Management (Agile/Scrum)", "Type": "general", "Course Name": "Agile Project Management", "Platform": "LinkedIn Learning", "Link": "https://www.linkedin.com/learning/agile-project-management-19760751"},
    {"Skill": "Financial Modeling", "Type": "general", "Course Name": "Financial Modeling & Valuation Analyst", "Platform": "CFI", "Link": "https://corporatefinanceinstitute.com/certifications/fmva/"},
    {"Skill": "Digital Marketing", "Type": "general", "Course Name": "Google Digital Marketing & E-commerce Certificate", "Platform": "Coursera", "Link": "https://www.coursera.org/professional-certificates/google-digital-marketing-ecommerce"},
    {"Skill": "Proprietary CRM Software", "Type": "firm-specific", "Course Name": "Internal CRM Training Module", "Platform": "Company LMS", "Link": "#"},
    {"Skill": "Internal Compliance Procedures", "Type": "firm-specific", "Course Name": "Annual Compliance Refresher", "Platform": "Company LMS", "Link": "#"},
    {"Skill": "Company-specific HR Software", "Type": "firm-specific", "Course Name": "HRIS System Masterclass", "Platform": "Company LMS", "Link": "#"},
    {"Skill": "Legacy System Maintenance", "Type": "firm-specific", "Course Name": "Legacy System Deep Dive", "Platform": "Company Wiki", "Link": "#"},
    {"Skill": "Legal Case Management Software", "Type": "firm-specific", "Course Name": "LegalTech Workflow Mastery", "Platform": "Vendor Portal", "Link": "#"},
    {"Skill": "Specific Accounting Standards (Internal)", "Type": "firm-specific", "Course Name": "Advanced Corporate Accounting", "Platform": "Company Training", "Link": "#"},
])
