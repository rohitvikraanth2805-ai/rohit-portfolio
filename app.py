from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="ROHIT VIKRAANTH S | PORTFOLIO",
    page_icon="💼",
    layout="centered",
)

# High-Contrast Light Theme Styling
st.markdown(
    """
<style>
  /* Force light theme container */
  .stApp {
    background-color: #ffffff !important;
    color: #000000 !important;
  }

  .block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 3rem;
  }

  /* Centered and Capitalized Headings */
  .main-title {
    text-align: center;
    text-transform: uppercase;
    font-size: 2.2rem;
    font-weight: 800;
    letter-spacing: 1.5px;
    color: #000000;
    margin-bottom: 0.2rem;
  }
  .sub-title {
    text-align: center;
    font-size: 1.1rem;
    font-weight: 600;
    color: #334155;
    margin-bottom: 0.8rem;
  }
  .contact-row {
    text-align: center;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
    color: #1e293b;
    font-weight: 500;
  }
  .contact-row a {
    color: #0284c7 !important;
    text-decoration: underline;
  }
  .section-header {
    text-align: center;
    text-transform: uppercase;
    font-size: 1.25rem;
    font-weight: 800;
    letter-spacing: 1.2px;
    color: #0f172a;
    margin: 1.8rem 0 0.8rem 0;
  }

  /* High-Contrast Card / Box Styling */
  .card-box {
    background-color: #f8fafc;
    border: 1.5px solid #cbd5e1;
    border-radius: 10px;
    padding: 1.25rem 1.5rem;
    margin-bottom: 1rem;
    color: #000000;
    font-size: 0.95rem;
    line-height: 1.6;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-weight: 700;
    font-size: 1.05rem;
    color: #000000;
    margin-bottom: 0.4rem;
  }
  .card-date {
    font-size: 0.85rem;
    font-weight: 600;
    color: #475569;
  }
  .pill {
    display: inline-block;
    background-color: #e2e8f0;
    border: 1px solid #94a3b8;
    border-radius: 999px;
    padding: 0.25rem 0.75rem;
    font-size: 0.85rem;
    font-weight: 600;
    margin: 0.2rem 0.2rem;
    color: #0f172a;
  }

  /* Centered Download Button Container */
  .stDownloadButton {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
  }
  .stDownloadButton button {
    background-color: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    font-weight: 600;
  }
</style>
""",
    unsafe_allow_html=True,
)

# Top Profile Header (Centered & Capitalized)
st.markdown('<div class="main-title">ROHIT VIKRAANTH S</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Full Stack Web Development & Machine Learning</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="contact-row">
  ✉️ <a href="mailto:rs5483@srmist.edu.in">rs5483@srmist.edu.in</a> &nbsp;|&nbsp; 
  📞 +91 9080345650 &nbsp;|&nbsp; 
  🎓 Graduation: 2027
</div>
""",
    unsafe_allow_html=True,
)

# Centered Download CV Button
pdf_path = Path("S.Rohit-Resume.pdf")
if not pdf_path.exists():
    pdf_path = Path("Rohit_Resume.pdf")

if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📄 DOWNLOAD RESUME (CV)",
            data=f.read(),
            file_name="Rohit_Vikraanth_Resume.pdf",
            mime="application/pdf",
        )

# Section: Professional Summary
st.markdown(
    '<div class="section-header">PROFESSIONAL SUMMARY</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="card-box">
  Motivated B.Tech Computer Science and Engineering student with a strong interest in Full Stack Development and Machine Learning. Skilled in developing data-driven applications using Python, Java, JavaScript, and modern web technologies. Passionate about building scalable software solutions, applying artificial intelligence to real-world problems, and continuously learning emerging technologies to contribute effectively in software development and AI-driven projects.
</div>
""",
    unsafe_allow_html=True,
)

# Section: Education
st.markdown(
    '<div class="section-header">EDUCATION</div>', unsafe_allow_html=True
)
st.markdown(
    """
<div class="card-box">
  <div class="card-header">
    <span>SRM Institute of Science and Technology, Vadapalani</span>
    <span class="card-date">2023 – 2027</span>
  </div>
  <div style="color: #334155; font-size: 0.95rem;">
    B.Tech in Computer Science and Engineering &nbsp;•&nbsp; <strong>CGPA: 7.81 / 10</strong>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Section: Projects
st.markdown('<div class="section-header">PROJECTS</div>', unsafe_allow_html=True)

st.markdown(
    """
<div class="card-box">
  <div class="card-header">
    <span>AI Based Predictive Caching</span>
    <span class="card-date">Mar 2026 – Present</span>
  </div>
  <div style="color: #0369a1; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.5rem;">Tech: Python, TensorFlow, LSTM</div>
  <ul style="margin: 0; padding-left: 1.2rem; color: #000000; font-size: 0.95rem;">
    <li>Developed an AI-based predictive caching solution using Python, TensorFlow, and LSTM to improve Content Delivery Network (CDN) performance.</li>
    <li>Applied sequence prediction techniques to optimize caching decisions and reduce network latency.</li>
    <li>Publication Track: <a href="https://ijpub.org/ijvra/track.php" target="_blank" style="color: #0284c7; text-decoration: underline;">ijpub.org/ijvra/track.php ↗</a></li>
  </ul>
</div>

<div class="card-box">
  <div class="card-header">
    <span>IPL Team Winning Prediction Dataset</span>
    <span class="card-date">Oct 2025 – Present</span>
  </div>
  <div style="color: #0369a1; font-size: 0.85rem; font-weight: 700; margin-bottom: 0.5rem;">Tech: Python, Machine Learning, Statistical Modeling</div>
  <ul style="margin: 0; padding-left: 1.2rem; color: #000000; font-size: 0.95rem;">
    <li>Built machine learning models in Python to predict IPL match outcomes using historical match statistics and performance metrics.</li>
  </ul>
</div>
""",
    unsafe_allow_html=True,
)

# Section: Technical Skills
st.markdown(
    '<div class="section-header">TECHNICAL SKILLS</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="card-box">
  <div style="margin-bottom: 0.75rem;">
    <strong style="color: #000000;">Programming Languages:</strong><br>
    <div style="margin-top: 0.35rem;">
      <span class="pill">Python</span>
      <span class="pill">Java</span>
      <span class="pill">MySQL</span>
      <span class="pill">C++</span>
      <span class="pill">JavaScript</span>
    </div>
  </div>
  <div style="margin-bottom: 0.75rem;">
    <strong style="color: #000000;">Web & Software Engineering:</strong><br>
    <div style="margin-top: 0.35rem;">
      <span class="pill">Full Stack Web Development</span>
      <span class="pill">Frontend Development</span>
      <span class="pill">Backend Development</span>
      <span class="pill">Business Analytics</span>
    </div>
  </div>
  <div>
    <strong style="color: #000000;">Productivity & Tools:</strong><br>
    <div style="margin-top: 0.35rem;">
      <span class="pill">Microsoft Word</span>
      <span class="pill">Microsoft Excel</span>
      <span class="pill">Microsoft PowerPoint</span>
      <span class="pill">Git & GitHub</span>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# Section: Certifications
st.markdown(
    '<div class="section-header">CERTIFICATIONS</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="card-box">
  <ul style="margin: 0; padding-left: 1.2rem; color: #000000; font-size: 0.95rem; line-height: 1.8;">
    <li><strong>Data Science Professional Certification</strong> — Board Infinity</li>
    <li><strong>Cloud Computing Certification</strong> — NASSCOM</li>
    <li><strong>Machine Learning Specialization</strong> — NASSCOM</li>
    <li><strong>Natural Language Processing (NLP)</strong> — UpGrad</li>
    <li><strong>Full Stack Web Development Certification</strong> — MongoDB</li>
    <li><strong>Computer Networks Certification</strong> — SRM Institute of Science and Technology, Vadapalani</li>
    <li><strong>Computer Networks Fundamentals</strong> — SkillUp</li>
    <li><strong>Project Publication Certification</strong> — International Journal of Advanced Research in Computer and Communication Engineering (IJARCCE)</li>
  </ul>
</div>
""",
    unsafe_allow_html=True,
)

# Section: Publications
st.markdown(
    '<div class="section-header">PUBLICATIONS</div>',
    unsafe_allow_html=True,
)
st.markdown(
    """
<div class="card-box">
  <ul style="margin: 0; padding-left: 1.2rem; color: #000000; font-size: 0.95rem; line-height: 1.8;">
    <li><strong>AI Based Predictive Caching</strong> — Published in April 2026</li>
    <li><strong>IPL Winning Predictions Using Machine Learning</strong> — Published in November 2025</li>
  </ul>
</div>
""",
    unsafe_allow_html=True,
)