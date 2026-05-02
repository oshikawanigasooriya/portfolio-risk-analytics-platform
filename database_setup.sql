CREATE DATABASE portfolio_risk_db;

USE portfolio_risk_db;

CREATE TABLE portfolios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100),
    weight DECIMAL(10,2),
    investment_amount DECIMAL(10,2)
);

CREATE TABLE risk_reports (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100),
    var_value DECIMAL(10,2),
    expected_shortfall DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO portfolios
(asset_name, weight, investment_amount)
VALUES
('AAPL', 30.00, 500000.00),
('MSFT', 25.00, 400000.00),
('TSLA', 20.00, 300000.00);