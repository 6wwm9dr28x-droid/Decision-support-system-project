# Integrated Decision Support System (DSS) for Accommodation Matching and Occupancy Optimization in Berlin

## Overview
This project develops an **Integrated Decision Support System (DSS)** to address Berlin’s housing challenges, focusing on **tenants and landlords**. The DSS integrates verified housing data, payment validation, and occupancy forecasting to support transparent, efficient, and data-driven housing decisions.

---

## Background & Problem Context
Berlin’s housing market is competitive and fragmented. Tenants face:
- **Payment channel fragmentation** → delays or failed transfers across platforms.
- **Listing verification issues** → outdated or fraudulent postings.
- **Approximate location data** → difficulty in evaluating housing options.
- **Occupancy uncertainty** → landlords struggle to forecast demand and minimize vacancies.

The DSS aims to solve these issues by combining **verified listings, fraud detection, and occupancy optimization** into a unified platform.

---

## Project Objectives
1. Match tenants with **verified and affordable housing**.
2. Implement **data validation and listing verification** to reduce scams.
3. Forecast **occupancy demand and capacity** for landlords.
4. Provide **interactive dashboards** for tenants and landlords.

---

## Scope & DSS Type
- **Decision Type:** Semi-structured (algorithmic + human validation).  
- **Classification:** Hybrid DSS (Model-Driven + Data-Driven + Knowledge-Driven).  
- **Users:** Tenant, Landlord.  
- **Scope:** Berlin housing market (student dorms, verified private rentals, occupancy mapping).  

---

## DSS Components
| Subsystem | Function |
|-----------|-----------|
| **Data Management (DMSS)** | Collects housing and user preference data; cleans and stores centrally. |
| **Model Management (MMSS)** | Predictive models for occupancy forecasting and tenant-to-housing matching. |
| **Knowledge Management (KMSS)** | Encodes policies, verification rules, eligibility criteria, prioritization logic. |
| **User Interface (UIS)** | Dashboards showing verified listings and occupancy recommendations. |

---

## Data, Models, and Tools

### Data Sources
- **Berlin Rental Market Dataset** (Airbnb data, Kaggle) → housing availability, price, geolocation.  
- **Hotel Booking & Demand Datasets** (Kaggle) → occupancy forecasting, cancellation patterns.  
- **Hotel Reviews & Ratings Dataset** → satisfaction and quality indicators.  
- **Hotel Room Prices Dataset** → pricing validation and comparisons.  

### Models & Algorithms
- **Matching & Clustering:** Weighted scoring, k-means grouping by price/distance.  
- **Optimization:** Linear programming for demand vs. supply balance.  
- **Forecasting:** Prophet / ARIMA for occupancy and demand prediction.  
- **Verification:** Rule-based + ML models for fraud detection and duplicate removal.  

### Technologies
- **Python** (Pandas, Scikit-learn, Prophet, OR-Tools)  
- **Databases:** PostgreSQL / MongoDB  
- **Visualization:** Power BI, Streamlit  
- **ETL:** Airbyte  

---

## Alignment with Simon’s Decision-Making Model
| Phase | DSS Support |
|-------|-------------|
| **Intelligence** | Collects and validates housing and payment data. |
| **Design** | Generates optimal matches based on affordability and verification. |
| **Choice** | Recommends verified listings to tenants and landlords. |
| **Implementation** | Updates allocations, confirms payments, tracks occupancy metrics. |

---

## Expected Outcomes
- Verified and transparent housing recommendation system.  
- Fraud prevention via automated data verification.  
- Improved occupancy optimization for landlords.  
- User-friendly dashboards for monitoring and forecasting.  

---

## Comparative Perspective
| Aspect | Tenant Accommodation DSS | Revenue Optimization DSS | Proposed Berlin DSS |
|--------|--------------------------|--------------------------|---------------------|
| **Main Focus** | Fair allocation | Profit maximization | Matching, verification, occupancy |
| **Key Problem Solved** | Allocation fairness | Revenue optimization | Data accuracy, trust |
| **Users** | Tenant | Landlord | Tenant, Landlord |
| **Tools** | Power BI | Python, Metabase | Python, Power BI |
| **Output** | Placement results | Revenue forecasts | Verified listings + occupancy map |

---

## Timeline
| Phase | Weeks | Deliverables |
|-------|-------|--------------|
| Planning | 3–5 | Finalize topic, assign roles, identify datasets |
| Analysis | 6–7 | Clean & validate Berlin housing data |
| Design | 8–9 | Define DSS architecture, models, rule sets |
| Construction | 10–13 | Develop matching + optimization models, integrate verification |
| Implementation | 14 | Build interactive dashboard, test DSS functionality |
| Presentation | 15–16 | Deliver final DSS prototype + group presentation |

---

## System Architecture Diagram

```mermaid
flowchart TD
    A[Berlin Housing Data] --> B[Data Management Subsystem (DMSS)]
    B --> C[Model Management Subsystem (MMSS)]
    C --> D[Knowledge Management Subsystem (KMSS)]
    D --> E[User Interface Subsystem (UIS)]

    subgraph DMSS
        B1[Collect housing and tenant preferences]
        B2[Clean & store in central warehouse]
    end

    subgraph MMSS
        C1[Matching algorithms: weighted scoring, clustering]
        C2[Forecasting: Prophet / ARIMA]
        C3[Optimization: Linear programming]
    end

    subgraph KMSS
        D1[Verification rules]
        D2[Eligibility criteria]
        D3[Prioritization policies]
    end

    subgraph UIS
        E1[Dashboards: verified listings]
        E2[Occupancy recommendations]
    end
