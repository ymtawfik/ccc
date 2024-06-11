import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import os

# Load the dataset
file_path = "cereal.csv"  # Use the correct path relative to the script's location

if not os.path.isfile(file_path):
    st.error(f"File not found: {file_path}. Please make sure the file exists.")
else:
    data = pd.read_csv(file_path)

    # Prepare the data
    X = data[['calories', 'protein', 'fat', 'sodium', 'fiber', 'carbo', 'sugars', 'potass', 'vitamins', 'shelf', 'weight', 'cups']]
    y = data['rating']

    # Train the model
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X, y)

    # Streamlit app
    st.title('Cereal Rating Predictor')

    # Display the image
    image_path = "ceraalll.png"  # Path to the image

    if os.path.isfile(image_path):
        st.image(image_path, caption='A bowl of colorful cereal', use_column_width=True)
    else:
        st.warning(f"Image file not found: {image_path}")

    st.write("""
    ### Predict the rating of a cereal based on its nutritional information.
    """)

    # User input
    calories = st.number_input('Calories', min_value=0, value=70)
    protein = st.number_input('Protein', min_value=0, value=4)
    fat = st.number_input('Fat', min_value=0, value=1)
    sodium = st.number_input('Sodium', min_value=0, value=130)
    fiber = st.number_input('Fiber', min_value=0.0, value=10.0)
    carbo = st.number_input('Carbohydrates', min_value=0.0, value=5.0)
    sugars = st.number_input('Sugars', min_value=0, value=6)
    potass = st.number_input('Potassium', min_value=-1, value=280)
    vitamins = st.number_input('Vitamins', min_value=0, value=25)
    shelf = st.number_input('Shelf', min_value=1, value=3)
    weight = st.number_input('Weight (oz)', min_value=0.0, value=1.0)
    cups = st.number_input('Cups', min_value=0.0, value=0.33)

    # Prediction
    input_data = pd.DataFrame({
        'calories': [calories],
        'protein': [protein],
        'fat': [fat],
        'sodium': [sodium],
        'fiber': [fiber],
        'carbo': [carbo],
        'sugars': [sugars],
        'potass': [potass],
        'vitamins': [vitamins],
        'shelf': [shelf],
        'weight': [weight],
        'cups': [cups]
    })

    prediction = model.predict(input_data)[0]
    st.write(f'Predicted Rating: {prediction:.2f}')
