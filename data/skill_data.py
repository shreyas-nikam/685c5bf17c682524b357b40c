
# data/skill_data.py
import pandas as pd

SKILL_CATEGORIES = {
    "Python Programming": "general",
    "Data Analysis (Pandas, NumPy)": "general",
    "Machine Learning (Scikit-learn, TensorFlow)": "general",
    "Cloud Computing (AWS, Azure, GCP)": "general",
    "SQL Database Management": "general",
    "Communication Skills": "general",
    "Project Management (Agile/Scrum)": "general",
    "Proprietary CRM Software (e.g., Salesforce Customization)": "firm-specific",
    "Internal Financial Reporting Tools": "firm-specific",
    "Company-specific HRIS": "firm-specific",
    "Niche Industry Regulations Compliance": "firm-specific",
    "Advanced Excel Modeling": "general",
    "Cybersecurity Best Practices": "general",
    "Network Administration": "general",
    "Digital Marketing Analytics": "general",
    "Content Creation (e.g., Adobe Creative Suite)": "general",
    "Legal Research (LexisNexis, Westlaw)": "firm-specific",
    "Medical Billing Software": "firm-specific",
    "CAD Software (e.g., AutoCAD, SolidWorks)": "general",
    "Supply Chain Optimization (SAP)": "firm-specific",
}

# This DataFrame will be used for personalized resource recommendations
LEARNING_RESOURCES = pd.DataFrame([
    {"Skill": "Python Programming", "Type": "general", "Course Name": "Python for Everybody", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/python"},
    {"Skill": "Data Analysis (Pandas, NumPy)", "Type": "general", "Course Name": "Data Analysis with Python", "Platform": "edX", "Link": "https://www.edx.org/learn/data-analysis/ibm-data-analysis-with-python"},
    {"Skill": "Machine Learning (Scikit-learn, TensorFlow)", "Type": "general", "Course Name": "Machine Learning Specialization", "Platform": "Coursera", "Link": "https://www.coursera.org/specializations/machine-learning-introduction"},
    {"Skill": "Cloud Computing (AWS, Azure, GCP)", "Type": "general", "Course Name": "AWS Certified Cloud Practitioner", "Platform": "Udemy", "Link": "https://www.udemy.com/course/aws-certified-cloud-practitioner-clf-c01/"},
    {"Skill": "SQL Database Management", "Type": "general", "Course Name": "SQL for Data Science", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/sql-for-data-science"},
    {"Skill": "Communication Skills", "Type": "general", "Course Name": "Dynamic Public Speaking", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/public-speaking"},
    {"Skill": "Project Management (Agile/Scrum)", "Type": "general", "Course Name": "Agile Project Management", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/agile-project-management"},
    {"Skill": "Proprietary CRM Software (e.g., Salesforce Customization)", "Type": "firm-specific", "Course Name": "Salesforce Admin Beginner Trail", "Platform": "Salesforce Trailhead", "Link": "https://trailhead.salesforce.com/content/learn/trails/administrator-beginner"},
    {"Skill": "Internal Financial Reporting Tools", "Type": "firm-specific", "Course Name": "Internal Tools Training", "Platform": "Company LMS", "Link": "#"},
    {"Skill": "Company-specific HRIS", "Type": "firm-specific", "Course Name": "HRIS System Mastery", "Platform": "Company Intranet", "Link": "#"},
    {"Skill": "Niche Industry Regulations Compliance", "Type": "firm-specific", "Course Name": "Compliance Training 2024", "Platform": "Industry Association", "Link": "#"},
    {"Skill": "Advanced Excel Modeling", "Type": "general", "Course Name": "Excel Skills for Business: Advanced", "Platform": "Coursera", "Link": "https://www.coursera.org/specializations/excel-skills-for-business-advanced"},
    {"Skill": "Cybersecurity Best Practices", "Type": "general", "Course Name": "Introduction to Cybersecurity", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/introduction-to-cybersecurity-for-business"},
    {"Skill": "Network Administration", "Type": "general", "Course Name": "Cisco CCNA Training", "Platform": "Udemy", "Link": "https://www.udemy.com/course/cisco-ccna-200-301-complete/"},
    {"Skill": "Digital Marketing Analytics", "Type": "general", "Course Name": "Google Analytics Certification", "Platform": "Google Skillshop", "Link": "https://skillshop.withgoogle.com/certification/google-analytics-individual-qualification"},
    {"Skill": "Content Creation (e.g., Adobe Creative Suite)", "Type": "general", "Course Name": "Adobe Creative Cloud Masterclass", "Platform": "Domestika", "Link": "https://www.domestika.org/en/courses/2873-adobe-creative-cloud-masterclass"},
    {"Skill": "Legal Research (LexisNexis, Westlaw)", "Type": "firm-specific", "Course Name": "Legal Research Training", "Platform": "LexisNexis/Westlaw", "Link": "#"},
    {"Skill": "Medical Billing Software", "Type": "firm-specific", "Course Name": "Medical Billing and Coding Certification", "Platform": "AHIMA", "Link": "#"},
    {"Skill": "CAD Software (e.g., AutoCAD, SolidWorks)", "Type": "general", "Course Name": "AutoCAD 2024 Essential Training", "Platform": "LinkedIn Learning", "Link": "https://www.linkedin.com/learning/autocad-2024-essential-training"},
    {"Skill": "Supply Chain Optimization (SAP)", "Type": "firm-specific", "Course Name": "SAP S/4HANA Supply Chain Management", "Platform": "SAP Learning Hub", "Link": "#"},
])

# Define recommended skills for different occupations
OCCUPATION_RECOMMENDED_SKILLS = {
    "Software Engineer": {
        "general": ["Python Programming", "Machine Learning (Scikit-learn, TensorFlow)", "Cloud Computing (AWS, Azure, GCP)", "SQL Database Management", "Project Management (Agile/Scrum)"],
        "firm-specific": ["Proprietary CRM Software (e.g., Salesforce Customization)", "Internal Financial Reporting Tools"]
    },
    "Data Scientist": {
        "general": ["Python Programming", "Data Analysis (Pandas, NumPy)", "Machine Learning (Scikit-learn, TensorFlow)", "Cloud Computing (AWS, Azure, GCP)", "SQL Database Management"],
        "firm-specific": ["Internal Financial Reporting Tools", "Niche Industry Regulations Compliance"]
    },
    "Financial Analyst": {
        "general": ["Advanced Excel Modeling", "Data Analysis (Pandas, NumPy)", "SQL Database Management", "Communication Skills"],
        "firm-specific": ["Internal Financial Reporting Tools", "Niche Industry Regulations Compliance"]
    },
    "Accountant": {
        "general": ["Advanced Excel Modeling", "Cybersecurity Best Practices"],
        "firm-specific": ["Internal Financial Reporting Tools", "Company-specific HRIS"]
    },
    "Customer Service Representative": {
        "general": ["Communication Skills", "Cybersecurity Best Practices"],
        "firm-specific": ["Proprietary CRM Software (e.g., Salesforce Customization)", "Company-specific HRIS"]
    },
    "Paralegal": {
        "general": ["Communication Skills", "Advanced Excel Modeling"],
        "firm-specific": ["Legal Research (LexisNexis, Westlaw)", "Niche Industry Regulations Compliance"]
    },
    "Marketing Specialist": {
        "general": ["Digital Marketing Analytics", "Content Creation (e.g., Adobe Creative Suite)"],
        "firm-specific": ["Proprietary CRM Software (e.g., Salesforce Customization)"]
    },
    "Manufacturing Worker": {
        "general": ["Advanced Excel Modeling", "Cybersecurity Best Practices"],
        "firm-specific": ["Supply Chain Optimization (SAP)", "Internal Financial Reporting Tools"]
    }
}

