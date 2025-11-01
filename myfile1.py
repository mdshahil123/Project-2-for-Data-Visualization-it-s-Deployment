import pickle
import streamlit as st

model2=pickle.load(open("areaprice2.pkl","rb"))


def mydeploy():
    st.title("Area Price Predictions")
    Area=st.number_input("Enter the Value of Area")
    Bedrooms=st.number_input("Enter the Value of bedrooms")
    Age=st.number_input("Enter the Value of age")
    pred=st.button("Predict")

    if pred:
        x=model2.predict([[Area,Bedrooms,Age]])
        st.write("The price is :",x[0])






mydeploy()