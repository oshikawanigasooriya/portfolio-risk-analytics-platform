# Financial Engineering - Portfolio Risk Analytics Platform

## Project Overview

This project is a comprehensive Portfolio Risk Analytics Platform developed using Python, MySQL, Monte Carlo Simulation, and Power BI Dashboarding.

The system integrates real-time market data with financial risk models to calculate Value at Risk (VaR), simulate future stock price movements using Monte Carlo Simulation, and generate professional portfolio risk reports.

This project is designed for financial engineering applications such as investment analysis, portfolio optimization, and risk management.

---

## Technologies Used

- Python
- MySQL
- MySQL Workbench
- yFinance API
- NumPy
- Pandas
- Matplotlib
- Monte Carlo Simulation
- Value at Risk (VaR)
- Power BI
- GitHub

---

## Key Features

### Real-Time Market Data Collection
- Fetch stock market data using yFinance API

### Portfolio Database Management
- Store portfolio assets and investment details using MySQL

### Value at Risk (VaR) Analysis
- Calculate downside portfolio risk using 95% confidence interval

### Monte Carlo Simulation
- Simulate multiple future stock price paths for risk forecasting

### Power BI Dashboard
- Interactive visualization for:
  - Portfolio Allocation
  - Value at Risk Analysis
  - Risk Reporting
  - Asset Performance

---

## Project Structure

portfolio-risk-analytics-platform/
│
├── main.py
├── db_test.py
├── var_calculation.py
├── monte_carlo.py
├── portfolio_report.csv
├── requirements.txt
├── README.md
│
├── screenshots/
│   └── powerbi_dashboard.png
│
└── sql/
    └── database_setup.sql

---

## Sample Dashboard

(Add Power BI dashboard screenshot here)

---

## SQL Database Setup

Run the SQL file:

sql/database_setup.sql

This will create:

- portfolio_risk_db
- portfolios table
- risk_reports table

---

## Installation

### Install Required Libraries

```bash
pip install -r requirements.txt
