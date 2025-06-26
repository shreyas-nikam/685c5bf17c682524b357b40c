
import streamlit as st
import pandas as pd
from calculations import (
    calculate_fexp, calculate_fhc, calculate_fus, calculate_fcr,
    calculate_v_idiosyncratic_raw, calculate_v_idiosyncratic_normalized,
    calculate_h_base_ttv, calculate_systematic_risk,
    calculate_p_systemic, calculate_p_individual_conditional, calculate_p_claim,
    calculate_l_payout, calculate_expected_loss, calculate_monthly_premium
)
from data_utils import (
    get_occupation_hazard, get_role_multiplier, get_company_type_factor,
    get_education_level_factor, get_education_field_factor, get_school_tier_factor,
    get_economic_climate_modifier, get_ai_innovation_index,
    get_learning_resources_by_skill_type, get_skills_for_occupation
)
from visualizations import (
    plot_risk_factor_contributions, plot_historical_trends,
    plot_skill_proficiency, plot_skill_gap_radar
)
from actuarial_params import (
    BETA_SYSTEMIC, BETA_INDIVIDUAL, LAMBDA, P_MIN, TTV,
    W_CR, W_US, GAMMA_GEN, GAMMA_SPEC, W_ECON, W_INNO
)
from data.occupation_data import OCCUPATION_HAZARDS, COMPANY_TYPE_FACTORS
from data.education_data import EDUCATION_LEVEL_FACTORS, EDUCATION_FIELD_FACTORS, SCHOOL_TIER_FACTORS
from data.environmental_data import ECONOMIC_CLIMATE_SCENARIOS, AI_INNOVATION_SCENARIOS
from data.skill_data import LEARNING_RESOURCES, SKILL_CATEGORIES

st.set_page_config(page_title="AI Risk Score - V3", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("AI Risk Score - V3")
st.divider()

st.markdown("""
### Welcome to the Personalized Upskilling Recommender!

In today's rapidly evolving job market, driven by advancements in Artificial Intelligence, understanding and mitigating your personal risk of job displacement is crucial. This application, "AI Risk Score - V3", empowers you to assess your vulnerability, identify skill gaps, and strategize your upskilling journey to enhance your career resilience.

We leverage a sophisticated **multi-factor risk model** to calculate your unique **AI-Q score**. This score quantifies your susceptibility to AI-driven changes, considering various dimensions of your professional profile. The application also helps you understand how acquiring new skills, particularly **general and portable skills**, can directly reduce your risk and even lower your potential "AI displacement insurance" premium.

This tool is built upon the actuarial and economic models detailed in our research, making complex concepts tangible and actionable. We specifically reference and explain **Formula 4** from the research document to demonstrate how specific skills (general vs. firm-specific) impact an individual's Idiosyncratic Risk score.

Navigate through the sections using the sidebar:
-   **Risk Assessment**: Input your professional details to calculate your current AI-Q score and understand the factors contributing to it.
-   **Upskilling Path**: Discover recommended skills and learning resources tailored to your profile and mitigate your risk.
-   **Progress Tracking**: Monitor how your upskilling efforts impact your risk score and hypothetical premium over time.

---

#### Core Concepts and Mathematical Foundations

This application's calculations are based on the following key mathematical models:

##### Idiosyncratic Risk (Vulnerability)
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

This formula combines individual-specific attributes to produce a personalized vulnerability score. The final $V_{i}(t)$ is normalized to a scale of 0-100 using:
$$
V_{i}(t) = \min(100.0, \max(5.0, V_{raw} \cdot 50.0))
$$

##### Human Capital Factor
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
-   $f_{exp}$: Experience Factor, a decaying function of years of experience, calculated as:
    $$
    f_{exp} = 1 - (0.015 \cdot \min(	ext{years\_experience}, 20))
    $$

##### Company Risk Factor
The Company Risk Factor ($FCR$) quantifies the stability and growth prospects of the individual's current employer, analogous to a corporate credit rating.
$$
FCR = w_{1} \cdot S_{senti} + w_{2} \cdot S_{fin} + w_{3} \cdot S_{growth}
$$
For this application, $S_{senti}$, $S_{fin}$, and $S_{growth}$ are aggregated and represented by a single factor derived from a synthetic lookup based on company type (e.g., "Big Firm", "Mid-size Firm", "Startup").

##### Upskilling Factor
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

The condition $\gamma_{gen} > \gamma_{spec}$ ensures that acquiring portable skills provides a greater reduction in risk, operationalizing the document's emphasis.

##### Systematic Risk (Hazard)
The Systematic Risk score ($H_{i}$) is a dynamic index reflecting the macro-level automation hazard of an occupation, adjusted by broader environmental factors.
$$
H_{i} = H_{base}(t) \cdot (w_{econ} M_{econ} + w_{inno} I_{AI})
$$
Where:
-   $H_{i}$: The final Systematic Risk score.
-   $H_{base}(t)$: Base Occupational Hazard for the occupation at time $t$.
-   $M_{econ}$: Economic Climate Modifier, capturing macroeconomic environment's effect on AI investment.
-   $I_{AI}$: AI Innovation Index, capturing velocity of technological change.
-   $w_{econ}, w_{inno}$: Calibration weights that sum to 1.0.

##### Base Occupational Hazard (with TTV Modifier)
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

##### Annual Claim Probability
The annual probability of a claim ($P_{claim}$) is modeled as the joint probability of a systemic event and that event leading to a loss for the individual.
$$
P_{claim} = P_{systemic} \cdot P_{individual|systemic}
$$
Where:
-   $P_{systemic}$: Probability of a systemic displacement event in the individual's industry.
    $$
    P_{systemic} = \frac{H_{i}}{100} \cdot eta_{systemic}
    $$
-   $P_{individual|systemic}$: Conditional probability of job loss for the individual, given a systemic event.
    $$
    P_{individual|systemic} = \frac{V_{i}(t)}{100} \cdot eta_{individual}
    $$
Where $eta_{systemic}$ is the Systemic Event Base Probability and $eta_{individual}$ is the Individual Loss Base Probability.

##### Expected Loss
The Annual Expected Loss ($E[Loss]$) is the total payout amount multiplied by the probability of a claim.
$$
E[Loss] = P_{claim} \cdot L_{payout}
$$
The payout amount ($L_{payout}$) is calculated as:
$$
L_{payout} = \left(\frac{	ext{Annual Salary}}{12} \cdot 	ext{Coverage Duration}\right) \cdot 	ext{Coverage Percentage}
$$

##### Monthly Premium
The monthly premium ($P_{monthly}$) is the final step where the annual expected loss is adjusted by a loading factor, converted to a monthly figure, and floored at the minimum premium.
$$
P_{monthly} = \max\left(\frac{E[Loss] \cdot \lambda}{12}, P_{min}\right)
$$
Where $\lambda$ is the Loading Factor and $P_{min}$ is the Minimum Premium.

---
""")

# Initialize session state for persistent data
if 'idiosyncratic_risk_history' not in st.session_state:
    st.session_state['idiosyncratic_risk_history'] = pd.DataFrame(columns=['Month', 'Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium'])
if 'skill_progress_history' not in st.session_state:
    st.session_state['skill_progress_history'] = pd.DataFrame(columns=['Month', 'General Skill Progress', 'Firm-Specific Skill Progress'])
if 'current_month' not in st.session_state:
    st.session_state['current_month'] = 0
if 'user_skills_proficiency' not in st.session_state:
    st.session_state['user_skills_proficiency'] = {} # To store proficiency for radar chart

# Sidebar for Navigation and Global Settings
st.sidebar.header("Global Parameters")
with st.sidebar.expander("Actuarial & Payout Settings"):
    annual_salary = st.number_input("Annual Salary ($)", min_value=10000, max_value=500000, value=75000, step=5000)
    coverage_percentage = st.slider("Coverage Percentage (%)", min_value=0.0, max_value=1.0, value=0.6, step=0.05, format="%.2f")
    coverage_duration = st.number_input("Coverage Duration (Months)", min_value=1, max_value=24, value=6, step=1)
    beta_systemic = st.slider("Systemic Event Base Probability (β_systemic)", min_value=0.01, max_value=0.5, value=BETA_SYSTEMIC, step=0.01)
    beta_individual = st.slider("Individual Loss Base Probability (β_individual)", min_value=0.01, max_value=1.0, value=BETA_INDIVIDUAL, step=0.01)
    loading_factor = st.slider("Loading Factor (λ)", min_value=1.0, max_value=3.0, value=LAMBDA, step=0.1)
    minimum_premium = st.number_input("Minimum Premium (P_min) ($)", min_value=5.0, max_value=100.0, value=P_MIN, step=5.0)

with st.sidebar.expander("Model Weights & Time-to-Value"):
    gamma_gen = st.slider("General Skill Weight (γ_gen)", min_value=0.1, max_value=0.9, value=GAMMA_GEN, step=0.05)
    gamma_spec = st.slider("Firm-Specific Skill Weight (γ_spec)", min_value=0.1, max_value=0.9, value=GAMMA_SPEC, step=0.05)
    if gamma_gen <= gamma_spec:
        st.warning("Warning: General Skill Weight (γ_gen) should ideally be greater than Firm-Specific Skill Weight (γ_spec).")
    w_econ = st.slider("Economic Climate Weight (w_econ)", min_value=0.0, max_value=1.0, value=W_ECON, step=0.05)
    w_inno = st.slider("AI Innovation Weight (w_inno)", min_value=0.0, max_value=1.0, value=W_INNO, step=0.05)
    if not (0.95 <= (w_econ + w_inno) <= 1.05):
        st.warning("Warning: Economic and AI Innovation weights (w_econ + w_inno) should ideally sum close to 1.0.")
    ttv_months = st.slider("Time-to-Value Period (TTV) (Months)", min_value=3, max_value=36, value=TTV, step=1)


page = st.sidebar.selectbox(label="Navigation", options=["Risk Assessment", "Upskilling Path", "Progress Tracking"])

if page == "Risk Assessment":
    st.header("Risk Assessment")
    st.markdown("""
    Input your professional details and environmental factors below to calculate your personalized AI Risk Score (AI-Q Score)
    and your hypothetical monthly premium.
    """)

    st.subheader("1. Your Profile (Human Capital Factor)")
    col1, col2 = st.columns(2)
    with col1:
        current_occupation = st.selectbox("Current Occupation", options=list(OCCUPATION_HAZARDS.keys()), index=2) # Default to Software Engineer
        years_experience = st.slider("Years of Experience", min_value=0, max_value=40, value=5, step=1)
        highest_education_level = st.selectbox("Highest Education Level", options=list(EDUCATION_LEVEL_FACTORS.keys()), index=2) # Default Bachelor's
    with col2:
        education_field = st.selectbox("Education Field", options=list(EDUCATION_FIELD_FACTORS.keys()), index=0) # Default Tech
        school_tier = st.selectbox("School Tier", options=list(SCHOOL_TIER_FACTORS.keys()), index=1) # Default Tier 2
        company_type = st.selectbox("Company Type", options=list(COMPANY_TYPE_FACTORS.keys()), index=0) # Default Big Firm

    st.subheader("2. Environmental Modifiers")
    col3, col4 = st.columns(2)
    with col3:
        economic_climate = st.selectbox("Economic Climate", options=list(ECONOMIC_CLIMATE_SCENARIOS.keys()))
    with col4:
        ai_innovation_pace = st.selectbox("AI Innovation Pace", options=list(AI_INNOVATION_SCENARIOS.keys()))

    st.subheader("3. Current Skill Progress (Upskilling Factor)")
    general_skill_progress = st.slider("General Skill Progress (0-100%)", min_value=0, max_value=100, value=50, step=5) / 100.0
    firm_specific_skill_progress = st.slider("Firm-Specific Skill Progress (0-100%)", min_value=0, max_value=100, value=50, step=5) / 100.0

    st.markdown("""
    Click the button below to calculate your AI Risk Score and see how different factors contribute to it.
    """)

    if st.button("Calculate AI-Q Score"):
        # Retrieve factors
        f_exp = calculate_fexp(years_experience)
        f_role = get_role_multiplier(current_occupation)
        f_level = get_education_level_factor(highest_education_level)
        f_field = get_education_field_factor(education_field)
        f_school = get_school_tier_factor(school_tier)
        fcr_value = get_company_type_factor(company_type) # FCR is directly looked up

        # Calculate FHC
        fhc = calculate_fhc(f_role, f_level, f_field, f_school, f_exp)

        # Calculate FUS
        fus = calculate_fus(general_skill_progress, firm_specific_skill_progress, gamma_gen, gamma_spec)

        # Calculate V_raw and V_i(t) (Idiosyncratic Risk)
        v_raw = calculate_v_idiosyncratic_raw(fhc, fcr_value, fus, W_CR, W_US)
        v_idiosyncratic_normalized = calculate_v_idiosyncratic_normalized(v_raw)

        # Calculate H_base (no TTV in initial calculation, k=0)
        h_base_current = get_occupation_hazard(current_occupation)
        h_base = calculate_h_base_ttv(h_base_current, h_base_current, 0, ttv_months) # k=0 for initial calculation

        # Retrieve environmental modifiers
        m_econ = get_economic_climate_modifier(economic_climate)
        i_ai = get_ai_innovation_index(ai_innovation_pace)

        # Calculate H_i (Systematic Risk)
        h_systematic = calculate_systematic_risk(h_base, m_econ, i_ai, w_econ, w_inno)

        # Calculate Probabilities and Loss
        p_systemic = calculate_p_systemic(h_systematic, beta_systemic)
        p_individual_conditional = calculate_p_individual_conditional(v_idiosyncratic_normalized, beta_individual)
        p_claim = calculate_p_claim(p_systemic, p_individual_conditional)
        l_payout = calculate_l_payout(annual_salary, coverage_duration, coverage_percentage)
        e_loss = calculate_expected_loss(p_claim, l_payout)
        p_monthly = calculate_monthly_premium(e_loss, loading_factor, minimum_premium)

        st.session_state['last_calculated_v_idiosyncratic'] = v_idiosyncratic_normalized
        st.session_state['last_calculated_h_systematic'] = h_systematic
        st.session_state['last_calculated_p_monthly'] = p_monthly

        st.session_state['last_fhc'] = fhc
        st.session_state['last_fcr'] = fcr_value
        st.session_state['last_fus'] = fus
        st.session_state['last_h_base'] = h_base_current # Store the raw H_base for visualization
        st.session_state['last_m_econ'] = m_econ
        st.session_state['last_i_ai'] = i_ai

        st.session_state['current_month'] = 0 # Reset month for progress tracking

        # Add initial state to history
        new_row_history = pd.DataFrame([{
            'Month': st.session_state['current_month'],
            'Idiosyncratic Risk': v_idiosyncratic_normalized,
            'Systematic Risk': h_systematic,
            'Monthly Premium': p_monthly
        }])
        st.session_state['idiosyncratic_risk_history'] = pd.concat([st.session_state['idiosyncratic_risk_history'], new_row_history], ignore_index=True)

        new_row_skill_history = pd.DataFrame([{
            'Month': st.session_state['current_month'],
            'General Skill Progress': general_skill_progress * 100,
            'Firm-Specific Skill Progress': firm_specific_skill_progress * 100
        }])
        st.session_state['skill_progress_history'] = pd.concat([st.session_state['skill_progress_history'], new_row_skill_history], ignore_index=True)

        st.session_state['user_skills_proficiency'] = {
            "General Skills": general_skill_progress * 100,
            "Firm-Specific Skills": firm_specific_skill_progress * 100
        }

        st.success("AI-Q Score Calculated Successfully!")

    if 'last_calculated_v_idiosyncratic' in st.session_state:
        st.subheader("Current AI Risk Assessment Results")
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric("Idiosyncratic Risk ($V_i(t)$)", f"{st.session_state['last_calculated_v_idiosyncratic']:.2f}")
        with col_res2:
            st.metric("Systematic Risk ($H_i$)", f"{st.session_state['last_calculated_h_systematic']:.2f}")
        with col_res3:
            st.metric("Estimated Monthly Premium ($P_{monthly}$)", f"${st.session_state['last_calculated_p_monthly']:.2f}")

        st.markdown("---")
        st.subheader("Risk Factor Contributions")
        fig_idiosyncratic, fig_systematic = plot_risk_factor_contributions(
            st.session_state['last_fhc'], st.session_state['last_fcr'], st.session_state['last_fus'],
            st.session_state['last_h_base'], st.session_state['last_m_econ'], st.session_state['last_i_ai']
        )
        st.plotly_chart(fig_idiosyncratic, use_container_width=True)
        st.plotly_chart(fig_systematic, use_container_width=True)

        st.subheader("Detailed Factor Explanations")
        with st.expander("Human Capital Factor ($FHC$)"):
            st.markdown("""
            The Human Capital Factor ($FHC$) quantifies your inherent resilience based on your professional background.
            A lower $FHC$ indicates stronger foundational resilience. It's calculated as:
            $$
            FHC = f_{role} \cdot f_{level} \cdot f_{field} \cdot f_{school} \cdot f_{exp}
            $$
            Where:
            -   $f_{role}$: Role Multiplier, reflecting inherent job title vulnerability.
            -   $f_{level}$: Education Level Factor (e.g., PhD has lower factor, thus lower risk).
            -   $f_{field}$: Education Field Factor (e.g., STEM fields have lower factor).
            -   $f_{school}$: Institution Tier Factor (e.g., Tier 1 schools have lower factor).
            -   $f_{exp}$: Experience Factor, which generally decreases with experience up to 20 years.
            Current $FHC$: **{st.session_state['last_fhc']:.2f}**
            """)

        with st.expander("Company Risk Factor ($FCR$)"):
            st.markdown("""
            The Company Risk Factor ($FCR$) assesses the stability and growth prospects of your employer.
            A lower $FCR$ implies a more stable company, reducing your risk. For this demonstration,
            $FCR$ is derived from the selected company type:
            $$
            FCR = w_{1} \cdot S_{senti} + w_{2} \cdot S_{fin} + w_{3} \cdot S_{growth}
            $$
            Current $FCR$: **{st.session_state['last_fcr']:.2f}** (from company type lookup)
            """)

        with st.expander("Upskilling Factor ($FUS$)"):
            st.markdown("""
            The Upskilling Factor ($FUS$) directly reflects how your learning efforts mitigate risk.
            Crucially, it differentiates between general (portable) and firm-specific skills.
            A higher progress in general skills leads to a greater reduction in risk.
            $$
            F_{US} = 1 - (\gamma_{gen} P_{gen}(t) + \gamma_{spec} P_{spec}(t))
            $$
            Where $P_{gen}(t)$ and $P_{spec}(t)$ are your progress (0-1) in general and firm-specific skills respectively.
            Note that $\gamma_{gen} > \gamma_{spec}$ ensures general skills have a stronger impact.
            Current $FUS$: **{st.session_state['last_fus']:.2f}**
            """)

        with st.expander("Systematic Risk ($H_i$)"):
            st.markdown("""
            The Systematic Risk ($H_i$) reflects the broader automation hazard of your occupation,
            adjusted by macroeconomic and AI innovation trends.
            $$
            H_{i} = H_{base}(t) \cdot (w_{econ} M_{econ} + w_{inno} I_{AI})
            $$
            -   $H_{base}(t)$: Base Occupational Hazard for your role.
            -   $M_{econ}$: Economic Climate Modifier (e.g., recession increases risk).
            -   $I_{AI}$: AI Innovation Index (e.g., rapid breakthroughs increase risk).
            Current $H_i$: **{st.session_state['last_calculated_h_systematic']:.2f}**
            """)

elif page == "Upskilling Path":
    st.header("Upskilling Path")
    st.markdown("""
    Based on your current occupation, explore recommended skills and learning resources.
    Focus on **general, portable skills** to significantly reduce your Idiosyncratic Risk.
    """)

    current_occupation_for_skills = st.selectbox(
        "Select your Current Occupation to see recommended skills:",
        options=list(OCCUPATION_HAZARDS.keys()),
        key="upskill_occupation_select"
    )

    recommended_skills = get_skills_for_occupation(current_occupation_for_skills)

    st.subheader("Recommended High-Impact Skills")
    col_gen_skills, col_firm_skills = st.columns(2)

    with col_gen_skills:
        st.markdown("##### General (Portable) Skills")
        for skill in recommended_skills.get("general", []):
            st.markdown(f"- **{skill}**")
    with col_firm_skills:
        st.markdown("##### Firm-Specific Skills")
        for skill in recommended_skills.get("firm-specific", []):
            st.markdown(f"- **{skill}**")

    # Skill Gap Analysis (Conceptual Radar Chart)
    st.subheader("Skill Gap Analysis (Conceptual)")
    st.markdown("""
    *This radar chart conceptually illustrates your current skill proficiency against recommended levels.
    In a full implementation, actual proficiency assessments would feed this visualization.*
    """)
    if st.session_state['user_skills_proficiency']:
        # For demonstration, let's assume recommended skills are 80% for general, 70% for firm-specific
        rec_prof_gen = 80
        rec_prof_spec = 70
        recommended_for_radar = {
            "General Skills": rec_prof_gen,
            "Firm-Specific Skills": rec_prof_spec
        }
        fig_radar = plot_skill_gap_radar(st.session_state['user_skills_proficiency'], recommended_for_radar)
        st.plotly_chart(fig_radar, use_container_width=True)
    else:
        st.info("Please calculate your AI-Q Score in the 'Risk Assessment' section first to see skill insights.")


    st.subheader("Personalized Learning Resources")
    skill_type_filter = st.radio("Filter resources by skill type:", options=["All", "general", "firm-specific"], horizontal=True)

    filtered_resources = LEARNING_RESOURCES
    if skill_type_filter != "All":
        filtered_resources = get_learning_resources_by_skill_type(skill_type_filter)

    st.dataframe(filtered_resources, use_container_width=True, hide_index=True)

    st.subheader("Career Path Diversification (Simulate Transition)")
    st.markdown("""
    Considering a career transition to a lower-risk occupation? Simulate the impact on your Systematic Risk.
    """)
    target_occupation = st.selectbox(
        "Select a Target Occupation (e.g., lower H_base)",
        options=[occ for occ in OCCUPATION_HAZARDS.keys() if occ != current_occupation_for_skills],
        key="target_occupation_select"
    )
    months_into_transition = st.slider("Months into Transition Pathway (k)", min_value=0, max_value=ttv_months, value=0, step=1)

    if st.button("Simulate Transition Impact"):
        if 'last_calculated_h_systematic' in st.session_state:
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
                
                # Also calculate hypothetical new premium
                if 'last_calculated_v_idiosyncratic' in st.session_state:
                    sim_p_systemic = calculate_p_systemic(simulated_h_systematic, beta_systemic)
                    sim_p_individual_conditional = calculate_p_individual_conditional(st.session_state['last_calculated_v_idiosyncratic'], beta_individual)
                    sim_p_claim = calculate_p_claim(sim_p_systemic, sim_p_individual_conditional)
                    sim_l_payout = calculate_l_payout(annual_salary, coverage_duration, coverage_percentage)
                    sim_e_loss = calculate_expected_loss(sim_p_claim, sim_l_payout)
                    sim_p_monthly = calculate_monthly_premium(sim_e_loss, loading_factor, minimum_premium)
                    st.success(f"Predicted Monthly Premium ($P_{{monthly}}$) after transition: **${sim_p_monthly:.2f}**")
                else:
                    st.warning("Please calculate your initial AI-Q Score in the 'Risk Assessment' section first.")
            else:
                st.warning("Please calculate your initial AI-Q Score in the 'Risk Assessment' section first.")
        else:
            st.warning("Please calculate your initial AI-Q Score in the 'Risk Assessment' section first.")


elif page == "Progress Tracking":
    st.header("Progress Tracking")
    st.markdown("""
    Track your progress over time and see how your upskilling efforts
    and career transitions impact your AI Risk Score and estimated monthly premium.
    """)

    st.subheader("Update Your Progress")
    col_update1, col_update2 = st.columns(2)
    with col_update1:
        new_general_skill_progress = st.slider("Update General Skill Progress (0-100%)", min_value=0, max_value=100, value=st.session_state['skill_progress_history']['General Skill Progress'].iloc[-1] if not st.session_state['skill_progress_history'].empty else 50, step=5) / 100.0
    with col_update2:
        new_firm_specific_skill_progress = st.slider("Update Firm-Specific Skill Progress (0-100%)", min_value=0, max_value=100, value=st.session_state['skill_progress_history']['Firm-Specific Skill Progress'].iloc[-1] if not st.session_state['skill_progress_history'].empty else 50, step=5) / 100.0
    
    # Placeholder for updating other factors if needed for historical tracking
    # e.g., simulating changes in years of experience, economic climate, etc.
    st.caption("Note: Other factors (occupation, company type, etc.) are assumed constant unless updated via Risk Assessment.")

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

            st.session_state['user_skills_proficiency'] = {
                "General Skills": new_general_skill_progress * 100,
                "Firm-Specific Skills": new_firm_specific_skill_progress * 100
            }

            st.success(f"Progress updated for Month {st.session_state['current_month']}!")
        else:
            st.warning("Please calculate your initial AI-Q Score in the 'Risk Assessment' section first.")

    st.subheader("Historical Performance")
    if not st.session_state['idiosyncratic_risk_history'].empty:
        st.markdown("##### AI Risk Score and Premium Trend")
        fig_trend = plot_historical_trends(st.session_state['idiosyncratic_risk_history'])
        st.plotly_chart(fig_trend, use_container_width=True)

        st.markdown("##### Skill Proficiency Trend")
        fig_skill_trend = plot_skill_proficiency(st.session_state['skill_progress_history'])
        st.plotly_chart(fig_skill_trend, use_container_width=True)

        st.subheader("Impact Summary")
        if st.session_state['current_month'] > 0:
            initial_v = st.session_state['idiosyncratic_risk_history']['Idiosyncratic Risk'].iloc[0]
            current_v = st.session_state['idiosyncratic_risk_history']['Idiosyncratic Risk'].iloc[-1]
            v_change = initial_v - current_v

            initial_premium = st.session_state['idiosyncratic_risk_history']['Monthly Premium'].iloc[0]
            current_premium = st.session_state['idiosyncratic_risk_history']['Monthly Premium'].iloc[-1]
            premium_change = initial_premium - current_premium

            st.markdown(f"""
            Over the last **{st.session_state['current_month']}** month(s):
            - Your Idiosyncratic Risk has changed by **{v_change:.2f}** points.
            - Your Estimated Monthly Premium has changed by **${premium_change:.2f}**.
            """)
            if v_change > 0:
                st.success("Great job! Your efforts have reduced your Idiosyncratic Risk and monthly premium.")
            elif v_change < 0:
                st.error("Your Idiosyncratic Risk has increased. Consider focusing on high-impact skills.")
            else:
                st.info("Your Idiosyncratic Risk has remained stable.")
    else:
        st.info("No historical data available. Please calculate your initial AI-Q Score in the 'Risk Assessment' section.")


st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.")
