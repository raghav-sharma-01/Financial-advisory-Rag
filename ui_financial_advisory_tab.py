import streamlit as st
import requests

BACKEND_URL = "http://localhost:8001"


def render_financial_advisory_tab():

    st.header("💰 Financial Advisory")

    st.write(
        "Enter your details below to check your eligibility "
        "for relevant financial schemes."
    )

    st.divider()

    # -----------------------------
    # User Details Form
    # -----------------------------

    with st.form("financial_advisory_form"):

        st.subheader("👤 Personal & Financial Details")

        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                value=30,
                step=1
            )

            annual_income = st.number_input(
                "Annual Income (₹)",
                min_value=0,
                value=180000,
                step=10000
            )

        with col2:
            land_acres = st.number_input(
                "Land Holdings (Acres)",
                min_value=0.0,
                value=2.0,
                step=0.5
            )

            dependents = st.number_input(
                "Number of Dependents",
                min_value=0,
                max_value=20,
                value=3,
                step=1
            )

        st.divider()

        submitted = st.form_submit_button(
            "🔍 Check Eligibility",
            use_container_width=True
        )

    # -----------------------------
    # Send data to backend
    # -----------------------------

    if submitted:

        payload = {
            "age": age,
            "income_annual": annual_income,
            "land_acres": land_acres,
            "dependents": dependents
        }

        with st.spinner("Checking eligibility and generating advisory..."):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/financial-advisory/rag",
                    json=payload,
                    timeout=60
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Eligibility check completed!")

                    # -----------------------------
                    # Eligibility Result
                    # -----------------------------

                    st.subheader("📋 Eligibility Result")

                    eligibility = result.get(
                        "eligibility",
                        "No eligibility information available."
                    )

                    st.info(eligibility)

                    # -----------------------------
                    # AI Explanation
                    # -----------------------------

                    st.subheader("🤖 AI Financial Advisory")

                    explanation = result.get(
                        "explanation",
                        "No explanation available."
                    )

                    st.write(explanation)

                    # -----------------------------
                    # Sources
                    # -----------------------------

                    sources = result.get("sources", [])

                    if sources:

                        st.subheader("📚 Sources")

                        for source in sources:
                            st.write(f"• {source}")

                else:

                    st.error(
                        f"Backend error: {response.status_code}"
                    )

                    st.code(response.text)

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Could not connect to the Financial Advisory backend."
                )

                st.info(
                    "Make sure the backend is running on "
                    "http://localhost:8001"
                )

            except Exception as e:

                st.error(f"Something went wrong: {e}")