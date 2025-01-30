import streamlit as st
from PIL import Image
import plotly.io as pio
import os
import json

# Set JSON file paths
file_path_1 = os.path.join(os.getcwd(), 'app/utils/forecast_weather_figure.json')
file_path_2 = os.path.join(os.getcwd(), 'app/utils/forecast_figure.json')

# Load Forecast data from JSON files
forecast_file_path = os.path.join(os.getcwd(), 'app/utils/forecast_data.json')

try:
    with open(forecast_file_path, 'r') as f:
        forecast_data = json.load(f)
except FileNotFoundError:
    st.error(f"File not found: {forecast_file_path}")
    forecast_data = None

# Load Plotly figures from JSON files
try:
    forecast_weather_fig = pio.read_json(file_path_1)
except FileNotFoundError:
    st.error(f"File not found: {file_path_1}")
    forecast_weather_fig = None

try:
    forecast_fig = pio.read_json(file_path_2)
except FileNotFoundError:
    st.error(f"File not found: {file_path_2}")
    forecast_fig = None

# Title
st.title("Proof-of-Concept, Prédiction de la balance électrique roumaine avec NeuralProphet et données météo")

# Slider for navigation
slide = st.slider("Select Slide", 1, 7, 1)

if slide == 1:
    st.header("Preuve de concept : Prédiction de la balance électrique roumaine avec NeuralProphet et données météo")

    st.write(
        "Ce dashboard présente une synthèse des données et des résultats obtenus lors de la prédiction "
        "de la balance électrique roumaine (différence entre la production et la consommation d'électricité) "
        "à l'aide de NeuralProphet et des données météo associées."
    )

    st.markdown("""
    - **Slide 2** : Analyse de saisonnalité et d'auto-corrélation de la balance électrique.
    - **Slide 3** : Présentation des prédictions du modèle Random Forest (baseline).
    - **Slide 4** : Comparaison des scores MAE et MSE entre Random Forest et NeuralProphet.
    - **Slide 5** : Graphique intéractif d'entraînement du modèle (évaluation).
    - **Slide 6** : Graphique intéractif des prédictions du modèle à horizon 5 jours.
    - **Slide 7** : Outil pour prédire la balance électrique à horizon 5 jours, avec les données météo associées.
    """)

    image = Image.open('app/utils/consumptionvsproduction.png')
    st.image(image, caption='Production VS Consommation')

    image = Image.open('app/utils/electricitybalance.png')
    st.image(image, caption='Evolution du surplus/déficit en électricité (balance électrique)')
elif slide == 2:
    st.header("Analyse de saisonnalité de la balance électrique")
    st.write("Le graphique suivant montre que la balance électrique est sujette à de nombreuses variations saisonnières.")
    image = Image.open('app/utils/balanceseasonality.png')
    st.image(image, caption='Saisonnalité de la balance électrique')
    st.header("Analyse ACF et PCF de la balance électrique")
    st.write("Les graphiques ACF et PCF montrent que la balance électrique est corrélée avec ses valeurs passées.")
    image = Image.open('app/utils/ACFPCF.png')
    st.image(image, caption='ACF et PCF')
elif slide == 3:
    st.header("Random Forest - Prédictions issues du modèle baseline")
    st.write('Les prédictions du modèle Random Forest sont affichées ci-dessous. On remarque que le modèle éprouve des difficultées à prédire les valeurs extrêmes.')
    image = Image.open('app/utils/randomforest.png')
    st.image(image, caption='Random Forest')
elif slide == 4:
    st.header("Comparaison des scores MAE and MSE entre RandomForest et NeuralProphet")
    st.write("Ci-dessous, les scores MAE et MSE des modèles Random Forest et NeuralProphet sont comparés. On remarque que NeuralProphet obtient de bien meilleurs résultats.")
    mae_rf = 619.5269
    mse_rf = 789.9172
    mae_weather = 154.2477
    mse_weather = 204.5053
    st.write(f"Random Forest - MAE: {mae_rf}, MSE: {mse_rf}")
    st.write(f"Model Weather - MAE: {mae_weather}, MSE: {mse_weather}")
elif slide == 5:
    st.header("Graphique intéractif d'entraînement du modèle pour évaluation.")
    st.write("Vous pouvez zoomer et déplacer le graphique pour explorer les données.")
    if forecast_weather_fig:
        st.plotly_chart(forecast_weather_fig)
    else:
        st.error("Impossible de charger le graphique.")
elif slide == 6:
    st.header("Graphique intéractif des prédictions du modèle à horizon 5 jours.")
    if forecast_fig:
        st.plotly_chart(forecast_fig)
    else:
        st.error("Impossible de charger le graphique.")
elif slide == 7:
    st.header("Prédiction de la balance électrique à horizon 5 jours, avec les données météo associées.")
    if forecast_data:

        user_index = st.number_input(
        "Nous sommes le 31 mars 2024 à 21h, date de fin des données d'entraînement.\
        Sélectionnez votre horizon de prédiction (en heures), jusqu'à 140 heures (5 jours, horizon raisonnable pour des données météo):",
        min_value=1,
        max_value=len(forecast_data),
        value=1
        )

        selected_item = forecast_data[user_index - 1]

        if selected_item is not None:
            st.write(f"**Date et heure**: {selected_item['ds']}")
            st.write(f"**Prédiction du surplus/déficit en électricité**: {selected_item['electricity_balance_forecast']} MW")
            st.write(f"**Vitesse du vent à 100m**: {selected_item['wind_speed_forecast']} Km/h")
            st.write(f"**Température**: {selected_item['temperature_forecast']} °C")
        else:
            st.warning("Aucune donnée de prédiction disponible à cet horizon.")