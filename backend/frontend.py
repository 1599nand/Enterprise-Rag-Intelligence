import streamlit as st
import requests

st.set_page_config(
    page_title="Enterprise RAG Assistant",
    page_icon="🤖",
    layout="wide"
)

# Sidebar
st.sidebar.title("Enterprise RAG")
st.sidebar.markdown("Secure Multi-Source Retrieval")

st.sidebar.info(
    "Demo Users:\n\n"
    "alice → HR\n\n"
    "bob → Engineering\n\n"
    "charlie → Finance\n\n"
    "admin → Full Access"
)

# Main title
st.title("Enterprise Secure RAG Assistant")

st.markdown(
    """
    This system demonstrates:
    - RBAC-based retrieval
    - Secure enterprise search
    - Semantic retrieval
    - Citation-aware responses
    """
)

# Input section
col1, col2 = st.columns(2)


with col1:
    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

with col2:
    query = st.text_input(
        "Ask a question",
        placeholder="Ask enterprise query"
    )
    
# Button
if st.button("Submit Query"):

    if not username or not query:
        st.warning("Please enter both username and query")

    else:

        try:

            response = requests.post(
                "http://127.0.0.1:8001/ask",
                json={
                    "username": username,
                    "query": query
                }
            )

            data = response.json()
            
            st.divider()

            # Answer section
            st.subheader("Generated Response")

            if "Access denied" in data.get("answer", ""):
                st.error(data["answer"])
            else:
                st.success(data["answer"])

            # Citations
            if "citations" in data:
                st.subheader("Citations")

                for citation in data["citations"]:
                    st.code(citation)

            # Confidence
            if "confidence" in data:
                st.subheader("Confidence")
                
                st.info(data["confidence"])

        except Exception as e:
            st.error(f"Backend connection failed: {e}")