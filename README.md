# TerraAI: AI & Multi-Criteria EIA Construction Site Selection System

An end-to-end intelligent Geospatial AI & Academic Environmental Impact Assessment (EIA) platform for automated construction feasibility, hazard vulnerability, foundation engineering, and multi-criteria site suitability analysis across India.

---

## 🏗️ Key Features

* **Multi-Source Geospatial Live Ingestion**:
  * Soil parameters (ISRIC SoilGrids & Bhuvan Geo-Portal)
  * Climate, Precipitation & Extreme Weather (NASA POWER Ag-Climatology)
  * Environmental Hazards, Floods, Seismic Zones & Waterways (USGS / Overpass OSM / BMTPC Atlas)
  * Ecological Sensitivity, Sanctuaries & Wildlife Corridors (GBIF & MoEFCC Protected Area Database)
* **5 Academic & Statutory EIA Methodologies**:
  * **Checklist Method**: Statutory Weighted Compliance ($25\%$ Soil, $20\%$ Seismic, $20\%$ Flood, $20\%$ Eco, $15\%$ pH).
  * **Leopold Matrix**: 2D Interaction Matrix ($[-10\dots+10]$ Magnitude $\times$ $[1\dots10]$ Importance) with normalized index calculation.
  * **Sorensen Network Method**: Cause $\rightarrow$ Condition $\rightarrow$ Effect hazard pathways per IS 1893:2016.
  * **McHarg Spatial Overlay**: Multi-Criteria GIS weighted linear combination ($35\%$ Soil, $25\%$ Climate, $25\%$ Hazard, $15\%$ Eco) with S-1 to S-4 Zonal classification.
  * **Stacking Ensemble AI Modeling**: Random Forest + XGBoost + Extra Trees $\rightarrow$ Ridge Meta-Regressor ($R^2 = 0.9123$, $\text{MAE} = \pm 1.99\text{ pts}$).
* **3D Visual & Hazard Simulation Engine**:
  * Interactive Three.js physical simulation (flood inundation depth, earthquake dynamic oscillation, soft soil settlement).
  * Plain-English stakeholder scorecards for non-technical clients.
* **Automated PDF Report Generation**:
  * Export official engineering and environmental screening dossiers formatted per Indian Standards (IS 1904, IS 1893, IS 2911, IS 13920).

---

## 🚀 Quickstart & Local Setup

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/Selvi-github/terra_AI_construction_site.git
cd terra_AI_construction_site
pip install -r requirements.txt
```

### 2. Run Application
```bash
python app.py
```
Open **[http://127.0.0.1:5000](http://127.0.0.1:5000)** in your browser.

---

## ☁️ Deploy to Render (Cloud Hosting)

This repository includes [`render.yaml`](render.yaml) and [`Procfile`](Procfile) for 1-click cloud deployment:

1. Create a free account at **[render.com](https://render.com/)**.
2. Click **New +** $\rightarrow$ **Web Service** and connect this GitHub repository.
3. Set the following parameters:
   * **Runtime**: `Python 3`
   * **Build Command**: `pip install -r requirements.txt`
   * **Start Command**: `gunicorn --workers 2 --threads 4 --timeout 120 app:app`
4. Click **Deploy Web Service** to launch.

---

## 📜 Standards & References
* **IS 1904:1986 / 2021**: Code of practice for design and construction of foundations in soils.
* **IS 1893 (Part 1): 2016**: Criteria for Earthquake Resistant Design of Structures.
* **IS 13920:2016**: Ductile Design and Detailing of Reinforced Concrete Structures.
* **MoEFCC EIA Notification 2006**: Environmental Clearance and Eco-Sensitive Zone (ESZ) guidelines.
