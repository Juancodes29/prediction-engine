
import streamlit as st

st.set_page_config(
    page_title="Juan's Prediction Engine",
    page_icon="⚾",
    layout="wide"
)

st.title("⚾ Juan's Prediction Engine")
st.caption("MLB + World Cup Prediction Platform")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Today's Picks", "15")

with col2:
    st.metric("A+ Picks", "2")

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

    st.subheader("Top Picks Today")

    st.dataframe(
        {
            "Game":[
                "Phillies @ Mets",
                "Dodgers @ Padres",
                "Twins @ Rockies"
            ],
            "Pick":[
                "Phillies",
                "Dodgers",
                "Twins"
            ],
            "Grade":[
                "A+",
                "A",
                "A+"
            ],
            "Confidence":[
                "92%",
                "87%",
                "90%"
            ]
        },
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
