from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="ROHIT VIKRAANTH S | RESUME",
    page_icon="📄",
    layout="centered",
)

# Download Button at the top
pdf_path = Path("Rohit_Resume.pdf")
if not pdf_path.exists():
    pdf_path = Path("S.Rohit-Resume.pdf")

if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📄 DOWNLOAD OFFICIAL RESUME (PDF)",
            data=f.read(),
            file_name="Rohit_Vikraanth_Resume.pdf",
            mime="application/pdf",
        )

# Pure HTML/CSS Canvas (Renders cleanly without markdown indentation bugs)
html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
body {
  background-color: transparent;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  display: flex;
  justify-content: center;
  padding: 10px 0;
}

/* Strict A4 Proportions */
.a4-container {
  width: 794px;
  min-height: 1123px;
  background: #ffffff;
  display: flex;
  flex-direction: row;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
  border-radius: 4px;
  overflow: hidden;
}

/* Left Dark Panel (Zero gap) */
.left-pane {
  width: 34%;
  background-color: #2b2b2b;
  color: #ffffff;
  padding: 40px 25px;
}

/* Right White Panel (Zero gap) */
.right-pane {
  width: 66%;
  background-color: #ffffff;
  color: #1f2421;
  padding: 40px 35px;
}

/* Left Side Styles */
.dark-title {
  font-size: 16px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #ffffff;
  margin-top: 30px;
  margin-bottom: 12px;
  padding-bottom: 5px;
  border-bottom: 2px solid #555555;
}
.dark-title:first-child {
  margin-top: 0;
}
.dark-text {
  font-size: 13px;
  color: #d1d5db;
  margin-bottom: 8px;
  line-height: 1.5;
  word-break: break-word;
}
.dark-text a {
  color: #93c5fd;
  text-decoration: none;
}
.skill-tag {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  color: #ffffff;
  margin-bottom: 7px;
  display: block;
}

/* Right Side Center Header */
.header-name {
  text-align: center;
  font-size: 32px;
  font-weight: 900;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: #1f2421;
  margin: 0;
}
.header-role {
  text-align: center;
  font-size: 13px;
  font-weight: 700;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  color: #64748b;
  margin-top: 8px;
}
.header-location {
  text-align: center;
  font-size: 13px;
  color: #475569;
  margin-top: 4px;
  margin-bottom: 30px;
}

/* Right Side Section Headings */
.light-title {
  font-size: 15px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #1f2421;
  margin-top: 24px;
  margin-bottom: 10px;
  padding-bottom: 4px;
  border-bottom: 2px solid #1f2421;
}
.light-title:first-of-type {
  margin-top: 0;
}

.body-text {
  font-size: 13.5px;
  line-height: 1.6;
  color: #334155;
}
.item-head {
  font-size: 14.5px;
  font-weight: 700;
  color: #0f172a;
}
.item-date {
  font-size: 12px;
  font-weight: 600;
  color: #64748b;
  margin-bottom: 5px;
}
.bullets {
  padding-left: 18px;
  margin-top: 4px;
  margin-bottom: 14px;
  color: #334155;
  font-size: 13px;
  line-height: 1.55;
}
</style>
</head>
<body>

<div class="a4-container">

  <!-- LEFT DARK SIDEBAR -->
  <div class="left-pane">
    
    <div class="dark-title">CONTACT</div>
    <div class="dark-text">✉️ <a href="mailto:rs5483@srmist.edu.in">rs5483@srmist.edu.in</a>[cite: 1]</div>
    <div class="dark-text">📞 +91 9080345650[cite: 1]</div>
    <div class="dark-text">📍 Chennai, India</div>

    <div class="dark-title">MY SKILLS</div>
    <div class="skill-tag">FULL STACK WEB DEV[cite: 1]</div>
    <div class="skill-tag">MACHINE LEARNING[cite: 1]</div>
    <div class="skill-tag">PYTHON PROGRAMMING[cite: 1]</div>
    <div class="skill-tag">JAVA[cite: 1]</div>
    <div class="skill-tag">C++[cite: 1]</div>
    <div class="skill-tag">MYSQL[cite: 1]</div>
    <div class="skill-tag">DEEP LEARNING / LSTM[cite: 1]</div>
    <div class="skill-tag">FRONTEND DEVELOPMENT[cite: 1]</div>
    <div class="skill-tag">BUSINESS ANALYTICS[cite: 1]</div>

    <div class="dark-title">CERTIFICATIONS</div>
    <div class="dark-text">• Data Science — Board Infinity[cite: 1]</div>
    <div class="dark-text">• Cloud Computing — NASSCOM[cite: 1]</div>
    <div class="dark-text">• Machine Learning — NASSCOM[cite: 1]</div>
    <div class="dark-text">• NLP — UpGrad[cite: 1]</div>
    <div class="dark-text">• Full Stack Dev — MongoDB[cite: 1]</div>
    <div class="dark-text">• Networks — SRM & SkillUp[cite: 1]</div>
    <div class="dark-text">• Publication — IJARCCE[cite: 1]</div>

  </div>

  <!-- RIGHT WHITE PANEL -->
  <div class="right-pane">
    
    <!-- CENTERED NAME & TITLE IN ALL CAPS -->
    <h1 class="header-name">ROHIT VIKRAANTH S</h1>
    <div class="header-role">FULL-STACK DEVELOPER & ML ENTHUSIAST</div>
    <div class="header-location">📍 SRM Institute of Science and Technology, Vadapalani[cite: 1]</div>

    <!-- ABOUT ME -->
    <div class="light-title">⦿ ABOUT ME</div>
    <div class="body-text" style="margin-bottom: 20px;">
      Motivated B.Tech Computer Science and Engineering student with a strong interest in Full Stack Development and Machine Learning[cite: 1]. Skilled in developing scalable, data-driven applications using Python, Java, JavaScript, and modern web technologies[cite: 1]. Passionate about building software solutions, sequence modeling, and applying artificial intelligence to real-world latency challenges[cite: 1].
    </div>

    <!-- EDUCATION -->
    <div class="light-title">📖 MY EDUCATION</div>
    <div style="border-left: 3px solid #1f2421; padding-left: 10px; margin-bottom: 20px;">
      <div class="item-head">B.Tech in Computer Science and Engineering[cite: 1]</div>
      <div style="font-size: 13px; color: #334155;">SRM Institute of Science and Technology, Vadapalani[cite: 1]</div>
      <div class="item-date">GRADUATION: 2027 | CGPA: 7.81 / 10[cite: 1]</div>
    </div>

    <!-- PROJECTS & RESEARCH -->
    <div class="light-title">💼 PROJECTS & RESEARCH</div>
    
    <div>
      <div class="item-head">AI-Based Predictive Caching[cite: 1]</div>
      <div class="item-date">March 2026 – Present | Python, TensorFlow, LSTM[cite: 1]</div>
      <ul class="bullets">
        <li>Developed an AI-based predictive caching solution using Python, TensorFlow, and LSTM to improve Content Delivery Network (CDN) performance[cite: 1].</li>
        <li>Applied sequence prediction techniques to optimize caching decisions and minimize network latency[cite: 1].</li>
        <li>Publication Track: <a href="https://ijpub.org/ijvra/track.php" target="_blank" style="color: #2563eb; text-decoration: none;">ijpub.org/ijvra/track.php ↗</a>[cite: 1]</li>
      </ul>
    </div>

    <div>
      <div class="item-head">IPL Team Winning Prediction Dataset[cite: 1]</div>
      <div class="item-date">October 2025 – Present | Python, Machine Learning[cite: 1]</div>
      <ul class="bullets">
        <li>Engineered machine learning models in Python to forecast match outcomes using historical statistics and performance metrics[cite: 1].</li>
      </ul>
    </div>

    <!-- PUBLICATIONS -->
    <div class="light-title">📝 PUBLICATIONS</div>
    <ul class="bullets" style="margin-bottom: 0;">
      <li><strong>AI Based Predictive Caching</strong> — International Journal Track (April 2026)[cite: 1]</li>
      <li><strong>IPL Winning Predictions Using Machine Learning</strong> — Published (November 2025)[cite: 1]</li>
    </ul>

  </div>

</div>

</body>
</html>
"""

# Render full A4 canvas
components.html(html_content, height=1180, scrolling=False)