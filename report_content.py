# report_content.py
# Contains full 49-section technical content for TerraAI project reports

SECTIONS_CONTENT = [
    (1, "Abstract", """
1.1 Overview
The TerraAI platform is an autonomous, cloud-based geotechnical and environmental decision support system engineered to revolutionize preliminary construction site selection, environmental impact assessment (EIA), and structural risk mitigation across India. Conventional civil engineering preliminary site selection is an inherently fragmented, time-intensive, and error-prone process. It frequently relies on scattered government maps, isolated soil sampling boreholes, offline climate historical averages, and subjective consultant assessments. These traditional approaches introduce substantial delays—often taking several weeks to months—and fail to capture complex, multi-domain interactions such as high water table saturation, cyclic seismic vulnerability, soil corrosivity, and statutory eco-sensitive buffer restrictions prior to capital investment.

TerraAI resolves this foundational bottleneck by establishing an automated, multimodal data ingestion and machine learning evaluation pipeline. By inputting any geographic coordinates or selecting a location on an interactive GIS map within India, the system queries global and national satellite earth observation databases—including ISRIC SoilGrids for 3D soil mechanics, NASA POWER for 30-day meteorological indices, OpenStreetMap for drainage and waterways, BMTPC Vulnerability Atlas for hazard classifications, and GBIF/MoEFCC databases for protected wildlife sanctuaries. The platform integrates a Stacking Ensemble Machine Learning model (Random Forest, XGBoost, and Extra Trees feeding a Ridge Meta-Regressor) yielding verified feasibility scores (R² = 0.9123, MAE = ±1.99 points), structural lifespan projections, and preliminary foundation recommendations strictly compliant with Indian Standards (IS 1904:1986/2021, IS 1893:2016, IS 2911:2010, and IS 13920:2016).

1.2 Purpose & Motivation
The primary purpose of TerraAI is to provide civil engineers, urban planners, government regulatory authorities, infrastructure developers, and academic researchers with an instant, scientifically rigorous Stage-0/1 preliminary screening tool. Furthermore, the platform implements all five academic Environmental Impact Assessment (EIA) methodologies—Statutory Weighted Checklist, Leopold 2D Interaction Matrix, Sorensen Cause-Condition-Effect Network, McHarg Multi-Criteria Spatial Overlay, and Predictive AI Modeling—accompanied by real-time Three.js 3D structural hazard reaction simulations and automated, publication-ready PDF engineering dossiers.
"""),
    (2, "Abstract — Extended Discussion", """
2.1 Problem and Solution
In major infrastructure and residential development projects, geotechnical site failures represent one of the most catastrophic financial and structural risks. Post-construction differential foundation settlement, slope failures, seismic resonance damage, and unexpected groundwater inundation frequently trace back to inadequate preliminary screening. In conventional workflows, preliminary stage assessments either rely on oversimplified assumptions or incur substantial financial overheads from manual exploratory boreholes prior to basic feasibility verification.

TerraAI delivers a scalable, automated computational solution. The system orchestrates 64 distinct geospatial and geotechnical features across four interconnected domains: Geotechnical Soil Mechanics, Climate & Meteorological Stress, Natural Hazards & Inundation, and Ecological & Wildlife Sensitivity. The predictive core evaluates load-bearing capacity against building structural categories (Houses, Apartments, Hospitals, Schools, Bridges, Industrial Warehouses, and Malls) and dynamic storey heights, generating transparent, mathematically derived risk indexes.

2.2 Expected Impact & Societal Value
By digitizing and automating Stage-0/1 site screening, TerraAI reduces preliminary evaluation timelines from 3–4 weeks down to under 3 seconds while reducing preliminary surveying expenditures by over 80%. It prevents unviable developments in hazard-prone floodplains, coastal inundation zones, and protected wildlife corridors. The system was recognized with the Special Mention Award at the state-level TANCAM TNWISE 2026 Hackathon for its contribution to sustainable smart infrastructure and environmental preservation in Tamil Nadu and across India.
"""),
    (3, "Introduction", """
Construction site selection is the foundational phase of all civil engineering and architectural projects. The physical longevity, structural stability, economic viability, and environmental legality of any building depend directly on the interaction between superstructure gravity/dynamic loads and the underlying subsoil and regional climate.

Historically, civil engineering relied on localized field surveys and historical municipal registers. However, with accelerating urbanization, climate change-induced extreme weather events, and stringent statutory environmental clearance mandates (such as the MoEFCC EIA Notification 2006), traditional manual site evaluation methods have proven inadequate. TerraAI addresses this modern challenge by deploying an intelligent, end-to-end Geospatial Artificial Intelligence (GeoAI) platform. The system operates autonomously: users interact with a modern web dashboard or programmatic REST API, selecting coordinates anywhere across India to trigger an automated cascade of spatial data retrieval, ML inference, multi-criteria EIA calculations, and 3D physical hazard simulations.
"""),
    (4, "Background and Motivation", """
4.1 Need for Automated Geotechnical Screening
Traditional geotechnical exploration begins with borehole drilling, Standard Penetration Tests (SPT), and laboratory soil mechanics analysis. While physical borehole investigations remain essential for final structural execution (Stage-2 detailed design), conducting physical boreholes across multiple candidate sites during preliminary shortlisting (Stage-0/1) is cost-prohibitive and time-consuming. An automated screening tool allows developers to screen hundreds of square kilometers instantly.

4.2 Remote Geospatial Sensing & Earth Observation
Over the past decade, satellite remote sensing, digital elevation models (DEM), and global soil grid databases have achieved sub-kilometer spatial resolutions. Platforms such as ISRIC World Soil Information, NASA POWER Ag-Climatology, and OpenStreetMap provide multi-spectral, calibrated earth observation data. However, converting raw geospatial raster arrays into actionable structural engineering insights requires domain-specific feature engineering, spatial indexing, and machine learning calibration.

4.3 Digital Record Keeping & Decision Traceability
Municipal authorities, banking institutions, and insurance underwriters require transparent, auditable records justifying site selection decisions. TerraAI replaces handwritten notes and disconnected spreadsheets with a unified digital repository, automated PDF generation, and SHAP-based feature importance explainability.
"""),
    (5, "Problem Statement & Research Questions", """
Core Problem Statement:
How can multi-source satellite geospatial observations, geotechnical parameters, and environmental hazard indices be autonomously harvested, synthesized, and evaluated to provide instantaneous, mathematically rigorous, and statutory-compliant construction site feasibility assessments and Environmental Impact Evaluations?

Key Research & Engineering Questions:
1. How can heterogeneous spatial APIs (ISRIC, NASA POWER, OSM, BMTPC) be integrated into a unified sub-3-second ETL pipeline with robust caching and offline fallback mechanisms?
2. What machine learning ensemble architecture maximizes prediction precision (R² > 0.90) for construction feasibility and lifespan estimation across diverse Indian soil topographies?
3. How can the 5 academic EIA methodologies (Checklist, Leopold Matrix, Sorensen Network, McHarg Overlay, Predictive AI) be mathematically normalized to eliminate arbitrary scoring and guarantee strict alignment with Indian Standards (IS 1904, IS 1893, IS 13920)?
4. How can complex geotechnical hazards (pore pressure rise, cyclic seismic shear, differential settlement) be visualized through real-time 3D WebGL simulations for non-technical stakeholders?
"""),
    (6, "Project Objectives", """
The primary engineering objectives of the TerraAI project are:
1. To develop an autonomous geospatial ETL pipeline ingesting live soil, climate, hazard, and biodiversity data across India.
2. To train, validate, and deploy a Stacking Machine Learning Regressor (Random Forest, XGBoost, Extra Trees, Ridge Meta-Regressor) achieving R² ≥ 0.91 and MAE ≤ 2.0 points.
3. To implement a Computer Vision CNN model for automated soil classification from field excavation photographs.
4. To engineer all 5 academic Environmental Impact Assessment (EIA) methodologies with complete mathematical transparency and explicit normalization formulas.
5. To build an interactive 3D WebGL Physical Hazard Simulation Engine using Three.js to model real-time structural reactions to flooding, seismic vibrations, and soil settlement.
6. To design an automated ReportLab PDF engine compiling publication-ready engineering dossiers compliant with Indian Standards.
7. To provide secure, rate-limited RESTful APIs and deploy the platform on a production cloud environment (Render / Gunicorn).
"""),
    (7, "Scope of the Project", """
The scope of TerraAI encompasses preliminary Stage-0 and Stage-1 construction site feasibility screening across the entire geographic territory of the Republic of India. The platform analyzes building categories ranging from residential houses to high-rise commercial structures and municipal bridges.

7.1 Target Users and Stakeholders
• Civil & Structural Engineers: Rapid shortlisting of foundation configurations and preliminary safe bearing capacity estimates.
• Real Estate & Infrastructure Developers: Cost-benefit analysis and hazard screening prior to land acquisition.
• Environmental Consultants & EIA Auditors: Automated generation of statutory Leopold matrices, Sorensen networks, and MoEFCC buffer audits.
• Municipal Planners & Government Regulators: Zoning compliance, disaster vulnerability mapping, and urban expansion planning.
• Financial Institutions & Insurers: Actuarial climate risk assessment and structural asset durability rating.
"""),
    (8, "Significance and Industrial Relevance", """
The industrial significance of TerraAI lies in transforming a traditionally manual, high-latency consulting workflow into an instantaneous, objective, and data-driven software service. By identifying critical failure modes—such as expansive black cotton soil shrink-swell, coastal floodwater inundation, high seismic acceleration, or eco-sensitive sanctuary encroachment—at Stage-0, the platform prevents multimillion-rupee project abandonments, litigation, and structural disasters.
"""),
    (9, "Existing Site Screening System", """
In the conventional approach:
1. Developers hire field surveyors to conduct manual site visits and boundary measurements.
2. Geotechnical consultants drill physical trial pits and boreholes, sending core samples for lab testing (2–4 weeks).
3. Environmental consultants manually search regional town planning maps, seismic zoning charts, and forest reserve gazettes.
4. Reports are compiled manually in word processors with subjective qualitative scoring.
"""),
    (10, "Limitations of the Existing System", """
• High Financial Cost: Exploratory drilling for multiple candidate plots incurs massive preliminary capital expenditure.
• Significant Time Latency: Turnaround times typically range between 20 to 45 business days.
• Fragmented Data Silos: Soil, seismic, climate, and biodiversity records are maintained by disparate agencies without unified spatial intersection.
• Lack of Mathematical Normalization: Qualitative EIA reports frequently lack reproducible numerical formulas.
• Zero Interactive Simulation: Clients and non-technical stakeholders cannot visualize how physical hazards impact the building.
"""),
    (11, "Proposed TerraAI System", """
The proposed TerraAI platform integrates satellite remote sensing, machine learning predictive modeling, statutory Indian Standards rules engines, academic EIA matrices, and WebGL physics simulation into a cohesive, web-based platform. Users select coordinates via an interactive map, and the system executes real-time data ingestion, algorithmic inference, multi-criteria spatial overlay, and 3D simulation rendering in under 3 seconds.
"""),
    (12, "System Architecture & End-to-End Pipeline", """
The TerraAI system architecture follows a decoupled, modular microservices-oriented design:
1. Client Layer: Single Page Application (SPA) built with HTML5, CSS3 Glassmorphism design system, Vanilla JavaScript ES6+, Leaflet GIS, and Three.js WebGL.
2. API & Gateway Layer: Flask WSGI application managed by Gunicorn, featuring JWT authentication, CORS middleware, and Flask-Limiter IP throttling.
3. Ingestion & ETL Layer: Spatial query dispatchers connecting to ISRIC SoilGrids REST APIs, NASA POWER Climatology, OpenStreetMap Overpass API, BMTPC Vulnerability Dataset, and GBIF Protected Areas.
4. AI/ML Inference Layer: Stacking Ensemble Regressor, Fast TreeSHAP explainer, and PyTorch MobileNetV2 Soil Image Classifier.
5. EIA Evaluation Engine: Mathematical calculation core executing Checklist, Leopold Matrix, Sorensen Network, McHarg Overlay, and Predictive AI models.
6. Presentation & Document Engine: Three.js 3D structural reaction canvas and ReportLab publication-grade PDF compiler.
"""),
    (13, "System Modules Breakdown", """
The platform is organized into five primary functional modules:
• Module 1: Geospatial Ingestion & Feature Engineering Module
• Module 2: Stacking Ensemble ML Prediction Engine
• Module 3: Multi-Method Academic EIA Evaluation Core
• Module 4: 3D WebGL Physical Hazard Simulation Canvas
• Module 5: ReportLab PDF Compilation & REST API Service
"""),
    (14, "Core Geospatial Data Ingestion Module", """
The ingestion module executes asynchronous parallel spatial queries:
• ISRIC SoilGrids: Extracts bulk density (bdod), clay fraction, sand fraction, silt fraction, and pH across 0–30 cm depths to calculate Terzaghi safe bearing capacity (kN/m²), shrink-swell potential, and permeability.
• NASA POWER Climatology: Retrieves 30-day precipitation indices, max wind speeds (km/h), relative humidity (%), extreme temperature variations, and frost day frequencies.
• OpenStreetMap Overpass API: Computes exact geodesic distance to nearest rivers, lakes, coastlines, and floodplains.
• BMTPC Vulnerability Atlas: Spatial KDTree mapping against historical failure points, landslide hazard zones, and seismic acceleration maps.
• GBIF & MoEFCC Protected Area Database: Computes distance to nearest national parks, wildlife sanctuaries, and elephant corridors, verifying 10 km Eco-Sensitive Zone (ESZ) buffers.
"""),
    (15, "Machine Learning Prediction Engine", """
The predictive core employs a Stacking Regressor architecture:
• Base Estimators:
  1. Random Forest Regressor (300 estimators, max depth = 16)
  2. XGBoost Regressor (n_estimators = 250, learning_rate = 0.05, subsample = 0.8)
  3. Extra Trees Regressor (200 estimators, min_samples_split = 4)
• Meta-Regressor: Ridge Regression with L2 regularization (alpha = 1.0)
• Performance: Achieves R² = 0.9123, MAE = ±1.99 points, and RMSE = 2.45 on 5-fold stratified cross-validation across 10,000+ pan-India geo-points.
• Foundation Recommendation Engine: Maps effective bearing capacity (accounting for building structural weight multipliers) to isolated footings, strip footings, raft foundations, or deep pile foundations per IS 1904:1986.
"""),
    (16, "Academic EIA 5-Method Evaluation Module", """
TerraAI implements all five standard EIA methodologies with complete mathematical transparency:
1. Checklist Method: Evaluates 5 statutory parameters weighted per Indian Standards:
   - Soil Bearing Capacity (25%)
   - Seismic Hazard Audit (20%)
   - Flood Exposure (20%)
   - Eco-Sensitive Buffer (20%)
   - Soil Corrosivity / pH (15%)
   Weighted Compliance = Sum of passed weights (e.g. 60.0% for 3/5 PASS).
2. Leopold Interaction Matrix: Evaluates a 5x5 interaction grid between construction activities (excavation, substructure, superstructure, paving, occupancy) and environmental receptors (soil, hydrology, dynamic safety, runoff, ecology). Magnitude (M) is scored on [-10..+10] and Importance (I) on [1..10].
   Normalized Leopold Index = 100 * (1 - (|Net Adverse Impact| / 190)).
3. Sorensen Network Method: Maps cause-condition-effect causal pathways (e.g. Precipitation -> Pore Pressure -> Foundation Instability) with IS 1893:2016 engineered mitigations.
4. McHarg Spatial Overlay Model: Multi-criteria linear combination:
   Composite Score = (0.35 * Soil) + (0.25 * Climate) + (0.25 * Hazard) + (0.15 * Eco).
   Assigns Zonal Suitability: S-1 (>=80), S-2 (60-79.9), S-3 (40-59.9), S-4 (<40).
5. Predictive AI Modeling: Continuous ML stacking inference providing R² = 0.9123 and MAE = ±1.99 pts.
"""),
    (17, "3D Visual & Hazard Physical Simulation Module", """
Built on Three.js and WebGL, this module renders a 3D structural building model subjected to real-time physical environmental hazards:
• Flood Inundation Simulation: Dynamic rising water plane with sub-surface transparency and wave agitation, displaying inundation depth in meters.
• Earthquake Dynamic Oscillation: Harmonic lateral sinusoidal displacement of building storeys with damping decay curves per IS 1893:2016.
• Soft Ground Soil Settlement: Differential vertical subsidence and tilting indicating shear failure in low bearing capacity strata.
• Plain-English Stakeholder Cards: Four intuitive summary cards explaining structural integrity for non-technical clients.
"""),
    (18, "Technology Stack Overview", """
The software stack combines modern open-source web technologies and high-performance Python machine learning libraries:
• Frontend: HTML5, Vanilla CSS3 (Custom Design Tokens), JavaScript (ES6+), Leaflet GIS, Three.js WebGL.
• Backend: Python 3.11, Flask WSGI Framework, Gunicorn Server, Werkzeug, PyJWT, Flask-Limiter, ReportLab PDF Engine.
• Machine Learning: Scikit-Learn, XGBoost, SHAP, NumPy, Pandas, SciPy, PyTorch.
• Geospatial & Mapping: Leaflet.js, OpenStreetMap, CartoDB, Esri Satellite Tiles, Haversine Spatial Geodesics.
• Deployment: Render Cloud Infrastructure, Git Version Control, Gunicorn WSGI container.
"""),
    (19, "Frontend Technologies & Visual System", """
19.1 HTML5 & Vanilla CSS Modular Design System
Designed without bulky third-party CSS frameworks to guarantee ultra-fast load times (<100ms) and maximum aesthetic control. Utilizes a curated dark-mode palette featuring deep midnight slate (#0A0F1D), cyan accent gradients (#06B6D4 to #3B82F6), glassmorphism cards, and smooth CSS cubic-bezier transitions.

19.2 JavaScript ES6+ Reactive Client Engine
Orchestrates client-side state management, asynchronous fetch calls, real-time geocoding search, tab navigation, dynamic Leaflet marker updates, and DOM rendering without frontend framework overhead.

19.3 Leaflet GIS & Satellite Tile Layers
Integrates Leaflet 1.9.4 with OpenStreetMap and Esri World Imagery basemaps, custom pulsing SVG coordinate pins, and bounding box restrictions centered on India.

19.4 Three.js WebGL 3D Simulation Engine
Renders high-framerate (60 FPS) procedural 3D structural geometry, lighting shaders, procedural water materials, and dynamic camera orbits.
"""),
    (20, "Backend Technologies & ML Services", """
20.1 Python 3.11 Execution Environment
Leverages Python 3.11 for improved bytecode execution speed, optimized memory allocation, and rich scientific library support.

20.2 Flask WSGI RESTful Framework
Provides lightweight, high-performance RESTful API endpoints with modular blueprints, JSON serialization, and centralized error handling.

20.3 Gunicorn Production Web Server
Pre-fork worker model running 2 workers with 4 asynchronous threads each and a 120-second timeout to handle concurrent spatial satellite ingestion requests.

20.4 JWT Authentication & Security Middleware
Implements Flask-JWT-Extended for token-based API authentication and Flask-Limiter for IP-based rate limiting.
"""),
    (21, "Database & Feature Store Design", """
The application incorporates a hybrid data architecture:
• Local Feature Store & KDTree Index: In-memory spatial index of 10,000+ historical geo-points and BMTPC structural failure labels for sub-millisecond geographic proximity queries.
• Persistent Database: SQLite / PostgreSQL database managed via Flask-SQLAlchemy storing user accounts, analysis logs, expert feedback reviews, and cached spatial bounding boxes.
"""),
    (22, "Detailed Database Schema & Metadata Dictionary", """
Key Database Entities:
1. Users Table: `id` (PK, UUID), `username` (VARCHAR 80), `email` (VARCHAR 120, UNIQUE), `password_hash` (VARCHAR 255), `created_at` (TIMESTAMP).
2. Analysis_History Table: `id` (PK), `user_id` (FK), `latitude` (FLOAT), `longitude` (FLOAT), `building_type` (VARCHAR), `floors` (INT), `feasibility_score` (FLOAT), `risk_level` (VARCHAR), `foundation_type` (VARCHAR), `eia_json` (JSONB), `created_at` (TIMESTAMP).
3. Expert_Reviews Table: `id` (PK), `analysis_id` (FK), `expert_score` (FLOAT), `comments` (TEXT), `submitted_at` (TIMESTAMP).
"""),
    (23, "Data Flow & Geospatial ETL Pipeline", """
The data flow follows a 6-stage lifecycle:
1. Coordinate Ingestion: User clicks Leaflet map or inputs lat/lon coordinates.
2. Asynchronous Dispatch: Backend fires parallel HTTP requests to ISRIC, NASA POWER, and OSM APIs.
3. Feature Engineering & Spatial Synthesis: Combines raw API responses with KDTree historical databases to construct a 64-feature vector.
4. Model Inference & SHAP Calculation: Stacking ensemble generates predictions while TreeSHAP computes local feature attributions.
5. EIA Method Normalization: Calculates Checklist, Leopold, Sorensen, and McHarg metrics.
6. Client Response & PDF Compilation: Returns structured JSON to web client and enables 1-click ReportLab PDF generation.
"""),
    (24, "RESTful API Endpoint Reference", """
Key API Endpoints:
• `POST /api/analyze`: Ingests `{"lat": float, "lon": float, "building_type": str, "floors": int}` and returns complete feasibility, risk, domain scores, and EIA method results.
• `POST /api/report`: Accepts analysis payload and streams an official, publication-grade PDF dossier.
• `GET /api/health`: Health check endpoint returning model loading status.
• `GET /api/datasets/status`: Returns record counts and column metadata of the feature store.
• `POST /api/auth/login` & `POST /api/auth/register`: JWT authentication endpoints.
"""),
    (25, "Indian Engineering Standards Compliance (IS Codes)", """
TerraAI embeds strict compliance rules derived from official Bureau of Indian Standards (BIS) and MoEFCC codes:
• IS 1904:1986 / 2021: Code of practice for design and construction of foundations in soils (Safe Bearing Capacity thresholds: >=100 kN/m² for footings, <60 kN/m² for raft/piles).
• IS 1893 (Part 1): 2016: Criteria for Earthquake Resistant Design of Structures (Seismic Zone II to V design spectrum accelerations).
• IS 2911 (Part 1/Sec 1): 2010: Design and construction of pile foundations in weak/waterlogged strata.
• IS 13920:2016: Ductile design and detailing of reinforced concrete structures subjected to seismic forces.
• IS 2720 (Part 26): Laboratory determination of soil pH and chemical corrosivity (safe range 6.0 <= pH <= 8.5).
• MoEFCC EIA Notification 2006: Statutory 10 km Eco-Sensitive Zone (ESZ) environmental clearance buffer mandates.
"""),
    (26, "Mathematical Consistency & Normalization Logic", """
To eliminate arbitrary scoring and guarantee scientific rigor:
• Checklist Formula: Compliance = Sum(Passed Parameter Weights) = 25% (Soil) + 20% (Seismic) + 20% (Flood) + 20% (Eco) + 15% (pH).
• Leopold Normalization: Leopold Index = 100 * (1 - (|Net Adverse Impact| / 190)), where 190 is the theoretical maximum adverse sum (5 activities * 10 max adverse * avg importance).
• McHarg Overlay Formula: Composite Score = (0.35 * Soil) + (0.25 * Climate) + (0.25 * Hazard) + (0.15 * Eco).
• Stacking Meta-Regression: Final Score = 0.40 * RF + 0.35 * XGB + 0.25 * ExtraTrees (calibrated by Ridge Meta-Regressor).
"""),
    (27, "Authentication, Security & Rate Limiting", """
27.1 Security Best Practices & Data Validation
• Passwords hashed using PBKDF2 with SHA-256 salts.
• JWT access tokens signed with HMAC-SHA256 with 24-hour expiration.
• Input validation strictly bounds latitude (8.0° to 37.0° N) and longitude (68.0° to 97.5° E) within Indian borders.
• Flask-Limiter enforces rate limits (60 requests/minute for general endpoints, 10 requests/minute for heavy PDF generation) to prevent DoS attacks.
"""),
    (28, "Functional Requirements Specification", """
• FR-01: System shall allow geographic coordinate input via interactive map click or coordinate search box.
• FR-02: System shall fetch live soil mechanics parameters from ISRIC SoilGrids.
• FR-03: System shall fetch 30-day precipitation and climate stress indices from NASA POWER.
• FR-04: System shall predict overall feasibility score (0–100) and lifespan (years) using the Stacking Ensemble.
• FR-05: System shall compute all 5 academic EIA methodologies with visible mathematical formulas.
• FR-06: System shall render 3D WebGL structural reactions for flood, seismic, and settlement stresses.
• FR-07: System shall generate downloadable, formatted PDF engineering screening dossiers.
"""),
    (29, "Non-Functional Requirements Specification", """
29.1 Usability & Accessibility: Clean, high-contrast dark-mode interface with responsive design across desktop and mobile.
29.2 Performance & Latency: Complete end-to-end analysis turnaround under 3.0 seconds under normal network conditions.
29.3 Reliability & Fault Tolerance: Automatic fallback to local spatial KDTrees if external satellite APIs timeout.
29.4 Security & Integrity: Full CSRF, SQL injection, and XSS sanitization.
29.5 Maintainability & Modularity: Decoupled frontend templates, modular Python backend services, and clean docstrings.
29.6 Scalability & Cloud Readiness: Stateless WSGI architecture ready for multi-instance container scaling on Render/AWS.
"""),
    (30, "Hardware Requirements", """
• Server / Cloud Environment: Minimum 1 vCPU (2.0 GHz+), 1 GB RAM, 2 GB SSD storage (Render Free / Starter tier).
• Client Device: Any modern laptop, desktop, or mobile device with WebGL-compatible graphics accelerator (Intel UHD / Nvidia / AMD / Apple Silicon) and minimum 2 GB RAM.
"""),
    (31, "Software & Dependency Requirements", """
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
    (33, "Implementation & Development Approach", """
33.1 Iterative Agile Engineering Pipeline
Development was executed across 6 agile sprints:
• Sprint 1: Geospatial data schema definition and multi-API connector development.
• Sprint 2: Feature engineering, dataset balancing, and ML stacking model training.
• Sprint 3: Mathematical formulation and coding of the 5 academic EIA methodologies.
• Sprint 4: Three.js 3D WebGL visual hazard simulation engine development.
• Sprint 5: UI/UX glassmorphism redesign and ReportLab PDF dossier generation.
• Sprint 6: Rigorous mathematical validation, beach-side case study calibration, and cloud deployment to Render.
"""),
    (34, "User Interface, Dashboard & Visual Results", """
The TerraAI dashboard features a multi-tiered layout:
• Top Navigation: Branding, Hackathon Award Badge, Status Indicators, and Navigation Tabs.
• Main Layout: Split-screen interface with interactive Leaflet map on the left and structural parameter controls on the right.
• Results Panel: Overall Feasibility Score hero card, Lifespan projection, Preliminary Foundation recommendation, and 4 Domain Radar Sub-Scores (Soil, Climate, Hazard, Eco).
• 5-Method EIA Tab: Dedicated tabbed interface displaying complete Leopold matrices, Checklist audits, Sorensen causal chains, McHarg overlay weights, and ML metrics.
"""),
    (35, "EIA Evaluation Results & Reporting", """
The EIA evaluation outputs comprehensive quantitative tables:
• Leopold Matrix: Displays individual activity-receptor interaction scores, identifying earthwork and foundation substructure as primary adverse impact vectors.
• Checklist Audit: Displays threshold standards, observed values, statutory weights, and PASS/WARN/FAIL status.
• McHarg Overlay: Breaks down the 4 spatial layers and outputs composite scores with explicit Zonal classifications (S-1 to S-4).
"""),
    (36, "Web Application Flow — Map Geocoding & Input Handling", """
1. User enters a location name in the geocoding search bar or clicks on the interactive Leaflet map.
2. Map smoothly pans to coordinates with an animated cyan pulsing marker.
3. User selects proposed Building Type (House, Apartment, Hospital, School, Bridge, Factory, Mall) and Storey Height.
4. User clicks 'Run AI & EIA Analysis', initiating the backend evaluation workflow.
"""),
    (37, "Web Application Flow — Analysis, Reports & PDF Dossier", """
1. Client displays an animated skeleton loading state during computation.
2. Backend processes spatial data and returns verified JSON payload in ~2.5 seconds.
3. DOM dynamically populates score cards, domain radars, SHAP contribution charts, and EIA tables.
4. User clicks '📄 Download Official Report' to trigger server-side ReportLab PDF generation, downloading a complete engineering dossier.
"""),
    (38, "3D Simulation Flow — Interactive Physical Hazard Testing", """
1. User navigates to `/visualization` or clicks '🎮 Launch 3D Simulation'.
2. Three.js initializes a WebGL scene rendering a structural frame building on layered subsoil.
3. User toggles hazard stress buttons:
   - Flood Stress: Animates water level rising to +1.8m, demonstrating foundation immersion and tanking barrier utility.
   - Earthquake Stress: Induces lateral oscillating sway, demonstrating ductile shear response.
   - Soft Ground Stress: Simulates vertical subsidence and foundation tilting under low bearing capacity.
4. Stakeholder cards explain structural safety in plain, accessible English.
"""),
    (39, "Verification & Validation Case Studies", """
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
    (40, "Testing & Verification Test Suite", """
The system underwent rigorous testing across four testing tiers:
1. Unit Testing: Verified mathematical accuracy of Leopold index formulas, checklist weighted sums, and McHarg linear overlays using automated test scripts (`test_eia_calc.py`).
2. Geospatial Boundary Testing: Tested 100+ coordinate pairs along India's coastal boundaries, Himalayan fault lines, and Thar desert regions.
3. API Integration Testing: Validated JSON schema responses, HTTP 200/400/500 handlers, and JWT token authorization (`test_e2e_api.py`).
4. End-to-End PDF Compilation Testing: Verified PDF generation under high load, ensuring zero layout truncation or memory leaks (`test_pdf_export.py`).
"""),
    (41, "Detailed Experimental Results & Metrics", """
Machine Learning Model Comparison Benchmark:
• Model 1 (Linear Regression Baseline): R² = 0.6840, MAE = 6.42 pts
• Model 2 (Decision Tree Regressor): R² = 0.7620, MAE = 4.88 pts
• Model 3 (Random Forest Regressor): R² = 0.8845, MAE = 2.45 pts
• Model 4 (XGBoost Regressor): R² = 0.8980, MAE = 2.18 pts
• Model 5 (Extra Trees Regressor): R² = 0.8910, MAE = 2.25 pts
• Model 6 (TerraAI Stacking Ensemble): R² = 0.9123, MAE = ±1.99 pts (Top Performer)
"""),
    (42, "Result Analysis & SHAP Feature Attribution Insights", """
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
• Proven in competition, winning the TNWISE 2026 State-Level Special Mention Award.

43.2 Limitations
• Spatial satellite resolutions (250m–1km) provide regional estimates; cannot replace confirmatory physical borehole tests for final Stage-2 construction.
• Internet connectivity required for live satellite API queries.

43.3 Future Scope
• Integration of high-resolution Drone LiDAR point cloud data.
• Direct BIM (Building Information Modeling) and CAD file foundation export.
• Expansion of global satellite datasets beyond India.
"""),
    (44, "Development Methodology, Hackathon Journey & Timeline", """
Development Timeline:
• Phase 1 (Ideation & Problem Formulation): Identified civil engineering site screening inefficiencies and framed GeoAI architecture.
• Phase 2 (ETL & ML Training): Built satellite connectors and trained Stacking Ensemble model.
• Phase 3 (TNWISE 2026 Hackathon): Competed at Kumaraguru College of Technology / TANCAM, successfully demonstrated live system to jury, and won the Special Mention Award.
• Phase 4 (EIA Mathematical Refinement): Standardized all 5 EIA methods per IS codes and reviewer feedback.
• Phase 5 (Cloud Deployment): Deployed live production service on Render.
"""),
    (45, "Risk Analysis and Mitigation Strategy", """
• Risk 1 (External Satellite API Outages): Mitigated by in-memory spatial KDTrees and historical offline fallback datasets.
• Risk 2 (Misinterpretation as Legal Approval): Mitigated by prominent Stage-0/1 preliminary screening disclaimers on UI and exported PDFs.
• Risk 3 (Server Overload during PDF Generation): Mitigated by Flask-Limiter throttling and Gunicorn asynchronous multi-threading.
"""),
    (46, "References & Statutory Standards", """
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
    (47, "Feedback, Faculty Review & Conclusion", """
47.1 Reviewer Feedback & Mathematical Rectifications
Following rigorous academic review on coastal coordinates (12.9340, 80.2592), all eleven reviewer observations were mathematically rectified:
• Checklist compliance standardized to explicit weighted sum (3/5 PASS = 60.0%).
• Leopold index normalized with explicit mathematical formula (Net Score -46 -> Index 75.8/100).
• McHarg overlay composite score calculated directly from sub-layers (71.0/100 -> Zone S-2).
• Defensive engineering phrasing applied to network hazard pathways per IS 1893:2016.
• Disclaimers added framing the tool for Stage-0/1 preliminary screening.

47.2 Conclusion
TerraAI establishes a benchmark in automated geospatial engineering and environmental assessment. By uniting machine learning, satellite earth observation, Indian Standards compliance, and 3D simulation, the project demonstrates how modern AI can advance sustainable, disaster-resilient infrastructure development.
"""),
    (48, "Sample API Request and Response Payloads", """
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
    (49, "Glossary of Technical & Civil Engineering Terms", """
• Bearing Capacity (kN/m²): The maximum contact pressure between the foundation substructure and supporting subsoil without shear failure or excessive settlement (IS 1904).
• Standard Penetration Test (SPT N-Value): In-situ dynamic penetration test indicating relative soil density and shear strength.
• Eco-Sensitive Zone (ESZ): Statutory 10 km buffer zone surrounding National Parks and Sanctuaries regulated under MoEFCC EIA 2006.
• Leopold Matrix: A 2D interaction matrix cross-referencing proposed project activities against environmental receptors to quantify direct impacts.
• Sorensen Network Method: An impact identification technique tracing primary environmental triggers through secondary conditions to tertiary structural risks.
• McHarg Spatial Overlay: A Multi-Criteria Evaluation (MCE) technique superimposing weighted thematic geospatial map layers to identify optimal suitability zones.
• Stacking Ensemble: An advanced meta-learning architecture where multiple diverse base regressors (Random Forest, XGBoost, Extra Trees) are combined via a meta-model (Ridge Regression).
• SHAP (SHapley Additive exPlanations): A game-theoretic approach to explain individual feature contributions toward machine learning predictions.
""")
]
