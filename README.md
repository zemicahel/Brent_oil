
# 📊 Brent Oil Bayesian Change Point Analysis (1987–2022)

## 🔍 Overview

This project investigates **structural regime changes in Brent crude oil prices** between **1987 and 2022** using a **Bayesian Change Point model implemented in PyMC**.

The analysis integrates:

* 📈 Time series diagnostics
* 🧠 Bayesian structural break detection
* 🌍 Geopolitical event mapping
* 🚀 Full-stack interactive dashboard

The goal is to detect statistically significant price regime shifts and assess their alignment with major geopolitical and economic events.

---

# 🎯 Objectives

* Detect structural breaks in Brent oil prices
* Quantify uncertainty in regime shifts using Bayesian inference
* Compare detected change points with real-world geopolitical events
* Communicate findings via an interactive dashboard

---

# 🗂 Project Structure

```
brent-oil-bayesian-change-point/
│
├── data/
│   └── raw/
│       └── BrentOilPrices.csv
│
├── events/
│   └── oil_market_events.csv
│
├── notebooks/
│   └── 01_change_point_analysis.ipynb
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── routes/
│   └── services/
│
├── frontend/
│   ├── src/
│   └── package.json
│
└── README.md
```

---

# 🧠 Methodology

## 1️⃣ Exploratory Data Analysis

* Time series visualization
* Rolling mean and volatility
* Return distribution analysis
* Stationarity testing (ADF / KPSS)

Key Findings:

* Price levels are non-stationary
* Returns exhibit volatility clustering
* Clear regime shifts during major crises

---

## 2️⃣ Bayesian Change Point Model

The model detects structural breaks in mean price levels.

### Model Components

* Prior distributions for:

  * Regime means
  * Volatility
  * Change point location
* Gaussian likelihood
* Posterior sampling via MCMC (PyMC)

### Why Bayesian?

* Provides credible intervals
* Quantifies timing uncertainty
* Incorporates prior economic reasoning
* Avoids overfitting

---

# 🌍 Geopolitical Event Dataset

The model output is compared against key events such as:

* Gulf War (1990)
* Asian Financial Crisis (1997)
* 9/11 Attacks (2001)
* Global Financial Crisis (2008)
* OPEC Production Decisions
* COVID-19 Pandemic (2020)
* Russia–Ukraine War (2022)

This enables contextual interpretation of regime shifts.

---

# 📈 Dashboard (Full Stack Implementation)

The project includes a responsive React dashboard that displays:

* Brent oil price time series
* Detected change point (vertical reference line)
* Regime statistics (before/after means)
* Event annotations

### Tech Stack

**Backend**

* Flask
* Pandas
* NumPy
* Custom change point computation

**Frontend**

* React (Vite)
* Recharts
* Axios

---

# ⚙️ Installation & Setup

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/brent-oil-bayesian-change-point.git
cd brent-oil-bayesian-change-point
```

---

## 2️⃣ Backend Setup

```bash
cd backend
python -m venv env
source env/bin/activate   # macOS/Linux
env\Scripts\activate      # Windows

pip install -r requirements.txt
python app.py
```

Backend runs at:

```
http://localhost:5000
```

---

## 3️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```
http://localhost:5173
```

---

# 📊 Example API Endpoints

```
GET /api/prices
GET /api/changepoints
GET /api/events
```

---

# 📌 Key Findings

* Brent oil prices exhibit clear structural regime shifts.
* Major geopolitical shocks align closely with detected change points.
* Volatility clustering intensifies during crisis periods.
* Bayesian modeling effectively quantifies regime uncertainty.

---

# ⚠️ Assumptions & Limitations

* Structural breaks reflect regime changes, not random noise.
* Temporal alignment does not imply causality.
* Model assumes piecewise-constant mean behavior.
* External confounders are not explicitly modeled.

---

# 📚 Academic Foundations

* Bayesian Inference
* Structural Break Detection
* Time Series Analysis
* Energy Economics

---

# 🚀 Future Improvements

* Multiple change point detection
* Regime-switching volatility models
* Event impact quantification
* Deployment (Render / Vercel)
* Docker containerization

---

# 👤 Author

**Zemicahel Abraham**
Data Science | Bayesian Modeling | Economic Analysis

---

# ⭐ Why This Project Matters

Oil price volatility affects:

* Energy security
* Inflation dynamics
* Fiscal policy
* Global economic stability

This project demonstrates how **probabilistic modeling can translate raw market data into policy-relevant insights.**

---

---

# 💎 Optional: Add Badges (Recommended)

At the top of your README you can add:

```markdown
![Python](https://img.shields.io/badge/Python-3.10-blue)
![React](https://img.shields.io/badge/React-18-blue)
![PyMC](https://img.shields.io/badge/Bayesian-PyMC-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
```

