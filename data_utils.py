
# data_utils.py
import pandas as pd
from data.occupation_data import OCCUPATION_HAZARDS, ROLE_MULTIPLIERS, COMPANY_TYPE_FACTORS
from data.education_data import EDUCATION_LEVEL_FACTORS, EDUCATION_FIELD_FACTORS, SCHOOL_TIER_FACTORS
from data.skill_data import SKILL_CATEGORIES, LEARNING_RESOURCES
from data.environmental_data import ECONOMIC_CLIMATE_SCENARIOS, AI_INNOVATION_SCENARIOS

def get_occupation_hazards():
    return OCCUPATION_HAZARDS

def get_role_modifiers():
    return ROLE_MULTIPLIERS

def get_company_type_factors():
    return COMPANY_TYPE_FACTORS

def get_education_level_factors():
    return EDUCATION_LEVEL_FACTORS

def get_education_field_factors():
    return EDUCATION_FIELD_FACTORS

def get_school_tier_factors():
    return SCHOOL_TIER_FACTORS

def get_skill_categories():
    return SKILL_CATEGORIES

def get_learning_resources():
    return LEARNING_RESOURCES

def get_economic_climate_scenarios():
    return ECONOMIC_CLIMATE_SCENARIOS

def get_ai_innovation_scenarios():
    return AI_INNOVATION_SCENARIOS

def get_all_occupations():
    return sorted(list(OCCUPATION_HAZARDS.keys()))

def get_all_education_levels():
    return sorted(list(EDUCATION_LEVEL_FACTORS.keys()))

def get_all_education_fields():
    return sorted(list(EDUCATION_FIELD_FACTORS.keys()))

def get_all_school_tiers():
    return sorted(list(SCHOOL_TIER_FACTORS.keys()))

def get_all_company_types():
    return sorted(list(COMPANY_TYPE_FACTORS.keys()))

def get_skills_by_type(skill_type: str):
    return [skill for skill, s_type in SKILL_CATEGORIES.items() if s_type == skill_type]

def get_recommended_skills_for_occupation(occupation: str):
    # This is a placeholder for a more sophisticated recommendation engine.
    # For now, it returns a generic list of high-impact skills.
    # In a real application, this would be based on detailed job analysis
    # and AI skill demand.
    if occupation in ["Paralegal", "Legal Assistant", "Data Entry Clerk", "Customer Service Representative", "Accountant", "Librarian", "Retail Sales Associate", "Truck Driver", "Janitor", "Farmer", "Waiter/Waitress", "Medical Assistant", "Medical Secretary", "Administrative Assistant", "Receptionist", "Bookkeeper", "Payroll Clerk", "Librarian Assistant", "Teacher Assistant", "Paraprofessional", "Childcare Worker", "Preschool Teacher", "Kindergarten Teacher", "Elementary School Teacher", "Middle School Teacher", "Proofreader", "Translator (Literary)", "Floral Designer", "Bank Teller", "Travel Agent", "Fisherman", "Sailor", "X-ray Technician", "Phlebotomist", "Medical Biller", "Medical Coder"]:
        general_skills = ["Data Analysis (Pandas/NumPy)", "SQL Database Management", "Microsoft Office Suite", "Communication Skills", "Problem Solving", "Critical Thinking", "Business Acumen", "Cybersecurity Fundamentals"]
        firm_specific_skills = ["Proprietary CRM Software (e.g., Salesforce Customization)", "Internal Data Warehouse Queries (Company X)", "Specific HRIS System (e.g., Workday Configuration)", "Advanced Excel for Financial Reporting (Company Y)"]
    elif occupation in ["Teacher", "Nurse", "Artist", "Writer", "Journalist", "Chef", "Construction Worker", "Electrician", "Plumber", "Biologist", "Chemist", "Geologist", "Sociologist", "Psychologist", "Historian", "Archaeologist", "Anthropologist", "Philosopher", "Linguist", "Interpreter", "Editor", "Graphic Designer", "Project Manager", "Human Resources Manager", "Marketing Specialist", "Financial Advisor", "Auditor", "Tax Accountant", "Police Officer", "Firefighter", "Paramedic", "Social Worker", "Counselor", "Therapist", "Veterinarian", "Pharmacist", "Medical Technologist", "Physical Therapist", "Occupational Therapist", "Speech-Language Pathologist", "Dietitian", "Nutritionist", "Sports Coach", "Fitness Trainer", "Realtor", "Insurance Agent", "Stockbroker", "Loan Officer", "Flight Attendant", "Ship Captain", "Forester", "Wildlife Biologist", "Environmental Scientist", "Urban Planner", "Cartographer", "Geographer", "Meteorologist", "Oceanographer", "Food Scientist", "Agricultural Scientist", "Horticulturist", "Agronomist", "Animal Scientist", "Veterinary Technician", "Dental Hygienist", "Acupuncturist", "Massage Therapist", "Pharmacy Technician", "Surgical Technologist", "Health Information Technician", "Executive Assistant", "Office Manager", "General Manager", "Store Manager", "Retail Manager", "Restaurant Manager", "Hotel Manager", "Event Manager", "Fundraiser", "Non-profit Manager", "Community Organizer", "Pastor", "Religious Worker", "Clergy", "Museum Curator", "Archivist", "Conservator", "High School Teacher", "Research Assistant", "Lab Technician", "Scientific Illustrator", "Technical Writer", "Copywriter", "Photographer", "Videographer", "Sound Engineer", "Actor", "Musician", "Dancer", "Choreographer", "Composer", "Illustrator", "Animator", "Fashion Designer", "Jewelry Designer", "Interior Designer", "Landscape Architect", "Urban Designer", "Software Tester", "Quality Assurance Analyst", "Technical Support Specialist", "Network Administrator", "Business Analyst", "Operations Manager", "Supply Chain Manager", "Logistics Manager", "Procurement Manager", "Sales Manager", "Marketing Manager", "Brand Manager", "Public Relations Specialist", "Claims Adjuster", "Loss Prevention Specialist", "Compliance Officer", "Fraud Investigator", "Arbitrator", "Mediator", "Optometrist", "Chiropractor"]:
        general_skills = ["Python Programming", "Data Analysis (Pandas/NumPy)", "Machine Learning (Scikit-learn/TensorFlow/PyTorch)", "Cloud Computing (AWS/Azure/GCP)", "Project Management (Agile/Scrum)", "Communication Skills", "Critical Thinking", "Problem Solving", "AI Ethics & Governance", "Data Privacy Regulations (GDPR/CCPA)", "Business Acumen", "Financial Modeling", "Statistical Analysis", "Cybersecurity Fundamentals"]
        firm_specific_skills = ["Proprietary CRM Software (e.g., Salesforce Customization)", "Enterprise Resource Planning (ERP) System (e.g., SAP/Oracle Apps)", "Specific Banking Compliance Regulations", "Healthcare EMR System (e.g., Epic/Cerner)"]
    elif occupation in ["Software Engineer", "Data Scientist", "Machine Learning Engineer", "Research Scientist", "Cybersecurity Analyst", "Web Developer", "UX/UI Designer", "Cloud Architect", "DevOps Engineer", "Product Manager", "Scrum Master", "Management Consultant", "Financial Quant", "Actuary", "Investment Banker", "Portfolio Manager", "Risk Manager", "Legal Counsel", "Judge", "Pilot", "Air Traffic Controller", "Biomedical Engineer", "Electrical Engineer", "Mechanical Engineer", "Civil Engineer", "Chemical Engineer", "Aerospace Engineer", "Physicist", "Astronomer", "Geophysicist", "Materials Scientist", "Economist", "Statistician", "Mathematician", "Architect", "Industrial Designer", "Product Designer", "Game Designer", "System Administrator", "Database Administrator", "Cybersecurity Engineer", "Information Security Analyst", "IT Manager", "Business Intelligence Analyst", "Data Analyst", "Operations Research Analyst", "Management Analyst", "Market Research Analyst", "Underwriter"]:
        general_skills = ["Python Programming", "Data Analysis (Pandas/NumPy)", "Machine Learning (Scikit-learn/TensorFlow/PyTorch)", "SQL Database Management", "Cloud Computing (AWS/Azure/GCP)", "Project Management (Agile/Scrum)", "AI Ethics & Governance", "Data Privacy Regulations (GDPR/CCPA)", "Containerization (Docker/Kubernetes)", "DevOps Methodologies", "Natural Language Processing (NLP)", "Computer Vision", "Reinforcement Learning", "Big Data Technologies (Spark/Hadoop)", "Blockchain Fundamentals", "Quantum Computing Concepts", "Robotics", "IoT (Internet of Things)", "Generative AI", "Prompt Engineering", "Large Language Models (LLMs)", "Transformer Models", "Fine-tuning LLMs", "Vector Databases", "RAG (Retrieval-Augmented Generation)", "Autonomous Agents", "Human-in-the-Loop AI", "Reinforcement Learning from Human Feedback (RLHF)", "AI Safety", "AI Alignment", "Existential Risk from AI", "AI Policy & Regulation", "International AI Governance", "AI Explainability Tools (LIME/SHAP)", "Adversarial Attacks on AI", "Federated Learning", "Differential Privacy", "Homomorphic Encryption", "Secure Multiparty Computation (SMC)", "Zero-Knowledge Proofs (ZKPs)", "Quantum Cryptography", "Post-Quantum Cryptography", "Cyber Threat Intelligence", "Security Information and Event Management (SIEM)", "Security Orchestration, Automation and Response (SOAR)", "Identity and Access Management (IAM)", "Endpoint Detection and Response (EDR)", "Extended Detection and Response (XDR)", "Network Security", "Application Security", "IoT Security", "Industrial Control System (ICS) Security", "Operational Technology (OT) Security", "SCADA Security", "Physical Security Systems", "Business Continuity Planning (BCP)", "Disaster Recovery Planning (DRP)", "Crisis Management", "Organizational Resilience", "Digital Transformation Strategy", "Innovation Management", "Strategic Planning", "Market Entry Strategy", "Competitive Analysis", "Brand Management", "Product Lifecycle Management (PLM)", "Value Chain Analysis", "Porter's Five Forces", "SWOT Analysis", "PESTEL Analysis", "Scenario Planning", "Foresight & Futures Studies", "System Dynamics Modeling", "Agent-Based Modeling", "Complex Systems Theory", "Network Science", "Game Design Principles", "Level Design", "Character Design", "Game Development Engines (Unity/Unreal)", "Virtual Production", "Immersive Experiences", "Neuroscience Fundamentals", "Cognitive Science", "Behavioral Economics", "Human-Computer Interaction (HCI)", "Service-Oriented Architecture (SOA)", "Event-Driven Architecture (EDA)", "Message Brokers", "Workflow Automation", "Business Process Management (BPM)", "Robotic Process Automation (RPA)", "Low-Code/No-Code Development", "Citizen Data Science", "Data Visualization Tools (Tableau/PowerBI)", "Geographic Information Systems (GIS)", "Computer-Aided Design (CAD)", "Building Information Modeling (BIM)", "Finite Element Analysis (FEA)", "Computational Fluid Dynamics (CFD)", "Augmented Analytics", "Prescriptive Analytics", "Descriptive Analytics", "Predictive Analytics", "Storytelling in Data", "Data Ethics", "Bias Detection in AI", "Fairness in AI", "Privacy-Preserving AI", "Trustworthy AI", "Robust AI", "Green AI", "Sustainable AI", "AI for Good", "AI for Social Impact", "AI in Healthcare", "AI in Finance", "AI in Retail", "AI in Manufacturing", "AI in Education", "AI in Law", "AI in Government", "AI in Cybersecurity", "AI in Marketing", "AI in HR", "AI in Supply Chain", "AI in Logistics", "AI in Agriculture", "AI in Energy", "AI in Environment", "AI in Smart Cities", "AI in Autonomous Vehicles", "AI in Robotics", "AI in Space Exploration", "AI in Art & Creativity", "AI in Music", "AI in Gaming", "AI in Sports", "AI in Customer Service", "AI in Sales", "AI in Product Development", "AI in Research", "AI in Science", "AI in Engineering", "AI in Design", "AI in Journalism", "AI in Translation", "AI in Legal Professions", "AI in Medical Diagnostics", "AI in Drug Discovery", "AI in Personalized Medicine", "AI in Public Safety", "AI in National Security", "AI in Defense", "AI in Space", "AI in Oceanography", "AI in Meteorology", "AI in Geology", "AI in Astronomy", "AI in Physics", "AI in Chemistry", "AI in Biology", "AI in Mathematics", "AI in Economics", "AI in Sociology", "AI in Psychology", "AI in Anthropology", "AI in History", "AI in Philosophy", "AI in Linguistics", "AI in Archaeology", "AI in Arts", "AI in Literature", "AI in Film", "AI in Theater", "AI in Dance", "AI in Fashion", "AI in Architecture", "AI in Urban Planning", "AI in Interior Design", "AI in Landscape Design", "AI in Industrial Design", "AI in UX/UI", "AI in Web Development", "AI in Mobile Development", "AI in Cloud Computing", "AI in Data Management", "AI in Data Engineering", "AI in Data Science", "AI in Machine Learning Engineering", "AI in DevOps", "AI in Cybersecurity Operations", "AI in IT Operations", "AI in Business Analytics", "AI in Management Consulting", "AI in Operations Management", "AI in Project Management", "AI in Program Management", "AI in Portfolio Management", "AI in Risk Management", "AI in Compliance", "AI in Audit", "AI in Financial Planning", "AI in Investment Banking", "AI in Wealth Management", "AI in Actuarial Science", "AI in Underwriting", "AI in Claims Processing", "AI in Fraud Detection", "AI in Insurance", "AI in Banking", "AI in Fintech", "AI in Regtech", "AI in Suptech", "AI in Legaltech", "AI in Edtech", "AI in Healthtech", "AI in Proptech", "AI in Greentech", "AI in Sports Analytics", "AI in Media & Entertainment", "AI in Publishing", "AI in Journalism", "AI in Broadcasting", "AI in Film Production", "AI in Music Production", "AI in Game Development", "AI in VFX", "AI in Animation", "AI in Content Creation", "AI in Digital Marketing", "AI in E-commerce", "AI in Customer Relations", "AI in Sales Automation", "AI in Talent Acquisition", "AI in Employee Training", "AI in Performance Management", "AI in Workplace Safety", "AI in Facilities Management", "AI in Smart Buildings", "AI in Smart Grids", "AI in Renewable Energy", "AI in Waste Management", "AI in Water Management", "AI in Air Quality Monitoring", "AI in Biodiversity Conservation", "AI in Climate Modeling", "AI in Disaster Prediction", "AI in Emergency Response", "AI in Public Services", "AI in Smart Government", "AI in Defense Systems", "AI in Military Applications", "AI in Space Robotics", "AI in Satellite Image Analysis", "AI in Space Debris Tracking", "AI in Asteroid Detection", "AI in Exoplanet Discovery", "AI in Cosmic Ray Analysis", "AI in Particle Physics Experiments", "AI in Fusion Energy Research", "AI in Quantum Computing Applications", "AI in Advanced Materials Design", "AI in Drug Synthesis", "AI in Chemical Reaction Optimization", "AI in Protein Folding Prediction", "AI in Gene Editing Optimization", "AI in Personalized Diagnostics", "AI in Robotic Surgery", "AI in Prosthetics & Bionics", "AI in Brain-Computer Interfaces (BCI)", "AI in Neuroprosthetics", "AI in Elderly Care Robotics", "AI in Home Automation", "AI in Smart Appliances", "AI in Personalized Entertainment", "AI in Content Recommendation", "AI in Generative Art", "AI in Algorithmic Composition", "AI in Procedural Content Generation (Gaming)", "AI in Game AI Development", "AI in Sports Analytics & Performance", "AI in Refereeing & Officiating", "AI in Fan Engagement", "AI in Stadium Operations", "AI in Personalized Coaching", "AI in Fitness Tracking", "AI in Nutrition Planning", "AI in Mental Wellness Apps"]
        firm_specific_skills = ["Custom Trading Algorithms (QuantUniversity)", "Niche Legal Specialty (e.g., Patent Law for AI)", "Specific Research Lab Protocols (e.g., CRISPR Gene Editing Techniques)", "Proprietary Design Software (e.g., AutoDesk Revit Customization)"]
    else:
        general_skills = ["Python Programming", "Data Analysis (Pandas/NumPy)", "Communication Skills", "Problem Solving"]
        firm_specific_skills = [] # No specific firm-specific skills for generic roles

    return {
        "general": [s for s in general_skills if s in SKILL_CATEGORIES and SKILL_CATEGORIES[s] == 'general'],
        "firm_specific": [s for s in firm_specific_skills if s in SKILL_CATEGORIES and SKILL_CATEGORIES[s] == 'firm-specific']
    }

def get_learning_resources_for_skills(skills: list):
    return LEARNING_RESOURCES[LEARNING_RESOURCES['Skill'].isin(skills)]
