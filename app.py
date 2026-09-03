from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="ROHIT VIKRAANTH S | RESUME",
    page_icon="📄",
    layout="centered",
)

# Custom CSS for the clean two-tone template styling
st.markdown(
    """<style>
/* Main container padding */
.block-container {
  max-width: 860px;
  padding: 1.5rem 1rem 3rem 1rem;
}

/* Header Slate Card */
.resume-header {
  background-color: #2e353d;
  padding: 2.5rem 2rem;
  border-radius: 6px 6px 0 0;
  color: #ffffff;
  margin-bottom: 0px;
}
.resume-name {
  font-size: 2.3rem;
  font-weight: 700;
  margin: 0;
  color: #ffffff;
}
.resume-role {
  font-size: 1.1rem;
  color: #cbd5e1;
  margin-top: 0.35rem;
}

/* Headings */
.sidebar-heading {
  font-size: 1.15rem;
  font-weight: 700;
  color: #1e293b;
  margin-top: 1.2rem;
  margin-bottom: 0.6rem;
}
.sidebar-heading:first-child {
  margin-top: 0;
}
.main-heading {
  font-size: 1.2rem;
  font-weight: 700;
  color: #1e293b;
  border-bottom: 2px solid #1e293b;
  padding-bottom: 0.3rem;
  margin-top: 1.4rem;
  margin-bottom: 0.8rem;
}
.main-heading:first-child {
  margin-top: 0;
}

/* Details and typography */
.contact-item {
  font-size: 0.9rem;
  margin-bottom: 0.6rem;
  color: #334155;
  line-height: 1.4;
}
.contact-item a {
  color: #1e293b;
  text-decoration: none;
}
.edu-title {
  font-size: 0.92rem;
  font-weight: 700;
  color: #0f172a;
  line-height: 1.35;
}
.edu-sub {
  font-size: 0.85rem;
  color: #475569;
  margin-top: 0.15rem;
}
.skill-item {
  font-size: 0.88rem;
  color: #334155;
  margin-bottom: 0.45rem;
}

.summary-text {
  font-size: 0.92rem;
  line-height: 1.6;
  color: #334155;
}
.job-title {
  font-size: 1rem;
  font-weight: 700;
  color: #0f172a;
}
.job-date {
  font-size: 0.82rem;
  color: #64748b;
  margin-bottom: 0.35rem;
}
.bullets {
  padding-left: 1.15rem;
  margin-top: 0.2rem;
  margin-bottom: 1rem;
  color: #334155;
  font-size: 0.9rem;
  line-height: 1.55;
}
</style>""",
    unsafe_allow_html=True,
)

# Download Button at top
pdf_path = Path("Rohit_Resume.pdf")
if not pdf_path.exists():
    pdf_path = Path("S.Rohit-Resume.pdf")

if pdf_path.exists():
    with open(pdf_path, "rb") as f:
        st.download_button(
            label="📄 Download Official PDF",
            data=f.read(),
            file_name="Rohit_Vikraanth_Resume.pdf",
            mime="application/pdf",
        )

# Slate Top Banner
st.markdown(
    """<div class="resume-header">
  <div class="resume-name">Rohit Vikraanth S</div>
  <div class="resume-role">Full Stack Developer & Machine Learning Enthusiast</div>
</div>""",
    unsafe_allow_html=True,
)

# Two-column layout using native Streamlit columns
col_left, col_right = st.columns([1, 1.7], gap="medium")

# Left Column (Beige Sidebar)
with col_left:
    with st.container():
        st.markdown(
            """<div style="background-color: #ece7e1; padding: 1.5rem; border-radius: 0 0 0 6px; min-height: 750px;">
  <div class="sidebar-heading">Contact Details</div>
  <div class="contact-item">✉️ <a href="mailto:rs5483@srmist.edu.in">rs5483@srmist.edu.in</a></div>
  <div class="contact-item">📞 +91 9080345650</div>
  <div class="contact-item">📍 Chennai, India</div>

  <div class="sidebar-heading">Education</div>
  <div style="margin-bottom: 1rem;">
    <div class="edu-title">• Bachelor of Technology in Computer Science & Engineering</div>
    <div class="edu-sub">SRM Institute of Science and Technology, Vadapalani</div>
    <div class="edu-sub">2023 – 2027 | CGPA: 7.81 / 10</div>
  </div>

  <div class="sidebar-heading">Skills</div>
  <div class="skill-item">• Full Stack Web Development</div>
  <div class="skill-item">• Machine Learning & Deep Learning</div>
  <div class="skill-item">• Python Programming</div>
  <div class="skill-item">• Java Development</div>
  <div class="skill-item">• C++ Programming</div>
  <div class="skill-item">• MySQL Database Management</div>
  <div class="skill-item">• Frontend (HTML, CSS, JavaScript)</div>
  <div class="skill-item">• Business Analytics</div>
</div>""",
            unsafe_allow_html=True,
        )

# Right Column (White Content Panel)
with col_right:
    with st.container():
        st.markdown(
            """<div style="background-color: #ffffff; padding: 1.5rem; border-radius: 0 0 6px 0; min-height: 750px;">
  <div class="main-heading">Summary</div>
  <div class="summary-text">
    Motivated B.Tech Computer Science and Engineering student with a strong interest in Full Stack Development and Machine Learning. Skilled in developing data-driven applications using Python, Java, JavaScript, and modern web technologies. Passionate about building scalable software solutions, applying artificial intelligence to real-world problems, and continuously learning emerging technologies.
  </div>

  <div class="main-heading">Work & Projects</div>
  <div>
    <div class="job-title">AI-Based Predictive Caching</div>
    <div class="job-date">March 2026 – Present</div>
    <ul class="bullets">
      <li>Developed an AI-based predictive caching solution using Python, TensorFlow, and LSTM to improve Content Delivery Network (CDN) performance.</li>
      <li>Applied sequence prediction techniques to optimize caching decisions and reduce latency.</li>
      <li>Publication: <a href="https://ijpub.org/ijvra/track.php" target="_blank" style="color: #2563eb; text-decoration: none;">ijpub.org/ijvra/track.php ↗</a></li>
    </ul>
  </div>

  <div>
    <div class="job-title">IPL Team Winning Prediction Dataset</div>
    <div class="job-date">October 2025 – Present</div>
    <ul class="bullets">
      <li>Built machine learning models in Python to predict IPL match outcomes using historical match statistics and performance metrics.</li>
      <li>Trained predictive algorithms with feature engineering on multi-season match data.</li>
    </ul>
  </div>

  <div class="main-heading">Publications</div>
  <ul class="bullets" style="margin-bottom: 0;">
    <li><strong>AI Based Predictive Caching</strong> — Published April 2026</li>
    <li><strong>IPL Winning Predictions Using Machine Learning</strong> — Published November 2025</li>
  </ul>

  <div class="main-heading">Certifications</div>
  <ul class="bullets" style="margin-bottom: 0;">
    <li>Data Science — Board Infinity</li>
    <li>Cloud Computing & Machine Learning — NASSCOM</li>
    <li>Full Stack Web Development — MongoDB</li>
    <li>Natural Language Processing — UpGrad</li>
    <li>Computer Networks — SRM Vadapalani & SkillUp</li>
    <li>Project Publication — IJARCCE</li>
  </ul>
</div>""",
            unsafe_allow_html=True,
        )