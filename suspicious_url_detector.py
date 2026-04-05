import streamlit as st
import re

# Page title
st.set_page_config(page_title="Suspicious URL Detector", page_icon="🛡️")

st.title("🛡️ Suspicious URL Detection")
st.write("Enter a URL to check whether it is safe or suspicious.")

def detect_phishing(url):
    suspicious = False
    reasons = []

    if "@" in url:
        suspicious = True
        reasons.append("Contains '@' symbol")

    if "-" in url:
        suspicious = True
        reasons.append("Contains '-' symbol")

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        suspicious = True
        reasons.append("Contains IP address instead of domain")

    if suspicious:
        return True, reasons
    else:
        return False, []

# Input box
url = st.text_input("Enter URL here:")

if st.button("Check URL"):
    if url:
        result, reasons = detect_phishing(url)

        if result:
            st.error("⚠️ Suspicious URL - Possible Phishing")
            st.write("### Reasons:")
            for reason in reasons:
                st.write(f"- {reason}")
        else:
            st.success("✅ Safe URL")
    else:
        st.warning("Please enter a URL.")