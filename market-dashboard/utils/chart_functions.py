import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st


def sanitize_help(text: str) -> str:
    if text is None:
        return None
    return text.replace("%", "%%").replace("{", "{{").replace("}", "}}").replace("[", "").replace("]", "")


def display_metric_safe(column, label: str, value, help=None):
    if isinstance(value, (float, int)) and not pd.isna(value):
        if any(keyword in label for keyword in ["SMA", "Low", "High", "Price"]):
            display_value = f"${value:,.2f}"
        else:
            display_value = f"{value:,.2f}"
        column.metric(label=label, value=display_value, help=sanitize_help(help))
    else:
        column.metric(label=label, value="Not Enough Data...", help=sanitize_help(help))


def display_gauge(column, value, title, bar_color="darkblue"):

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={'text': title},

        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': bar_color},
            'steps': [
                {'range': [0, 30], 'color': "green"},
                {'range': [30, 70], 'color': "yellow"},
                {'range': [70, 100], 'color': "red"}
            ],
        }
    ))
    # Change gauge height for mobile
    if st.session_state.get("is_mobile", False):
        fig.update_layout(margin=dict(t=20, b=20), height=250)
    else:
        fig.update_layout(margin=dict(t=20, b=50), height=400)

    column.plotly_chart(fig, use_container_width=True)


def display_price_chart(df: pd.DataFrame, column_name: str = "Close", asset_name: str = ""):

    fig = px.line(df, x='Date', y=column_name, title=f"{asset_name} Price")
    st.plotly_chart(fig, use_container_width=True)
