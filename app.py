import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="Credit Default App", layout="centered")

# -----------------------------
# CUSTOM CSS (BLACK + RED + BOLD)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background: #000000;
    color: white;
}

/* Card Container */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background: #111111;
    border: 1px solid red !important;
    border-radius: 15px;
    padding: 20px;
}

/* Titles and text */
h1, h2, h3, h4, p, label {
    font-weight: bold !important;
    color: white !important;
}

/* Subtext */
.subtext {
    text-align: center;
    color: red !important;
    font-weight: bold;
}

/* Buttons */
.stButton>button, .stFormSubmitButton>button {
    width: 100%;
    height: 45px;
    border-radius: 10px;
    font-weight: bold;
    background: red;
    color: white;
    border: none;
}

.stButton>button:hover, .stFormSubmitButton>button:hover {
    background: #cc0000;
    color: white;
}

/* Inputs */
input, .stNumberInput, .stSlider {
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SESSION STATE
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

# -----------------------------
# LOGIN PAGE
# -----------------------------
if not st.session_state.logged_in:
    st.markdown("<h1>🔐 LOGIN</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtext'>ENTER YOUR CREDENTIALS</p>", unsafe_allow_html=True)

    with st.container(border=True):
        username = st.text_input("USERNAME")
        password = st.text_input("PASSWORD", type="password")

        if st.button("LOGIN"):
            if username == "admin" and password == "1234":
                st.session_state.logged_in = True
                st.success("LOGIN SUCCESSFUL ✅")
                st.rerun()
            else:
                st.error("INVALID CREDENTIALS ❌")

# -----------------------------
# MAIN APP
# -----------------------------
else:
    st.markdown("<h1>💳 CREDIT DEFAULT PREDICTION</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtext'>AI RISK ANALYSIS SYSTEM</p>", unsafe_allow_html=True)

    with st.container(border=True):
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("AGE", min_value=18, max_value=100, value=30, step=1)
            income = st.number_input("MONTHLY INCOME (₹)", min_value=0.0, max_value=10000000.0, value=25000.0, step=1000.0)

        with col2:
            loan = st.number_input("LOAN AMOUNT (₹)", min_value=0.0, max_value=10000000.0, value=50000.0, step=5000.0)
            credit_score = st.slider("CREDIT SCORE", min_value=300, max_value=900, value=650)

        st.markdown("---")

        predict_clicked = st.button("🚀 PREDICT RISK")
        if predict_clicked:
            st.session_state.prediction_done = True
            st.session_state.last_age = age
            st.session_state.last_income = income
            st.session_state.last_loan = loan
            st.session_state.last_credit_score = credit_score

        if st.session_state.prediction_done:
            cur_age = st.session_state.get("last_age", age)
            cur_income = st.session_state.get("last_income", income)
            cur_loan = st.session_state.get("last_loan", loan)
            cur_credit_score = st.session_state.get("last_credit_score", credit_score)

            # Calculate Risk
            risk = 0
            analysis_points = []
            suggestions = []

            # 1. Credit score risk
            if cur_credit_score < 600:
                risk += 50
                analysis_points.append("• LOW CREDIT SCORE (< 600)")
                suggestions.append("• Focus on paying bills on time to boost your credit score.")
            elif cur_credit_score < 700:
                risk += 20
                analysis_points.append("• MODERATE CREDIT SCORE (600–699)")
                suggestions.append("• Aim to bring credit score above 700 for better loan terms.")

            # 2. Loan vs Annual Income risk
            annual_income = cur_income * 12
            if annual_income > 0 and cur_loan > annual_income:
                risk += 30
                analysis_points.append("• HIGH LOAN-TO-INCOME RATIO (Loan exceeds 1 year of income)")
                suggestions.append("• Consider reducing the loan amount or extending tenure.")
            elif annual_income > 0 and cur_loan > (cur_income * 6):
                risk += 15
                analysis_points.append("• MODERATE LOAN-TO-INCOME RATIO (Loan exceeds 6 months of income)")

            # 3. Monthly income threshold
            if cur_income < 15000:
                risk += 20
                analysis_points.append("• LOW MONTHLY INCOME (< ₹15,000)")
                suggestions.append("• Adding a co-borrower or guarantor can improve approval chances.")

            # 4. Age factor (younger borrowers with limited credit history)
            if cur_age < 21:
                risk += 10
                analysis_points.append("• LIMITED CREDIT HISTORY (Age < 21)")

            risk = min(risk, 100)

            st.subheader("📊 RISK SCORE")
            st.progress(risk / 100.0)
            st.write(f"**Score:** {risk} / 100")

            if risk > 60:
                st.error("⚠️ HIGH RISK OF DEFAULT")
            elif risk > 30:
                st.warning("⚠️ MODERATE RISK OF DEFAULT")
            else:
                st.success("✅ LOW RISK OF DEFAULT")

            st.markdown("### 🔍 ANALYSIS")
            if analysis_points:
                for point in analysis_points:
                    st.write(point)
            else:
                st.write("• All credit and financial indicators are in good standing.")

            st.markdown("### 💡 SUGGESTIONS")
            if suggestions:
                for suggestion in suggestions:
                    st.write(suggestion)
            else:
                st.write("• Excellent profile! Continue maintaining your current financial habits.")

            st.markdown("### 📋 SUMMARY")
            st.write(f"AGE: {cur_age}")
            st.write(f"INCOME: ₹{cur_income:,.2f}")
            st.write(f"LOAN: ₹{cur_loan:,.2f}")
            st.write(f"CREDIT SCORE: {cur_credit_score}")

    if st.button("LOGOUT"):
        st.session_state.logged_in = False
        st.session_state.prediction_done = False
        st.rerun()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("📊 CREDIT RISK SYSTEM | STREAMLIT APP")