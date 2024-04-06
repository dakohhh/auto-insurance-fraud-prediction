import streamlit as st


st.title("Insurance Fraud Detection")


with st.form("my_form"):
   
   customers_name_input = st.text_input("What is the customer's name")
   customer_age_input = st.slider("What is the customer's age")

   month_as_customer_input = st.text_input("How many months has the customer been in service")

   policy_deductable_input = st.text_input("Policy Deductable")

   umbrella_limit_input = st.text_input("Umbrella Limit")


   incident_type_input = st.selectbox("What is the incident type",  ("Parked Car", "Single Vehicle Collision", "Vehicle Theft", "Multi-vehicle Collision"))
   collision_type_input  = st.selectbox("What is the collision type",  ("Front Collision", "Rear Collision", "Side Collision"))

   incident_severity_input = st.selectbox("What is the incident severity", ("Major", "Minor"))


   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("month_as_customer", month_as_customer_input, "customer_age", customer_age_input, "customers_name", customers_name_input)