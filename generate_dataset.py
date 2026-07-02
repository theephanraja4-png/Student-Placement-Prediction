import pandas as pd
import random

random.seed(42)

departments = [
    "CSE","IT","ECE","EEE","MECH","CIVIL"
]

genders = ["Male","Female"]

rows = []

for i in range(1,2001):

    gender = random.choice(genders)
    age = random.randint(20,25)
    dept = random.choice(departments)

    cgpa = round(random.uniform(5.5,9.9),2)

    tenth = random.randint(55,99)
    twelfth = random.randint(55,99)
    degree = random.randint(55,95)

    projects = random.randint(0,6)
    internships = random.randint(0,3)
    certifications = random.randint(0,8)

    coding = random.randint(1,10)
    communication = random.randint(1,10)
    aptitude = random.randint(40,100)
    english = random.randint(1,10)
    leadership = random.randint(1,10)
    teamwork = random.randint(1,10)
    hackathons = random.randint(0,5)

    backlogs = random.randint(0,5)

    score = (
        cgpa*10 +
        projects*6 +
        internships*8 +
        certifications*3 +
        coding*4 +
        communication*3 +
        aptitude*0.4 +
        english*2 +
        teamwork*2 -
        backlogs*10
    )

    placement = "Yes" if score >= 170 else "No"

    rows.append([
        i,
        gender,
        age,
        dept,
        cgpa,
        tenth,
        twelfth,
        degree,
        projects,
        internships,
        certifications,
        coding,
        communication,
        aptitude,
        english,
        leadership,
        teamwork,
        hackathons,
        backlogs,
        placement
    ])

columns = [
    "Student_ID",
    "Gender",
    "Age",
    "Department",
    "CGPA",
    "Tenth_Percentage",
    "Twelfth_Percentage",
    "Degree_Percentage",
    "Projects",
    "Internships",
    "Certifications",
    "Coding_Skill",
    "Communication",
    "Aptitude",
    "English",
    "Leadership",
    "Teamwork",
    "Hackathons",
    "Backlogs",
    "Placement"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("placement_dataset.csv", index=False)

print("Dataset Created Successfully!")