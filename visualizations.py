
import plotly.express as px
import pandas as pd

def plot_risk_factor_contributions(fhc: float, fcr: float, fus: float, h_base: float, m_econ: float, i_ai: float):
    """
    Generates bar charts showing contributions to Idiosyncratic and Systematic Risk.
    """
    # Idiosyncratic Risk Contributions
    idiosyncratic_data = {
        'Factor': ['Human Capital (FHC)', 'Company Risk (FCR)', 'Upskilling (FUS)'],
        'Value': [fhc, fcr, fus]
    }
    df_idiosyncratic = pd.DataFrame(idiosyncratic_data)
    fig_idiosyncratic = px.bar(df_idiosyncratic, x='Factor', y='Value',
                               title='Idiosyncratic Risk Factor Contributions',
                               color='Factor',
                               labels={'Value': 'Factor Value (Lower is Better for FUS, Higher for others)'},
                               color_discrete_map={
                                   'Human Capital (FHC)': 'blue',
                                   'Company Risk (FCR)': 'red',
                                   'Upskilling (FUS)': 'green'
                               },
                               hover_data={'Value': ':.2f'})
    fig_idiosyncratic.update_layout(yaxis_title="Factor Value (Note: FUS acts as a reduction)", showlegend=False)


    # Systematic Risk Contributions
    systematic_data = {
        'Factor': ['Base Occupational Hazard (H_base)', 'Economic Climate (M_econ)', 'AI Innovation (I_AI)'],
        'Value': [h_base, m_econ, i_ai]
    }
    df_systematic = pd.DataFrame(systematic_data)
    fig_systematic = px.bar(df_systematic, x='Factor', y='Value',
                            title='Systematic Risk Factor Contributions',
                            color='Factor',
                            labels={'Value': 'Factor Value (Higher is Worse)'},
                            color_discrete_map={
                                'Base Occupational Hazard (H_base)': 'orange',
                                'Economic Climate (M_econ)': 'purple',
                                'AI Innovation (I_AI)': 'brown'
                            },
                            hover_data={'Value': ':.2f'})
    fig_systematic.update_layout(yaxis_title="Factor Value", showlegend=False)

    return fig_idiosyncratic, fig_systematic

def plot_historical_trends(history_df: pd.DataFrame):
    """
    Generates a line chart tracking AI-Q score, Systematic Risk, and Monthly Premium over time.
    history_df should have columns: 'Month', 'Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium'.
    """
    if history_df.empty:
        return px.line(title="No Historical Data Available")

    fig = px.line(history_df, x='Month', y=['Idiosyncratic Risk', 'Systematic Risk', 'Monthly Premium'],
                  title='AI Risk Score and Premium Trend Over Time',
                  labels={
                      'value': 'Score/Premium',
                      'variable': 'Metric',
                      'Month': 'Months from Start'
                  },
                  hover_data={'value': ':.2f'})
    fig.update_layout(hovermode="x unified")
    fig.update_xaxes(dtick=1) # Ensure months are distinct on x-axis
    return fig

def plot_skill_proficiency(skill_progress_df: pd.DataFrame):
    """
    Generates a line chart showing general vs. firm-specific skill progress over time.
    skill_progress_df should have columns: 'Month', 'General Skill Progress', 'Firm-Specific Skill Progress'.
    """
    if skill_progress_df.empty:
        return px.line(title="No Skill Progress Data Available")

    fig = px.line(skill_progress_df, x='Month', y=['General Skill Progress', 'Firm-Specific Skill Progress'],
                  title='Skill Proficiency Over Time',
                  labels={
                      'value': 'Progress (%)',
                      'variable': 'Skill Type',
                      'Month': 'Months from Start'
                  },
                  range_y=[0, 100],
                  hover_data={'value': ':.1f'})
    fig.update_layout(hovermode="x unified")
    fig.update_xaxes(dtick=1)
    return fig

def plot_skill_gap_radar(user_skills: dict, recommended_skills: dict):
    """
    Generates a radar chart comparing user's current skill proficiency against recommended proficiency.
    This is a conceptual function; actual implementation would need more detailed skill proficiency data.
    For simplicity, let's assume skills are rated 0-100.
    """
    # Example data structure
    # user_skills = {"Python": 70, "SQL": 60, "Communication": 80}
    # recommended_skills = {"Python": 90, "SQL": 80, "Communication": 75}

    skills = sorted(list(set(user_skills.keys()) | set(recommended_skills.keys())))
    user_prof = [user_skills.get(s, 0) for s in skills]
    rec_prof = [recommended_skills.get(s, 0) for s in skills]

    if not skills:
        return px.line(title="No Skill Data for Radar Chart") # Return an empty plot or message

    df_radar = pd.DataFrame(dict(
        r=user_prof + rec_prof,
        theta=skills * 2,
        category=['Your Proficiency'] * len(skills) + ['Recommended'] * len(skills)
    ))

    fig = px.line_polar(df_radar, r='r', theta='theta', line_close=True, color='category',
                        title='Skill Gap Analysis',
                        range_r=[0, 100],
                        labels={'r': 'Proficiency (%)'})
    fig.update_traces(fill='toself')
    return fig
