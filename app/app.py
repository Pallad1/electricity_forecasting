import streamlit as st
from PIL import Image
import pickle

with open('app/utils/forecast_weather_figure.pkl', 'rb') as f:
    forecast_weather_fig = pickle.load(f)

with open('app/utils/forecast_figure.pkl', 'rb') as f:
    forecast_fig = pickle.load(f)

# Title
st.title("Proof-of-Concept, Prédiction de la balance électrique roumaine avec NeuralProphet et données météo")

# Slider for navigation
slide = st.slider("Select Slide", 1, 10, 1)

# Display content based on slider value
if slide == 1:
    st.header("Introduction")
    st.write("Proof-of-Concept, Prédiction de la balance électrique roumaine avec NeuralProphet et données météo")
elif slide == 2:
    st.header("Consumption vs Production")
    image = Image.open('app/utils/consumptionvsProduction.png')
    st.image(image, caption='Consumption vs Production')
elif slide == 3:
    st.header("Electricity Balance")
    image = Image.open('app/utils/electricitybalance.png')
    st.image(image, caption='Electricity Balance')
elif slide == 4:
    st.header("Balance Seasonality")
    image = Image.open('app/utils/balanceseasonality.png')
    st.image(image, caption='Balance Seasonality')
elif slide == 5:
    st.header("ACF and PCF")
    image = Image.open('app/utils/ACFPCF.png')
    st.image(image, caption='ACF and PCF')
elif slide == 6:
    st.header("Balance Seasonality")
    image = Image.open('app/utils/balanceseasonality.png')
    st.image(image, caption='Balance Seasonality')
elif slide == 7:
    st.header("Random Forest")
    image = Image.open('app/utils/randomforest.png')
    st.image(image, caption='Random Forest')

elif slide == 8:
    st.header("MAE and MSE Scores")
    st.write("Displaying MAE and MSE scores for Random Forest and model_weather")
    mae_rf = 619.5269
    mse_rf = 789.9172
    mae_weather = 154.2477
    mse_weather = 204.5053
    st.write(f"Random Forest - MAE: {mae_rf}, MSE: {mse_rf}")
    st.write(f"Model Weather - MAE: {mae_weather}, MSE: {mse_weather}")

elif slide == 9:
    st.header("Forecasting Model Weather")
    st.plotly_chart(forecast_weather_fig)

elif slide == 10:
    st.header("Forecasting Model")
    st.plotly_chart(forecast_fig)