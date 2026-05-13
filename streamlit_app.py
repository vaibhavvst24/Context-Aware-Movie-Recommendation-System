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

/* ---------------------------------------------------
MAIN APP BACKGROUND
--------------------------------------------------- */

.stApp {

    background:
        linear-gradient(
            rgba(33, 40, 51, 0.1),
            rgba(33, 40, 51, 0.1)
        ),

        url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?q=80&w=2070&auto=format&fit=crop");

    background-size: cover;

    background-position: center;

    background-attachment: fixed;

    color: #F0E8D5;
}


/* ---------------------------------------------------
REMOVE STREAMLIT DEFAULT UI
--------------------------------------------------- */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.stDeployButton {
    display: none;
}


/* ---------------------------------------------------
MAIN CONTAINER
--------------------------------------------------- */

.block-container {

    padding-top: 2rem;

    padding-bottom: 2rem;

    max-width: 750px;
}


/* ---------------------------------------------------
HEADER SECTION
--------------------------------------------------- */

.custom-header {

    background: rgba(255,255,255,0.05);

    backdrop-filter: blur(10px);

    padding: 25px;

    border-radius: 18px;

    text-align: center;

    margin-bottom: 30px;

    box-shadow: 0px 4px 20px rgba(0,0,0,0.4);
}


/* ---------------------------------------------------
MAIN TITLE
--------------------------------------------------- */

.main-title {

    font-size: 34px;

    font-weight: bold;

    color: #F0E8D5;

    margin-bottom: 18px;

    text-shadow: 0px 0px 18px rgba(212,163,115,0.4);
}


/* ---------------------------------------------------
SUBTITLE
--------------------------------------------------- */

.sub-title {

    font-size: 20px;

    color: #D4A373;

    font-weight: 500;

    text-align: center;
            
    margin-bottom: 28px;
}


/* ---------------------------------------------------
INPUT LABELS
--------------------------------------------------- */

label {

    color: #F0E8D5 !important;

    font-size: 16px !important;

    font-weight: 500;
}


/* ---------------------------------------------------
INPUT FIELDS
--------------------------------------------------- */

.stNumberInput input,
.stSelectbox div[data-baseweb="select"] {

    background-color: rgba(255,255,255,0.06) !important;

    color: #F0E8D5 !important;

    border-radius: 10px !important;

    border: 1px solid rgba(255,255,255,0.1) !important;
}


/* ---------------------------------------------------
BUTTON
--------------------------------------------------- */

.stButton > button {

    width: 408%;

    background: #D4A373;

    color: #212833;

    font-size: 18px;

    font-weight: bold;

    border-radius: 12px;

    border: none;

    padding: 8px;

    margin-top: 13px;

    transition: 0.3s ease;

    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

.stButton > button:hover {

    background: #E6B17E;

    color: #212833;

    transform: scale(1.02);

    box-shadow: 0px 6px 18px rgba(212,163,115,0.4);
}


/* ---------------------------------------------------
TOP RECOMMENDATION HEADING
--------------------------------------------------- */

.recommendation-heading {

    color: #F0E8D5 !important;

    text-align: center;

    font-size: 34px;

    font-weight: bold;

    margin-top: 35px;

    margin-bottom: 25px;

    text-shadow: 0px 0px 12px rgba(212,163,115,0.5);
}


/* ---------------------------------------------------
RECOMMENDATION CARDS
--------------------------------------------------- */

.recommendation-box {

    background: rgba(255,255,255,0.07);

    backdrop-filter: blur(8px);

    color: #F0E8D5;

    padding: 18px;

    border-radius: 15px;

    margin-bottom: 15px;

    border-left: 7px solid #D4A373;

    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);

    transition: 0.3s ease;

    font-size: 18px;
}

.recommendation-box:hover {

    transform: translateY(-4px);

    background: rgba(255,255,255,0.1);

    box-shadow: 0px 8px 20px rgba(0,0,0,0.5);
}


/* ---------------------------------------------------
FOOTER
--------------------------------------------------- */

.footer {

    text-align: center;

    margin-top: 110px;

    padding-top: 20px;

    color: #cfcfcf;

    font-size: 14px;
}


/* ---------------------------------------------------
HIGHLIGHT TEXT
--------------------------------------------------- */

.highlight {

    color: #D4A373 !important;

    font-weight: bold;

    text-shadow: 0px 0px 10px rgba(212,163,115,0.3);
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
            🎬 <b>{movie}</b><br>
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