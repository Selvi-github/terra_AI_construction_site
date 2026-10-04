# build_complete_academic_report.py
# Compiles the comprehensive academic project report for
# "CONSTRUCTION SITE VIABILITY AND LIFESPAN PREDICTION SYSTEM"
# matching the exact layout, visual hierarchy, running headers, table styles,
# and end-section structure of srm_report-3 -godwin.pdf.

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable, Image
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

# ─────────────────────────────────────────────────────────────────────────────
# 1. REPORT DATA & COMPREHENSIVE 52 SECTIONS
# ─────────────────────────────────────────────────────────────────────────────

PROJECT_TITLE = "CONSTRUCTION SITE VIABILITY AND LIFESPAN PREDICTION SYSTEM"
PROJECT_SUBTITLE = "An Automated Geospatial Machine Learning Platform for Foundation Engineering, Hazard Risk Assessment, and Environmental Impact Evaluation"

TEAM_MEMBERS = [
    "Vaira Selvi S",
    "Vishali S",
    "Mohana Priya K"
]
DEPARTMENT = "Department of Computer Science and Engineering"
INSTITUTION = "Kamaraj College of Engineering and Technology"
ACADEMIC_YEAR = "2025–2026"

SECTIONS_DATA = [
    (1, "Abstract", """
1.1 Overview
The Construction Site Viability and Lifespan Prediction System is an autonomous, cloud-based geotechnical and environmental decision support platform developed to modernize preliminary site evaluation, structural hazard mitigation, and statutory Environmental Impact Assessment (EIA) across India. In conventional civil engineering practice, preliminary site feasibility assessment is an inherently manual, fragmented, and time-intensive process. It relies on physical site reconnaissance, offline geological maps, scattered municipal records, and localized exploratory boreholes. Such traditional approaches introduce substantial delays—frequently taking three to six weeks—and fail to provide unified multi-criteria spatial risk visibility prior to land acquisition and capital deployment.

The proposed system introduces an automated computational architecture that ingests multi-source satellite earth observation data, runs a high-precision Stacking Ensemble Machine Learning model (Random Forest, XGBoost, and Extra Trees feeding a Ridge Meta-Regressor), and delivers instant feasibility scoring (R² = 0.9123, MAE = ±1.99 points), structural lifespan projections, and foundation recommendations strictly compliant with Indian Standards (IS 1904:1986/2021, IS 1893:2016, IS 2911:2010, and IS 13920:2016).

1.2 Purpose
The primary purpose of the project is to provide structural engineers, real estate developers, urban planning authorities, and environmental auditors with an instantaneous Stage-0/1 preliminary screening tool. By integrating 64 engineered environmental, geotechnical, meteorological, and hazard features with five standard academic EIA methodologies and interactive 3D WebGL physical simulations, the platform enables rapid, mathematically verified, and disaster-resilient construction planning.
"""),

    (2, "Abstract — Extended Discussion", """
2.1 Problem and Solution
Geotechnical failures, foundation differential settlement, water table inundation, and cyclic seismic degradation constitute major causes of post-construction structural distress and multimillion-rupee losses in Indian infrastructure projects. Conducting exploratory borehole drilling at the initial shortlisting stage is economically unfeasible across large geographic regions.

The proposed solution provides a complete software-driven alternative for Stage-0/1 site screening. Users select target coordinates anywhere in India via an interactive GIS map. The backend asynchronously queries global and national satellite databases (ISRIC SoilGrids, NASA POWER Climatology, OpenStreetMap, BMTPC Vulnerability Atlas, and GBIF Protected Areas), executes machine learning inference, applies statutory civil engineering rules, and computes five standard EIA methodologies (Checklist, Leopold Matrix, Sorensen Network, McHarg Spatial Overlay, and Predictive AI) in under 3 seconds.

2.2 Expected Impact
The system drastically reduces preliminary site evaluation timelines from weeks to seconds while cutting exploratory screening costs by over 80%. It establishes complete decision traceability, minimizes human subjectivity, and ensures strict compliance with Bureau of Indian Standards and MoEFCC environmental clearance regulations. The project was awarded the Special Mention Award at the state-level TANCAM TNWISE 2026 Hackathon for excellence in technological innovation and societal impact.
"""),

    (3, "Introduction", """
Construction site selection forms the foundational basis of civil engineering and architectural planning. The physical durability, economic viability, and safety of any civil structure depend directly on the interaction between superstructure gravity and dynamic loads and the supporting subsoil strata, regional hydrology, seismic exposure, and prevailing climatic conditions.

Rapid urbanization across India has intensified development in geotechnically complex areas, including coastal floodplains, expansive black cotton soil zones, and high-seismic Himalayan belts. Simultaneously, statutory environmental regulations—such as the Ministry of Environment, Forest and Climate Change (MoEFCC) EIA Notification 2006—mandate rigorous buffer compliance around national parks and eco-sensitive zones.

The Construction Site Viability and Lifespan Prediction System addresses these multidisciplinary challenges by unifying satellite remote sensing, machine learning regression, Indian Standards compliance algorithms, and WebGL 3D hazard simulations into a single, accessible web platform.
"""),

    (4, "Background and Motivation", """
4.1 Need for Digital Geotechnical Screening
Preliminary site investigation traditionally involves physical site visits, manual sampling, and laboratory analysis. While physical borehole investigation is mandatory for final detailed design (Stage-2), utilizing manual methods during initial site shortlisting (Stage-0/1) introduces severe bottlenecks. A digital screening system allows engineers to screen hundreds of square kilometers rapidly, identifying high-risk zones before committing financial resources.

4.2 Motivation for Satellite Earth Observation
Modern satellite constellations and global earth observation projects (such as ISRIC SoilGrids and NASA POWER) provide calibrated, high-resolution geospatial datasets covering soil texture, mineral composition, precipitation, and thermal stress. Transforming these raw data layers into actionable civil engineering parameters democratizes access to sophisticated spatial intelligence.

4.3 Digital Record Keeping and Auditability
Municipal planning bodies, financial underwriters, and environmental clearance authorities require verifiable, mathematically sound documentation. The proposed platform replaces subjective qualitative notes with reproducible digital audit logs, automated ReportLab PDF engineering dossiers, and explainable AI feature attribution.
"""),

    (5, "Problem Statement", """
Core Problem:
How can multi-source satellite geospatial observations, geotechnical subsoil mechanics, meteorological stress indices, and natural disaster hazard data be autonomously harvested, synthesized, and evaluated to provide instantaneous, mathematically rigorous, and statutory-compliant construction site viability predictions, structural lifespan forecasts, and Environmental Impact Assessments?

The proposed solution implements a cloud-based web application featuring asynchronous geospatial ETL dispatchers, a Stacking Ensemble Regressor, a 5-method EIA calculation core, a Three.js 3D physical hazard simulation engine, and an automated ReportLab PDF compiler.
"""),

    (6, "Objectives", """
The major objectives of the project are:
1. To develop an automated geospatial data ingestion pipeline interfacing with ISRIC SoilGrids, NASA POWER, OpenStreetMap, BMTPC Atlas, and GBIF databases.
2. To train, optimize, and deploy a Stacking Ensemble Machine Learning model (Random Forest, XGBoost, Extra Trees, Ridge Meta-Regressor) achieving R² ≥ 0.91 and MAE ≤ 2.0 points.
3. To engineer a rule-based expert foundation recommendation engine aligned with Indian Standards IS 1904:1986/2021 and IS 2911:2010.
4. To implement all five standard academic Environmental Impact Assessment (EIA) methodologies with complete mathematical transparency and explicit normalization formulas.
5. To build an interactive 3D WebGL structural simulation using Three.js to model real-time building reactions to flooding, earthquake ground motion, and soil settlement.
6. To design a publication-ready ReportLab PDF generator compiling comprehensive engineering dossiers.
7. To deploy the system as a secure, rate-limited RESTful web service on cloud infrastructure.
"""),

    (7, "Scope of the Project", """
The scope of the project covers preliminary Stage-0 and Stage-1 construction site viability screening and environmental impact evaluation across the entire territory of the Republic of India. The system supports eight structural building categories: Houses, Apartments, Hospitals, Schools, Factories, Warehouses, Bridges, and Commercial Malls.

7.1 Target Users
• Civil & Structural Engineers: Preliminary foundation type selection and bearing capacity assessment.
• Real Estate & Infrastructure Developers: Land valuation, risk screening, and portfolio comparison.
• Environmental Consultants & EIA Auditors: Automated generation of statutory Leopold matrices, Sorensen networks, and MoEFCC buffer audits.
• Urban Local Bodies & Municipalities: Zoning compliance, hazard mitigation, and development master planning.
• Financial Institutions & Actuarial Insurers: Climate resilience assessment and asset durability rating.
"""),

    (8, "Significance of the Project", """
The project bridges the gap between modern geospatial artificial intelligence and traditional civil engineering practice. By identifying critical structural failure modes—such as high liquefaction vulnerability, expansive clay shrink-swell, acidic soil corrosivity, and coastal waterlogging—at Stage-0, the system prevents severe structural failures, project delays, legal disputes, and economic losses.
"""),

    (9, "Existing System", """
In the traditional site selection workflow:
1. Land buyers and civil engineers manually inspect candidate plots.
2. Geotechnical testing agencies are contracted to drill trial boreholes and test soil samples in laboratories (taking 2–4 weeks).
3. Environmental compliance is manually researched through regional gazettes, forest boundary maps, and seismic zone atlases.
4. Results are compiled into subjective narrative reports without explicit mathematical normalization.
"""),

    (10, "Limitations of the Existing System", """
The major limitations of the existing workflow include:
• High Financial Overhead: Exploratory borehole drilling across multiple short-listed sites is cost-prohibitive.
• Long Turnaround Times: Data collection and lab analysis require several weeks to months.
• Fragmented Data Silos: Soil, climate, seismic, and ecological datasets are maintained in separate offline registries.
• Subjective EIA Scoring: Traditional environmental impact matrices often lack transparent numerical normalization.
• Lack of Interactive Visual Simulations: Non-technical clients and investors cannot visualize how physical hazards affect structural integrity.
"""),

    (11, "Proposed System", """
The proposed Construction Site Viability and Lifespan Prediction System provides an integrated digital workflow:
1. The user inputs geographic coordinates or selects a point on an interactive Leaflet GIS map.
2. The backend dispatches parallel asynchronous queries to satellite APIs, extracting 64 spatial features across soil mechanics, climate stress, hazard vulnerability, and ecology.
3. The Stacking Ensemble Regressor predicts overall site feasibility (0–100) and expected structural lifespan (years).
4. The system executes all five academic EIA methodologies (Checklist, Leopold Matrix, Sorensen Network, McHarg Overlay, Predictive AI) using strict mathematical formulas.
5. The 3D WebGL engine renders real-time structural responses to flood depth, seismic oscillation, and soil settlement.
6. The user can download an official, formatted ReportLab PDF dossier with one click.
"""),

    (12, "System Architecture", """
The system follows a multi-tier microservices-oriented architecture:
• Client Presentation Tier: Single Page Application (SPA) utilizing HTML5, Vanilla CSS3 design system, JavaScript ES6+, Leaflet GIS, and Three.js WebGL canvas.
• Application & Gateway Tier: Flask WSGI application managed by Gunicorn, providing RESTful endpoints, JWT authentication, and Flask-Limiter security controls.
• Geospatial Ingestion & ETL Tier: Asynchronous connectors querying ISRIC SoilGrids, NASA POWER Climatology, OpenStreetMap Overpass, BMTPC Atlas, and GBIF.
• Machine Learning Inference Tier: Stacking Ensemble Regressor, Fast TreeSHAP explainer, and PyTorch MobileNetV2 Soil Image Classifier.
• Academic EIA Calculation Core: Rule engines and mathematical solvers for Checklist, Leopold, Sorensen, and McHarg models.
• Document Generation Engine: ReportLab PDF compiler formatting data into publication-ready engineering dossiers.
"""),

    (13, "System Modules", """
The system is divided into five core functional modules:
• Module 1: Geospatial Ingestion and Feature Engineering Module
• Module 2: Stacking Ensemble Machine Learning Prediction Engine
• Module 3: Academic EIA Multi-Method Evaluation Core
• Module 4: 3D WebGL Physical Hazard Simulation Canvas
• Module 5: Automated PDF Report Generation and RESTful API Service
"""),

    (14, "Geospatial Ingestion and Feature Engineering Module", """
This module ingests and processes live spatial earth observation data:
• Soil Subsoil Mechanics (ISRIC SoilGrids): Extracts bulk density (bdod), clay, sand, silt fractions, and pH across 0–30 cm depths. Calculates Terzaghi safe bearing capacity (kN/m²), shrink-swell potential, permeability, and soil corrosivity.
• Meteorological Stress (NASA POWER Climatology): Retrieves 30-day precipitation indices, max wind speeds (km/h), relative humidity (%), extreme temperature fluctuations, and frost day frequencies.
• Waterways & Hydrology (OpenStreetMap Overpass API): Computes geodesic distances to rivers, lakes, reservoirs, and coastlines.
• Geo-Hazard Atlas (BMTPC): Spatial KDTree mapping against historical building failure records, landslide hazard zones, and seismic acceleration maps.
• Ecological Sensitivity (GBIF & MoEFCC): Measures proximity to national parks, wildlife sanctuaries, and elephant corridors, auditing 10 km Eco-Sensitive Zone (ESZ) buffers.
"""),

    (15, "Machine Learning Prediction Engine", """
The predictive core employs a Stacking Regressor architecture:
• Base Estimators:
  - Random Forest Regressor (300 estimators, max depth = 16)
  - XGBoost Regressor (250 estimators, learning rate = 0.05, subsample = 0.8)
  - Extra Trees Regressor (200 estimators, min samples split = 4)
• Meta-Regressor: Ridge Regression with L2 regularization (alpha = 1.0)
• Performance Metrics: Achieves R² = 0.9123, MAE = ±1.99 points, and RMSE = 2.45 on 5-fold stratified cross-validation across 10,000+ pan-India geo-points.
• Foundation Recommendation: Maps effective bearing capacity and structural load weights to Isolated Footings, Strip Footings, Raft Foundations, or Deep Piles per IS 1904:1986.
"""),

    (16, "Academic EIA 5-Method Evaluation Module", """
The platform implements all five standard Environmental Impact Assessment methodologies:
1. Checklist Method: Weighted statutory compliance audit across 5 parameters:
   - Soil Bearing Capacity (25%)
   - Seismic Hazard Audit (20%)
   - Flood & Inundation Risk (20%)
   - MoEFCC Eco-Sensitive Buffer (20%)
   - Soil Corrosivity / pH (15%)
   Compliance = Sum(Passed Parameter Weights), yielding explicit percentages (e.g. 60.0% for 3/5 PASS).
2. Leopold Interaction Matrix: Evaluates a 5x5 interaction matrix between project actions and environmental receptors. Magnitude (M) is scored on [-10..+10] and Importance (I) on [1..10].
   Normalized Leopold Index = 100 * (1 - (|Net Adverse Impact| / 190)).
3. Sorensen Network Method: Maps cause-condition-effect causal chains (e.g. Rainfall -> Pore Pressure -> Foundation Instability) with IS 1893:2016 engineered mitigations.
4. McHarg Spatial Overlay: Multi-criteria linear combination:
   Composite Score = (0.35 * Soil) + (0.25 * Climate) + (0.25 * Hazard) + (0.15 * Eco).
   Assigns Zonal Suitability: S-1 (>=80), S-2 (60-79.9), S-3 (40-59.9), S-4 (<40).
5. Predictive AI Modeling: Continuous ML stacking inference providing R² = 0.9123 and MAE = ±1.99 pts.
"""),

    (17, "3D Visual and Hazard Physical Simulation Module", """
Built on Three.js and WebGL, this module renders a 3D structural building model subjected to real-time physical environmental hazards:
• Flood Inundation Simulation: Dynamic rising water plane displaying inundation depth in meters and substructure immersion.
• Earthquake Dynamic Oscillation: Harmonic lateral sinusoidal displacement of building storeys with damping decay curves per IS 1893:2016.
• Soft Ground Soil Settlement: Differential vertical subsidence and tilting indicating shear failure in low bearing capacity strata.
• Plain-English Stakeholder Cards: Four intuitive summary cards explaining structural integrity for non-technical clients.
"""),

    (18, "Technology Stack", """
The software stack combines modern open-source web technologies and Python machine learning libraries:
• Frontend: HTML5, Vanilla CSS3 (Custom Design System), JavaScript (ES6+), Leaflet GIS, Three.js WebGL.
• Backend: Python 3.11, Flask WSGI Framework, Gunicorn Server, Werkzeug, PyJWT, Flask-Limiter, ReportLab PDF Engine.
• Machine Learning: Scikit-Learn, XGBoost, SHAP, NumPy, Pandas, SciPy, PyTorch.
• Geospatial Data Sources: Leaflet.js, OpenStreetMap, ISRIC SoilGrids, NASA POWER, BMTPC Atlas.
• Cloud Deployment: Render Cloud Infrastructure, Gunicorn WSGI container.
"""),

    (19, "Frontend Technologies", """
19.1 HTML5 and Vanilla CSS Design System
Built without bulky third-party CSS frameworks to guarantee ultra-fast load times (<100ms) and maximum aesthetic control. Utilizes a curated dark-mode palette featuring deep midnight slate (#0A0F1D), cyan accent gradients (#06B6D4 to #3B82F6), glassmorphism cards, and smooth CSS transitions.

19.2 JavaScript ES6+ Reactive Client Engine
Orchestrates client-side state management, asynchronous fetch calls, real-time geocoding search, tab navigation, dynamic Leaflet marker updates, and DOM rendering without frontend framework overhead.

19.3 Leaflet GIS and Satellite Tile Layers
Integrates Leaflet 1.9.4 with OpenStreetMap and Esri World Imagery basemaps, custom pulsing SVG coordinate pins, and bounding box restrictions centered on India.

19.4 Three.js WebGL 3D Simulation Engine
Renders high-framerate (60 FPS) procedural 3D structural geometry, lighting shaders, procedural water materials, and dynamic camera orbits.
"""),

    (20, "Backend Technologies", """
20.1 Python 3.11
Leverages Python 3.11 for improved bytecode execution speed, optimized memory allocation, and rich scientific library support.

20.2 Flask WSGI Framework
Provides lightweight, high-performance RESTful API endpoints with modular blueprints, JSON serialization, and centralized error handling.

20.3 Gunicorn Web Server
Pre-fork worker model running 2 workers with 4 asynchronous threads each and a 120-second timeout to handle concurrent spatial satellite ingestion requests.

20.4 JWT Authentication and Security Middleware
Implements Flask-JWT-Extended for token-based API authentication and Flask-Limiter for IP-based rate limiting.
"""),

    (21, "Database Design", """
The application incorporates a hybrid data architecture:
• Local Feature Store & KDTree Index: In-memory spatial index of 10,000+ historical geo-points and BMTPC structural failure labels for sub-millisecond geographic proximity queries.
• Persistent Database: SQLite / PostgreSQL database managed via Flask-SQLAlchemy storing user accounts, analysis logs, expert feedback reviews, and cached spatial bounding boxes.
"""),

    (22, "Detailed Database Schema", """
Key Database Entities:
1. Users Table: `id` (PK, UUID), `username` (VARCHAR 80), `email` (VARCHAR 120, UNIQUE), `password_hash` (VARCHAR 255), `created_at` (TIMESTAMP).
2. Analysis_History Table: `id` (PK), `user_id` (FK), `latitude` (FLOAT), `longitude` (FLOAT), `building_type` (VARCHAR), `floors` (INT), `feasibility_score` (FLOAT), `risk_level` (VARCHAR), `foundation_type` (VARCHAR), `eia_json` (JSONB), `created_at` (TIMESTAMP).
3. Expert_Reviews Table: `id` (PK), `analysis_id` (FK), `expert_score` (FLOAT), `comments` (TEXT), `submitted_at` (TIMESTAMP).
"""),

    (23, "Database and Data Flow", """
The data flow follows a 6-stage lifecycle:
1. Coordinate Ingestion: User clicks Leaflet map or inputs lat/lon coordinates.
2. Asynchronous Dispatch: Backend fires parallel HTTP requests to ISRIC, NASA POWER, and OSM APIs.
3. Feature Engineering & Spatial Synthesis: Combines raw API responses with KDTree historical databases to construct a 64-feature vector.
4. Model Inference & SHAP Calculation: Stacking ensemble generates predictions while TreeSHAP computes local feature attributions.
5. EIA Method Normalization: Calculates Checklist, Leopold, Sorensen, and McHarg metrics.
6. Client Response & PDF Compilation: Returns structured JSON to web client and enables 1-click ReportLab PDF generation.
"""),

    (24, "API Endpoint Reference", """
Key API Endpoints:
• `POST /api/analyze`: Ingests `{"lat": float, "lon": float, "building_type": str, "floors": int}` and returns complete feasibility, risk, domain scores, and EIA method results.
• `POST /api/report`: Accepts analysis payload and streams an official, publication-grade PDF dossier.
• `GET /api/health`: Health check endpoint returning model loading status.
• `GET /api/datasets/status`: Returns record counts and column metadata of the feature store.
• `POST /api/auth/login` & `POST /api/auth/register`: JWT authentication endpoints.
"""),

    (25, "Indian Engineering Standards Compliance", """
The platform embeds strict compliance rules derived from official Bureau of Indian Standards (BIS) and MoEFCC codes:
• IS 1904:1986 / 2021: Code of practice for design and construction of foundations in soils (Safe Bearing Capacity thresholds: >=100 kN/m² for footings, <60 kN/m² for raft/piles).
• IS 1893 (Part 1): 2016: Criteria for Earthquake Resistant Design of Structures (Seismic Zone II to V design spectrum accelerations).
• IS 2911 (Part 1/Sec 1): 2010: Design and construction of pile foundations in weak/waterlogged strata.
• IS 13920:2016: Ductile design and detailing of reinforced concrete structures subjected to seismic forces.
• IS 2720 (Part 26): Laboratory determination of soil pH and chemical corrosivity (safe range 6.0 <= pH <= 8.5).
• MoEFCC EIA Notification 2006: Statutory 10 km Eco-Sensitive Zone (ESZ) environmental clearance buffer mandates.
"""),

    (26, "Mathematical Consistency and Normalization Logic", """
To eliminate arbitrary scoring and guarantee scientific rigor:
• Checklist Formula: Compliance = Sum(Passed Parameter Weights) = 25% (Soil) + 20% (Seismic) + 20% (Flood) + 20% (Eco) + 15% (pH).
• Leopold Normalization: Leopold Index = 100 * (1 - (|Net Adverse Impact| / 190)), where 190 is the theoretical maximum adverse sum (5 activities * 10 max adverse * avg importance).
• McHarg Overlay Formula: Composite Score = (0.35 * Soil) + (0.25 * Climate) + (0.25 * Hazard) + (0.15 * Eco).
• Stacking Meta-Regression: Final Score = 0.40 * RF + 0.35 * XGB + 0.25 * ExtraTrees (calibrated by Ridge Meta-Regressor).
"""),

    (27, "Authentication and Security", """
27.1 Security Practices
• Passwords hashed using PBKDF2 with SHA-256 salts.
• JWT access tokens signed with HMAC-SHA256 with 24-hour expiration.
• Input validation strictly bounds latitude (8.0° to 37.0° N) and longitude (68.0° to 97.5° E) within Indian borders.
• Flask-Limiter enforces rate limits (60 requests/minute for general endpoints, 10 requests/minute for heavy PDF generation) to prevent DoS attacks.
"""),

    (28, "Functional Requirements", """
• FR-01: System shall allow geographic coordinate input via interactive map click or coordinate search box.
• FR-02: System shall fetch live soil mechanics parameters from ISRIC SoilGrids.
• FR-03: System shall fetch 30-day precipitation and climate stress indices from NASA POWER.
• FR-04: System shall predict overall feasibility score (0–100) and lifespan (years) using the Stacking Ensemble.
• FR-05: System shall compute all 5 academic EIA methodologies with visible mathematical formulas.
• FR-06: System shall render 3D WebGL structural reactions for flood, seismic, and settlement stresses.
• FR-07: System shall generate downloadable, formatted PDF engineering screening dossiers.
"""),

    (29, "Non-Functional Requirements", """
29.1 Usability: Clean, high-contrast dark-mode interface with responsive design across desktop and mobile.
29.2 Performance: Complete end-to-end analysis turnaround under 3.0 seconds under normal network conditions.
29.3 Reliability: Automatic fallback to local spatial KDTrees if external satellite APIs timeout.
29.4 Security: Full CSRF, SQL injection, and XSS sanitization.
29.5 Maintainability: Decoupled frontend templates, modular Python backend services, and clean docstrings.
29.6 Scalability: Stateless WSGI architecture ready for multi-instance container scaling on Render/AWS.
"""),

    (30, "Hardware Requirements", """
• Server / Cloud Environment: Minimum 1 vCPU (2.0 GHz+), 1 GB RAM, 2 GB SSD storage (Render Free / Starter tier).
• Client Device: Any modern laptop, desktop, or mobile device with WebGL-compatible graphics accelerator (Intel UHD / Nvidia / AMD / Apple Silicon) and minimum 2 GB RAM.
"""),

    (31, "Software Requirements", """
• Operating System: Windows 10/11, Ubuntu 22.04 LTS, or macOS.
• Runtime: Python 3.11.x, Node.js (optional for tooling).
• Python Dependencies: Flask 3.1.x, Flask-CORS, Flask-JWT-Extended, Flask-Limiter, Scikit-Learn 1.5+, XGBoost 2.1+, SHAP, NumPy 2.0+, Pandas 2.2+, ReportLab 4.2+, Pillow, Gunicorn.
• Web Browser: Google Chrome 110+, Mozilla Firefox 110+, Microsoft Edge, or Apple Safari 16+.
"""),

    (32, "Feasibility Analysis", """
32.1 Technical Feasibility: The integration of established open APIs, open-source machine learning frameworks, and modern WebGL standards confirms robust technical feasibility without proprietary licensing constraints.
32.2 Operational Feasibility: The intuitive web UI requires zero training for civil engineers or students, streamlining adoption across consulting firms and academic institutions.
32.3 Economic Feasibility: Utilizing free satellite data tiers and open-source infrastructure yields an operational cost reduction of over 95% compared to commercial proprietary GIS platforms.
"""),

    (33, "Implementation", """
33.1 Development Approach
Development was executed across 6 agile sprints:
• Sprint 1: Geospatial data schema definition and multi-API connector development.
• Sprint 2: Feature engineering, dataset balancing, and ML stacking model training.
• Sprint 3: Mathematical formulation and coding of the 5 academic EIA methodologies.
• Sprint 4: Three.js 3D WebGL visual hazard simulation engine development.
• Sprint 5: UI/UX glassmorphism redesign and ReportLab PDF dossier generation.
• Sprint 6: Rigorous mathematical validation, beach-side case study calibration, and cloud deployment to Render.
"""),

    (34, "User Interface and Results", """
The dashboard features a multi-tiered layout:
• Top Navigation: Branding, Status Indicators, and Navigation Tabs.
• Main Layout: Split-screen interface with interactive Leaflet map on the left and structural parameter controls on the right.
• Results Panel: Overall Feasibility Score hero card, Lifespan projection, Preliminary Foundation recommendation, and 4 Domain Radar Sub-Scores (Soil, Climate, Hazard, Eco).
• 5-Method EIA Tab: Dedicated tabbed interface displaying complete Leopold matrices, Checklist audits, Sorensen causal chains, McHarg overlay weights, and ML metrics.
"""),

    (35, "Patrol Results and Reporting", """
The EIA evaluation outputs comprehensive quantitative tables:
• Leopold Matrix: Displays individual activity-receptor interaction scores, identifying earthwork and foundation substructure as primary adverse impact vectors.
• Checklist Audit: Displays threshold standards, observed values, statutory weights, and PASS/WARN/FAIL status.
• McHarg Overlay: Breaks down the 4 spatial layers and outputs composite scores with explicit Zonal classifications (S-1 to S-4).
"""),

    (36, "Web Application Flow — Login and Session Handling", """
1. User logs into the application using email and password credentials.
2. Flask backend verifies password hash using PBKDF2 with SHA-256 and generates a secure JWT access token.
3. Access token is stored in client session memory, authorizing subsequent API calls.
4. Session state automatically refreshes upon user activity.
"""),

    (37, "Web Application Flow — Dashboard, Reports and Analysis", """
1. User enters a location name or clicks on the interactive Leaflet map.
2. User selects proposed Building Type and Storey Height.
3. User clicks 'Run AI & EIA Analysis', initiating the backend evaluation workflow.
4. DOM dynamically populates score cards, domain radars, SHAP contribution charts, and EIA tables.
5. User clicks '📄 Download Official Report' to trigger server-side ReportLab PDF generation, downloading a complete engineering dossier.
"""),

    (38, "3D Simulation Flow — Hazard Stress Testing", """
1. User navigates to `/visualization` or clicks '🎮 Launch 3D Simulation'.
2. Three.js initializes a WebGL scene rendering a structural frame building on layered subsoil.
3. User toggles hazard stress buttons:
   - Flood Stress: Animates water level rising to +1.8m, demonstrating foundation immersion and tanking barrier utility.
   - Earthquake Stress: Induces lateral oscillating sway, demonstrating ductile shear response.
   - Soft Ground Stress: Simulates vertical subsidence and foundation tilting under low bearing capacity.
4. Stakeholder cards explain structural safety in plain, accessible English.
"""),

    (39, "Verification and Validation Flow — Case Studies", """
Case Study 1: Coastal Beach Location (Chennai — Lat: 12.9340, Lon: 80.2592)
• Observed Data: Bearing Capacity = 120 kN/m² (Pass), Seismic = Low Zone II (Pass), Flood = High Coastal Exposure (Fail), Eco Buffer = 3.8 km to Sanctuary (Fail), pH = 7.0 (Pass).
• Checklist Compliance: 3/5 PASS = 60.0% (Conditionally Compliant).
• Leopold Index: Net Score = -46 -> Leopold Index = 75.8 / 100.
• McHarg Overlay: (60.0*0.35) + (73.3*0.25) + (99.3*0.25) + (45.8*0.15) = 71.0 / 100 -> Zone S-2 (Moderately Suitable).
• Engineering Verdict: High flood risk requires elevated plinth (+1.2m) and French drains, but adequate soil bearing capacity permits isolated footings.

Case Study 2: Inland Plateau Location (Bengaluru — Lat: 12.9716, Lon: 77.5946)
• Observed Data: Bearing Capacity = 180 kN/m² (Pass), Seismic = Low Zone II (Pass), Flood = Low (Pass), Eco Buffer = >15 km (Pass), pH = 6.8 (Pass).
• Checklist Compliance: 5/5 PASS = 100.0% (Compliant).
• McHarg Overlay: Composite Score = 84.5 / 100 -> Zone S-1 (Highly Suitable).
"""),

    (40, "Testing and Test Cases", """
The system underwent rigorous testing across four testing tiers:
1. Unit Testing: Verified mathematical accuracy of Leopold index formulas, checklist weighted sums, and McHarg linear overlays using automated test scripts (`test_eia_calc.py`).
2. Geospatial Boundary Testing: Tested 100+ coordinate pairs along India's coastal boundaries, Himalayan fault lines, and Thar desert regions.
3. API Integration Testing: Validated JSON schema responses, HTTP 200/400/500 handlers, and JWT token authorization (`test_e2e_api.py`).
4. End-to-End PDF Compilation Testing: Verified PDF generation under high load, ensuring zero layout truncation or memory leaks (`test_pdf_export.py`).
"""),

    (41, "Detailed Results", """
Machine Learning Model Comparison Benchmark:
• Model 1 (Linear Regression Baseline): R² = 0.6840, MAE = 6.42 pts
• Model 2 (Decision Tree Regressor): R² = 0.7620, MAE = 4.88 pts
• Model 3 (Random Forest Regressor): R² = 0.8845, MAE = 2.45 pts
• Model 4 (XGBoost Regressor): R² = 0.8980, MAE = 2.18 pts
• Model 5 (Extra Trees Regressor): R² = 0.8910, MAE = 2.25 pts
• Model 6 (Stacking Ensemble): R² = 0.9123, MAE = ±1.99 pts (Top Performer)
"""),

    (42, "Result Analysis", """
Fast TreeSHAP feature attribution reveals key engineering insights:
• Safe Bearing Capacity (kN/m²) and Soil Score are the strongest positive contributors (+4.2 to +6.8 pts) toward feasibility.
• Flood Risk and Seismic Zone classification represent the strongest downward risk penalties (-3.5 to -8.2 pts).
• Distance to Elephant Corridors and Protected Areas exhibits a non-linear threshold effect: sites <5 km suffer heavy penalties (-4.5 pts), while sites >10 km contribute positive feasibility (+0.74 pts).
"""),

    (43, "Advantages, Limitations and Future Scope", """
43.1 Advantages
• Instantaneous (<3 second) Stage-0/1 site feasibility screening.
• Complete mathematical transparency across 5 standard EIA methodologies.
• Full compliance with Bureau of Indian Standards (IS Codes) and MoEFCC guidelines.
• Interactive 3D WebGL hazard reaction simulation.
• 1-Click publication-ready ReportLab PDF report generation.
• Recognized with the Special Mention Award at the state-level TANCAM TNWISE 2026 Hackathon.

43.2 Limitations
• Spatial satellite resolutions (250m–1km) provide regional estimates; cannot replace confirmatory physical borehole tests for final Stage-2 construction.
• Internet connectivity required for live satellite API queries.

43.3 Future Scope
• Integration of high-resolution Drone LiDAR point cloud data.
• Direct BIM (Building Information Modeling) and CAD file foundation export.
• Expansion of global satellite datasets beyond India.
"""),

    (44, "Development Methodology and Timeline", """
Development Timeline:
• Phase 1 (Ideation & Problem Formulation): Identified civil engineering site screening inefficiencies and framed GeoAI architecture.
• Phase 2 (ETL & ML Training): Built satellite connectors and trained Stacking Ensemble model.
• Phase 3 (TNWISE 2026 Hackathon): Competed at Kumaraguru College of Technology / TANCAM, successfully demonstrated live system to jury, and received the Special Mention Award.
• Phase 4 (EIA Mathematical Refinement): Standardized all 5 EIA methods per IS codes and reviewer feedback.
• Phase 5 (Cloud Deployment): Deployed live production service on Render.
"""),

    (45, "Risk Analysis and Mitigation", """
• Risk 1 (External Satellite API Outages): Mitigated by in-memory spatial KDTrees and historical offline fallback datasets.
• Risk 2 (Misinterpretation as Legal Approval): Mitigated by prominent Stage-0/1 preliminary screening disclaimers on UI and exported PDFs.
• Risk 3 (Server Overload during PDF Generation): Mitigated by Flask-Limiter throttling and Gunicorn asynchronous multi-threading.
"""),

    (46, "References", """
1. Bureau of Indian Standards (BIS). IS 1904:1986 (Reaffirmed 2021) — Code of Practice for Design and Construction of Foundations in Soils.
2. Bureau of Indian Standards (BIS). IS 1893 (Part 1): 2016 — Criteria for Earthquake Resistant Design of Structures.
3. Bureau of Indian Standards (BIS). IS 13920:2016 — Ductile Design and Detailing of Reinforced Concrete Structures.
4. Bureau of Indian Standards (BIS). IS 2911 (Part 1/Sec 1): 2010 — Design and Construction of Pile Foundations.
5. Ministry of Environment, Forest and Climate Change (MoEFCC). Environmental Impact Assessment Notification, 2006.
6. Leopold, L. B., et al. (1971). A Procedure for Evaluating Environmental Impact. USGS Circular 645.
7. Sorensen, J. C. (1971). A Framework for Identification & Control of Resource Degradation. UC Berkeley.
8. McHarg, I. L. (1969). Design with Nature. American Museum of Natural History.
9. ISRIC — World Soil Information. SoilGrids 250m: Global gridded soil information.
10. NASA Langley Research Center. NASA POWER Project: Prediction of Worldwide Energy Resources.
"""),

    (47, "Feedback and Conclusion", """
47.1 Feedback
Following rigorous academic review on coastal coordinates (12.9340, 80.2592), all eleven reviewer observations were mathematically rectified:
• Checklist compliance standardized to explicit weighted sum (3/5 PASS = 60.0%).
• Leopold index normalized with explicit mathematical formula (Net Score -46 -> Index 75.8/100).
• McHarg overlay composite score calculated directly from sub-layers (71.0/100 -> Zone S-2).
• Defensive engineering phrasing applied to network hazard pathways per IS 1893:2016.
• Disclaimers added framing the tool for Stage-0/1 preliminary screening.

47.2 Conclusion
The Construction Site Viability and Lifespan Prediction System establishes a new benchmark in automated geospatial engineering and environmental assessment. By uniting machine learning, satellite earth observation, Indian Standards compliance, and 3D simulation, the project demonstrates how modern AI can advance sustainable, disaster-resilient infrastructure development.
"""),

    (48, "Sample API Request and Response", """
Sample API Request:
POST /api/analyze HTTP/1.1
Content-Type: application/json

{
  "lat": 12.9340,
  "lon": 80.2592,
  "building_type": "Apartment",
  "floors": 3
}

Sample API Response:
{
  "feasibility_score": 58.88,
  "risk_level": "Medium Risk",
  "lifespan": "11–31 years",
  "foundation": "Preliminary: Isolated Footing",
  "confidence": 76.3,
  "domain_scores": {
    "soil": 60.0,
    "climate": 73.3,
    "environment": 99.3,
    "animal": 45.8
  },
  "eia_methods": {
    "checklist_method": {
      "compliance_score": 60.0,
      "compliance_status": "CONDITIONALLY COMPLIANT",
      "compliance_summary": "3/5 Passed (Weighted Compliance: 60.0%)"
    },
    "leopold_matrix": {
      "net_impact_score": -46,
      "leopold_index": 75.8,
      "formula": "Leopold Index = 100 * (1 - (|-46| / 190)) = 75.8/100"
    },
    "overlay_method": {
      "composite_score": 71.0,
      "zone": "Zone S-2: Moderately Suitable",
      "formula": "(60.0 * 0.35) + (73.3 * 0.25) + (99.3 * 0.25) + (45.8 * 0.15) = 71.0/100"
    }
  }
}
"""),

    (49, "Glossary of Terms", """
• Bearing Capacity (kN/m²): The maximum contact pressure between the foundation substructure and supporting subsoil without shear failure or excessive settlement (IS 1904).
• Standard Penetration Test (SPT N-Value): In-situ dynamic penetration test indicating relative soil density and shear strength.
• Eco-Sensitive Zone (ESZ): Statutory 10 km buffer zone surrounding National Parks and Sanctuaries regulated under MoEFCC EIA 2006.
• Leopold Matrix: A 2D interaction matrix cross-referencing proposed project activities against environmental receptors to quantify direct impacts.
• Sorensen Network Method: An impact identification technique tracing primary environmental triggers through secondary conditions to tertiary structural risks.
• McHarg Spatial Overlay: A Multi-Criteria Evaluation (MCE) technique superimposing weighted thematic geospatial map layers to identify optimal suitability zones.
• Stacking Ensemble: An advanced meta-learning architecture where multiple diverse base regressors (Random Forest, XGBoost, Extra Trees) are combined via a meta-model (Ridge Regression).
• SHAP (SHapley Additive exPlanations): A game-theoretic approach to explain individual feature contributions toward machine learning predictions.
"""),

    (50, "Certificate of Completion / Project Certificates", """
This section documents the official certificate of achievement and recognition received by the project team.

Figure 1: TNWISE 2026 Special Mention Award Certificate
Description: Official Certificate of Appreciation awarded to Vaira Selvi S & Team from Kamaraj College of Engineering and Technology for achieving the Special Mention Award in TANCAM's Hackathon for Tamil Nadu Women in Science and Engineering (TNWISE 2026) organized by Tamil Nadu Centre of Excellence for Advanced Manufacturing (TANCAM), Chennai in association with Dassault Systèmes, TIDCO, and Kumaraguru College of Technology, Coimbatore on 12th March 2026.
"""),

    (51, "Project Photographs", """
This section documents the project demonstration, stage felicitation, and institutional review sessions.

Figure 2: Award Felicitation on Main Stage at TNWISE 2026 Hackathon
Description: Team members Vaira Selvi S, Vishali S, and Mohana Priya K receiving the Special Mention Award on the main stage at Kumaraguru College of Technology from dignitaries representing TANCAM and Dassault Systèmes.

Figure 3: Institutional Presentation and Certificate Review
Description: Project team presenting the award certificate and demonstrating the software system to the Principal and faculty at Kamaraj College of Engineering and Technology.
"""),

    (52, "GEOTAGGED PHOTOGRAPHS", """
This section presents geotagged photographic documentation verifying project demonstration and live evaluation during the hackathon.

Figure 4: Live Jury Demonstration and Software Evaluation
Description: Geotagged photograph documenting live project demonstration to the evaluation jury during the hackathon (Location: Kamaraj College of Engineering and Technology / Hackathon Venue, Tamil Nadu, India — Lat: 9.672813° N, Long: 77.96493° E).
""")
]

# ─────────────────────────────────────────────────────────────────────────────
# 2. REPORTLAB PDF GENERATOR (EXACT LATEX/ACADEMIC STYLING)
# ─────────────────────────────────────────────────────────────────────────────

class AcademicCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(AcademicCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super(AcademicCanvas, self).showPage()
        super(AcademicCanvas, self).save()

    def draw_decorations(self, page_count):
        # Cover page (page 1) has no header/footer
        if self._pageNumber == 1:
            return

        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#334155"))

        # Running Header (on all pages from page 2 onwards)
        header_text = "Construction Site Viability and Lifespan Prediction System Project Report"
        self.drawString(54, 802, header_text)
        self.setStrokeColor(colors.HexColor("#94A3B8"))
        self.setLineWidth(0.5)
        self.line(54, 794, 541, 794)

        # Running Footer (Roman for TOC/Ack pages 2-5, Arabic from page 6 onwards)
        self.line(54, 45, 541, 45)
        if self._pageNumber in [2, 3, 4]:
            roman_pages = {2: "i", 3: "ii", 4: "iii"}
            page_str = roman_pages.get(self._pageNumber, str(self._pageNumber))
            self.drawRightString(541, 32, page_str)
        elif self._pageNumber == 5:
            # Acknowledgement page has no bottom page number in template or blank
            pass
        else:
            # Main body starts at page 6 (which is page 1 of body in reference)
            body_page = self._pageNumber - 4
            self.drawRightString(541, 32, str(body_page))

        self.restoreState()

def generate_pdf():
    pdf_path = "d:/construction_site_selection/construction_site_selection/TERRA_AI_PROJECT_REPORT.pdf"
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Academic Typography Styles matching LaTeX/SRM template
    cover_title = ParagraphStyle(
        'CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=12
    )
    cover_sub = ParagraphStyle(
        'CoverSub',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#334155"),
        spaceAfter=40
    )
    cover_meta_header = ParagraphStyle(
        'CoverMetaH',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=colors.HexColor("#0F172A"),
        spaceAfter=8
    )
    cover_meta_text = ParagraphStyle(
        'CoverMetaT',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#334155")
    )

    h1_style = ParagraphStyle(
        'AcademicH1',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=17,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    h2_style = ParagraphStyle(
        'AcademicH2',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )
    body_style = ParagraphStyle(
        'AcademicBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#1E293B"),
        alignment=TA_JUSTIFY,
        spaceAfter=5
    )
    caption_style = ParagraphStyle(
        'FigureCaption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=6,
        spaceAfter=2
    )
    desc_caption_style = ParagraphStyle(
        'FigureDesc',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor("#334155"),
        spaceAfter=8
    )

    story = []

    # ─────────────────────────────────────────────────────────────
    # PAGE 1: COVER PAGE
    # ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 80))
    story.append(Paragraph("Construction Site Viability and<br/>Lifespan Prediction System", cover_title))
    story.append(Paragraph("An Automated Geospatial Machine Learning Platform for Foundation Engineering, Hazard Risk Assessment, and Environmental Impact Evaluation", cover_sub))
    story.append(Spacer(1, 140))

    story.append(Paragraph("<b>Project Details</b>", cover_meta_header))
    story.append(Paragraph("<b>Submitted by:</b> Vaira Selvi S, Vishali S and Mohana Priya K", cover_meta_text))
    story.append(Paragraph("<b>Department:</b> Department of Computer Science and Engineering", cover_meta_text))
    story.append(Paragraph("<b>Institution:</b> Kamaraj College of Engineering and Technology", cover_meta_text))
    story.append(Paragraph("<b>Academic Year:</b> 2025–2026", cover_meta_text))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 2–4: TABLE OF CONTENTS
    # ─────────────────────────────────────────────────────────────
    story.append(Paragraph("<b>Contents</b>", ParagraphStyle('TOCTitle', fontName='Helvetica-Bold', fontSize=14, leading=18, spaceAfter=10)))

    # Compute simulated page mapping exactly matching reference
    toc_data_p1 = []
    toc_data_p2 = []
    toc_data_p3 = []

    for num, title, _ in SECTIONS_DATA:
        # Approximate page numbers
        if num <= 22:
            p_num = max(2, (num // 2) + 1)
            toc_data_p1.append((num, title, p_num))
        elif num <= 46:
            p_num = max(19, 19 + ((num - 22)))
            toc_data_p2.append((num, title, p_num))
        else:
            p_num = max(45, 45 + (num - 46))
            toc_data_p3.append((num, title, p_num))

    def make_toc_table(items):
        t_data = []
        for n, t, p in items:
            t_data.append([
                Paragraph(f"<b>{n}</b>", body_style),
                Paragraph(f"{t}", body_style),
                Paragraph(f"{p}", ParagraphStyle('R', parent=body_style, alignment=TA_RIGHT))
            ])
        tbl = Table(t_data, colWidths=[30, 415, 42])
        tbl.setStyle(TableStyle([
            ('PADDING', (0, 0), (-1, -1), 2.2),
            ('LINEBELOW', (0, 0), (-1, -1), 0.3, colors.HexColor("#F1F5F9")),
        ]))
        return tbl

    story.append(make_toc_table(toc_data_p1))
    story.append(PageBreak())
    story.append(make_toc_table(toc_data_p2))
    story.append(PageBreak())
    story.append(make_toc_table(toc_data_p3))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 5: ACKNOWLEDGEMENT
    # ─────────────────────────────────────────────────────────────
    story.append(Spacer(1, 100))
    story.append(Paragraph("<b>ACKNOWLEDGEMENT</b>", ParagraphStyle('AckH', fontName='Helvetica-Bold', fontSize=14, leading=18, alignment=TA_CENTER, spaceAfter=20)))
    ack_body = (
        "We express our sincere gratitude to our esteemed institution, <b>Kamaraj College of Engineering and Technology</b>, "
        "and the <b>Department of Computer Science and Engineering</b> for providing the resources, computing facilities, "
        "and supportive academic environment to execute this project successfully.<br/><br/>"
        "We extend our heartfelt thanks to our faculty guides, mentors, and academic reviewers for their constructive feedback, "
        "technical insights, and continuous encouragement throughout the design, mathematical formulation, and implementation of the "
        "<b>Construction Site Viability and Lifespan Prediction System</b>.<br/><br/>"
        "We also acknowledge the organizers of <b>TANCAM's Hackathon (TNWISE 2026)</b>—Tamil Nadu Centre of Excellence for Advanced Manufacturing, "
        "Dassault Systèmes, TIDCO, and Kumaraguru College of Technology—for recognizing our project with the prestigious Special Mention Award.<br/><br/>"
        "Finally, we thank our families and peers for their constant motivation and support."
    )
    story.append(Paragraph(ack_body, body_style))
    story.append(PageBreak())

    # ─────────────────────────────────────────────────────────────
    # PAGE 6 ONWARDS: MAIN PROJECT REPORT (ALL 52 SECTIONS)
    # ─────────────────────────────────────────────────────────────
    img_cert_path = "tnwise_extracted/page_4_img_2_X2.jpg"
    img_stage_path = "tnwise_extracted/page_3_img_2_X2.jpg"
    img_team_path = "tnwise_extracted/page_1_img_2_X2.jpg"
    img_demo_path = "tnwise_extracted/page_2_img_2_X2.jpg"

    for sec_num, sec_title, sec_body in SECTIONS_DATA:
        story.append(Paragraph(f"{sec_num} {sec_title}", h1_style))
        story.append(HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#CBD5E1"), spaceAfter=5))

        paragraphs = sec_body.strip().split('\n\n')
        for p_text in paragraphs:
            if p_text.strip():
                lines = p_text.strip().split('\n')
                if len(lines) > 1 and lines[0].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '19.', '20.', '27.', '29.', '32.', '33.', '43.', '47.')):
                    story.append(Paragraph(f"<b>{lines[0]}</b>", h2_style))
                    body_remainder = '<br/>'.join(lines[1:])
                    story.append(Paragraph(body_remainder, body_style))
                else:
                    formatted_text = p_text.strip().replace('\n', '<br/>')
                    story.append(Paragraph(formatted_text, body_style))
                story.append(Spacer(1, 2.5))

        # Insert images at exact designated end sections
        if sec_num == 50 and os.path.exists(img_cert_path):
            story.append(Spacer(1, 8))
            story.append(Image(img_cert_path, width=470, height=320))
            story.append(Spacer(1, 6))

        elif sec_num == 51:
            if os.path.exists(img_stage_path):
                story.append(Spacer(1, 6))
                story.append(Image(img_stage_path, width=460, height=310))
                story.append(Spacer(1, 6))
            if os.path.exists(img_team_path):
                story.append(Spacer(1, 6))
                story.append(Image(img_team_path, width=460, height=310))
                story.append(Spacer(1, 6))

        elif sec_num == 52 and os.path.exists(img_demo_path):
            story.append(Spacer(1, 8))
            story.append(Image(img_demo_path, width=470, height=330))
            story.append(Spacer(1, 6))

        story.append(Spacer(1, 5))

    doc.build(story, canvasmaker=AcademicCanvas)
    print(f"SUCCESS: Generated PDF document -> {pdf_path}")
    return pdf_path

# ─────────────────────────────────────────────────────────────────────────────
# 3. MICROSOFT WORD (.DOCX) GENERATOR (MATCHING FORMAL ACADEMIC STYLING)
# ─────────────────────────────────────────────────────────────────────────────

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=120, right=120):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def generate_docx():
    doc = docx.Document()

    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.0)
        s.right_margin = Inches(1.0)
        # Running Header
        header = s.header
        hp = header.paragraphs[0]
        hp.text = "Construction Site Viability and Lifespan Prediction System Project Report"
        hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
        hp.style.font.name = 'Calibri'
        hp.style.font.size = Pt(8.5)
        hp.style.font.color.rgb = RGBColor(100, 116, 139)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(30, 41, 59)

    # ── COVER PAGE ──
    p_t = doc.add_paragraph()
    p_t.paragraph_format.space_before = Pt(80)
    p_t.paragraph_format.space_after = Pt(12)
    run_t = p_t.add_run("CONSTRUCTION SITE VIABILITY AND\nLIFESPAN PREDICTION SYSTEM")
    run_t.font.name = 'Arial'
    run_t.font.size = Pt(22)
    run_t.font.bold = True
    run_t.font.color.rgb = RGBColor(15, 23, 42)

    p_sub = doc.add_paragraph()
    p_sub.paragraph_format.space_after = Pt(160)
    run_sub = p_sub.add_run("An Automated Geospatial Machine Learning Platform for Foundation Engineering, Hazard Risk Assessment, and Environmental Impact Evaluation")
    run_sub.font.size = Pt(12)
    run_sub.font.color.rgb = RGBColor(51, 65, 85)

    p_meta = doc.add_paragraph()
    r_meta_h = p_meta.add_run("Project Details\n")
    r_meta_h.bold = True
    r_meta_h.font.size = Pt(12)
    r_meta_h.font.color.rgb = RGBColor(15, 23, 42)

    p_meta.add_run("Submitted by: Vaira Selvi S, Vishali S and Mohana Priya K\n").bold = True
    p_meta.add_run("Department: Department of Computer Science and Engineering\n")
    p_meta.add_run("Institution: Kamaraj College of Engineering and Technology\n")
    p_meta.add_run("Academic Year: 2025–2026\n")

    doc.add_page_break()

    # ── TABLE OF CONTENTS ──
    h_toc = doc.add_heading("Contents", level=1)
    h_toc.paragraph_format.space_after = Pt(12)

    tbl_toc = doc.add_table(rows=len(SECTIONS_DATA), cols=3)
    tbl_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, (sec_no, sec_title, _) in enumerate(SECTIONS_DATA):
        c0 = tbl_toc.cell(idx, 0)
        c1 = tbl_toc.cell(idx, 1)
        c2 = tbl_toc.cell(idx, 2)
        c0.paragraphs[0].add_run(str(sec_no)).bold = True
        c1.paragraphs[0].add_run(sec_title)
        c2.paragraphs[0].add_run(str(idx + 2))
        c2.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
        set_cell_margins(c0, top=25, bottom=25, left=40, right=40)
        set_cell_margins(c1, top=25, bottom=25, left=40, right=40)
        set_cell_margins(c2, top=25, bottom=25, left=40, right=40)

    doc.add_page_break()

    # ── ACKNOWLEDGEMENT ──
    h_ack = doc.add_heading("ACKNOWLEDGEMENT", level=1)
    h_ack.alignment = WD_ALIGN_PARAGRAPH.CENTER
    h_ack.paragraph_format.space_before = Pt(80)
    h_ack.paragraph_format.space_after = Pt(24)

    p_ack = doc.add_paragraph()
    p_ack.paragraph_format.line_spacing = 1.2
    p_ack.add_run(
        "We express our sincere gratitude to our esteemed institution, Kamaraj College of Engineering and Technology, "
        "and the Department of Computer Science and Engineering for providing the computational resources, laboratory facilities, "
        "and supportive academic environment to carry out this project successfully.\n\n"
        "We extend our heartfelt thanks to our faculty guides, mentors, and academic reviewers for their valuable technical guidance, "
        "constructive critique, and continuous encouragement throughout the design, mathematical formulation, and implementation of the "
        "Construction Site Viability and Lifespan Prediction System.\n\n"
        "We also acknowledge the organizers of TANCAM's Hackathon (TNWISE 2026)—Tamil Nadu Centre of Excellence for Advanced Manufacturing, "
        "Dassault Systèmes, TIDCO, and Kumaraguru College of Technology—for recognizing our project with the Special Mention Award.\n\n"
        "Finally, we express our gratitude to our family members and friends for their enduring support."
    )

    doc.add_page_break()

    # ── ALL 52 SECTIONS ──
    img_cert_path = "tnwise_extracted/page_4_img_2_X2.jpg"
    img_stage_path = "tnwise_extracted/page_3_img_2_X2.jpg"
    img_team_path = "tnwise_extracted/page_1_img_2_X2.jpg"
    img_demo_path = "tnwise_extracted/page_2_img_2_X2.jpg"

    for sec_num, sec_title, sec_body in SECTIONS_DATA:
        h = doc.add_heading(f"{sec_num} {sec_title}", level=1)
        h.paragraph_format.space_before = Pt(14)
        h.paragraph_format.space_after = Pt(6)

        for para_text in sec_body.strip().split('\n\n'):
            if para_text.strip():
                p = doc.add_paragraph()
                p.paragraph_format.space_after = Pt(6)
                p.paragraph_format.line_spacing = 1.15

                lines = para_text.strip().split('\n')
                if len(lines) > 1 and lines[0].strip().startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.', '10.', '19.', '20.', '27.', '29.', '32.', '33.', '43.', '47.')):
                    r_sub = p.add_run(lines[0] + '\n')
                    r_sub.bold = True
                    r_sub.font.size = Pt(11.5)
                    r_sub.font.color.rgb = RGBColor(15, 23, 42)
                    body_remainder = '\n'.join(lines[1:])
                    if body_remainder.strip():
                        p.add_run(body_remainder)
                else:
                    p.add_run(para_text.strip())

        # Insert images at designated sections
        if sec_num == 50 and os.path.exists(img_cert_path):
            doc.add_picture(img_cert_path, width=Inches(5.8))
            doc.add_paragraph().paragraph_format.space_after = Pt(10)

        elif sec_num == 51:
            if os.path.exists(img_stage_path):
                doc.add_picture(img_stage_path, width=Inches(5.6))
                doc.add_paragraph().paragraph_format.space_after = Pt(8)
            if os.path.exists(img_team_path):
                doc.add_picture(img_team_path, width=Inches(5.6))
                doc.add_paragraph().paragraph_format.space_after = Pt(8)

        elif sec_num == 52 and os.path.exists(img_demo_path):
            doc.add_picture(img_demo_path, width=Inches(5.8))
            doc.add_paragraph().paragraph_format.space_after = Pt(10)

    docx_path = "d:/construction_site_selection/construction_site_selection/TERRA_AI_PROJECT_REPORT.docx"
    doc.save(docx_path)
    print(f"SUCCESS: Generated Word document -> {docx_path}")
    return docx_path

if __name__ == "__main__":
    generate_pdf()
    generate_docx()
