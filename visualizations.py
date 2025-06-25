
# visualizations.py
import plotly.express as px
import pandas as pd

def create_risk_breakdown_bar_chart(risk_factors: dict, title: str, y_axis_title: str):
    """
    Creates a bar chart showing the contribution of different risk factors.
    Args:
        risk_factors (dict): A dictionary where keys are factor names and values are their scores.
        title (str): Title of the chart.
        y_axis_title (str): Title for the Y-axis.
    """
    df = pd.DataFrame(list(risk_factors.items()), columns=['Factor', 'Value'])
    fig = px.bar(df, x='Factor', y='Value', text='Value',
                 title=title,
                 labels={'Value': y_axis_title},
                 color_discrete_sequence=px.colors.qualitative.Plotly)
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
    fig.update_yaxes(range=[0, df['Value'].max() * 1.2]) # Add some padding to y-axis
    return fig

def create_ai_q_score_trend_line_chart(history_df: pd.DataFrame):
    """
    Creates a line chart tracking AI-Q score and premium over time.
    Args:
        history_df (pd.DataFrame): DataFrame with columns like 'Month', 'Idiosyncratic Risk (Vi)',
                                  'Systematic Risk (Hi)', 'Monthly Premium'.
    """
    if history_df.empty:
        return None

    # Melt the DataFrame to plot multiple lines
    df_melted = history_df.melt(id_vars=['Month'],
                                value_vars=['Idiosyncratic Risk (Vi)', 'Systematic Risk (Hi)', 'Monthly Premium ($)'],
                                var_name='Metric', value_name='Value')

    fig = px.line(df_melted, x='Month', y='Value', color='Metric',
                  title='AI Risk Score and Premium Trend Over Time',
                  labels={'Value': 'Score / Amount', 'Month': 'Months from Start'},
                  hover_data={'Metric': True, 'Value': ':.2f'})
    fig.update_traces(mode='lines+markers')
    fig.update_layout(hovermode="x unified")
    return fig

def create_skill_proficiency_line_chart(skill_history_df: pd.DataFrame):
    """
    Creates a line chart showing general vs. firm-specific skill progress over time.
    Args:
        skill_history_df (pd.DataFrame): DataFrame with columns like 'Month', 'General Skill Progress (%)',
                                         'Firm-Specific Skill Progress (%)'.
    """
    if skill_history_df.empty:
        return None

    df_melted = skill_history_df.melt(id_vars=['Month'],
                                      value_vars=['General Skill Progress (%)', 'Firm-Specific Skill Progress (%)'],
                                      var_name='Skill Type', value_name='Progress')

    fig = px.line(df_melted, x='Month', y='Progress', color='Skill Type',
                  title='Skill Proficiency Progress Over Time',
                  labels={'Progress': 'Progress (%)', 'Month': 'Months from Start'},
                  range_y=[0, 100],
                  hover_data={'Skill Type': True, 'Progress': ':.1f'})
    fig.update_traces(mode='lines+markers')
    fig.update_layout(hovermode="x unified")
    return fig
