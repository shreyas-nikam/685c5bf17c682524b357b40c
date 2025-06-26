
# visualizations.py
# Functions for generating interactive charts

import plotly.express as px
import pandas as pd

def plot_risk_factor_contributions(
    fhc_score: float, fcr_score: float, fus_score: float,
    h_base_score: float, m_econ_score: float, i_ai_score: float
):
    """
    Generates a bar chart showing the relative contributions of Idiosyncratic and Systematic Risk factors.
    """
    # Data for Idiosyncratic Risk factors
    idiosyncratic_data = {
        'Factor': ['Human Capital (FHC)', 'Company Risk (FCR)', 'Upskilling (FUS)'],
        'Contribution': [fhc_score, fcr_score, fus_score],
        'Type': ['Idiosyncratic'] * 3
    }
    # Data for Systematic Risk factors
    systematic_data = {
        'Factor': ['Base Hazard (H_base)', 'Economic Climate (M_econ)', 'AI Innovation (I_AI)'],
        'Contribution': [h_base_score, m_econ_score, i_ai_score],
        'Type': ['Systematic'] * 3
    }

    df_idiosyncratic = pd.DataFrame(idiosyncratic_data)
    df_systematic = pd.DataFrame(systematic_data)

    df_combined = pd.concat([df_idiosyncratic, df_systematic])

    # For visualization, it's often better to show the "impact" or "contribution to risk"
    # FHC, FCR are directly proportional to risk. FUS is inversely proportional (1 - FUS)
    # Let's adjust FUS for visualization to show how much it *reduces* risk or its *positive* contribution to mitigating risk.
    # For a contribution bar chart, it makes more sense to show raw factors as they feed into the score.
    # The magnitude of FHC, FCR, FUS might vary greatly, making a direct bar chart hard to interpret for "contribution".
    # Instead, let's normalize or show the components that *drive* the raw score.
    # V_raw = FHC * (w_CR * FCR + w_US * FUS)
    # H_i = H_base(t) * (w_econ * M_econ + w_inno * I_AI)

    # Let's visualize the *percentage* contribution if possible, or just the raw input values.
    # For simplicity, let's just plot the values themselves, with proper labels.
    # A bar chart with FHC, FCR, FUS as separate bars for Idiosyncratic Risk
    # and H_base, M_econ, I_AI for Systematic Risk.

    # Option 1: Show normalized contribution to the final risk score
    # This might require passing the weights W_CR, W_US, W_ECON, W_INNO as well,
    # and then calculate (FHC * W_CR * FCR) or similar.
    # For now, let's keep it simple as a bar chart of the direct calculated factors.

    # Let's assume for the purpose of this plot, higher is "more" of that factor.
    # For FUS, a higher score means *less* risk, so perhaps visualize (1-FUS) if we want to show risk contribution.
    # The spec says "Bar charts showing risk factor contributions."
    # Let's show the factors that are multiplied/added as their values.
    # For FUS, it's 1 - (gamma_gen P_gen + gamma_spec P_spec). A lower FUS value (closer to 0) means more upskilling, lower risk.
    # So, for a "contribution to risk" visualization, it might be clearer to show (1-FUS) or its inverse.
    # However, the functions return FUS directly. Let's plot FUS directly and clarify in markdown.

    fig = px.bar(
        df_combined,
        x='Factor',
        y='Contribution',
        color='Type',
        barmode='group',
        title='Contribution of Risk Factors',
        labels={'Contribution': 'Factor Value', 'Factor': 'Risk Component'},
        hover_data={'Contribution': ':.2f'}
    )
    fig.update_layout(xaxis_title="Risk Factor", yaxis_title="Factor Value (Higher is often higher risk)")
    return fig

def plot_ai_q_score_trend(history: pd.DataFrame):
    """
    Generates a line chart tracking AI-Q score (V_i(t) and H_i) and Premium over time.
    `history` DataFrame should have columns like 'Time', 'Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium'.
    """
    if history.empty:
        return None

    fig = px.line(
        history,
        x='Time',
        y=['Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium'],
        title='AI-Q Score and Premium Trend Over Time',
        labels={'value': 'Score/Premium', 'variable': 'Metric', 'Time': 'Progress Step'},
        hover_data={'value': ':.2f'}
    )
    fig.update_traces(mode='lines+markers')
    fig.update_layout(yaxis_title="Value", legend_title="Metric")
    return fig

def plot_skill_proficiency_over_time(history: pd.DataFrame):
    """
    Generates a line chart showing general vs. firm-specific skill progress over time.
    `history` DataFrame should have columns like 'Time', 'General Skill Progress', 'Firm-Specific Skill Progress'.
    """
    if history.empty:
        return None

    fig = px.line(
        history,
        x='Time',
        y=['General Skill Progress', 'Firm-Specific Skill Progress'],
        title='Skill Proficiency Over Time',
        labels={'value': 'Progress (%)', 'variable': 'Skill Type', 'Time': 'Progress Step'},
        hover_data={'value': ':.0f'}
    )
    fig.update_traces(mode='lines+markers')
    fig.update_layout(yaxis_title="Progress (%)", legend_title="Skill Type", yaxis_range=[0, 100])
    return fig

