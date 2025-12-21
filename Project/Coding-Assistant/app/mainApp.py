import streamlit as st
from app.chains.debug_chain import run_debug

# -------------------------------
# Page config
# -------------------------------
st.set_page_config(
    page_title="Code Assistant & Jira Creator",
    layout="centered"
)

st.title("🛠️ Code Assistant & Jira Creator")
st.caption(
    "Analyze system / CI logs using LLMs and optionally create Jira tickets automatically."
)

# -------------------------------
# Log input
# -------------------------------
log_input = st.text_area(
    "Paste your logs here",
    height=250,
    placeholder="Paste SSH / CI / build / runtime logs here..."
)

# -------------------------------
# Action button
# -------------------------------
if st.button("🔍 Analyze Logs"):
    if not log_input.strip():
        st.warning("Please paste some logs before submitting.")
    else:
        with st.spinner("Analyzing logs..."):
            try:
                result = run_debug(log_input)

                st.success("Analysis completed")

                # -------------------------------
                # Structured output
                # -------------------------------
                st.subheader("📄 Analysis Result")
                st.json(result.model_dump())

                # -------------------------------
                # Jira status (nice UX)
                # -------------------------------
                if result.jira_ticket_required:
                    if result.jira_ticket_id:
                        st.info(
                            f"✅ Jira ticket created: **{result.jira_ticket_id}**"
                        )
                    else:
                        st.warning(
                            "⚠️ Jira ticket was required but could not be created."
                        )
                else:
                    st.info("ℹ️ Jira ticket not required for this issue.")

            except Exception as e:
                st.error("Something went wrong during analysis")
                st.exception(e)

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption(
    "Built with LangChain + Groq | Structured outputs | Deterministic workflows"
)
