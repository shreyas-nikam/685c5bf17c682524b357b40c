id: 685c5bf17c682524b357b40c_documentation
summary: AI Risk Score - V3 Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# AI Risk Score Codelab: Understanding and Mitigating Job Displacement Risk

This codelab provides a comprehensive guide to understanding and utilizing the "AI Risk Score - V3" application. This application is designed to help individuals assess their risk of job displacement due to advancements in Artificial Intelligence, identify skill gaps, and strategize their upskilling journey. We'll explore the functionalities of each section, the underlying calculations, and how to interpret the results. This codelab is vital because it tackles a relevant and growing concern in today's job market. By understanding the risk factors and taking proactive steps, individuals can enhance their career resilience.

## Setting Up the Environment

Duration: 00:05

Before diving into the application's features, ensure you have the following prerequisites:

*   **Python 3.7+:** The application is built using Python.
*   **Streamlit:** The user interface is built with Streamlit. Install it using:

    ```bash
    pip install streamlit
    ```
*   **Other libraries:**  Install the required libraries using:

    ```bash
    pip install pandas plotly numpy
    ```

    These libraries are essential for data manipulation and visualization.

*   **Download Application Files:** Download all the python files (app.py, calculations.py, data_utils.py, visualizations.py, actuarial_params.py) and the data folder with all the data files.
*   **Directory structure:** Make sure all the data files are present inside the `data` folder.
*   **Run the App:** Navigate to the directory containing `app.py` and run the application using:

    ```bash
    streamlit run app.py
    ```

    This command will launch the application in your web browser.

## Understanding the Application Architecture

Duration: 00:10

The application's architecture can be broken down into several key components:

*   **`app.py`:** This is the main script that orchestrates the entire application. It handles the user interface, user input, and calls the necessary functions to perform calculations and display results. It uses Streamlit to create the interactive elements.
*   **`calculations.py`:** This module contains all the actuarial calculations needed to determine the AI risk score, probabilities, expected loss, and monthly premium. It defines functions for calculating factors like FHC, FCR, FUS, and systematic risk.
*   **`data_utils.py`:** This module is responsible for fetching data from various data sources (e.g., occupation hazards, education factors, economic climate scenarios). It provides functions to retrieve these values based on user selections.
*   **`visualizations.py`:** This module handles the creation of interactive plots and charts using Plotly. It generates visualizations to show risk factor contributions, historical trends, skill proficiency, and skill gaps.
*   **`actuarial_params.py`:** This file defines the constant parameters used in the actuarial calculations, such as beta values, loading factors, and weights.
*   **`data/`:** This directory contains the data files used by the application, including occupation hazards, education factors, economic climate scenarios, and skill learning resources.

**Data Flow:**

1.  The user interacts with the Streamlit UI (`app.py`), providing input such as their occupation, education level, and skill progress.
2.  `app.py` calls functions from `data_utils.py` to retrieve relevant data based on the user's input.
3.  `app.py` then calls functions from `calculations.py` to perform the actuarial calculations using the user input and retrieved data.
4.  The calculated results are passed to `visualizations.py` to generate plots and charts, which are then displayed in the Streamlit UI.
5.  `actuarial_params.py` provides constant parameters required for the calculations.

## Exploring the Risk Assessment Section

Duration: 00:15

The "Risk Assessment" section is where users input their professional details and environmental factors to calculate their personalized AI Risk Score (AI-Q Score). Let's break down the input fields and the calculations performed.

**1. User Profile (Human Capital Factor):**

*   **Current Occupation:** Select your current occupation from the dropdown list. Each occupation has an associated base hazard score and role multiplier. This information is sourced from `data/occupation_data.py`.
*   **Years of Experience:**  Indicate your years of experience. This value affects the experience factor ($f_{exp}$), which is calculated using the `calculate_fexp` function in `calculations.py`.
*   **Highest Education Level:** Select your highest education level. Each level has an associated education level factor, fetched from `data/education_data.py` using the `get_education_level_factor` function in `data_utils.py`.
*   **Education Field:** Select your field of education. This selection contributes to the Human Capital Factor(FHC).
*   **School Tier:**  Select the tier of the institution you attended. It impacts the Human Capital Factor.
*   **Company Type:** Select your company type. The Company Risk Factor (FCR) is directly looked up based on the selected company type from `data/occupation_data.py` using the `get_company_type_factor` function in `data_utils.py`.

**2. Environmental Modifiers:**

*   **Economic Climate:** Select the current economic climate. It is used to derive the Economic Climate Modifier from `data/environmental_data.py`.
*   **AI Innovation Pace:**  Select the pace of AI innovation. This value influences the Systematic Risk.

**3. Current Skill Progress (Upskilling Factor):**

*   **General Skill Progress:**  Indicate your progress in acquiring general, portable skills (e.g., Python, Data Analysis).
*   **Firm-Specific Skill Progress:**  Indicate your progress in acquiring firm-specific skills (e.g., proprietary software).

**Calculations:**

When you click the "Calculate AI-Q Score" button, the following calculations are performed:

1.  **Retrieve Factors:**  The application retrieves all the necessary factors based on your input using functions from `data_utils.py`.
2.  **Calculate FHC:** The Human Capital Factor (FHC) is calculated using the `calculate_fhc` function in `calculations.py`. The formula is:

    ```
    FHC = f_{role} * f_{level} * f_{field} * f_{school} * f_{exp}
    ```

3.  **Calculate FUS:** The Upskilling Factor (FUS) is calculated using the `calculate_fus` function in `calculations.py`. The formula is:

    ```
    F_{US} = 1 - (gamma_{gen} * P_{gen} + gamma_{spec} * P_{spec})
    ```

    Where $P_{gen}$ and $P_{spec}$ are your progress in general and firm-specific skills, respectively, and $\gamma_{gen}$ and $\gamma_{spec}$ are the weighting parameters defined in `actuarial_params.py`.

4.  **Calculate Idiosyncratic Risk:** The raw Idiosyncratic Risk ($V_{raw}$) is calculated using the `calculate_v_idiosyncratic_raw` function in `calculations.py`. The normalized Idiosyncratic Risk ($V_{i}(t)$) is then calculated using the `calculate_v_idiosyncratic_normalized` function.

    ```
    V_{raw} = FHC * (w_{CR} * FCR + w_{US} * FUS)
    V_{i}(t) = min(100.0, max(5.0, V_{raw} * 50.0))
    ```

5.  **Calculate Systematic Risk:** The Base Occupational Hazard ($H_{base}$) is retrieved using `get_occupation_hazard` and potentially adjusted based on transition pathway.  Then the systematic risk ($H_i$) is calculated.

    ```
    H_{i} = H_{base}(t) * (w_{econ} * M_{econ} + w_{inno} * I_{AI})
    ```

6.  **Calculate Probabilities and Loss:** The probabilities of systemic and individual loss events are calculated, along with the expected loss and monthly premium, using functions in `calculations.py`.

**Results:**

The calculated results are displayed as metrics:

*   **Idiosyncratic Risk ($V_i(t)$):** A measure of your individual vulnerability.
*   **Systematic Risk ($H_i$):** A measure of the overall risk associated with your occupation.
*   **Estimated Monthly Premium ($P_{monthly}$):** A hypothetical premium based on your risk profile.

The section also includes plots showing the contributions of different factors to the Idiosyncratic and Systematic Risk scores, offering insights into the key drivers of your risk.

## Deep Dive into the Code: Risk Assessment Calculations

Duration: 00:20

Let's examine the core code snippets responsible for calculating the risk factors in `app.py` and `calculations.py`.

**1. Calculating FHC:**

```python
f_exp = calculate_fexp(years_experience)
f_role = get_role_multiplier(current_occupation)
f_level = get_education_level_factor(highest_education_level)
f_field = get_education_field_factor(education_field)
f_school = get_school_tier_factor(school_tier)
fcr_value = get_company_type_factor(company_type) # FCR is directly looked up

# Calculate FHC
fhc = calculate_fhc(f_role, f_level, f_field, f_school, f_exp)
```

This snippet retrieves the individual factors contributing to the Human Capital Factor and then calls the `calculate_fhc` function:

```python
def calculate_fhc(f_role: float, f_level: float, f_field: float, f_school: float, f_exp: float) -> float:
    """
    Calculates the Human Capital Factor (FHC).
    FHC = f_{role} * f_{level} * f_{field} * f_{school} * f_{exp}
    """
    return f_role * f_level * f_field * f_school * f_exp
```

**2. Calculating FUS:**

```python
general_skill_progress = st.slider("General Skill Progress (0-100%)", min_value=0, max_value=100, value=50, step=5) / 100.0
firm_specific_skill_progress = st.slider("Firm-Specific Skill Progress (0-100%)", min_value=0, max_value=100, value=50, step=5) / 100.0
fus = calculate_fus(general_skill_progress, firm_specific_skill_progress, gamma_gen, gamma_spec)
```

This retrieves the user's skill progress and calculates the Upskilling Factor using:

```python
def calculate_fus(p_gen: float, p_spec: float, gamma_gen: float = GAMMA_GEN, gamma_spec: float = GAMMA_SPEC) -> float:
    """
    Calculates the Upskilling Factor (F_US).
    F_{US} = 1 - (gamma_{gen} P_{gen}(t) + gamma_{spec} P_{spec}(t))
    """
    return 1 - (gamma_gen * p_gen + gamma_spec * p_spec)
```

Notice how the `gamma_gen` and `gamma_spec` parameters, defined in `actuarial_params.py`, control the relative impact of general and firm-specific skills.

**3. Calculating Systematic Risk:**

```python
h_base_current = get_occupation_hazard(current_occupation)
h_base = calculate_h_base_ttv(h_base_current, h_base_current, 0, ttv_months) # k=0 for initial calculation

# Retrieve environmental modifiers
m_econ = get_economic_climate_modifier(economic_climate)
i_ai = get_ai_innovation_index(ai_innovation_pace)

# Calculate H_i (Systematic Risk)
h_systematic = calculate_systematic_risk(h_base, m_econ, i_ai, w_econ, w_inno)
```

This calculates the systematic risk using:

```python
def calculate_systematic_risk(h_base: float, m_econ: float, i_ai: float, w_econ: float = W_ECON, w_inno: float = W_INNO) -> float:
    """
    Calculates the Systematic Risk score (H_i).
    H_{i} = H_{base}(t) * (w_{econ} M_{econ} + w_{inno} I_{AI})
    """
    return h_base * (w_econ * m_econ + w_inno * i_ai)
```

The weights `w_econ` and `w_inno` from `actuarial_params.py` determine the influence of the economic climate and AI innovation pace.

## Analyzing Risk Factor Contributions

Duration: 00:10

After calculating the AI-Q score, the application displays bar charts illustrating the contributions of different factors to the Idiosyncratic and Systematic Risks. These visualizations are generated by the `plot_risk_factor_contributions` function in `visualizations.py`.

**Idiosyncratic Risk Factors:**

*   **Human Capital (FHC):**  A lower FHC is better. It is your foundational resilience.
*   **Company Risk (FCR):**  A lower FCR is better. A company's stability reduces your risk.
*   **Upskilling (FUS):**  A lower FUS is better.  This acts as a risk reduction, so lower is better.

**Systematic Risk Factors:**

*   **Base Occupational Hazard (H_base):** A lower H_base is better. Represents the inherent risk of your occupation.
*   **Economic Climate (M_econ):**  A lower M_econ is better.
*   **AI Innovation (I_AI):** A lower I_AI is better.

By analyzing these charts, you can identify the factors that contribute the most to your risk and take targeted actions to mitigate them. For example, if your FHC is high, you might consider pursuing further education or gaining more experience. If your H_base is high, you might consider upskilling or transitioning to a lower-risk occupation.

## Diving into the Upskilling Path Section

Duration: 00:15

The "Upskilling Path" section provides personalized recommendations for skills and learning resources to help you reduce your risk.

**1. Recommended High-Impact Skills:**

Based on your selected occupation, the application suggests a list of general (portable) and firm-specific skills. These recommendations are generated by the `get_skills_for_occupation` function in `data_utils.py`.

The `get_skills_for_occupation` function currently provides placeholder suggestions and can be improved using more sophisticated logic, connecting to databases or even machine learning models that analyze job market trends and skill requirements.

**2. Skill Gap Analysis (Conceptual):**

The radar chart visually compares your current skill proficiency against recommended levels. This chart is generated by the `plot_skill_gap_radar` function in `visualizations.py`. The chart is conceptual and relies on the user's self-assessment of their skill proficiency.

**3. Personalized Learning Resources:**

The application provides a table of learning resources, filtered by skill type (general or firm-specific). This table is populated using the `LEARNING_RESOURCES` DataFrame from `data/skill_data.py` and filtered using the `get_learning_resources_by_skill_type` function in `data_utils.py`.

**4. Career Path Diversification (Simulate Transition):**

This feature allows you to simulate the impact of transitioning to a lower-risk occupation on your Systematic Risk.

*   You select a target occupation, and the application calculates the new Systematic Risk based on the target occupation's base hazard.

This helps you evaluate the potential benefits of changing careers to reduce your overall risk exposure.

## Examining the Code: Upskilling Recommendations

Duration: 00:10

Let's explore the code snippets responsible for generating upskilling recommendations.

**1. Getting Recommended Skills:**

```python
current_occupation_for_skills = st.selectbox(
    "Select your Current Occupation to see recommended skills:",
    options=list(OCCUPATION_HAZARDS.keys()),
    key="upskill_occupation_select"
)

recommended_skills = get_skills_for_occupation(current_occupation_for_skills)
```

This code snippet retrieves the user's selected occupation and calls the `get_skills_for_occupation` function in `data_utils.py`:

```python
def get_skills_for_occupation(occupation: str):
    """
    Placeholder function to suggest high-impact skills for an occupation.
    In a real app, this would be a more sophisticated lookup or ML model.
    """
    # For demonstration, we'll return a mix of general and specific skills
    # based on the occupation.
    if "Engineer" in occupation or "Analyst" in occupation:
        return {
            "general": ["Python", "Data Analysis", "Machine Learning", "Cloud Computing", "SQL", "Project Management"],
            "firm-specific": ["Proprietary CRM Software", "Company-specific Financial Models"]
        }
    elif "Paralegal" in occupation or "HR" in occupation:
        return {
            "general": ["Communication", "Problem Solving", "Critical Thinking", "Project Management", "Negotiation"],
            "firm-specific": ["Internal Compliance Procedures", "Legacy System Maintenance"]
        }
    elif "Financial Advisor" in occupation:
        return {
            "general": ["Data Analysis", "Critical Thinking", "Communication", "Advanced Excel"],
            "firm-specific": ["Company-specific Financial Models", "Internal Compliance Procedures"]
        }
    elif "Customer Service" in occupation:
        return {
            "general": ["Communication", "Problem Solving", "Critical Thinking"],
            "firm-specific": ["Proprietary CRM Software", "Internal Compliance Procedures"]
        }
    else:
        return {
            "general": ["Python", "Data Analysis", "Project Management", "Communication"],
            "firm-specific": ["Internal Compliance Procedures", "Proprietary CRM Software"]
        }
```

**2. Simulating Career Transition:**

```python
h_current_base = get_occupation_hazard(current_occupation_for_skills)
h_target_base = get_occupation_hazard(target_occupation)

h_base_after_transition = calculate_h_base_ttv(h_current_base, h_target_base, months_into_transition, ttv_months)

# Recalculate systematic risk with new H_base, using previous M_econ and I_AI
if 'last_m_econ' in st.session_state and 'last_i_ai' in st.session_state:
    simulated_h_systematic = calculate_systematic_risk(
        h_base_after_transition,
        st.session_state['last_m_econ'],
        st.session_state['last_i_ai'],
        w_econ, w_inno
    )
    st.info(f"Simulated Base Occupational Hazard after {months_into_transition} months: **{h_base_after_transition:.2f}**")
    st.success(f"Predicted Systematic Risk (H_i) after transition: **{simulated_h_systematic:.2f}**")
```

This snippet retrieves the base hazards for the current and target occupations, calculates the adjusted base hazard using the `calculate_h_base_ttv` function, and then recalculates the systematic risk.

## Understanding the Progress Tracking Section

Duration: 00:15

The "Progress Tracking" section allows you to monitor how your upskilling efforts and career transitions impact your AI Risk Score and estimated monthly premium over time.

**1. Update Your Progress:**

*   **General Skill Progress:** Update your current progress in general skills.
*   **Firm-Specific Skill Progress:** Update your current progress in firm-specific skills.

**2. Historical Performance:**

The application displays charts showing the trends of:

*   **AI Risk Score and Premium:** Tracks the changes in Idiosyncratic Risk, Systematic Risk, and Monthly Premium over time.
*   **Skill Proficiency:** Tracks your progress in general and firm-specific skills over time.

The section also provides a summary of the impact of your efforts, showing the change in Idiosyncratic Risk and estimated monthly premium over the tracking period.

## Examining the Code: Progress Tracking Implementation

Duration: 00:10

Let's explore the code snippets responsible for tracking progress over time.

**1. Logging New Progress:**

```python
new_general_skill_progress = st.slider("Update General Skill Progress (0-100%)", min_value=0, max_value=100, value=st.session_state['skill_progress_history']['General Skill Progress'].iloc[-1] if not st.session_state['skill_progress_history'].empty else 50, step=5) / 100.0
new_firm_specific_skill_progress = st.slider("Update Firm-Specific Skill Progress (0-100%)", min_value=0, max_value=100, value=st.session_state['skill_progress_history']['Firm-Specific Skill Progress'].iloc[-1] if not st.session_state['skill_progress_history'].empty else 50, step=5) / 100.0

if st.button("Log New Progress"):
    if 'last_calculated_v_idiosyncratic' in st.session_state:
        st.session_state['current_month'] += 1

        # Recalculate FUS with new skill progress
        updated_fus = calculate_fus(new_general_skill_progress, new_firm_specific_skill_progress, gamma_gen, gamma_spec)

        # Recalculate V_raw and V_i(t)
        updated_v_raw = calculate_v_idiosyncratic_raw(st.session_state['last_fhc'], st.session_state['last_fcr'], updated_fus, W_CR, W_US)
        updated_v_idiosyncratic = calculate_v_idiosyncratic_normalized(updated_v_raw)

        # Systematic risk is assumed constant unless base occupation changes or environmental factors are updated
        updated_h_systematic = st.session_state['last_calculated_h_systematic']

        # Recalculate probabilities and premium
        updated_p_systemic = calculate_p_systemic(updated_h_systematic, beta_systemic)
        updated_p_individual_conditional = calculate_p_individual_conditional(updated_v_idiosyncratic, beta_individual)
        updated_p_claim = calculate_p_claim(updated_p_systemic, updated_p_individual_conditional)
        updated_l_payout = calculate_l_payout(annual_salary, coverage_duration, coverage_percentage)
        updated_e_loss = calculate_expected_loss(updated_p_claim, updated_l_payout)
        updated_p_monthly = calculate_monthly_premium(updated_e_loss, loading_factor, minimum_premium)

        # Append to history
        new_row_history = pd.DataFrame([{
            'Month': st.session_state['current_month'],
            'Idiosyncratic Risk': updated_v_idiosyncratic,
            'Systematic Risk': updated_h_systematic,
            'Monthly Premium': updated_p_monthly
        }])
        st.session_state['idiosyncratic_risk_history'] = pd.concat([st.session_state['idiosyncratic_risk_history'], new_row_history], ignore_index=True)

        new_row_skill_history = pd.DataFrame([{
            'Month': st.session_state['current_month'],
            'General Skill Progress': new_general_skill_progress * 100,
            'Firm-Specific Skill Progress': new_firm_specific_skill_progress * 100
        }])
        st.session_state['skill_progress_history'] = pd.concat([st.session_state['skill_progress_history'], new_row_skill_history], ignore_index=True)

        st.success(f"Progress updated for Month {st.session_state['current_month']}!")
    else:
        st.warning("Please calculate your initial AI-Q Score in the 'Risk Assessment' section first.")
```

This code snippet retrieves the updated skill progress, recalculates the Idiosyncratic Risk and Monthly Premium, and appends the new values to the historical data stored in `st.session_state`.

**2. Plotting Historical Trends:**

```python
fig_trend = plot_historical_trends(st.session_state['idiosyncratic_risk_history'])
st.plotly_chart(fig_trend, use_container_width=True)

fig_skill_trend = plot_skill_proficiency(st.session_state['skill_progress_history'])
st.plotly_chart(fig_skill_trend, use_container_width=True)
```

This code snippet retrieves the historical data from `st.session_state` and uses the `plot_historical_trends` and `plot_skill_proficiency` functions in `visualizations.py` to generate the trend charts.

## Key TakeAways

Duration: 00:05

*   The AI Risk Score application provides a valuable tool for assessing and mitigating job displacement risk.
*   Understanding the underlying calculations and factors contributing to the AI-Q score is crucial for making informed decisions about your career.
*   Focusing on acquiring general, portable skills can significantly reduce your Idiosyncratic Risk.
*   The application allows you to track your progress over time and see the impact of your upskilling efforts.

By utilizing the AI Risk Score application and following the guidance in this codelab, you can take proactive steps to enhance your career resilience and thrive in the evolving job market.
