import streamlit as st
from guardrail.decision import classify_prompt
from llm.llama_client import generate_response

st.title("🛡️ SmartGuard Hybrid Firewall")

prompt = st.text_area("Enter Prompt")

if st.button("Run"):
    result = classify_prompt(prompt)

    st.write("### Guardrail Output")
    st.json(result)

    if result["verdict"] == "Safe":
        response = generate_response(prompt)
        st.write("### LLM Output")
        st.write(response)
    else:
        st.error("Blocked 🚫")
        st.write("Category:", result["category"])