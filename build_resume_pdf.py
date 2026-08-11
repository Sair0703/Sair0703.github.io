"""Generate a clean, one-page, ATS-friendly resume PDF with clickable links."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_RIGHT
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

OUT = "/Users/saianand/Downloads/Sai_Anand_Resume.pdf"
INK = HexColor("#1a1a1a"); MUT = HexColor("#444444"); LINK = HexColor("#1a56db")
ACC = HexColor("#111111")

ss = getSampleStyleSheet()
name = ParagraphStyle("name", parent=ss["Normal"], fontName="Helvetica-Bold",
                      fontSize=17, textColor=INK, spaceAfter=2, alignment=1)
contact = ParagraphStyle("contact", parent=ss["Normal"], fontSize=8.5, textColor=MUT, alignment=1, spaceAfter=1, leading=10.5)
sec = ParagraphStyle("sec", parent=ss["Normal"], fontName="Helvetica-Bold", fontSize=9.5, textColor=ACC, spaceBefore=5, spaceAfter=1, tracking=1)
role = ParagraphStyle("role", parent=ss["Normal"], fontSize=9.1, textColor=INK, leading=10.8)
date = ParagraphStyle("date", parent=ss["Normal"], fontSize=8.4, textColor=MUT, alignment=TA_RIGHT, leading=10.8)
sub = ParagraphStyle("sub", parent=ss["Normal"], fontSize=8.2, textColor=MUT, leading=9.8, spaceAfter=0.5)
bullet = ParagraphStyle("bullet", parent=ss["Normal"], fontSize=8.7, textColor=INK,
                        leading=10.4, leftIndent=11, firstLineIndent=-8, spaceAfter=0.8)
skill = ParagraphStyle("skill", parent=ss["Normal"], fontSize=8.6, textColor=INK, leading=11, spaceAfter=0.5)

def L(url, text=None):  # clickable link
    return f'<a href="https://{url}" color="#1a56db">{text or url}</a>'

doc = SimpleDocTemplate(OUT, pagesize=letter, leftMargin=0.5*inch, rightMargin=0.5*inch,
                        topMargin=0.4*inch, bottomMargin=0.35*inch)
E = []

def rule():
    E.append(HRFlowable(width="100%", thickness=0.6, color=HexColor("#bbbbbb"), spaceBefore=1, spaceAfter=3))

def header(title):
    E.append(Paragraph(title.upper(), sec)); rule()

def entry(left_html, dates, bullets, subline=None):
    t = Table([[Paragraph(left_html, role), Paragraph(dates, date)]],
              colWidths=[5.2*inch, 2.2*inch])
    t.setStyle(TableStyle([("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                           ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
                           ("VALIGN",(0,0),(-1,-1),"TOP")]))
    E.append(t)
    if subline: E.append(Paragraph(subline, sub))
    for b in bullets: E.append(Paragraph("•  " + b, bullet))
    E.append(Spacer(1, 2.5))

# ---- Header ----
E.append(Paragraph("SAIRISHABH (SAI) ANAND", name))
E.append(Paragraph("(626) 541-4651 &nbsp;·&nbsp; sa0316151@gmail.com &nbsp;·&nbsp; U.S. Permanent Resident (Green Card)", contact))
E.append(Paragraph(f'{L("sair0703.github.io","Portfolio")} &nbsp;·&nbsp; {L("github.com/Sair0703","GitHub")} &nbsp;·&nbsp; {L("linkedin.com/in/sai-anand","LinkedIn")}', contact))
E.append(Spacer(1, 4))

# ---- Experience ----
header("Experience")
entry("<b>GridRaster</b> — Computer Vision &amp; Spatial Intelligence Engineer (Intern &rarr; Full-Time Offer)", "May 2026 – Present", [
  "Built a 3D depth-reconstruction pipeline for aerospace part inspection — Apple Vision Pro capture &rarr; FoundationStereo stereo depth &rarr; GPU processing on an NVIDIA DGX Spark — engineering the AVP-server &harr; Mac-server system that streams and processes each scan.",
  "Reached 1.5–2.2 mm median as-built-vs-CAD accuracy on aircraft components (best in the company, matching the prior HoloLens benchmark), validated against MetraScan metrology ground truth via CloudCompare point-picking (10 scans × 28 measurements per part).",
  "Built a markerless scene-change-detection system with a claims-based test harness (24/24 automated checks); caught a registration-metric bug inflating error ~5×, then certified alignment with no external ground truth via closure (0.62 cm over 3 hops) and zero false positives on controls.",
])
entry("<b>Prox</b> — Software Engineer Intern", "Mar 2026 – May 2026", [
  "Cut store-distance query latency 60%+ (to &lt;500 ms) across a deal-intelligence engine spanning 10,000+ stores by introducing PostGIS spatial indexing and bounding-box pre-filtering.",
  "Held 5,000+ concurrent users in load tests by engineering an event-driven push-notification pipeline (deduplication, rate-limiting, real-time price-delta detection) feeding a multi-factor ranking algorithm.",
  "Architected an end-to-end data pipeline (scraper &rarr; normalization &rarr; storage &rarr; scoring &rarr; notification) with strict stage boundaries so each service scales independently.",
])
entry("<b>NULogic (NU Technology Inc.)</b> — Product &amp; Systems Engineering Intern", "Jan 2026 – Mar 2026", [
  "Accelerated sprint planning and cross-team alignment by translating product requirements into API contracts, data models, and event-driven architecture designs.",
  "Prevented costly late-stage rework by flagging scalability and performance constraints during early design reviews.",
])

# ---- Projects ----
header("Projects")
entry(f'<b>Redline</b> — Self-Verifying Agentic AI Code Reviewer', "Python, FastAPI, LLM, SSE", [
  "Cut false positives in LLM code review with a two-stage agentic pipeline: a <i>find</i> pass flags defects in any git diff or GitHub PR, and an adversarial <i>verify</i> pass challenges each finding before it is shown — grounded to exact file:line via unified-diff parsing.",
  "Reviews real GitHub PRs with full-file context and posts inline comments; streams live review traces to a React UI via server-sent events with severity-ranked findings and fixes.",
], subline=f'{L("redline-cs25.onrender.com","Live demo")} &nbsp;·&nbsp; {L("github.com/Sair0703/Redline","Code")}')
entry(f'<b>Wanderly</b> — AI-Powered Travel Recommendation Platform', "FastAPI, React, PostgreSQL, Redis, Docker, LLM", [
  "Built a content + behavioral recommendation engine with explainable matches, a multi-turn natural-language concierge, and an LLM day-by-day itinerary planner over real worldwide listing data.",
  "Scaled personalization with Redis caching and Docker; hardened with rate limiting, HTTPS/HSTS, and CSP; backend covered by 20 passing automated tests.",
], subline=f'{L("wanderly-p5v1.onrender.com","Live demo")} &nbsp;·&nbsp; {L("github.com/Sair0703/Wanderly","Code")}')
entry(f'<b>Real-Time Sign Language Detection</b>', "Python, TensorFlow, OpenCV, MediaPipe, LSTM", [
  "Achieved 92% accuracy across 20+ ASL gesture classes at 20–25 FPS on CPU by training an LSTM on MediaPipe keypoint features with a real-time inference pipeline.",
], subline=f'{L("sair0703.github.io/Sign-Language-Project","Live demo")} &nbsp;·&nbsp; {L("github.com/Sair0703/Sign-Language-Project","Code")}')

# ---- Hackathons ----
header("Hackathons &amp; Awards")
E.append(Paragraph("<b>ARM Create AI Optimization Challenge</b> (Hackathon) — Optimized AI model inference for efficient, low-latency execution on ARM-based edge hardware, aligned with production edge-AI work at GridRaster (an ARM partner).", bullet))
E.append(Spacer(1, 2.5))

# ---- Education ----
header("Education")
entry("<b>Oregon State University</b> — B.S. Computer Science &nbsp;·&nbsp; GPA: 3.8 / 4.0", "June 2025", [])

# ---- Skills ----
header("Technical Skills")
for line in [
  "<b>Languages:</b> JavaScript/TypeScript, Python, Java, C/C++, SQL, HTML/CSS",
  "<b>Frameworks &amp; DBs:</b> React, Node.js, FastAPI, Django, Express, Next.js, PostgreSQL (PostGIS), MongoDB, Redis",
  "<b>Cloud &amp; Infra:</b> AWS (EC2, S3, Lambda, RDS), Docker, Git, Linux, CI/CD, REST APIs, microservices, event-driven architecture",
  "<b>AI / ML / CV:</b> PyTorch, TensorFlow, OpenCV, MediaPipe, scikit-learn, LLM agents &amp; tool-use, object detection, depth estimation, 3D reconstruction, edge inference",
]:
    E.append(Paragraph(line, skill))

# ---- Certs ----
header("Certifications")
E.append(Paragraph("TensorFlow Developer Certificate (Google) &nbsp;·&nbsp; AWS Certified Cloud Practitioner &nbsp;·&nbsp; Machine Learning Specialization (DeepLearning.AI)", skill))

doc.build(E)
print("wrote", OUT)
