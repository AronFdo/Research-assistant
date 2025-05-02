import streamlit as st
from main import run_research_agent  # Make sure your main logic is in a callable function

st.set_page_config(page_title="AI Research Assistant", layout="wide")

st.title("🔍 AI Research Assistant")

query = st.text_input("Enter your research query:", "")

if st.button("Run Research"):
    if query:
        with st.spinner("Running agents..."):
            try:
                summary, analysis, pdf_path = run_research_agent(query)
                st.success("✅ Done!")

                st.subheader("📘 Summary")
                st.write(summary)

                st.subheader("🧠 Analysis & Next Steps")
                st.write(analysis)

                st.subheader("📄 Download Report")
                with open(pdf_path, "rb") as f:
                    st.download_button(
                        label="Download PDF Report",
                        data=f,
                        file_name=pdf_path.split("/")[-1],
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please enter a query first.")
