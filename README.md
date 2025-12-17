# 🏠 Integrated Decision Support System (DSS) for Accommodation Matching and Occupancy Optimization in Berlin

## 📌 Overview
This project develops an **Integrated Decision Support System (DSS)** to address Berlin’s housing challenges, focusing on **students, international renters, and housing administrators**. The DSS integrates verified housing data, transport accessibility, payment validation, and occupancy forecasting to support transparent, efficient, and data-driven housing decisions.

---

## 🎯 Background & Problem Context
Berlin’s housing market is competitive and fragmented. Students and renters face:
- **Payment channel fragmentation** → delays or failed transfers across platforms.
- **Listing verification issues** → outdated or fraudulent postings.
- **Approximate location data** → difficulty in commute calculations.
- **Transport accessibility gaps** → uncertainty about proximity to U-Bahn, S-Bahn, and buses.

The DSS aims to solve these issues by combining **verified listings, transport data, fraud detection, and occupancy optimization** into a unified platform.

---

## 🏆 Project Objectives
1. Match tenants with **verified, affordable, and accessible housing**.
2. Implement **data validation and listing verification** to reduce scams.
3. Integrate **transportation data** for commute calculations.
4. Forecast **occupancy demand and capacity** for housing providers.
5. Provide **interactive dashboards** for users and administrators.

---

## 🛠️ Scope & DSS Type
- **Decision Type:** Semi-structured (algorithmic + human validation).  
- **Classification:** Hybrid DSS (Model-Driven + Data-Driven + Knowledge-Driven).  
- **Users:** Students, international renters, housing administrators, property managers.  
- **Scope:** Berlin housing market (student dorms, verified private rentals, accessibility mapping).  

---

## ⚙️ DSS Components
| Subsystem | Function |
|-----------|-----------|
| **Data Management (DMSS)** | Collects housing, transport, and user preference data; cleans and stores centrally. |
| **Model Management (MMSS)** | Predictive models for occupancy forecasting and tenant-to-housing matching. |
| **Knowledge Management (KMSS)** | Encodes policies, verification rules, eligibility criteria, prioritization logic. |
| **User Interface (UIS)** | Dashboards showing verified listings, transport routes, and occupancy recommendations. |

---

## 📊 Data, Models, and Tools

### Data Sources
- **Berlin Rental Market Dataset** (Airbnb data, Kaggle) → housing availability, price, geolocation.  
- **Hotel Booking & Demand Datasets** (Kaggle) → occupancy forecasting, cancellation patterns.  
- **Hotel Reviews & Ratings Dataset** → satisfaction and quality indicators.  
- **Hotel Room Prices Dataset** → pricing validation and comparisons.  
- **Public Transport APIs (BVG, Google Maps)** → commute times, accessibility mapping.  

### Models & Algorithms
- **Matching & Clustering:** Weighted scoring, k-means grouping by price/distance.  
- **Optimization:** Linear programming for demand vs. supply balance.  
- **Forecasting:** Prophet / ARIMA for occupancy and demand prediction.  
- **Verification:** Rule-based + ML models for fraud detection and duplicate removal.  

### Technologies
- **Python** (Pandas, Scikit-learn, Prophet, OR-Tools)  
- **Databases:** PostgreSQL  
- **Visualization:** Power BI, Streamlit  
- **ETL:** Airbyte  
- **APIs:** BVG API, Google Maps API  

---

## 🧩 Alignment with Simon’s Decision-Making Model
| Phase | DSS Support |
|-------|-------------|
| **Intelligence** | Collects and validates housing, payments, and transport data. |
| **Design** | Generates optimal matches based on affordability, distance, verification. |
| **Choice** | Recommends verified, accessible listings to users/admins. |
| **Implementation** | Updates allocations, confirms payments, tracks occupancy metrics. |

---

## 📈 Expected Outcomes
- Verified and transparent housing recommendation system.  
- Fraud prevention via automated data verification.  
- Accurate commute and transport integration.  
- Improved occupancy optimization for dorms and rentals.  
- User-friendly dashboards for monitoring and forecasting.  

---

## 🔍 Comparative Perspective
| Aspect | Student Accommodation DSS | Revenue Optimization DSS | Proposed Berlin DSS |
|--------|---------------------------|--------------------------|---------------------|
| **Main Focus** | Fair allocation | Profit maximization | Matching, verification, accessibility |
| **Key Problem Solved** | Allocation fairness | Revenue optimization | Data accuracy, trust, mobility |
| **Users** | Students, admins | Hotel managers | Students, renters, admins |
| **Tools** | SQL, Power BI | Python, Metabase | Python, Power BI, BVG API |
| **Output** | Placement results | Revenue forecasts | Verified listings + occupancy map |

---

## 📅 Timeline
| Phase | Weeks | Deliverables |
|-------|-------|--------------|
| Planning | 3–5 | Finalize topic, assign roles, identify datasets |
| Analysis | 6–7 | Clean & validate Berlin housing + transport data |
| Design | 8–9 | Define DSS architecture, models, rule sets |
| Construction | 10–13 | Develop matching + optimization models, integrate verification |
| Implementation | 14 | Build interactive dashboard, test DSS functionality |
| Presentation | 15–16 | Deliver final DSS prototype + group presentation |

---
