
import pandas as pd

SKILL_CATEGORIES = {
    "Python": "general",
    "Data Analysis": "general",
    "Machine Learning": "general",
    "Cloud Computing": "general",
    "Project Management": "general",
    "Communication": "general",
    "Problem Solving": "general",
    "Critical Thinking": "general",
    "Proprietary CRM Software": "firm-specific",
    "Internal Compliance Procedures": "firm-specific",
    "Company-specific Financial Models": "firm-specific",
    "Legacy System Maintenance": "firm-specific",
    "Agile Scrum Master": "general", # Added for more general skills
    "SQL": "general", # Added for more general skills
    "Negotiation": "general", # Added for more general skills
    "Advanced Excel": "general", # Added for more general skills
}

LEARNING_RESOURCES = pd.DataFrame([
    {"Skill": "Python", "Type": "general", "Course Name": "Python for Data Science", "Platform": "Coursera", "Link": "https://www.coursera.org/courses?query=python%20for%20data%20science"},
    {"Skill": "Data Analysis", "Type": "general", "Course Name": "Data Analysis with Python", "Platform": "edX", "Link": "https://www.edx.org/learn/data-analysis/data-analysis-with-python"},
    {"Skill": "Machine Learning", "Type": "general", "Course Name": "Machine Learning Specialization", "Platform": "DeepLearning.AI", "Link": "https://www.deeplearning.ai/courses/machine-learning-specialization/"},
    {"Skill": "Cloud Computing", "Type": "general", "Course Name": "AWS Certified Cloud Practitioner", "Platform": "Udemy", "Link": "https://www.udemy.com/courses/aws-certified-cloud-practitioner-clf-c01/"},
    {"Skill": "Project Management", "Type": "general", "Course Name": "Google Project Management", "Platform": "Coursera", "Link": "https://www.coursera.org/professional-certificates/google-project-management"},
    {"Skill": "Proprietary CRM Software", "Type": "firm-specific", "Course Name": "Internal CRM Training Module 1", "Platform": "Internal LMS", "Link": "#"},
    {"Skill": "Internal Compliance Procedures", "Type": "firm-specific", "Course Name": "Compliance 101 for New Hires", "Platform": "Internal LMS", "Link": "#"},
    {"Skill": "Company-specific Financial Models", "Type": "firm-specific", "Course Name": "Advanced Financial Modeling with Acme Corp Data", "Platform": "Internal Training", "Link": "#"},
    {"Skill": "Legacy System Maintenance", "Type": "firm-specific", "Course Name": "Understanding XyZ Legacy System", "Platform": "Internal Wiki", "Link": "#"},
    {"Skill": "Agile Scrum Master", "Type": "general", "Course Name": "Professional Scrum Master I (PSM I)", "Platform": "Scrum.org", "Link": "https://www.scrum.org/courses/professional-scrum-master-i-psm-i"},
    {"Skill": "SQL", "Type": "general", "Course Name": "SQL for Data Science", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/sql-for-data-science"},
    {"Skill": "Negotiation", "Type": "general", "Course Name": "Successful Negotiation: Essential Strategies and Skills", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/negotiation-skills"},
    {"Skill": "Advanced Excel", "Type": "general", "Course Name": "Microsoft Excel - Excel from Beginner to Advanced", "Platform": "Udemy", "Link": "https://www.udemy.com/course/microsoft-excel-excel-from-beginner-to-advanced-p/"},
])
