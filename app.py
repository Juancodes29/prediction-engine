
import streamlit as st
import pandas as pd
picks = pd.read_csv("today_picks.csv")

total_picks = len(picks)
aplus_picks = len(picks[picks["Grade"].isin(["A++", "A+"])])

st.set_page_config(
    page_title="Juan's Prediction Engine",
    page_icon="⚾",
    layout="wide"
)

st.title("⚾ Juan's Prediction Engine")
st.caption("MLB + World Cup Prediction Platform")

col1, col2, col3, col4 = st.columns(4)

with col1:
     st.metric("Today's Picks", total_picks)

with col2:
    st.metric("A+ Picks", aplus_picks)

with col3:
    st.metric("Model Record", "127-94")

with col4:
    st.metric("Win Rate", "57.4%")

st.divider()

tab1, tab2, tab3 = st.tabs([
    "⚾ MLB Predictor",
    "⚽ World Cup Predictor",
    "📊 Results"
])

with tab1:
    
top_picks = picks[picks["Grade"].isin(["A++", "A+", "A"])]

best_pick = top_picks.sort_values("Bet Score", ascending=False).iloc[0]

st.markdown("### 🔥 Best Pick of the Day")

colA, colB, colC, colD = st.columns(4)

with colA:
    st.metric("Pick", best_pick["Pick"])

with colB:
    st.metric("Grade", best_pick["Grade"])

with colC:
    st.metric("Bet Score", best_pick["Bet Score"])

with colD:
    st.metric("Win %", f'{best_pick["Pick Win %"]}%')

st.divider()

    st.subheader("Top Picks Today")

st.dataframe(
    top_picks[[
        "Game",
        "Pick",
        "Pick Win %",
        "Vegas Win %",
        "Value Edge",
        "Bet Score",
        "Model Edge",
        "Grade",
        "Away Pitcher",
        "Home Pitcher"
    ]],
    use_container_width=True
)
st.subheader("🔥 Value Bets")

value_bets = picks[picks["Value Edge"] >= 5]

st.dataframe(
    value_bets[[
        "Game",
        "Pick",
        "Pick Win %",
        "Vegas Win %",
        "Value Edge",
        "Bet Score",
        "Grade"
    ]],
    use_container_width=True
)
with tab2:

    st.subheader("World Cup Predictor")

    st.info(
        "Future home of the World Cup model."
    )

with tab3:

    st.subheader("Performance")

    st.metric(
        "Historical Accuracy",
        "57.4%"
    )
