import streamlit as st
import pickle
import sklearn

st.title("titanic survival prediction")

st.write("This web application will predict  the survival rate of passengers")


model = pickle.load(open("Titanic_Model.pkl",'rb'))

Pclass = st.number_input("input your passenger class, (first class= 1,second class = 2, third class = 3)")
Age = st.number_input("what is the passengers age")
SibSp = st.number_input("Numbers of sibling or spouse")
Parch = st.number_input("Numbers of parent/children on board")
Fare = st.number_input("Amount paid for the ticket")
Sex_male = st.number_input("male = 1 , female = 0")
Embarked_Q = st.number_input("For Q location , input 1 and if not input 0")
Embarked_S = st.number_input("For S location , input 1 and if not input 0")

if st.button('Predict'):
   
   Pred = model.predict([[Pclass, Age, SibSp, Parch, Fare, Sex_male, Embarked_Q, Embarked_S]])
   st.text(f'Passengers survival rate is {Pred[0]}')
   
   st.text("Thank you for using the application")










