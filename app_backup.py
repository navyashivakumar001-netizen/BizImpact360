import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="BizImpact 360",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("BizImpact 360")
st.sidebar.caption("Business Decision Intelligence")

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

# Dashboard
if menu == "Dashboard":

    st.title("Business Overview")
    st.caption("Understand business changes before implementation.")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Projects", "0")
    col2.metric("Requirements", "0")
    col3.metric("Active Risks", "0")
    col4.metric("Scenarios", "0")

    st.divider()

    st.subheader("Business Intelligence Overview")

    col1, col2 = st.columns(2)

    with col1:
        st.info("Business Impact Analysis")
        st.write("Identify affected departments and processes.")

    with col2:
        st.info("Decision Intelligence")
        st.write("Evaluate decisions and identify better alternatives.")

    st.subheader("Business Performance")

    data = pd.DataFrame({
        "Category": ["Cost", "Revenue", "Risk", "Efficiency"],
        "Score": [65, 80, 45, 75]
    })

    fig = px.bar(
        data,
        x="Category",
        y="Score",
        title="Sample Business Performance"
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.title(menu)
    st.info(f"{menu} module is under development.")

    st.write(
        "This module will be implemented in upcoming development phases."
    )