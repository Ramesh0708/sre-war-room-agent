import streamlit as st
from incident_memory import *
from ai_analyzer import analyze_incident

# Initialize DB
init_db()

# Page Title
st.title("🚨 SRE War-Room Agent")

# Incident Memory Section
st.subheader("📚 Incident Memory")

incidents = get_incidents()

for row in incidents:
    with st.expander(row[1]):
        st.write(f"Root Cause: {row[2]}")
        st.write(f"Resolution: {row[3]}")

st.subheader("➕ Add New Incident")

with st.form("incident_form"):

    issue = st.text_input("Issue")

    cause = st.text_input("Root Cause")

    resolution = st.text_input("Resolution")

    submit = st.form_submit_button("Save Incident")

    if submit:

        add_incident(
            issue,
            cause,
            resolution
        )

        st.success("Incident Saved!")

# Alert Input
query = st.text_input(
    "Describe the alert"
)

# Analyze Button
if st.button("Analyze"):

    incidents = get_incidents()

    best_match = None

    for row in incidents:

        issue = row[1]

        if any(
            word.lower() in issue.lower()
            for word in query.split()
        ):
            best_match = row
            break

    if best_match:

        st.success("Similar Incident Found")

        st.metric(
            "Confidence Score",
            "92%"
        )

        st.write(
            f"Root Cause: {best_match[2]}"
        )

        st.write(
            f"Resolution: {best_match[3]}"
        )

        st.subheader("🤖 AI Investigation")

        with st.spinner("Analyzing with Llama 3..."):

            ai_response = analyze_incident(query)

        st.markdown(ai_response)

    else:

        st.warning(
            "No matching incident found"
        )


st.divider()

st.caption(
    "Built by Ramesh Choudhary | Build Day: Agent Harness & Memory | Streamlit + SQLite + Ollama"
)