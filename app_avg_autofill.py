import streamlit as st
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Define average values
avg_vals = {'engine_size': 2.0416666666666665, 'cylinder_capacity': 71.25, 'distance_covered': 164.58333333333334, 'installation_cost': 1175000.0, 'cost_per_scm': 404.0, 'cng_quantity': 18.270833333333332, 'cost_per_fill': 7381.416666666667, 'petrol_price': 935.0, 'petrol_qty': 15.864583333333334, 'petrol_cost_per_distance': 14833.385416666666, 'savings': 7451.96875}

# Define the trained model
def train_model():
    X = np.array([
        [1.8, 75, 200, 1100000, 404, 19.2, 7756.8, 935, 17.0, 15895.0],
        [3.0, 85, 240, 1700000, 404, 21.8, 8807.2, 935, 32.4, 30294.0],
        [1.8, 75, 150, 1100000, 404, 19.2, 7756.8, 935, 12.75, 11921.25],
        [1.8, 75, 150, 1100000, 404, 19.2, 7756.8, 935, 12.75, 11921.25],
        [1.8, 65, 110, 1100000, 404, 16.7, 6746.8, 935, 9.35, 8742.25],
    ])
    y = [8138.2, 21486.8, 4164.45, 4164.45, 1995.45]
    model = RandomForestRegressor(random_state=42)
    model.fit(X, y)
    return model

model = train_model()

st.set_page_config(page_title="CNG Savings Predictor")
st.title("CNG Cost Savings Predictor")
st.write("Enter basic vehicle and fuel details to estimate savings when switching to CNG.")

# User input
engine_size = st.number_input("Engine Size (L)", min_value=0.5, step=0.1)
cylinder_capacity = st.number_input("CNG Cylinder Capacity (L)", min_value=10)
distance_covered = st.number_input("Distance Covered (km)", min_value=0)
cost_per_scm = st.number_input("Cost per SCM of CNG (₦)", min_value=0)
petrol_price = st.number_input("Cost of Petrol per Litre (₦)", min_value=0)

# Predict button
if st.button("Predict Savings"):
    # Use average values for other parameters
    input_data = np.array([[
        engine_size,
        cylinder_capacity,
        distance_covered,
        avg_vals['installation_cost'],
        cost_per_scm,
        avg_vals['cng_quantity'],
        avg_vals['cost_per_fill'],
        petrol_price,
        avg_vals['petrol_qty'],
        avg_vals['petrol_cost_per_distance']
    ]])
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Savings: ₦{prediction:,.2f}")
