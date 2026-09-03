from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="ROHIT VIKRAANTH S | RESUME",
    page_icon="📄",
    layout="centered",
)

# Enforce strict A4 geometry and reset all Streamlit default spacing
st.markdown(
    """
    <style>
    /* Reset Streamlit outer margins */
    .block-container {
        max-width: 860px !important;
        padding-top: 1rem !important;
        padding-bottom: 2rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    header, footer, #MainMenu {
        visibility: hidden !important;
        height: 0 !important;
    }
    .stDownloadButton {
        display: flex;
        justify-content: center;
        margin-bottom: 1.2rem;
    }

    /* Fixed A4 Page Container */
    .a4-sheet {
        width: 100%;
        max-width: 820px;
        min-height: 1120px;
        margin: 0 auto;
        background-color: #ffffff;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
        display: flex;
        flex-direction: row;
        border-radius: 4px;
        overflow: hidden;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }

    /* Left Dark Panel */
    .sidebar-dark {
        width: 33%;
        background-color: #2b2b2b;
        color: #ffffff;
        padding: 3rem 1.6rem;
        box-sizing: border-box;
    }

    /* Right Light Panel */
    .main-white {
        width: 67%;
        background-color: #ffffff;
        color: #1f2421;
        padding: 3rem 2.2rem;
        box-sizing: border-box;
    }

    /* Left Headings */
    .dark-heading {
        font-size: 1.15rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #ffffff;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
        padding-bottom: 0.4rem;
        border-bottom: 2px solid #555555;
    }
    .dark-heading:first-child {
        margin-top: 0;
    }

    /* Left Content Typography */
    .dark-item {
        font-size: 0.86rem;
        color: #d1d5db;
        margin-bottom: 0.65rem;
        line-height: 1.45;
        word-break: break-all;
    }
    .dark-item a {
        color: #93c5fd;
        text-decoration: none;
    }
    .skill-badge {
        font-size: 0.82rem;
        font-weight: 700;
        letter-spacing: 1px;
        text-transform: uppercase;
        color: #ffffff;
        margin-bottom: 0.55rem;
        display: block;
    }

    /* Right Name & Title (Centered & Capitalized) */
    .header-name {
        text-align: center;
        font-size: 2.2rem;
        font-weight: 900;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: #1f2421;
        margin: 0;
        line-height: 1.2;
    }
    .header-role {
        text-align: center;
        font-size: 0.95rem;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #64748b;
        margin-top: 0.5rem;
        margin-bottom: 0.3rem;
    }
    .header-location {
        text-align: center;
        font-size: 0.9rem;
        color: #475569;
        margin-bottom: 2.2rem;
    }

    /* Right Section Titles */
    .white-heading {
        font-size: 1.15rem;
        font-weight: 800;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #1f2421;
        margin-top: 1.8rem;
        margin-bottom: 0.8rem;
        padding-bottom: 0.35rem;
        border-bottom: 2px solid #1f2421;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .white-heading:first-of-type {
        margin-top: 0;
    }

    /* Right Content Typography */
    .summary-p {
        font-size: 0.9rem;
        line-height: 1.6;
        color: #334155;
        margin-bottom: 1.5rem;
    }
    .item-title {
        font-size: 0.98rem;
        font-weight: 700;
        color: #0f172a;
    }
    .item-sub {
        font-size: 0.82rem;
        font-weight: 600;
        color: #64748b;
        margin-bottom: 0.4rem;
    }
    .bullets {
        padding-left: 1.2rem;
        margin-top: 0.3rem;
        margin-bottom: 1.2rem;
        color: #334155;
        font-size: 0.88rem;
        line-height: 1.55;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Download Button at Top
pdf_path = Path("Rohit_Resume.pdf")
if not pdf_path.exists():
    pdf_path = Path("S.Rohit-Resume.pdf")

if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📄 DOWNLOAD OFFICIAL PDF",
            data=f.read(),
            file_name="Rohit_Vikraanth_Resume.pdf",
            mime="application/pdf",
        )

# Complete Seamless A4 Sheet
st.markdown(
    """
<div class="a4-sheet">

    <!-- LEFT SIDEBAR: DARK CHARCOAL -->
    <div class="sidebar-dark">
        
        <div class="dark-heading">CONTACT</div>
        <div class="dark-item">✉️ <a href="mailto:rs5483@srmist.edu.in">rs5483@srmist.edu.in</a></div>
        <div class="dark-item">📞 +91 9080345650</div>
        <div class="dark-item">📍 Chennai, India</div>

        <div class="dark-heading">MY SKILLS</div>
        <div class="skill-badge">FULL STACK WEB DEV</div>
        <div class="skill-badge">MACHINE LEARNING</div>
        <div class="skill-badge">PYTHON PROGRAMMING</div>
        <div class="skill-badge">JAVA</div>
        <div class="skill-badge">C++</div>
        <div class="skill-badge">MYSQL</div>
        <div class="skill-badge">DEEP LEARNING / LSTM</div>
        <div class="skill-badge">FRONTEND (HTML/CSS/JS)</div>
        <div class="skill-badge">BUSINESS ANALYTICS</div>

        <div class="dark-heading">CERTIFICATIONS</div>
        <div class="dark-item">• Data Science — Board Infinity</div>
        <div class="dark-item">• Cloud Computing — NASSCOM</div>
        <div class="dark-item">• Machine Learning — NASSCOM</div>
        <div class="dark-item">• NLP — UpGrad</div>
        <div class="dark-item">• Full Stack Dev — MongoDB</div>
        <div class="dark-item">• Networks — SRM & SkillUp</div>

    </div>

    <!-- RIGHT MAIN PANEL: CLEAN WHITE -->
    <div class="main-white">

        <!-- CENTERED NAME & TITLE -->
        <h1 class="header-name">ROHIT VIKRAANTH S</h1>
        <div class="header-role">FULL-STACK DEVELOPER & ML ENTHUSIAST</div>
        <div class="header-location">📍 SRM Institute of Science and Technology, Vadapalani</div>

        <!-- ABOUT ME / SUMMARY -->
        <div class="white-heading">⦿ ABOUT ME</div>
        <div class="summary-p">
            Motivated B.Tech Computer Science and Engineering student with a strong focus on Full Stack Development and Machine Learning. Skilled in developing scalable, data-driven applications using Python, Java, and modern web frameworks. Passionate about sequence modeling, network latency optimization, and applying AI to solve real-world engineering problems.
        </div>

        <!-- EDUCATION -->
        <div class="white-heading">📖 MY EDUCATION</div>
        <div style="border-left: 3px solid #1f2421; padding-left: 0.8rem; margin-bottom: 1.4rem;">
            <div class="item-title">B.Tech in Computer Science and Engineering</div>
            <div style="font-size: 0.88rem; color: #334155;">SRM Institute of Science and Technology, Vadapalani</div>
            <div class="item-sub">GRADUATION: 2027 | CGPA: 7.81 / 10</div>
        </div>

        <!-- WORK EXPERIENCE & PROJECTS -->
        <div class="white-heading">💼 PROJECTS & RESEARCH</div>
        
        <div>
            <div class="item-title">AI-Based Predictive Caching</div>
            <div class="item-sub">March 2026 – Present | Python, TensorFlow, LSTM</div>
            <ul class="bullets">
                <li>Developed an AI-based predictive caching solution using Python and LSTM networks to optimize Content Delivery Network (CDN) caching.</li>
                <li>Applied sequence prediction to dynamically forecast traffic and minimize network latency.</li>
                <li>Publication: <a href="https://ijpub.org/ijvra/track.php" target="_blank" style="color: #2563eb; text-decoration: none;">ijpub.org/ijvra/track.php ↗</a></li>
            </ul>
        </div>

        <div>
            <div class="item-title">IPL Team Winning Prediction Dataset</div>
            <div class="item-sub">October 2025 – Present | Python, Machine Learning</div>
            <ul class="bullets">
                <li>Engineered machine learning models in Python to forecast match outcomes using historical stats, venue analysis, and player metrics.</li>
            </ul>
        </div>

        <!-- PUBLICATIONS -->
        <div class="white-heading">📝 PUBLICATIONS</div>
        <ul class="bullets" style="margin-bottom: 0;">
            <li><strong>AI Based Predictive Caching</strong> — International Journal Track (April 2026)</li>
            <li><strong>IPL Winning Predictions Using Machine Learning</strong> — Published (November 2025)</li>
        </ul>

    </div>

</div>
""",
    unsafe_allow_html=True,
)