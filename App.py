import streamlit as st
import datetime

# App Configuration
st.set_page_config(page_title="Protein Tracker", layout="centered")

# Set your target goal here
PROTEIN_GOAL = 140 

# Initialize storage
if 'total_protein' not in st.session_state:
    st.session_state.total_protein = 0
if 'logs' not in st.session_state:
    st.session_state.logs = []

# UI Header
st.title("🥩 Protein Tracker")

# Progress Bar and Stats
progress = st.session_state.total_protein / PROTEIN_GOAL
st.progress(min(progress, 1.0))
col_stats1, col_stats2 = st.columns(2)
col_stats1.metric("Current Total", f"{st.session_state.total_protein}g")
col_stats2.metric("Remaining", f"{max(0, PROTEIN_GOAL - st.session_state.total_protein)}g")

# Quick Add Section
st.subheader("Quick Add")
c1, c2 = st.columns(2)

with c1:
    if st.button("🍔 1/4lb Burger (20g)"):
        st.session_state.total_protein += 20
        st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - 1/4lb Beef (20g)")
    
    if st.button("🥚 2 Eggs (12g)"):
        st.session_state.total_protein += 12
        st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - 2 Large Eggs (12g)")

    if st.button("🥓 3 Bacon Slices (9g)"):
        st.session_state.total_protein += 9
        st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - 3 Bacon Slices (9g)")

with c2:
    if st.button("🥩 Ribeye/Steak (50g)"):
        st.session_state.total_protein += 50
        st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - Steak/Ribeye (50g)")
    
    if st.button("🍗 Chicken Thigh (15g)"):
        st.session_state.total_protein += 15
        st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - Chicken Thigh (15g)")

    if st.button("🧀 Cheese Snack (7g)"):
        st.session_state.total_protein += 7
        st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - Cheese/Snack (7g)")

# Manual Entry
st.divider()
manual_val = st.number_input("Custom Amount (g)", min_value=0, step=1)
if st.button("Add Custom Protein"):
    st.session_state.total_protein += manual_val
    st.session_state.logs.append(f"{datetime.datetime.now().strftime('%H:%M')} - Custom ({manual_val}g)")

# History
st.subheader("Today's Meals")
for item in reversed(st.session_state.logs):
    st.info(item)

# Reset & Farewell
st.divider()
if st.button("Reset for Tomorrow"):
    st.session_state.total_protein = 0
    st.session_state.logs = []
    st.rerun()

st.write("☀️ **Have a great day!**")
