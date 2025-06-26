# application_pages/page1.py
import streamlit as st
import pandas as pd
import textwrap # Import textwrap

from calculations import (
    calculate_fhc, calculate_fcr, calculate_fus, calculate_idiosyncratic_risk,
    calculate_h_base, calculate_systematic_risk,
    calculate_p_systemic, calculate_p_individual_given_systemic,
    calculate_annual_claim_probability, calculate_l_payout,
    calculate_expected_loss, calculate_monthly_premium
)
from data_utils import (
    get_occupation_list, get_education_level_list, get_education_field_list,
    get_school_tier_list, get_company_type_list,
    get_economic_climate_scenarios, get_ai_innovation_scenarios
)
from visualizations import plot_risk_factor_contributions
from actuarial_params import * # Import all constants to get default values initially

def run_page1():
    st.header("1. Risk Assessment")
    st.markdown("This section allows you to input your personal and professional details to calculate your AI-driven job displacement risk.")

    # Initialize session state for this page if not already done
    if 'page1_initialized' not in st.session_state:
        st.session_state.page1_initialized = True
        # Set initial values for inputs if not present
        if 'current_occupation' not in st.session_state: st.session_state.current_occupation = get_occupation_list()[0]
        if 'years_experience' not in st.session_state: st.session_state.years_experience = 5
        if 'education_level' not in st.session_state: st.session_state.education_level = get_education_level_list()[2] # Bachelor's
        if 'education_field' not in st.session_state: st.session_state.education_field = get_education_field_list()[0] # Tech/Engineering
        if 'school_tier' not in st.session_state: st.session_state.school_tier = get_school_tier_list()[1] # Tier 2
        if 'company_type' not in st.session_state: st.session_state.company_type = get_company_type_list()[0] # Big Firm
        if 'economic_climate' not in st.session_state: st.session_state.economic_climate = get_economic_climate_scenarios()[0] # Neutral
        if 'ai_innovation_pace' not in st.session_state: st.session_state.ai_innovation_pace = get_ai_innovation_scenarios()[0] # Neutral
        if 'general_skill_progress' not in st.session_state: st.session_state.general_skill_progress = 50
        if 'firm_specific_skill_progress' not in st.session_state: st.session_state.firm_specific_skill_progress = 50
        if 'annual_salary' not in st.session_state: st.session_state.annual_salary = 75000.0
        if 'coverage_percentage' not in st.session_state: st.session_state.coverage_percentage = 70
        if 'coverage_duration_months' not in st.session_state: st.session_state.coverage_duration_months = 6
        if 'target_occupation' not in st.session_state: st.session_state.target_occupation = None
        if 'months_elapsed_transition' not in st.session_state: st.session_state.months_elapsed_transition = 0

        # Initialize actuarial parameters in session state using imported constants as defaults
        if 'beta_systemic' not in st.session_state: st.session_state.beta_systemic = BETA_SYSTEMIC
        if 'beta_individual' not in st.session_state: st.session_state.beta_individual = BETA_INDIVIDUAL
        if 'loading_factor' not in st.session_state: st.session_state.loading_factor = LOADING_FACTOR
        if 'min_premium' not in st.session_state: st.session_state.min_premium = MIN_PREMIUM
        if 'ttv_period_months' not in st.session_state: st.session_state.ttv_period_months = TTV_PERIOD_MONTHS
        if 'gamma_gen' not in st.session_state: st.session_state.gamma_gen = GAMMA_GEN
        if 'gamma_spec' not in st.session_state: st.session_state.gamma_spec = GAMMA_SPEC
        if 'w_cr_param' not in st.session_state: st.session_state.w_cr_param = W_CR
        if 'w_us_param' not in st.session_state: st.session_state.w_us_param = W_US
        if 'w_econ_param' not in st.session_state: st.session_state.w_econ_param = W_ECON
        if 'w_inno_param' not in st.session_state: st.session_state.w_inno_param = W_INNO


    st.subheader("Your Profile Inputs")
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.current_occupation = st.selectbox(
            "Current Occupation",
            options=get_occupation_list(),
            key='current_occupation',
            help="Your current job role or industry."
        )
        st.session_state.years_experience = st.slider(
            "Years of Experience",
            min_value=0, max_value=40, value=st.session_state.years_experience,
            key='years_experience',
            help="Your total years of professional experience."
        )
        st.session_state.education_level = st.selectbox(
            "Highest Education Level",
            options=get_education_level_list(),
            key='education_level',
            help="Your highest educational attainment."
        )
    with col2:
        st.session_state.education_field = st.selectbox(
            "Education Field",
            options=get_education_field_list(),
            key='education_field',
            help="The field of your highest education, influencing transferable skills."
        )
        st.session_state.school_tier = st.selectbox(
            "School Tier",
            options=get_school_tier_list(),
            key='school_tier',
            help="The tier of your educational institution (proxy for quality)."
        )
        st.session_state.company_type = st.selectbox(
            "Company Type",
            options=get_company_type_list(),
            key='company_type',
            help="The type of company you work for, influencing its stability."
        )

    st.subheader("Environmental Modifiers")
    col3, col4 = st.columns(2)
    with col3:
        st.session_state.economic_climate = st.selectbox(
            "Economic Climate",
            options=get_economic_climate_scenarios(),
            key='economic_climate',
            help="Macroeconomic environment's effect on AI investment."
        )
    with col4:
        st.session_state.ai_innovation_pace = st.selectbox(
            "AI Innovation Pace",
            options=get_ai_innovation_scenarios(),
            key='ai_innovation_pace',
            help="Velocity of technological change in AI."
        )

    st.subheader("Skill Progress (Current)")
    col5, col6 = st.columns(2)
    with col5:
        st.session_state.general_skill_progress = st.slider(
            "General Skill Progress (%)",
            min_value=0, max_value=100, value=st.session_state.general_skill_progress,
            key='general_skill_progress',
            help="Your current progress in general/portable skills (e.g., Python, data analysis)."
        )
    with col6:
        st.session_state.firm_specific_skill_progress = st.slider(
            "Firm-Specific Skill Progress (%)",
            min_value=0, max_value=100, value=st.session_state.firm_specific_skill_progress,
            key='firm_specific_skill_progress',
            help="Your current progress in firm-specific skills (e.g., proprietary software)."
        )

    st.subheader("Actuarial Parameters (Adjust for Simulation)")
    col7, col8 = st.columns(2)
    with col7:
        st.session_state.annual_salary = st.number_input(
            "Annual Salary ($)",
            min_value=10000.0, max_value=500000.0, value=st.session_state.annual_salary, step=5000.0,
            key='annual_salary',
            help="Your annual income, used for loss calculation."
        )
        st.session_state.coverage_percentage = st.slider(
            "Coverage Percentage (%)",
            min_value=0, max_value=100, value=st.session_state.coverage_percentage,
            key='coverage_percentage',
            help="Percentage of salary to be covered in case of job displacement."
        )
        st.session_state.coverage_duration_months = st.number_input(
            "Coverage Duration (Months)",
            min_value=1, max_value=24, value=st.session_state.coverage_duration_months,
            key='coverage_duration_months',
            help="Number of months for payout if a claim is triggered."
        )
        st.session_state.beta_systemic = st.slider(
            "Systemic Event Base Probability (β_systemic)",
            min_value=0.01, max_value=0.50, value=st.session_state.beta_systemic, step=0.01,
            key='beta_systemic',
            help="Base probability of a systemic displacement event in your industry."
        )
        st.session_state.w_cr_param = st.slider(
            "Weight for Company Risk Factor (w_CR)",
            min_value=0.0, max_value=1.0, value=st.session_state.w_cr_param, step=0.05,
            key='w_cr_param',
            help="Weight for Company Risk Factor in Idiosyncratic Risk."
        )
    with col8:
        st.session_state.beta_individual = st.slider(
            "Individual Loss Base Probability (β_individual)",
            min_value=0.10, max_value=1.00, value=st.session_state.beta_individual, step=0.01,
            key='beta_individual',
            help="Base conditional probability of job loss for you, given a systemic event."
        )
        st.session_state.loading_factor = st.slider(
            "Loading Factor (λ)",
            min_value=1.0, max_value=2.5, value=st.session_state.loading_factor, step=0.1,
            key='loading_factor',
            help="Standard insurance multiplier added to expected loss."
        )
        st.session_state.min_premium = st.number_input(
            "Minimum Premium ($)",
            min_value=5.00, max_value=100.00, value=st.session_state.min_premium, step=5.00,
            key='min_premium',
            help="Minimum monthly premium to ensure policy viability."
        )
        st.session_state.ttv_period_months = st.slider(
            "Time-to-Value Period (TTV) for Transition (Months)",
            min_value=1, max_value=36, value=st.session_state.ttv_period_months, step=1,
            key='ttv_period_months',
            help="Total months for base hazard to transition to a new target occupation."
        )
        st.session_state.gamma_gen = st.slider(
            "Weight for General Skills (γ_gen)",
            min_value=0.1, max_value=0.9, value=st.session_state.gamma_gen, step=0.05,
            key='gamma_gen',
            help="Weight for general skills in Upskilling Factor. Should be > γ_spec."
        )
        st.session_state.gamma_spec = st.slider(
            "Weight for Firm-Specific Skills (γ_spec)",
            min_value=0.0, max_value=0.5, value=st.session_state.gamma_spec, step=0.05,
            key='gamma_spec',
            help="Weight for firm-specific skills in Upskilling Factor. Should be < γ_gen."
        )
        if st.session_state.gamma_gen <= st.session_state.gamma_spec:
            st.warning("Warning: γ_gen should be greater than γ_spec to properly reward portable skills. Auto-adjusting γ_gen.")
            st.session_state.gamma_gen = st.session_state.gamma_spec + 0.05 # Auto adjust
        
        st.session_state.w_us_param = 1.0 - st.session_state.w_cr_param # w_CR + w_US must sum to 1.0
        st.write(f"Weight for Upskilling Factor (w_US): {st.session_state.w_us_param:.2f} (auto-adjusted)")
        
        # Systematic Risk Weights (w_econ, w_inno) should also sum to 1.0, as per spec
        st.session_state.w_econ_param = st.slider(
            "Weight for Economic Climate (w_econ)",
            min_value=0.0, max_value=1.0, value=st.session_state.w_econ_param, step=0.05,
            key='w_econ_param',
            help="Weight for Economic Climate Modifier in Systematic Risk."
        )
        st.session_state.w_inno_param = 1.0 - st.session_state.w_econ_param
        st.write(f"Weight for AI Innovation (w_inno): {st.session_state.w_inno_param:.2f} (auto-adjusted)")


    if st.button("Calculate AI-Q Score"):
        # Calculate FHC
        fhc = calculate_fhc(
            occupation=st.session_state.current_occupation,
            years_experience=st.session_state.years_experience,
            education_level=st.session_state.education_level,
            education_field=st.session_state.education_field,
            school_tier=st.session_state.school_tier
        )
        st.session_state.fhc_score = fhc

        # Calculate FCR
        fcr = calculate_fcr(company_type=st.session_state.company_type)
        st.session_state.fcr_score = fcr

        # Calculate FUS
        # Use session state gamma values
        fus = calculate_fus(
            p_gen=st.session_state.general_skill_progress,
            p_spec=st.session_state.firm_specific_skill_progress
        )
        st.session_state.fus_score = fus

        # Calculate Idiosyncratic Risk V_i(t)
        # Use session state W_CR and W_US
        v_raw = fhc * (st.session_state.w_cr_param * fcr + st.session_state.w_us_param * fus)
        v_i_t = min(100.0, max(5.0, v_raw * 50.0)) # Normalization constant 50.0 is implicit in problem statement
        st.session_state.idiosyncratic_risk_score = v_i_t
        st.session_state.v_raw_score = v_raw # Store raw for explanation

        # Calculate H_base
        h_base = calculate_h_base(
            current_occupation=st.session_state.current_occupation,
            target_occupation=st.session_state.target_occupation, # Pass target_occupation for transition calculation
            months_elapsed_transition=st.session_state.months_elapsed_transition
        )
        st.session_state.h_base_score = h_base

        # Calculate Systematic Risk H_i
        # Use session state W_ECON and W_INNO
        h_i = calculate_systematic_risk(
            h_base=h_base,
            economic_climate=st.session_state.economic_climate,
            ai_innovation_pace=st.session_state.ai_innovation_pace
        )
        st.session_state.systematic_risk_score = h_i

        # Calculate P_systemic
        # Use session state values for beta_systemic from sliders
        p_systemic = (h_i / 100.0) * st.session_state.beta_systemic
        st.session_state.p_systemic_calc = p_systemic

        # Calculate P_individual|systemic
        # Use session state values for beta_individual from sliders
        p_individual_given_systemic = (v_i_t / 100.0) * st.session_state.beta_individual
        st.session_state.p_individual_given_systemic_calc = p_individual_given_systemic

        # Calculate P_claim
        p_claim = calculate_annual_claim_probability(p_systemic=p_systemic, p_individual_given_systemic=p_individual_given_systemic)
        st.session_state.p_claim_calc = p_claim

        # Calculate L_payout
        l_payout = calculate_l_payout(
            annual_salary=st.session_state.annual_salary,
            coverage_duration_months=st.session_state.coverage_duration_months,
            coverage_percentage=st.session_state.coverage_percentage
        )
        st.session_state.l_payout_calc = l_payout

        # Calculate Expected Loss E[Loss]
        e_loss = calculate_expected_loss(p_claim=p_claim, l_payout=l_payout)
        st.session_state.e_loss_calc = e_loss

        # Calculate Monthly Premium P_monthly
        # Use session state values for loading_factor, min_premium from sliders
        p_monthly = max((e_loss * st.session_state.loading_factor) / 12.0, st.session_state.min_premium)
        st.session_state.monthly_premium_calc = p_monthly

        # Store current results for progress tracking
        if 'ai_q_score_history' not in st.session_state:
            st.session_state.ai_q_score_history = pd.DataFrame(columns=['Time', 'Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium', 'General Skill Progress', 'Firm-Specific Skill Progress'])
        
        new_history_entry = {
            'Time': len(st.session_state.ai_q_score_history) + 1,
            'Idiosyncratic Risk': v_i_t,
            'Systematic Risk': h_i,
            'Monthly Premium': p_monthly,
            'General Skill Progress': st.session_state.general_skill_progress,
            'Firm-Specific Skill Progress': st.session_state.firm_specific_skill_progress
        }
        st.session_state.ai_q_score_history = pd.concat([st.session_state.ai_q_score_history, pd.DataFrame([new_history_entry])], ignore_index=True)


    if 'idiosyncratic_risk_score' in st.session_state:
        st.subheader("AI-Q Score Results")
        col_res1, col_res2, col_res3 = st.columns(3)
        with col_res1:
            st.metric(label="Idiosyncratic Risk (V_i(t))", value=f"{st.session_state.idiosyncratic_risk_score:.2f}")
        with col_res2:
            st.metric(label="Systematic Risk (H_i)", value=f"{st.session_state.systematic_risk_score:.2f}")
        with col_res3:
            st.metric(label="Estimated Monthly Premium", value=f"${st.session_state.monthly_premium_calc:.2f}")

        st.markdown("---")
        st.subheader("Risk Breakdown")
        if st.session_state.fhc_score is not None:
            fig_contributions = plot_risk_factor_contributions(
                fhc_score=st.session_state.fhc_score,
                fcr_score=st.session_state.fcr_score,
                fus_score=st.session_state.fus_score,
                h_base_score=st.session_state.h_base_score,
                m_econ_score=ECONOMIC_CLIMATE_SCENARIOS.get(st.session_state.economic_climate, 1.0), # Use the actual modifier value
                i_ai_score=AI_INNOVATION_SCENARIOS.get(st.session_state.ai_innovation_pace, 1.0) # Use the actual modifier value
            )
            st.plotly_chart(fig_contributions, use_container_width=True)
            st.markdown("📈 *The bar chart above visualizes the raw values of the factors contributing to your Idiosyncratic and Systematic Risk. Higher values generally indicate a higher contribution to risk, with the Upskilling Factor (FUS) being inversely proportional to risk (lower FUS means better upskilling and lower risk).*")


        st.markdown("---")
        st.subheader("Mathematical Foundations and Explanations")

        with st.expander("Idiosyncratic Risk (Vulnerability) - $V_{i}(t)$"):
            md_content = textwrap.dedent(f"""
            The Idiosyncratic Risk, or Vulnerability ($V_{{i}}(t)$), is a granular, multi-factor assessment of an individual's susceptibility to job displacement. It is calculated as a composite of Human Capital ($FHC$), Company Risk ($FCR$), and Proactive Upskilling efforts ($FUS$).

            The general form is:
            $$
            V_{{i}}(t) = f(FHC, FCR, FUS)
            $$
            And specifically, it is modeled as a weighted product:
            $$
            V_{{raw}} = FHC \cdot (w_{{CR}} \cdot FCR + w_{{US}} \cdot FUS)
            $$
            Where:
            -   $V_{{i}}(t)$: The final normalized Idiosyncratic Risk score for individual $i$ at time $t$.
            -   $V_{{raw}}$: The raw Idiosyncratic Risk score before normalization.
            -   $FHC$: Human Capital Factor, assessing foundational resilience.
            -   $FCR$: Company Risk Factor, quantifying employer stability.
            -   $FUS$: Upskilling Factor, reflecting proactive training efforts.
            -   $w_{{CR}}$: Weight for Company Risk Factor (current: {st.session_state.w_cr_param:.1f}).
            -   $w_{{US}}$: Weight for Upskilling Factor (current: {st.session_state.w_us_param:.1f}).

            The final $V_{{i}}(t)$ is normalized to a scale of 0-100 using:
            $$
            V_{{i}}(t) = \min(100.0, \max(5.0, V_{{raw}} \cdot 50.0))
            $$
            Your calculated $V_{{raw}}$ is: {st.session_state.v_raw_score:.2f}
            """)
            st.markdown(md_content)

        with st.expander("Human Capital Factor ($FHC$)"):
            md_content = textwrap.dedent(f"""
            The Human Capital Factor ($FHC$) assesses an individual's foundational resilience based on their educational and professional background. It is calculated as a weighted product of several sub-factors:
            $$
            FHC = f_{{role}} \cdot f_{{level}} \cdot f_{{field}} \cdot f_{{school}} \cdot f_{{exp}}
            $$
            Where:
            -   $f_{{role}}$: Role Multiplier, representing inherent job title vulnerability.
            -   $f_{{level}}$: Education Level Factor, based on highest education attained.
            -   $f_{{field}}$: Education Field Factor, rewarding transferable skills.
            -   $f_{{school}}$: Institution Tier Factor, proxy for quality of foundational training.
            -   $f_{{exp}}$: Experience Factor, a decaying function of years of experience, calculated as $1 - (0.015 \cdot \min(\text{{Years Experience}}, 20))$.

            Your calculated $FHC$ is: {st.session_state.fhc_score:.2f}
            """)
            st.markdown(md_content)

        with st.expander("Company Risk Factor ($FCR$)"):
            md_content = textwrap.dedent(f"""
            The Company Risk Factor ($FCR$) quantifies the stability and growth prospects of the individual's current employer, analogous to a corporate credit rating. For this synthetic application, it's derived from the chosen company type's underlying sentiment, financial health, and growth/AI-adoption scores.
            $$
            FCR = w_{{1}} \cdot S_{{senti}} + w_{{2}} \cdot S_{{fin}} + w_{{3}} \cdot S_{{growth}}
            $$
            Your calculated $FCR$ is: {st.session_state.fcr_score:.2f}
            """)
            st.markdown(md_content)

        with st.expander("Upskilling Factor ($FUS$)"):
            md_content = textwrap.dedent(f"""
            The Upskilling Factor ($FUS$) differentiates between skill types, rewarding portable skills more heavily. This formula directly addresses how individual learning efforts mitigate risk, especially emphasizing general, portable skills over firm-specific ones.
            $$
            F_{{US}} = 1 - (\gamma_{{gen}} P_{{gen}}(t) + \gamma_{{spec}} P_{{spec}}(t))
            $$
            Where:
            -   $P_{{gen}}(t)$: Individual's training progress (from 0 to 1) in "General" or "Portable" skills (e.g., Python, data analysis) at time $t$.
            -   $P_{{spec}}(t)$: Individual's training progress (from 0 to 1) in "Firm-Specific" skills (e.g., proprietary internal software) at time $t$.
            -   $\gamma_{{gen}}$: Weighting parameter for general skills (current: {st.session_state.gamma_gen:.2f}).
            -   $\gamma_{{spec}}$: Weighting parameter for firm-specific skills (current: {st.session_state.gamma_spec:.2f}).

            The condition $\gamma_{{gen}} > \gamma_{{spec}}$ ensures that acquiring portable skills provides a greater reduction in risk.
            Your calculated $FUS$ is: {st.session_state.fus_score:.2f}
            """)
            st.markdown(md_content)

        with st.expander("Systematic Risk (Hazard) - $H_{i}$"):
            md_content = textwrap.dedent(f"""
            The Systematic Risk score ($H_{{i}}$) is a dynamic index reflecting the macro-level automation hazard of an occupation, adjusted by broader environmental factors.
            $$
            H_{{i}} = H_{{base}}(t) \cdot (w_{{econ}} M_{{econ}} + w_{{inno}} I_{{AI}})
            $$
            Where:
            -   $H_{{base}}(t)$: Base Occupational Hazard for the occupation at time $t$.
            -   $M_{{econ}}$: Economic Climate Modifier (current: {ECONOMIC_CLIMATE_SCENARIOS.get(st.session_state.economic_climate, 1.0):.2f}), capturing macroeconomic environment's effect on AI investment.
            -   $I_{{AI}}$: AI Innovation Index (current: {AI_INNOVATION_SCENARIOS.get(st.session_state.ai_innovation_pace, 1.0):.2f}), capturing velocity of technological change.
            -   $w_{{econ}}, w_{{inno}}$: Calibration weights that sum to 1.0 (current: {st.session_state.w_econ_param:.1f}, {st.session_state.w_inno_param:.1f}).

            Your calculated $H_{{base}}(t)$ is: {st.session_state.h_base_score:.2f}
            Your calculated $H_{{i}}$ is: {st.session_state.systematic_risk_score:.2f}
            """)
            st.markdown(md_content)

        with st.expander("Annual Claim Probability - $P_{claim}$"):
            md_content = textwrap.dedent(f"""
            The annual probability of a claim ($P_{{claim}}$) is modeled as the joint probability of a systemic event and that event leading to a loss for the individual.
            $$
            P_{{claim}} = P_{{systemic}} \cdot P_{{individual|systemic}}
            $$
            Where:
            -   $P_{{systemic}}$: Probability of a systemic displacement event in the individual's industry.
                $$
                P_{{systemic}} = \frac{{H_{{i}}}}{{100}} \cdot \beta_{{systemic}}
                $$
                (Current $\beta_{{systemic}}$: {st.session_state.beta_systemic:.2f})
            -   $P_{{individual|systemic}}$: Conditional probability of job loss for the individual, given a systemic event.
                $$
                P_{{individual|systemic}} = \frac{{V_{{i}}(t)}}{{100}} \cdot \beta_{{individual}}
                $$
                (Current $\beta_{{individual}}$: {st.session_state.beta_individual:.2f})

            Your calculated $P_{{systemic}}$ is: {st.session_state.p_systemic_calc:.4f}
            Your calculated $P_{{individual|systemic}}$ is: {st.session_state.p_individual_given_systemic_calc:.4f}
            Your calculated $P_{{claim}}$ is: {st.session_state.p_claim_calc:.4f}
            """)
            st.markdown(md_content)

        with st.expander("Expected Loss - $E[Loss]$"):
            md_content = textwrap.dedent(f"""
            The Annual Expected Loss ($E[Loss]$) is the total payout amount multiplied by the probability of a claim.
            $$
            E[Loss] = P_{{claim}} \cdot L_{{payout}}
            $$
            The payout amount ($L_{{payout}}$) is calculated as:
            $$
            L_{{payout}} = \left(\frac{{\text{{Annual Salary}}}}{{12}} \cdot \text{{Coverage Duration}}\right) \cdot \text{{Coverage Percentage}}
            $$
            Your Annual Salary: ${st.session_state.annual_salary:,.2f}
            Coverage Duration: {st.session_state.coverage_duration_months} months
            Coverage Percentage: {st.session_state.coverage_percentage}%
            Your calculated $L_{{payout}}$ is: ${st.session_state.l_payout_calc:,.2f}
            Your calculated $E[Loss]$ is: ${st.session_state.e_loss_calc:,.2f}
            """)
            st.markdown(md_content)

        with st.expander("Monthly Premium - $P_{monthly}$"):
            md_content = textwrap.dedent(f"""
            The monthly premium ($P_{{monthly}}$) is the final step where the annual expected loss is adjusted by a loading factor, converted to a monthly figure, and floored at the minimum premium.
            $$
            P_{{monthly}} = \max\left(\frac{{E[Loss] \cdot \lambda}}{{12}}, P_{{min}}\right)
            $$
            Where:
            -   $\lambda$: Loading Factor (current: {st.session_state.loading_factor:.1f}), a standard insurance multiplier.
            -   $P_{{min}}$: Minimum Premium (current: ${st.session_state.min_premium:.2f}) to ensure policy viability.

            Your calculated $P_{{monthly}}$ is: ${st.session_state.monthly_premium_calc:.2f}
            """)
            st.markdown(md_content)
