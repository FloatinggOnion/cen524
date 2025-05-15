## Productivity Analysis Report for FlexiSAF Edusoft Limited
*Author: Jesse-Paul Miracle Osemeke*
*Matric No: 20CJ027483*
*Programme: Computer Engineering*

**Period:** November 2024 – April 2025
**Subjects:** 10 interns; **Styles:** Remote vs On‑site

### 1. Introduction

This report examines how hours worked influence tasks completed and whether work style (remote vs on‑site) modifies this relationship. We analyse six months of data for ten interns at FlexiSAF Edusoft Limited.

### 2. Methods

We simulated intern data for 10 employees over six months, recording:

* **Hours worked** (continuous)
* **Tasks completed** (count)
* **Work style** (categorical: Remote/On‑site)

A linear regression model was fitted with an interaction term between hours and on‑site style to estimate differential productivity gains.

### 3. Results & Visualisations

#### 3.1 Scatter Plot of Tasks vs Hours by Style

*(See Notebook Figure 1)*
A positive trend appears for both styles, with on‑site generally showing higher tasks per hour.

#### 3.2 Regression Coefficients

* **Intercept:** (baseline tasks at zero hours, remote)
* **Hours coefficient:** (tasks per additional hour, remote)
* **On‑site effect:** (baseline shift for on‑site)
* **Interaction (Hours × On‑site):** (extra tasks per hour when on‑site)

*(Exact values in Notebook)*

#### 3.3 Actual vs Predicted Tasks

*(See Notebook Figure 2)*
Predictions track closely with actuals, indicating a good fit and confirming that on‑site hours yield slightly higher productivity.

### 4. Discussion

Our analysis suggests that while increased hours boost tasks in both settings, on‑site work provides a modest additional productivity advantage per hour. This may reflect better access to resources, collaboration opportunities, or reduced distractions.

### 5. Conclusion

FlexiSAF Edusoft Limited can anticipate that shifting work on‑site leads to marginally greater per‑hour output. Future work should validate these findings on actual intern data and consider additional factors such as task complexity and employee experience.
