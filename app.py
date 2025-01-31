import pandas as pd
import streamlit as st
import joblib

model=joblib.load('xgb_model.jb')
st.title('Project by Saniya Ansari')
st.title('UAE Tourism Expense Prediction')
st.write('Enter details to calculate price.\n')
st.write('Guidelines:\n')
st.write('1)Country: 0-Australia, 1-Canada, 2-China, 3-France, 4-Germany, 5- India, 6-UK, 7-USA\n')
st.write('2)Gender: 0-Female, 1-Male, 2-Other')
st.write('3)Travel Purpose: 0-Business, 1-Education,2-Leisure,3-Medical\n')
st.write('4)Preferred Destination: 0-Adventure Park, 1-Beach, 2-City, 3-Countryside,4-Mountain\n')
st.write('5)Accomodation Type: 0-Airbnb,1-Hostel,2-Hotel,3-Resort\n')
st.write('6)With Family: 0-With Family, 1-Without Family')



input=['Country', 'Age', 'Gender', 'Travel_Purpose', 'Preferred_Destination',
       'Stay_Duration_Days', 'Spending_USD', 'Accommodation_Type',
       'Travel_Frequency_per_Year', 'Average_Spending_Accommodation_USD',
       'Average_Spending_Transport_USD', 'Average_Spending_Food_USD',
       'Average_Cost_Per_Day_AED', 'With_Family', 'Average_Spend',
       'Average_Cost_Per_Day_USD']

input_data={}

for features in input:
    input_data[features] = st.number_input(f"{features}",value=0.0, step=1.0 if features in ['Gender','With_Family','Travel_Purpose','Age'] else 0.1)

if st.button("Predict Price"):
    input_data['With_Family'] =1 if input_data['With_Family'] == "With Family" else 0

    input_df = pd.DataFrame([input_data],columns=input)

    predictions = model.predict(input_df)
    st.success(f"Predicted Budget Per Person: ${predictions[0]:,.2f}")

