import pandas as pd
import random
from faker import Faker
from datetime import datetime

# Initialize faker and seeds
fake = Faker()
Faker.seed(0)
random.seed(0)

# Sample data
job_titles = [
    "Software Engineer", "Data Scientist", "Web Developer", "Product Manager",
    "DevOps Engineer", "UX Designer", "Business Analyst", "AI Researcher",
    "Network Administrator", "Cybersecurity Analyst"
]

companies = [
    "TechNova Inc.", "InnoSoft Solutions", "Quantum Leap", "Pixel Dynamics",
    "CloudCore Systems", "NextGen Technologies", "InfoVerse", "AlphaWare",
    "SecureNet", "Visionary Labs"
]

locations = [
    "New York, NY", "San Francisco, CA", "Austin, TX", "Seattle, WA",
    "Boston, MA", "Chicago, IL", "Denver, CO", "Los Angeles, CA",
    "Atlanta, GA", "Miami, FL"
]

skills_pool = [
    "Python", "Java", "SQL", "JavaScript", "AWS", "Docker", "Kubernetes",
    "Machine Learning", "Deep Learning", "Excel", "Communication", "Teamwork",
    "Problem Solving", "Data Analysis", "React", "Node.js", "Linux"
]

# Generate fake data
rows = []
for i in range(1, 201):
    job_id = f"JOB{i:04d}"
    title = random.choice(job_titles)
    company = random.choice(companies)
    loc = random.choice(locations)
    city = loc.split(",")[0]
    location_for_map = f"{city}, USA"
    salary = f"${random.randint(60, 150)}k"
    skills = ", ".join(random.sample(skills_pool, k=random.randint(3, 6)))
    post_date = fake.date_between(start_date="-60d", end_date="today")
    description = fake.paragraph(nb_sentences=5)

    rows.append({
        "Job ID": job_id,
        "Job Title": title,
        "Company": company,
        "Location": loc,
        "Location for Map": location_for_map,
        "Salary": salary,
        "Skills": skills,
        "Post Date": post_date.strftime('%Y-%m-%d'),
        "Job Description": description
    })

# Create DataFrame and export
df = pd.DataFrame(rows)
final_path = "job_data.xlsx"
df.to_excel(final_path, index=False)

final_path
