

import streamlit as st
import plotly.express as px
import pandas as pd

# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="BizImpact 360",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------
# CUSTOM STYLING
# ---------------------------------

st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.block-container {
    padding-top: 2rem;
}

h1, h2, h3 {
    color: #172554;
}

[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 18px;
    border-radius: 10px;
    border: 1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------

st.sidebar.title("📊 BizImpact 360")

st.sidebar.caption(
    "Business Impact & Decision Intelligence"
)

st.sidebar.divider()

menu = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Requirements",
        "Impact Analysis",
        "Process Analysis",
        "What-if Simulation",
        "Risk Analysis",
        "Future Prediction",
        "Decision Intelligence",
        "Reports"
    ]
)


# ---------------------------------
# DASHBOARD
# ---------------------------------

if menu == "Dashboard":

    st.title("Business Overview")

    st.caption(
        "Understand business changes before implementation."
    )

    st.divider()

    # KPI CARDS

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Projects", "0")
    col2.metric("Requirements", "0")
    col3.metric("Active Risks", "0")
    col4.metric("Scenarios", "0")

    st.divider()

    # BUSINESS INTELLIGENCE

    st.subheader("Business Intelligence Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.info("Business Impact Analysis")

        st.write(
            "Identify affected departments, stakeholders "
            "and business processes."
        )

    with col2:

        st.info("Decision Intelligence")

        st.write(
            "Evaluate business decisions and identify "
            "better alternatives."
        )

    st.divider()

    # BUSINESS PERFORMANCE

    st.subheader("Business Performance")

    performance_data = pd.DataFrame({
        "Category": [
            "Cost",
            "Revenue",
            "Risk",
            "Efficiency"
        ],
        "Score": [
            65,
            80,
            45,
            75
        ]
    })

    fig = px.bar(
        performance_data,
        x="Category",
        y="Score",
        title="Sample Business Performance",
        text="Score"
    )

    fig.update_layout(
        yaxis_title="Illustrative Score",
        xaxis_title="Business Category",
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.caption(
        "Illustrative demo data – not actual business metrics."
    )

    st.divider()

    # RECENT ACTIVITIES

    st.subheader("Recent Business Activities")

    activity_data = pd.DataFrame({
        "Activity": [
            "Project environment created",
            "Dashboard initialized",
            "Business analysis module planned"
        ],
        "Status": [
            "Completed",
            "Completed",
            "Pending"
        ]
    })

    st.table(activity_data)

    st.divider()

    # RISK ALERTS

    st.subheader("Risk Alerts")

    col1, col2 = st.columns(2)

    with col1:

        st.warning(
            "No actual risk assessments available yet."
        )

    with col2:

        st.info(
            "Risk analysis module is under development."
        )

    st.divider()

    # DEPARTMENT IMPACT

    st.subheader("Department Impact")

    department_data = pd.DataFrame({
        "Department": [
            "Finance",
            "Operations",
            "Marketing",
            "Human Resources"
        ],
        "Impact Score": [
            0,
            0,
            0,
            0
        ],
        "Status": [
            "Not Analyzed",
            "Not Analyzed",
            "Not Analyzed",
            "Not Analyzed"
        ]
    })

    st.table(department_data)

    st.divider()

    # SCENARIO SUMMARY

    st.subheader("Scenario Summary")

    st.info(
        "No business scenarios have been created yet. "
        "Create scenarios in the What-if Simulation module."
    )


# ---------------------------------
# OTHER MODULES
# ---------------------------------

else:

    st.title(menu)

    st.caption(
        "BizImpact 360 - Business Decision Intelligence"
    )

    st.divider()

    if menu == "Requirements":

        st.subheader("Requirement Management")

        st.write(
            "Manage and track business requirements."
        )

    elif menu == "Impact Analysis":

        st.subheader("Business Impact Analysis")

        st.write(
            "Identify direct and indirect impacts "
            "on departments and stakeholders."
        )

    elif menu == "Process Analysis":

        st.subheader("Business Process Analysis")

        st.write(
            "Analyze As-Is and To-Be business processes."
        )

    elif menu == "What-if Simulation":

        st.subheader("What-if Scenario Simulation")

        st.write(
            "Compare different business scenarios "
            "before implementation."
        )

    elif menu == "Risk Analysis":

        st.subheader("Business Risk Analysis")

        st.write(
            "Estimate implementation costs and "
            "potential business risks."
        )

    elif menu == "Future Prediction":

        st.subheader("Future Business Prediction")

        st.write(
            "Predict possible future business outcomes "
            "using historical data."
        )

    elif menu == "Decision Intelligence":

        st.subheader("Decision Evaluation")

        st.write(
            "Evaluate business decisions and "
            "suggest better alternatives."
        )

    elif menu == "Reports":

        st.subheader("Business Impact Reports")

        st.write(
            "Generate business impact analysis reports."
        )

    st.info(
        "This module is currently under development."
    )