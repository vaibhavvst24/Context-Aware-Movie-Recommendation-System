import streamlit as st
from recommend import recommend_movies
st.markdown("""
<style>

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display:none;}

/* Remove top padding */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="centered"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(110deg, #212833, #f0e8d5);
    color: white;
}

/* Title */
.main-title {
    font-size: 35px;
    font-weight: bold;
    text-align: center;
    color: #202833;
    margin-bottom: 10px;
    text-shadow: 0 0 10px rgba(202,213,226,1.0);
    width: 105%;
}

/* Subtitle */
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #f2e2e0;
    margin-bottom: 30px;
    text-shadow: 0 0 10px rgba(49,65,88,1.0);
}

/* Card Container */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    color: #202833;
}

/* Input Fields */
.stNumberInput,
.stSelectbox {

    width: 100%;
    color: #202833;
}
            
/* Input Labels */
label {
    color: #202833;
    font-size: 16px !important;
}

/* Buttons */
.stButton > button {

    width: 383%;
    background: linear-gradient(100deg, #202833, #c7d5e4);
    color: #0a0a0a;
    font-size: 18px;
    font-weight: bold;

    border-radius: 10px;
    border: none;

    padding: 12px;

    transition: 0.5s;
}

.stButton > button:hover {

    transform: scale(1.03);
    background: linear-gradient(100deg, #c7d5e4, #202833);
    color: #0a0a0a;
    box-shadow: 0 6px 18px rgba(29,41,61,0.8);
}
            
.recommendation-heading {

    color: #202833;

    text-align: center;

    font-size: 35px;

    margin-top: 20px;

    margin-bottom: 20px;

    font-weight: bold;

    text-shadow: 0 0 10px rgba(202,213,226,1.0);
}


/* Recommendation Box */
.recommendation-box {

    background-color: #202833;

    padding: 15px;

    border-radius: 12px;

    margin-bottom: 10px;

    border-left: 8px solid #2B7FFF;

    font-size: 18px;
            
    color: #f2e2e0;
}

/* Hover Effect */
.recommendation-box:hover {

    transform: scale(1.02);

    box-shadow: 0 6px 18px rgba(43,127,255,0.5);
}
                       
/* Header */
.custom-header {

    background: rgba(255,255,255,0.08);

    padding: 15px;

    border-radius: 12px;

    text-align: center;

    margin-bottom: 25px;
}

.footer {

    text-align: center;

    margin-top: 20px;

    padding: 15px;

    color: #020618;

    font-size: 15px;

    border-top: 1.5px solid rgba(2,6,24,0.8);
}

.highlight {

    color: #202833 !important;

    font-weight: bold;

    font-size: 19px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown("""
    <div class="main-title">
        🎥 AI-Powered Movie Recommendation System
    </div>

    <div class="sub-title">
        Discover Movies Tailored to Your Mood & Preferences
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# USER INPUTS
# ---------------------------------------------------

user_id = st.number_input(
    "Enter User ID",
    min_value=1,
    value=1
)

context = st.selectbox(
    "Select Time Context",
    ["Morning 🌅", "Evening 🌇", "Night 🌙"]
)

context_map = {
    "Morning 🌅": 0,
    "Evening 🌇": 1,
    "Night 🌙": 2
}

context_value = context_map[context]

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------

if st.button("🤔 Recommend Movies"):

    recommendations = recommend_movies(
        user_id,
        context_value
    )

    st.markdown("""
    <div class="recommendation-heading">
        🍿 Top Recommendations
    </div>
    """, unsafe_allow_html=True)

    for movie, score in recommendations:

        st.markdown(f"""
        <div class="recommendation-box">
            ⭐ <b>{movie}</b><br>
            Predicted Rating: {score}
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("""
<div class="footer">
    Developed by 
    <span class="highlight">Vaibhav</span>
    • Powered by Streamlit
</div>
""", unsafe_allow_html=True)