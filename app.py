from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="ROHIT VIKRAANTH S | RESUME",
    page_icon="📄",
    layout="centered",
)

# Custom CSS to match the exact template layout and styling
st.markdown(
    """
<style>
  /* Reset and outer container */
  .block-container {
    max-width: 900px;
    padding: 1.5rem 1rem 3rem 1rem;
  }
  
  /* Resume Outer Canvas */
  .resume-container {
    background-color: #ffffff;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    border-radius: 4px;
    overflow: hidden;
    color: #1e293b;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }

  /* Top Slate Header Banner */
  .resume-header {
    background-color: #2e353d;
    padding: 3rem 2.5rem;
    color: #ffffff;
  }
  .resume-name {
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin: 0;
  }
  .resume-role {
    font-size: 1.15rem;
    color: #cbd5e1;
    font-weight: 400;
    margin-top: 0.4rem;
  }

  /* Split Layout Body */
  .resume-body {
    display: flex;
    min-height: 700px;
  }

  /* Left Sidebar (Beige/Warm Tint) */
  .sidebar-left {
    background-color: #e9e4dc;
    width: 38%;
    padding: 2.2rem 1.8rem;
    box-sizing: border-box;
  }

  /* Right Main Content Panel (Clean White) */
  .content-right {
    background-color: #ffffff;
    width: 62%;
    padding: 2.2rem 2.2rem;
    box-sizing: border-box;
  }

  /* Section Titles */
  .sidebar-heading {
    font-size: 1.15rem;
    font-weight: 700;
    color: #1e293b;
    margin-bottom: 0.9rem;
    margin-top: 1.5rem;
  }
  .sidebar-heading:first-child {
    margin-top: 0;
  }

  .main-heading {
    font-size: 1.25rem;
    font-weight: 700;
    color: #1e293b;
    border-bottom: 2px solid #1e293b;
    padding-bottom: 0.35rem;
    margin-bottom: 1.1rem;
    margin-top: 1.8rem;
  }
  .main-heading:first-child {
    margin-top: 0;
  }

  /* Left Column Specific Details */
  .contact-item {
    font-size: 0.9rem;
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
    gap: 0.6rem;
    color: #334155;
    word-break: break-all;
  }
  .contact-item a {
    color: #334155;
    text-decoration: none;
  }
  .education-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: #0f172a;
    line-height: 1.35;
  }
  .education-sub {
    font-size: 0.88rem;
    color: #475569;
    margin-top: 0.2rem;
  }
  .skill-item {
    font-size: 0.9rem;
    color: #334155;
    margin-bottom: 0.6rem;
  }

  /* Right Column Specific Details */
  .summary-text {
    font-size: 0.93rem;
    line-height: 1.6;
    color: #334155;
  }
  .job-title {
    font-size: 1.05rem;
    font-weight: 700;
    color: #0f172a;
  }
  .job-date {
    font-size: 0.85rem;
    color: #64748b;
    margin-bottom: 0.45rem;
  }
  .project-bullets {
    padding-left: 1.2rem;
    margin-top: 0.2rem;
    margin-bottom: 1.3rem;
    color: #334155;
    font-size: 0.91rem;
    line-height: 1.55;
  }

  /* Responsive Stacking for Small Mobile Screens */
  @media (max-width: 680px) {
    .resume-body {
      flex-direction: column;
    }
    .sidebar-left, .content-right {
      width: 100%;
    }
  }
</style>
""",
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

# Main Resume Structure HTML
st.markdown(
    """
<div class="resume-container">
  <!-- Header Banner -->
  <div class="resume-header">
    <h1 class="resume-name">Rohit Vikraanth S</h1>
    <div class="resume-role">Full Stack Developer & Machine Learning Enthusiast</div>
  </div>

  <!-- Main Body Split -->
  <div class="resume-body">
    
    <!-- Left Column (Contact, Education, Skills) -->
    <div class="sidebar-left">
      <div class="sidebar-heading">Contact Details</div>
      <div class="contact-item">✉️ <a href="mailto:rs5483@srmist.edu.in">rs5483@srmist.edu.in</a></div>
      <div class="contact-item">📞 +91 9080345650</div>
      <div class="contact-item">📍 Chennai, India</div>

      <div class="sidebar-heading">Education</div>
      <div style="margin-bottom: 1.2rem;">
        <div class="education-title">• Bachelor of Technology in Computer Science & Engineering</div>
        <div class="education-sub">SRM Institute of Science and Technology, Vadapalani</div>
        <div class="education-sub">2023 – 2027 | CGPA: 7.81 / 10</div>
      </div>

      <div class="sidebar-heading">Skills</div>
      <div class="skill-item">Full Stack Web Development</div>
      <div class="skill-item">Machine Learning & Deep Learning</div>
      <div class="skill-item">Python Programming</div>
      <div class="skill-item">Java Development</div>
      <div class="skill-item">C++ Programming</div>
      <div class="skill-item">MySQL Database Management</div>
      <div class="skill-item">Frontend (HTML, CSS, JavaScript)</div>
      <div class="skill-item">Business Analytics</div>
    </div>

    <!-- Right Column (Summary, Projects, Publications, Certifications) -->
    <div class="content-right">
      <div class="main-heading">Summary</div>
      <div class="summary-text">
        Motivated B.Tech Computer Science and Engineering student with a strong interest in Full Stack Development and Machine Learning. Skilled in developing data-driven applications using Python, Java, JavaScript, and modern web technologies. Passionate about building scalable software solutions, applying artificial intelligence to real-world problems, and continuously learning emerging technologies.
      </div>

      <div class="main-heading">Work & Projects</div>
      
      <div>
        <div class="job-title">AI-Based Predictive Caching</div>
        <div class="job-date">March 2026 – Present</div>
        <ul class="project-bullets">
          <li>Developed an AI-based predictive caching solution using Python, TensorFlow, and LSTM to improve Content Delivery Network (CDN) performance.</li>
          <li>Applied sequence prediction techniques to optimize caching decisions and significantly reduce latency.</li>
          <li>Research track: <a href="https://ijpub.org/ijvra/track.php" target="_blank" style="color: #2563eb; text-decoration: none;">ijpub.org/ijvra/track.php ↗</a></li>
        </ul>
      </div>

      <div>
        <div class="job-title">IPL Team Winning Prediction Dataset</div>
        <div class="job-date">October 2025 – Present</div>
        <ul class="project-bullets">
          <li>Built machine learning models in Python to predict IPL match outcomes using historical match statistics and performance metrics.</li>
          <li>Trained predictive algorithms with feature engineering on multi-season match data.</li>
        </ul>
      </div>

      <div class="main-heading">Publications</div>
      <ul class="project-bullets" style="margin-bottom: 0;">
        <li><strong>AI Based Predictive Caching</strong> — Published April 2026</li>
        <li><strong>IPL Winning Predictions Using Machine Learning</strong> — Published November 2025</li>
      </ul>

      <div class="main-heading">Certifications</div>
      <ul class="project-bullets" style="margin-bottom: 0;">
        <li>Data Science — Board Infinity</li>
        <li>Cloud Computing & Machine Learning — NASSCOM</li>
        <li>Full Stack Web Development — MongoDB</li>
        <li>Natural Language Processing — UpGrad</li>
        <li>Computer Networks — SRM Vadapalani & SkillUp</li>
        <li>Project Publication — IJARCCE</li>
      </ul>
    </div>

  </div>
</div>
""",
    unsafe_allow_html=True,
)