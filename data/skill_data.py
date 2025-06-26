
# data/skill_data.py
# Synthetic data for skills and learning resources
import pandas as pd

SKILL_CATEGORIES = {
    "Python Programming": "general",
    "Data Analysis (SQL, Pandas)": "general",
    "Machine Learning Concepts": "general",
    "Cloud Computing (AWS/Azure/GCP)": "general",
    "Project Management": "general",
    "Communication Skills": "general",
    "Critical Thinking": "general",
    "Proprietary CRM Software (Salesforce)": "firm-specific",
    "Internal HR System (Workday)": "firm-specific",
    "Company-specific Financial Modeling": "firm-specific",
    "Niche Industry Regulations": "firm-specific",
    "Legacy System Maintenance": "firm-specific",
    "Microsoft Office Suite (Advanced)": "general",
    "Generative AI Tools (e.g., ChatGPT, Midjourney)": "general",
    "Blockchain Fundamentals": "general",
    "Agile Methodologies": "general",
    "Cybersecurity Best Practices": "general",
    "Firm-specific Compliance Procedures": "firm-specific",
    "Supply Chain Optimization (Custom Software)": "firm-specific",
    "Brand-specific Marketing Strategy": "firm-specific",
    "Ethical AI Principles": "general"
}

LEARNING_RESOURCES = pd.DataFrame([
    {"Skill": "Python Programming", "Type": "general", "Course Name": "Python for Everybody", "Platform": "Coursera", "Link": "https://www.coursera.org/specializations/python"},
    {"Skill": "Data Analysis (SQL, Pandas)", "Type": "general", "Course Name": "Data Analyst Professional Certificate", "Platform": "Google (Coursera)", "Link": "https://www.coursera.org/professional-certificates/google-data-analytics"},
    {"Skill": "Machine Learning Concepts", "Type": "general", "Course Name": "Machine Learning by Andrew Ng", "Platform": "Coursera", "Link": "https://www.coursera.org/learn/machine-learning"},
    {"Skill": "Cloud Computing (AWS/Azure/GCP)", "Type": "general", "Course Name": "AWS Certified Cloud Practitioner", "Platform": "Udemy", "Link": "https://www.udemy.com/course/aws-certified-cloud-practitioner-clf-c01/"},
    {"Skill": "Project Management", "Type": "general", "Course Name": "PMP Certification Training", "Platform": "Project Management Institute", "Link": "https://www.pmi.org/certifications/project-management-pmp"},
    {"Skill": "Proprietary CRM Software (Salesforce)", "Type": "firm-specific", "Course Name": "Salesforce Administrator Certification Prep", "Platform": "Trailhead", "Link": "https://trailhead.salesforce.com/credentials/administratorcredentials"},
    {"Skill": "Internal HR System (Workday)", "Type": "firm-specific", "Course Name": "Workday HCM Training", "Platform": "Workday Learning", "Link": "https://www.workday.com/en-us/customer-experience/learning.html"},
    {"Skill": "Generative AI Tools (e.g., ChatGPT, Midjourney)", "Type": "general", "Course Name": "Generative AI for Beginners", "Platform": "Microsoft Learn", "Link": "https://learn.microsoft.com/en-us/training/paths/generative-ai-basics/"},
    {"Skill": "Ethical AI Principles", "Type": "general", "Course Name": "Responsible AI: Practices and Principles", "Platform": "Google (Coursera)", "Link": "https://www.coursera.org/learn/responsible-ai-practices-principles"},
    {"Skill": "Cybersecurity Best Practices", "Type": "general", "Course Name": "Introduction to Cybersecurity", "Platform": "IBM (Coursera)", "Link": "https://www.coursera.org/learn/introduction-to-cybersecurity-for-everyone"},
    {"Skill": "Agile Methodologies", "Type": "general", "Course Name": "Agile with Atlassian Jira", "Platform": "Atlassian (Coursera)", "Link": "https://www.coursera.org/specializations/agile-jira"}
]).set_index("Skill")
