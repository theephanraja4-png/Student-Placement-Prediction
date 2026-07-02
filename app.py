import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.graph_objects as go

st.set_page_config(
    page_title="Student Placement Prediction",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

.main{
background:#f6f8fc;
}

.title{
text-align:center;
font-size:42px;
font-weight:bold;
color:#1f4e79;
}

.subtitle{
text-align:center;
font-size:18px;
color:gray;
}

.block{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 3px 12px rgba(0,0,0,.12);
margin-bottom:20px;
}

.stButton>button{
background:#1565C0;
color:white;
height:55px;
font-size:20px;
font-weight:bold;
border-radius:12px;
width:100%;
}

</style>
""", unsafe_allow_html=True)

model = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")
encoders = joblib.load("label_encoders.pkl")

st.markdown("<div class='title'>🎓 AI Student Placement Prediction</div>", unsafe_allow_html=True)

st.markdown("<div class='subtitle'>K-Nearest Neighbors Machine Learning Model</div>", unsafe_allow_html=True)

st.success("✅ Trained KNN Model Loaded Successfully")

st.divider()

st.header("📝 Student Details")

col1,col2=st.columns(2)

with col1:

    gender=st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    age=st.slider(
        "Age",
        20,
        25,
        21
    )

    department=st.selectbox(
        "Department",
        [
        "CSE",
        "IT",
        "ECE",
        "EEE",
        "MECH",
        "CIVIL"
        ]
    )

    cgpa=st.slider(
        "CGPA",
        5.0,
        10.0,
        7.5
    )

    tenth=st.slider(
        "10th Percentage",
        40,
        100,
        80
    )

    twelfth=st.slider(
        "12th Percentage",
        40,
        100,
        80
    )

    degree=st.slider(
        "Degree Percentage",
        40,
        100,
        75
    )

    projects=st.slider(
        "Projects",
        0,
        6,
        2
    )

    internships=st.slider(
        "Internships",
        0,
        3,
        1
    )
    with col2:

          certifications = st.slider(
        "Certifications",
        0,
        8,
        2
    )

    coding = st.slider(
        "Coding Skill",
        1,
        10,
        6
    )

    communication = st.slider(
        "Communication Skill",
        1,
        10,
        6
    )

    aptitude = st.slider(
        "Aptitude Score",
        40,
        100,
        70
    )

    english = st.slider(
        "English Proficiency",
        1,
        10,
        6
    )

    leadership = st.slider(
        "Leadership",
        1,
        10,
        5
    )

    teamwork = st.slider(
        "Teamwork",
        1,
        10,
        6
    )

    hackathons = st.slider(
        "Hackathons",
        0,
        5,
        1
    )

    backlogs = st.slider(
        "Backlogs",
        0,
        5,
        0
    )

st.divider()

predict = st.button(
    "🎯 Predict Placement",
    use_container_width=True
)

if predict:

    gender = encoders["Gender"].transform([gender])[0]
    department = encoders["Department"].transform([department])[0]

    data = np.array([[
        gender,
        age,
        department,
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
        backlogs
    ]])

    data = scaler.transform(data)

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0]

    placed_probability = probability[1] * 100

    result = encoders["Placement"].inverse_transform([prediction])[0]

    st.divider()

    if result == "Yes":
        st.success("🎉 Congratulations! High Placement Chance")
    else:
        st.error("⚠ Low Placement Chance")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Placement",
            result
        )

    with col2:
        st.metric(
            "Probability",
            f"{placed_probability:.1f}%"
        )

    salary = 3

    if placed_probability >= 90:
        salary = 12
    elif placed_probability >= 80:
        salary = 9
    elif placed_probability >= 70:
        salary = 7
    elif placed_probability >= 60:
        salary = 5
    else:
        salary = 3

    with col3:
        st.metric(
            "Expected Salary",
            f"₹{salary} LPA"
        )

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=placed_probability,
        title={"text": "Placement Probability"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "green"},
            "steps": [
                {"range": [0, 40], "color": "#ffb3b3"},
                {"range": [40, 70], "color": "#ffe699"},
                {"range": [70, 100], "color": "#b6fcb6"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("🏢 Suggested Companies")

    if placed_probability >= 90:

        st.success("""
• Microsoft
• Google
• Amazon
• Adobe
• Zoho
• Oracle
""")

    elif placed_probability >= 75:

        st.info("""
• TCS
• Infosys
• Accenture
• Capgemini
• Cognizant
""")

    else:

        st.warning("""
Focus on improving your skills before campus placements.
""")

    st.subheader("📈 Suggestions")

    suggestions = []

    if cgpa < 8:
        suggestions.append("✔ Improve CGPA above 8.0")

    if projects < 3:
        suggestions.append("✔ Build more projects")

    if internships == 0:
        suggestions.append("✔ Complete at least one internship")

    if coding < 7:
        suggestions.append("✔ Practice DSA and Coding")

    if communication < 7:
        suggestions.append("✔ Improve Communication Skills")

    if aptitude < 70:
        suggestions.append("✔ Practice Aptitude Daily")

    if backlogs > 0:
        suggestions.append("✔ Clear all Backlogs")

    if len(suggestions) == 0:
        st.success("Excellent Profile! Keep improving consistently.")

    else:
        for item in suggestions:
            st.write(item)

    st.balloons()