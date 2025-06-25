
# Technical Specifications for Personalized Upskilling Recommender Streamlit Application

## Overview

The "Personalized Upskilling Recommender" is a Streamlit application designed to empower users to mitigate AI-driven job displacement risk. It provides a personalized assessment of an individual's vulnerability based on their current occupation, skills, and learning progress. By leveraging the multi-factor risk model detailed in the provided research document, the application calculates an AI-Q score, identifies skill gaps, suggests relevant learning resources, and allows users to track their progress, directly illustrating the concept of **Idiosyncratic Risk Mitigation**.

This application transforms complex actuarial and economic models into an intuitive, interactive tool, making the abstract concept of AI displacement risk tangible and actionable for individuals. It directly references and explains Formula 4 from the research document to demonstrate how specific skills (general vs. firm-specific) impact an individual's Idiosyncratic Risk score.

## Step-by-Step Development Process

1.  **Data Model Definition**:
    *   Define the structure of the synthetic dataset for:
        *   Occupation-specific baseline hazards ($H_{base}$).
        *   Lookup tables for Human Capital Factors ($f_{role}$, $f_{level}$, $f_{field}$, $f_{school}$).
        *   Company stability factors ($FCR$).
        *   Learning resources (courses, certifications) with associated skill categories (general/firm-specific).
        *   Historical/synthetic time-series data for Environmental Modifiers ($M_{econ}$, $I_{AI}$).
    *   Create Python dictionaries or Pandas DataFrames to store these lookups.

2.  **Core Calculation Module (`calculations.py`)**:
    *   Implement each mathematical formula from the document as a Python function.
    *   Ensure strict adherence to the defined LaTeX formatting for documentation within the app.
    *   Develop functions for:
        *   `calculate_fhc` (Human Capital Factor)
        *   `calculate_fcr` (Company Risk Factor)
        *   `calculate_fus` (Upskilling Factor)
        *   `calculate_idiosyncratic_risk` ($V_{i}(t)$)
        *   `calculate_h_base` (Base Occupational Hazard, including TTV modifier)
        *   `calculate_systematic_risk` ($H_{i}$)
        *   `calculate_annual_claim_probability` ($P_{claim}$)
        *   `calculate_expected_loss` ($E[Loss]$)
        *   `calculate_monthly_premium` ($P_{monthly}$)

3.  **Data Preprocessing and Utility Module (`data_utils.py`)**:
    *   Functions to load and manage synthetic data.
    *   Functions for data validation and sanitization.
    *   Utility functions for skill mapping and resource linking.

4.  **Visualization Module (`visualizations.py`)**:
    *   Functions using Plotly Express (or Matplotlib/Seaborn) to create interactive charts.
    *   Implement functions for:
        *   Bar charts showing risk factor contributions.
        *   Line charts tracking AI-Q score and premium over time based on upskilling progress.
        *   Scatter plots for skill gap analysis.
        *   Incorporate annotations and tooltips.

5.  **Streamlit Application Script (`app.py`)**:
    *   Set up the Streamlit page configuration.
    *   Design the user interface using Streamlit widgets for input and display.
    *   Integrate functions from `calculations.py`, `data_utils.py`, and `visualizations.py`.
    *   Manage application state using `st.session_state` for persistent user inputs and calculated results.
    *   Implement logic for real-time updates based on user interaction.
    *   Include explanatory markdown for concepts, definitions, and practical examples, with all mathematical formulae properly formatted in LaTeX.

## Core Concepts and Mathematical Foundations

This section details the key mathematical models and concepts from the research document that will be implemented in the application.

### Idiosyncratic Risk (Vulnerability)

The Idiosyncratic Risk, or Vulnerability ($V_{i}(t)$), is a granular, multi-factor assessment of an individual's susceptibility to job displacement. It is calculated as a composite of Human Capital ($FHC$), Company Risk ($FCR$), and Proactive Upskilling efforts ($FUS$).

The general form is:
$$
V_{i}(t) = f(FHC, FCR, FUS)
$$
And specifically, it is modeled as a weighted product:
$$
V_{raw} = FHC \cdot (w_{CR} \cdot FCR + w_{US} \cdot FUS)
$$
Where:
-   $V_{i}(t)$: The final normalized Idiosyncratic Risk score for individual $i$ at time $t$.
-   $V_{raw}$: The raw Idiosyncratic Risk score before normalization.
-   $FHC$: Human Capital Factor, assessing foundational resilience.
-   $FCR$: Company Risk Factor, quantifying employer stability.
-   $FUS$: Upskilling Factor, reflecting proactive training efforts.
-   $w_{CR}$: Weight for Company Risk Factor (e.g., 0.4).
-   $w_{US}$: Weight for Upskilling Factor (e.g., 0.6).

This formula combines individual-specific attributes to produce a personalized vulnerability score. The application will allow users to input their details and see how these factors contribute to their overall Idiosyncratic Risk. The final $V_{i}(t)$ is normalized to a scale of 0-100 using: $V_{i}(t) = \min(100.0, \max(5.0, V_{raw} \cdot 50.0))$.

### Human Capital Factor

The Human Capital Factor ($FHC$) assesses an individual's foundational resilience based on their educational and professional background. It is calculated as a weighted product of several sub-factors:
$$
FHC = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
$$
Where:
-   $FHC$: Human Capital Factor.
-   $f_{role}$: Role Multiplier, representing inherent job title vulnerability.
-   $f_{level}$: Education Level Factor, based on highest education attained.
-   $f_{field}$: Education Field Factor, rewarding transferable skills.
-   $f_{school}$: Institution Tier Factor, proxy for quality of foundational training.
-   $f_{exp}$: Experience Factor, a decaying function of years of experience.

This formula provides a detailed breakdown of how an individual's background contributes to their risk. The application will collect user inputs for these sub-factors and display their calculated $FHC$.

### Company Risk Factor

The Company Risk Factor ($FCR$) quantifies the stability and growth prospects of the individual's current employer, analogous to a corporate credit rating.
$$
FCR = w_{1} \cdot S_{senti} + w_{2} \cdot S_{fin} + w_{3} \cdot S_{growth}
$$
Where:
-   $FCR$: Company Risk Factor.
-   $S_{senti}$: Sentiment Score, derived from real-time NLP analysis of news concerning the company.
-   $S_{fin}$: Financial Health Score, based on the company's financial statements.
-   $S_{growth}$: Growth & AI-Adoption Score, indicating proactive AI adaptation.
-   $w_{1}, w_{2}, w_{3}$: Weighting parameters for each sub-factor.

This formula aggregates different aspects of a company's health and AI adoption to determine its stability, directly impacting the employee's displacement risk. The application will use a synthetic lookup based on company type (e.g., "Big Firm", "Mid-size Firm", "Startup") to represent these scores.

### Upskilling Factor

The Upskilling Factor ($FUS$) is enhanced to differentiate between skill types, rewarding portable skills more heavily. This formula directly addresses how individual learning efforts mitigate risk, especially emphasizing general, portable skills over firm-specific ones.
$$
F_{US} = 1 - (\gamma_{gen} P_{gen}(t) + \gamma_{spec} P_{spec}(t))
$$
Where:
-   $F_{US}$: Upskilling Factor.
-   $P_{gen}(t)$: Individual's training progress (from 0 to 1) in "General" or "Portable" skills (e.g., Python, data analysis) at time $t$.
-   $P_{spec}(t)$: Individual's training progress (from 0 to 1) in "Firm-Specific" skills (e.g., proprietary internal software) at time $t$.
-   $\gamma_{gen}$: Weighting parameter for general skills.
-   $\gamma_{spec}$: Weighting parameter for firm-specific skills.

This formula is critical to the "Personalized Upskilling Recommender" as it directly showcases the impact of upskilling on risk mitigation. The application will allow users to input their training progress for both general and firm-specific skills, demonstrating how $F_{US}$ changes and consequently reduces their Idiosyncratic Risk. The condition $\gamma_{gen} > \gamma_{spec}$ ensures that acquiring portable skills provides a greater reduction in risk, operationalizing the document's emphasis.

### Systematic Risk (Hazard)

The Systematic Risk score ($H_{i}$) is a dynamic index reflecting the macro-level automation hazard of an occupation, adjusted by broader environmental factors.
$$
H_{i} = H_{base}(t) \cdot (w_{econ} M_{econ} + w_{inno} I_{AI})
$$
Where:
-   $H_{i}$: The final Systematic Risk score.
-   $H_{base}(t)$: Base Occupational Hazard for the occupation at time $t$.
-   $M_{econ}$: Economic Climate Modifier, capturing macroeconomic environment's effect on AI investment.
-   $I_{AI}$: AI Innovation Index, capturing velocity of technological change.
-   $w_{econ}, w_{inno}$: Calibration weights that sum to 1.0 (e.g., 0.5 each).

This formula accounts for external factors influencing job displacement risk. The application will provide sliders or selections for synthetic $M_{econ}$ and $I_{AI}$ values to demonstrate their impact.

### Base Occupational Hazard (with TTV Modifier)

The foundational occupational hazard ($H_{base}(t)$) is adjusted for career transitions using a Time-to-Value (TTV) modifier, which blends current and target industry risks over a specified period.
$$
H_{base}(k) = \left(1 - \frac{k}{TTV}\right) \cdot H_{current} + \left(\frac{k}{TTV}\right) \cdot H_{target}
$$
Where:
-   $H_{base}(k)$: Base Occupational Hazard after $k$ months of transition.
-   $k$: Number of months elapsed since transition pathway completion.
-   $TTV$: Total number of months in the Time-to-Value period (e.g., 12 months).
-   $H_{current}$: Base Occupational Hazard of the individual's original industry.
-   $H_{target}$: Base Occupational Hazard of the new target industry.

This formula allows the application to simulate the gradual reduction in Systematic Risk as a user transitions to a lower-risk occupation.

### Economic Climate Modifier ($M_{econ}$) and AI Innovation Index ($I_{AI}$)

These environmental modifiers dynamically adjust risk based on real-time macro trends.
$$
M_{econ} = f(\text{GDP Growth, Sector Employment, Interest Rates})
$$
$$I_{AI} = f(\text{VC Funding, R\&D Spend, Public Salience})
$$
Where:
-   $M_{econ}$: A composite index (e.g., from 0.8 to 1.2).
-   $I_{AI}$: A momentum index (e.g., > 1.0 for rapid breakthroughs).

For the synthetic dataset, these will be represented as simple numerical inputs or selectable scenarios (e.g., "Recession", "Normal", "AI Boom").

### Annual Claim Probability

The annual probability of a claim ($P_{claim}$) is modeled as the joint probability of a systemic event and that event leading to a loss for the individual.
$$
P_{claim} = P_{systemic} \cdot P_{individual|systemic}
$$
Where:
-   $P_{claim}$: Annual probability of a claim.
-   $P_{systemic}$: Probability of a systemic displacement event in the individual's industry.
-   $P_{individual|systemic}$: Conditional probability of job loss for the individual, given a systemic event.

This formula combines the two main risk scores into a single probability.

The conditional probabilities are defined as:
$$
P_{systemic} = \frac{H_{i}}{100} \cdot \beta_{systemic}
$$
Where:
-   $P_{systemic}$: Probability of a systemic displacement event.
-   $H_{i}$: Final Systematic Risk Score.
-   $\beta_{systemic}$: Systemic Event Base Probability (e.g., 0.10).

And:
$$
P_{individual|systemic} = \frac{V_{i}(t)}{100} \cdot \beta_{individual}
$$
Where:
-   $P_{individual|systemic}$: Conditional probability of job loss.
-   $V_{i}(t)$: Final Idiosyncratic Risk Score.
-   $\beta_{individual}$: Individual Loss Base Probability (e.g., 0.50).

These formulae translate the complex risk scores into tangible probabilities of job displacement.

### Expected Loss

The Annual Expected Loss ($E[Loss]$) is the total payout amount multiplied by the probability of a claim.
$$
E[Loss] = P_{claim} \cdot L_{payout}
$$
Where:
-   $E[Loss]$: Annual Expected Loss.
-   $P_{claim}$: Annual Claim Probability.
-   $L_{payout}$: Total payout amount if a claim is triggered.

The payout amount ($L_{payout}$) is calculated as:
$$
L_{payout} = \left(\frac{\text{Annual Salary}}{12} \cdot \text{Coverage Duration}\right) \cdot \text{Coverage Percentage}
$$
Where:
-   Annual Salary: User's annual income.
-   Coverage Duration: Number of months for payout.
-   Coverage Percentage: Percentage of salary covered.

This formula provides a financial measure of the potential impact of displacement.

### Monthly Premium

The monthly premium ($P_{monthly}$) is the final step where the annual expected loss is adjusted by a loading factor, converted to a monthly figure, and floored at the minimum premium.
$$
P_{monthly} = \max\left(\frac{E[Loss] \cdot \lambda}{12}, P_{min}\right)
$$
Where:
-   $P_{monthly}$: Final monthly premium.
-   $E[Loss]$: Annual Expected Loss.
-   $\lambda$: Loading Factor (e.g., 1.5), a standard insurance multiplier.
-   $P_{min}$: Minimum Premium (e.g., $20.00) to ensure policy viability.

This formula translates the risk assessment into a tangible financial outcome for the user.

## Required Libraries and Dependencies

The application will leverage several Python libraries for its functionality:

*   **`streamlit` (Version: 1.x.x)**:
    *   **Role**: The core framework for building the interactive web application.
    *   **Specific Functions/Modules**:
        *   `st.title()`, `st.header()`, `st.subheader()`, `st.markdown()`: For structuring and displaying textual content, including mathematical formulas.
        *   `st.sidebar()`: For organizing input widgets and navigation.
        *   `st.text_input()`, `st.selectbox()`, `st.slider()`, `st.checkbox()`, `st.button()`: For capturing user inputs.
        *   `st.dataframe()`, `st.table()`: For displaying tabular data.
        *   `st.plotly_chart()`: For embedding interactive Plotly visualizations.
        *   `st.session_state`: For maintaining state across reruns and user interactions.
        *   `st.expander()`: For collapsible sections of content (e.g., for detailed explanations/documentation).
    *   **Import Statement**: `import streamlit as st`

*   **`pandas` (Version: 1.x.x or 2.x.x)**:
    *   **Role**: Used for data manipulation, storage of synthetic lookup tables, and preparing data for visualizations.
    *   **Specific Functions/Modules**:
        *   `pd.DataFrame`: For creating and manipulating tabular data (e.g., storing occupation parameters, skill definitions).
        *   `df.loc[]`, `df.merge()`: For efficient data lookup and joining.
    *   **Import Statement**: `import pandas as pd`

*   **`numpy` (Version: 1.x.x or 2.x.x)**:
    *   **Role**: Essential for numerical operations, especially for mathematical formulas involving exponents, sums, and transformations.
    *   **Specific Functions/Modules**:
        *   `np.min()`, `np.max()`: For normalization steps in formulas like $V_{i}(t)$ and $P_{monthly}$.
        *   Mathematical functions: `np.exp()`, etc., if more complex decaying functions or distributions are used.
    *   **Import Statement**: `import numpy as np`

*   **`plotly.express` (Version: 5.x.x)**:
    *   **Role**: For generating interactive and dynamic visualizations.
    *   **Specific Functions/Modules**:
        *   `px.line()`: For plotting AI-Q score and premium trends over time.
        *   `px.bar()`: For visualizing contributions of different risk factors.
        *   `px.scatter()`: For skill gap analysis, potentially comparing user skills against job requirements.
        *   Built-in annotations and tooltips for data interpretation.
    *   **Import Statement**: `import plotly.express as px`

*   **(Optional) `faker` (Version: 18.x.x)**:
    *   **Role**: Potentially used during development to generate more complex synthetic dataset elements programmatically.
    *   **Specific Functions/Modules**: Various providers for names, job titles, companies, etc.
    *   **Import Statement**: `from faker import Faker`

## Implementation Details

### Data Model

The application will rely on a synthetic dataset structured primarily as Python dictionaries and Pandas DataFrames, mimicking the information described in the research document:

*   **`occupation_data.py`**:
    *   `OCCUPATION_HAZARDS`: Dictionary mapping job titles/industries to initial $H_{base}$ values (e.g., `{"Paralegal": 65, "Senior Research Scientist": 30, "Software Engineer": 40}`).
    *   `ROLE_MULTIPLIERS`: Dictionary for $f_{role}$ values (e.g., `{"Paralegal": 1.35, "Senior Research Scientist": 0.3}`).
    *   `COMPANY_TYPE_FACTORS`: Dictionary for $FCR$ values based on company type (e.g., `{"Big firm": 0.95, "Mid-size firm": 1.00}`).
*   **`education_data.py`**:
    *   `EDUCATION_LEVEL_FACTORS`: Dictionary for $f_{level}$ values (e.g., `{"PhD": 0.85, "Master's": 0.90, "Bachelor's": 1.00}`).
    *   `EDUCATION_FIELD_FACTORS`: Dictionary for $f_{field}$ values (e.g., `{"Tech/Engineering/Quantitative Science": 0.90, "Liberal Arts/Humanities": 1.10}`).
    *   `SCHOOL_TIER_FACTORS`: Dictionary for $f_{school}$ values (e.g., `{"Tier 1": 0.95, "Tier 2": 1.00, "Tier 3": 1.05}`).
*   **`skill_data.py`**:
    *   `SKILL_CATEGORIES`: Dictionary mapping skills to 'general' or 'firm-specific' type (e.g., `{"Python": "general", "Data Analysis": "general", "Proprietary CRM Software": "firm-specific"}`).
    *   `LEARNING_RESOURCES`: DataFrame with columns: `Skill`, `Type`, `Course Name`, `Platform`, `Link`.
*   **`environmental_data.py`**:
    *   `ECONOMIC_CLIMATE_SCENARIOS`: Dictionary mapping scenario names to $M_{econ}$ values (e.g., `{"Neutral": 1.0, "Recession": 0.9, "Boom": 1.1}`).
    *   `AI_INNOVATION_SCENARIOS`: Dictionary mapping scenario names to $I_{AI}$ values (e.g., `{"Neutral": 1.0, "Rapid Breakthroughs": 1.2, "Slowdown": 0.8}`).
*   **`actuarial_params.py`**:
    *   Constants for $\beta_{systemic}$, $\beta_{individual}$, $\lambda$, $P_{min}$, $TTV$, $w_{CR}$, $w_{US}$, $\gamma_{gen}$, $\gamma_{spec}$, $w_{econ}$, $w_{inno}$, etc.

### Calculation Logic

All mathematical formulas will be implemented as functions within a `calculations.py` module. These functions will take user inputs and parameters from the synthetic data model as arguments.
Example for $f_{exp}$:
```python
def calculate_fexp(years_experience: float) -> float:
    """
    Calculates the Experience Factor (f_exp).
    f_exp = 1 - (0.015 * min(years_experience, 20))
    """
    return 1 - (0.015 * min(years_experience, 20))
```

Example for $F_{US}$:
```python
def calculate_fus(p_gen: float, p_spec: float, gamma_gen: float, gamma_spec: float) -> float:
    """
    Calculates the Upskilling Factor (F_US).
    F_US = 1 - (gamma_gen * p_gen + gamma_spec * p_spec)
    """
    return 1 - (gamma_gen * p_gen + gamma_spec * p_spec)
```

### Module Structure

```
├── app.py                      # Main Streamlit application
├── data_utils.py               # Data loading, lookups, and utility functions
├── calculations.py             # All AI-Q score and premium calculation functions
├── visualizations.py           # Functions for generating interactive charts
├── data/
│   ├── occupation_data.py      # Synthetic data for occupations, roles, companies
│   ├── education_data.py       # Synthetic data for education levels, fields, schools
│   ├── skill_data.py           # Synthetic data for skills and learning resources
│   └── environmental_data.py   # Synthetic data for environmental modifiers
├── actuarial_params.py         # Constants for actuarial parameters
└── README.md                   # Project description
```

### State Management

Streamlit's `st.session_state` will be used to store user inputs and intermediate calculation results. This ensures that the application maintains its state across reruns, allowing for dynamic updates without losing user-defined parameters.
Examples:
*   `st.session_state['user_occupation']`
*   `st.session_state['general_skill_progress']`
*   `st.session_state['idiosyncratic_risk_score']`
*   `st.session_state['ai_q_score_history']` (for progress tracking visualization)

## User Interface Components

The Streamlit application will be organized into logical sections to guide the user through the risk assessment and upskilling recommendation process.

### Sidebar (Navigation and Global Settings)

*   **Application Title**: "Personalized Upskilling Recommender"
*   **Section Navigation**: Radio buttons or select box for main sections: "Risk Assessment", "Upskilling Path", "Progress Tracking".
*   **Global Parameters (e.g., Actuarial)**:
    *   `Annual Salary`: `st.number_input()`
    *   `Coverage Percentage`: `st.slider()`
    *   `Coverage Duration`: `st.number_input()`
    *   `Systemic Event Base Probability (β_systemic)`: `st.slider()`
    *   `Individual Loss Base Probability (β_individual)`: `st.slider()`
    *   `Loading Factor (λ)`: `st.slider()`
    *   `Minimum Premium (P_min)`: `st.number_input()`
    *   `Time-to-Value Period (TTV)`: `st.slider()`
    *   `Upskilling Weights (γ_gen, γ_spec)`: `st.slider()` (with $\gamma_{gen} > \gamma_{spec}$ constraint)
    *   `Systematic Risk Weights (w_econ, w_inno)`: `st.slider()`

### Main Content Area

#### 1. Risk Assessment Section

*   **User Profile Inputs (Human Capital Factor)**:
    *   `Current Occupation`: `st.selectbox()` (linked to `occupation_data.py`)
    *   `Years of Experience`: `st.slider()`
    *   `Highest Education Level`: `st.selectbox()` (linked to `education_data.py`)
    *   `Education Field`: `st.selectbox()` (linked to `education_data.py`)
    *   `School Tier`: `st.selectbox()` (linked to `education_data.py`)
*   **Employer Details (Company Risk Factor)**:
    *   `Company Type`: `st.selectbox()` (e.g., "Big firm", "Mid-size firm", "Startup", linked to `company_data.py` for FCR lookup).
*   **Environmental Modifiers**:
    *   `Economic Climate`: `st.selectbox()` (e.g., "Neutral", "Recession", "Boom", linked to `environmental_data.py` for $M_{econ}$)
    *   `AI Innovation Pace`: `st.selectbox()` (e.g., "Neutral", "Rapid Breakthroughs", "Slowdown", linked to `environmental_data.py` for $I_{AI}$)
*   **Skill Progress (Upskilling Factor Input)**:
    *   `General Skill Progress`: `st.slider()` (0-100%)
    *   `Firm-Specific Skill Progress`: `st.slider()` (0-100%)
*   **Calculation Button**: `st.button("Calculate AI-Q Score")`
*   **Results Display**:
    *   **Current AI-Q Score**: `st.metric()` displaying the calculated $V_{i}(t)$, $H_{i}$, and $P_{monthly}$.
    *   **Risk Breakdown Visualization**: Bar chart showing the relative contributions of $FHC$, $FCR$, and $FUS$ to $V_{i}(t)$, and $H_{base}$, $M_{econ}$, $I_{AI}$ to $H_{i}$.
    *   **Explanatory Markdown**: For each calculated factor (e.g., Human Capital Factor, Company Risk Factor, Upskilling Factor, Systematic Risk), use `st.expander()` to display definitions, underlying formulas (in LaTeX), and practical implications, directly quoting and formatting as per the requirements.

#### 2. Upskilling Path Section

*   **Skill Gap Analysis**:
    *   Based on `Current Occupation` selected, display a list of "High Impact General Skills" and "High Impact Firm-Specific Skills" relevant to mitigating displacement for that role.
    *   Potentially a radar chart comparing user's current skill proficiency against recommended proficiency.
*   **Personalized Resource Recommendations**:
    *   Display a sortable table of `LEARNING_RESOURCES` (from `skill_data.py`) filtered by skill category and relevance.
    *   Include columns for `Skill`, `Course Name`, `Platform`, `Link`.
    *   Allow users to "add to learning path" (updating their `st.session_state` progress).
*   **Career Path Diversification**:
    *   Option to select a `Target Occupation` (lower $H_{base}$).
    *   `Months into Transition Pathway`: `st.slider()` to simulate $k$ for $H_{base}(k)$ calculation.
    *   Display predicted new $H_{i}$ and premium if transition is completed.
    *   Suggest skills required for career transition.

#### 3. Progress Tracking Section

*   **Learning Progress Inputs**:
    *   `General Skill Progress Update`: `st.slider()`
    *   `Firm-Specific Skill Progress Update`: `st.slider()`
    *   `Update Progress Button`: `st.button()`
*   **Historical Performance Visualization**:
    *   **AI-Q Score Trend**: Line chart showing $V_{i}(t)$, $H_{i}$, and $P_{monthly}$ over time as the user updates their skill progress or career transition status. Annotations on the chart indicating key progress milestones.
    *   **Skill Proficiency Over Time**: Line chart showing general vs. firm-specific skill progress.
*   **Impact Summary**: `st.markdown()` explaining how current progress has reduced their Idiosyncratic Risk and monthly premium.



### Appendix Code

```code
Vi(t) = f (FHC, FCR, FUS)
Vraw = FHC (WCRFCR + WUS FUS)
FHC = frole flevel ffield fschool fexp
FCR = W1 · Ssenti + W2. Sfin + W3. Sgrowth
FUS = 1 - (ygen Pgen(t) + Yspec Pspec(t))
Hi = Hbase (t) (Wecon Mecon + Winno. IAI)
Hbase (k) = (1 - k/TTV) · Hcurrent + (k/TTV) · Htarget
Mecon = f(GDP Growth, Sector Employment, Interest Rates)
IAI = f (VC Funding, R&D Spend, Public Salience)
Pclaim Psystemic Pindividual systemic
Psystemic = Hi/100 · Bsystemic
Pindividual systemic = Vi(t)/100 · Bindividual
Pmonthly = max ( E[Loss] · λ / 12 , Pmin )
Final Score: Vi(t) = min(100.0, max (5.0, Vraw - 50.0))

Human Capital Factor Sub-Factors (from Table 2):
Role (frole): ROLE_MULTIPLIERS
Level (flevel): EDUCATION_LEVEL
Field (ffield): EDUCATION_FIELD
School (fschool): SCHOOL_TIER
Experience (fexp): 1-(0.015min (Yrs, 20))
PRODUCT (FHC): (Multiply all above)

FUS = 1 - (0.7 Pidio (t))
Lpayout = ( (Annual Salary). Coverage Duration· Coverage Percentage / 12)
pclaim = (Vi / 100 · Bsystemic) (Hi / 100 · Bindividual)
E[Loss] = Pclaim · Lpayout
```