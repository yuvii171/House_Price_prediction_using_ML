
# House Price Prediction Model Using Machine Learning

An end-to-end data engineering and machine learning pipeline designed to automate property valuation. [cite_start]This project builds a scalable forecasting framework that addresses non-linear complexity, market heterogeneity, and feature interdependencies in real estate data[cite: 68].

[cite_start]This repository represents work completed during the training program: **AI/ML For Real Time Application** at **Motilal Nehru National Institute of Technology (MNNIT) Prayagraj**[cite: 1, 4].

---

## 📌 Project Overview

[cite_start]Traditional real estate appraisal methods often face challenges with consistency due to massive data points and localized assumptions[cite: 61, 62, 63]. [cite_start]This project resolves these bottlenecks by developing an automated ingestion and preprocessing pipeline alongside optimized predictive architectures to meet real-world industry benchmarks[cite: 75, 77].

### Core Objectives
* [cite_start]**Pipeline Engineering:** Automate data ingestion, mean/mode imputation, IQR outlier capping, categorical encoding, and variance scaling[cite: 75].
* [cite_start]**Algorithmic Analysis:** Implement and evaluate Linear Regression and Random Forest Regressor models[cite: 47, 48].
* [cite_start]**Target Performance:** Exceed an $R^2$ baseline metric of 0.85 on test datasets[cite: 77].
* [cite_start]**Feature Interpretability:** Identify and extract the key drivers behind property valuation[cite: 79].

---

## ⚙️ System Architecture & Methodology

[cite_start]The project structure follows a modular pipeline approach to avoid data leakage and ensure reproducible execution[cite: 121, 268]:

Raw Data Ingestion (1,200 Records) 
│
▼
Data Preprocessing (Imputation, Capping, Encoding) 
│
┌─────┴────────────────────────┐
▼                              ▼
Exploratory Data Analysis  Data Splitting & Normalization (80/20 Train-Test) 
│                              │
▼                              ├────────────────────────┐
Feature Engineering               ▼                        ▼
(Calculated Domain Metrics) Linear Regression Baseline Random Forest Regressor 
│                        │
▼                        ▼
Evaluation Metrics       Valuation & Deployment

Here is a clean, comprehensive, and professional `README.md` file content tailored for your GitHub repository. It breaks down your project structure, system architecture, and findings in a clear, scannable format.


# House Price Prediction Model Using Machine Learning

An end-to-end data engineering and machine learning pipeline designed to automate property valuation. [cite_start]This project builds a scalable forecasting framework that addresses non-linear complexity, market heterogeneity, and feature interdependencies in real estate data[cite: 68].

[cite_start]This repository represents work completed during the training program: **AI/ML For Real Time Application** at **Motilal Nehru National Institute of Technology (MNNIT) Prayagraj**[cite: 1, 4].

---

## 📌 Project Overview

[cite_start]Traditional real estate appraisal methods often face challenges with consistency due to massive data points and localized assumptions[cite: 61, 62, 63]. [cite_start]This project resolves these bottlenecks by developing an automated ingestion and preprocessing pipeline alongside optimized predictive architectures to meet real-world industry benchmarks[cite: 75, 77].

### Core Objectives
* [cite_start]**Pipeline Engineering:** Automate data ingestion, mean/mode imputation, IQR outlier capping, categorical encoding, and variance scaling[cite: 75].
* [cite_start]**Algorithmic Analysis:** Implement and evaluate Linear Regression and Random Forest Regressor models[cite: 47, 48].
* [cite_start]**Target Performance:** Exceed an $R^2$ baseline metric of 0.85 on test datasets[cite: 77].
* [cite_start]**Feature Interpretability:** Identify and extract the key drivers behind property valuation[cite: 79].

---

## ⚙️ System Architecture & Methodology

[cite_start]The project structure follows a modular pipeline approach to avoid data leakage and ensure reproducible execution[cite: 121, 268]:




Raw Data Ingestion (1,200 Records) 
│
▼
Data Preprocessing (Imputation, Capping, Encoding) 
│
┌─────┴────────────────────────┐
▼                              ▼
Exploratory Data Analysis  Data Splitting & Normalization (80/20 Train-Test) 
│                              │
▼                              ├────────────────────────┐
Feature Engineering               ▼                        ▼
(Calculated Domain Metrics) Linear Regression Baseline Random Forest Regressor 
│                        │
▼                        ▼
Evaluation Metrics       Valuation & Deployment 



### 🧠 Engineered Features
[cite_start]To give the models better predictive power, 6 new domain-specific features were generated[cite: 269]:
1.  [cite_start]**Price per Square Foot:** $\text{Price}_{\text{PSF}} = \frac{\text{Selling Price}}{\text{Building Size}}$ [cite: 270, 272]
2.  [cite_start]**Property Age:** $\text{Age} = 2026 - \text{Year Built}$ [cite: 271, 273]
3.  [cite_start]**Bathroom-to-Bedroom Ratio:** $\frac{\text{Bathrooms}}{\text{Bedrooms}}$ [cite: 274, 276]
4.  [cite_start]**Lot Size per Bedroom:** $\frac{\text{Lot Size}}{\text{Bedrooms}}$ [cite: 275, 276]
5.  [cite_start]**Total Living Units Score:** $\frac{\text{Bedrooms} + \text{Bathrooms}}{2}$ [cite: 277, 279, 280]
6.  [cite_start]**Location Quality Index:** $100 - \left(\frac{\text{Distance to Center}}{\text{Max Distance}} \times 100\right)$ [cite: 281, 282]

---

## 📊 Model Performance & Findings

[cite_start]The models were verified using 5-fold cross-validation to guarantee structural stability[cite: 292].

### Performance Metrics

| Algorithm Paradigm | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) | Test $R^2$ Score |
| :--- | :--- | :--- | :--- |
| **Linear Regression Baseline** | [cite_start]16,416.91 [cite: 293] | [cite_start]21,650.72 [cite: 293] | [cite_start]**0.967** [cite: 293] |
| **Random Forest Regressor** | [cite_start]41,107.42 [cite: 293] | [cite_start]50,409.55 [cite: 293] | [cite_start]0.823 [cite: 293] |

> [cite_start]**Note on Findings:** The optimized Random Forest configuration successfully captures complex regional variations, explaining up to 88.4% of price deviations in broader subsets[cite: 322]. [cite_start]Feature importance analysis indicates that **Building Size (34.8%)** and **Distance to City Center (22.4%)** remain the most critical driving factors behind property values[cite: 299, 301, 323].

---

## 🛑 Limitations & Future Scope

### Current Limitations
* [cite_start]**Geographic Boundaries:** Focused heavily on developing Indian regional markets such as Noida, Gurugram, Lucknow, and Prayagraj[cite: 326].
* [cite_start]**Qualitative Gaps:** Lacks local community parameters like safety indexes, neighborhood school ratings, or immediate access to transit hubs[cite: 328, 329].
* [cite_start]**Luxury Data Sparsity:** High-end pricing segments ($> ₹900,000$) are exceptionally rare in the dataset, leading to minor variance drops in luxury predictions[cite: 330, 331].

### Future Horizons
* [cite_start]**Short-Term:** Integrate automated hyperparameter tuning (Bayesian Optimization) and a SHAP framework for local interpretability insights[cite: 334, 335].
* [cite_start]**Medium-Term:** Introduce macroeconomic time-series features (interest rates, inflation tracking) and test advanced gradient boosting models[cite: 338].
* [cite_start]**Long-Term:** Build a comprehensive platform leveraging NLP for parsing property descriptions and Computer Vision for real-time condition grading via photos[cite: 339, 340].

---

## 👥 Authors & Acknowledgments

* [cite_start]**Contributors:** Yuvraj Singh, Yash Sharma, and Vanya Keshrawani (United College of Engineering & Research)[cite: 6, 7].
* [cite_start]**Program Coordinator:** Submitted to Arpit Dubey Sir[cite: 9].
* [cite_start]**Host Institution:** Organized via IIHMF, Motilal Nehru National Institute of Technology (MNNIT) Prayagraj[cite: 1, 2].

