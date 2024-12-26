import streamlit as st
from joblib import load
import numpy as np

def load_model():
    model = load('plant_health_model.joblib')
    return model

model = load_model()

st.sidebar.title(':red[Dashboard]')
app_mode = st.sidebar.selectbox('You can choose here.',['Home', 'About'],                
            placeholder="Select Pages...")

if app_mode == 'Home':
    st.title(':green[Plant Health Prediction]')
    st.image('images/International-Day-Of-Plant-Health-PB-8130368_1920.jpg', width= 512)
    Soil_Moisture = st.slider('Soil Moisture', 0.0 ,50.0, 0.0, step=0.01)
    Ambient_Temperature = st.slider('Ambient Temperature', 0.0, 50.0, 0.0)
    Soil_Temperature = st.slider('Soil Temperature', 0.0, 50.0, 0.0)
    Humidity = st.slider('Humidity', 0.0, 100.0, 0.0)
    Light_Intensity = st.slider('Light Intensity', 0.0, 1200.0, 0.0)
    Soil_pH = st.slider('Soil pH', 0.0, 10.0, 0.0)
    Nitrogen_Level = st.slider('Nitrogen Level', 0.0, 100.0, 0.0)
    Phosphorus_Level = st.slider('Phosphorus Level', 0.0, 100.0, 0.0)
    Potassium_Level = st.slider('Potassium Level', 0.0, 100.0, 0.0)
    Chlorophyll_Content = st.slider('Chlorophyll Content', 0.0, 100.0, 0.0)
    Electrochemical_Signal = st.slider('Electrochemical Signal', 0.0, 5.0, 0.0, step= 0.0001)
    
    features = np.array([
        Soil_Moisture, Ambient_Temperature, Soil_Temperature, Humidity, 
    Light_Intensity, Soil_pH, Nitrogen_Level, Phosphorus_Level, 
    Potassium_Level, Chlorophyll_Content, Electrochemical_Signal
    ]).reshape(1, -1)
    
    if st.button(':red[Predict]'):
        answer = model.predict(features)
        st.write(f'Predicted Plant Health : {answer}')
    
    st.sidebar.subheader(':red[Information]')
    def value_colour(variable, value):
        if value <= 20:
            colour = 'red'
        elif value >= 35:
            colour = 'blue'
        else:
            colour = 'green'
        return st.sidebar.write(f'{variable} : :{colour}[{value}]')

    def value_colour_for_100(variable, value):
        if value <= 35:
            colour = 'red'
        elif value >= 70:
            colour = 'blue'
        else:
            colour = 'green'
        return st.sidebar.write(f'{variable} : :{colour}[{value}]')

    value_colour("Soil Moisture", Soil_Moisture)
    value_colour("Ambient Temperature", Ambient_Temperature)
    value_colour("Soil Temperature", Soil_Temperature)
    value_colour_for_100("Humidity", Humidity)

    if Light_Intensity <= 400:
        st.sidebar.write(f'Soil pH : :red[{Light_Intensity}]')
    elif Light_Intensity >= 800:
        st.sidebar.write(f'Soil pH : :blue[{Light_Intensity}]')
    else:
        st.sidebar.write(f'Soil pH : :green[{Light_Intensity}]')

    if Soil_pH <= 3:
        st.sidebar.write(f'Soil pH : :red[{Soil_pH}]')
    elif Soil_pH >= 7:
        st.sidebar.write(f'Soil pH : :blue[{Soil_pH}]')
    elif Soil_pH > 3 and Soil_pH < 7:
        st.sidebar.write(f'Soil pH : :green[{Soil_pH}]')

    value_colour_for_100("Nitrogen Level", Nitrogen_Level)
    value_colour_for_100("Phosphorus Level", Phosphorus_Level)
    value_colour_for_100("Potassium Level", Potassium_Level)
    value_colour_for_100("Chlorophyll Content", Chlorophyll_Content)

    if Electrochemical_Signal <= 1:
        st.sidebar.write(f'Electrochemical Signal : :red[{Electrochemical_Signal}]')
    elif Electrochemical_Signal >= 2.3:
        st.sidebar.write(f'Electrochemical Signal : :blue[{Electrochemical_Signal}]')
    else:
        st.sidebar.write(f'Electrochemical Signal : :green[{Electrochemical_Signal}]')



if app_mode == 'About':
    st.title(':red[About our app]')
    st.subheader('Soil Properties 🌍:')
    st.image('images/Generated Image.jpeg', use_column_width= False, channels= 'RGB', width= 200)
    st.text("""Soil_Moisture (%) 💧: Indicates water content in the soil.
Soil_Temperature (°C) 🌡️: Represents temperature near the plant roots.
Soil_pH ⚗️: Reflects the acidity or alkalinity of the soil.
Nitrogen_Level (mg/kg) 🟢, Phosphorus_Level (mg/kg) 🟠, and Potassium_Level (mg/kg) 🟡: Measure nutrient levels critical for plant growth and health.""")
    st.subheader('Environmental Conditions 🌤️:')
    st.image('images/Generated Image (1).jpeg', use_column_width= False, width=200)
    st.text("""Ambient_Temperature (°C) 🌡️: Temperature surrounding the plant.
Humidity (%) 💦: Air humidity levels.
Light_Intensity (Lux) ☀️: Exposure to light, crucial for photosynthesis.
""")
    st.subheader('Plant Health Indicators 🌿:')
    st.image('images/Generated Image (2).jpeg', width=200, use_column_width= False)
    st.text("""Chlorophyll_Content (mg/m²) 🟩: Reflects photosynthetic activity.
Electrochemical_Signal (mV) ⚡: Represents stress signals due to environmental or internal factors.
""")
    st.subheader('Predict values')
    st.text("""Healthy ✅: Optimal plant conditions.
Moderate Stress ⚠️: Minor deviations from ideal conditions.
High Stress ❌: Severe stress requiring immediate intervention.
""")