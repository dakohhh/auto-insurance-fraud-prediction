from typing import Any
import joblib
from sklearn.svm import SVC
import numpy as np
import streamlit as st


model: SVC = joblib.load("insurace_fraud_model_SVC_Ignaz.pkl")


def construct_input(
    month_as_customer_input,
    customer_age_input,
    policy_state_input,
    policy_deductable_input,
    umbrella_limit_input,
    incident_type_input,
    collision_type_input,
    incident_severity_input,
    authorities_contacted_input,
    number_vehicles_invloved,
    property_damage_input,
    bodily_injuries,
    witnesses_input,
    police_report_input,
    total_claim_amount_input,
    property_claim_input,
):

    return np.array(
        [
            [
                month_as_customer_input,
                customer_age_input,
                policy_state_input,
                policy_deductable_input,
                umbrella_limit_input,
                incident_type_input,
                collision_type_input,
                incident_severity_input,
                authorities_contacted_input,
                number_vehicles_invloved,
                property_damage_input,
                bodily_injuries,
                witnesses_input,
                police_report_input,
                total_claim_amount_input,
                property_claim_input,
            ]
        ]
    )


def incident_type_to_value(choice: Any):

    choices = {
        "Parked Car": 1,
        "Single Vehicle Collision": 2,
        "Vehicle Theft": 3,
        "Multi-vehicle Collision": 0,
    }

    return choices[choice]


def collision_type_to_value(choice: Any):

    choices = {
        "Front Collision": 0,
        "Rear Collision": 1,
        "Side Collision": 2,
    }

    return choices[choice]


def incidcent_severity_to_value(choice: Any):

    choices = {"Major": 0, "Minor": 1, "Total Loss": 2, "Trivial Damage": 3}

    return choices[choice]


def authorities_contacted_to_value(choice: Any):

    choices = {"Ambulance": 0, "Fire": 1, "Other": 2, "Police": 3}

    return choices[choice]


def property_damage_to_value(choice: Any):

    choices = {"No": 0, "Yes": 1}
    return choices[choice]


def police_report_to_value(choice: Any):

    choices = {"No": 0, "Yes": 1}
    return choices[choice]


def policy_state_to_value(choice: Any):

    choices = {"OH": 2, "IL": 0, "IN": 1}

    return choices[choice]


st.set_page_config(page_title="Insurance claim Fraud Detection")

st.title("Insurance Fraud Detection")


with st.form("my_form"):

    customers_name_input = st.text_input("What is the customer's name")

    customer_age_input = st.slider("What is the customer's age")

    month_as_customer_input = st.number_input(
        "How many months has the customer been in service"
    )

    policay_state_input = st.selectbox(
        "What is the policy state",
        (
            "OH",
            "IL",
            "IN",
        ),
    )

    policy_deductable_input = st.number_input("Policy Deductable")

    umbrella_limit_input = st.number_input("Umbrella Limit")

    incident_type_input = st.selectbox(
        "What is the incident type",
        (
            "Parked Car",
            "Single Vehicle Collision",
            "Vehicle Theft",
            "Multi-vehicle Collision",
        ),
    )

    collision_type_input = st.selectbox(
        "What is the collision type",
        ("Front Collision", "Rear Collision", "Side Collision"),
    )

    incident_severity_input = st.selectbox(
        "What is the incident severity",
        ("Major", "Minor", "Total Loss", "Trivial Damage"),
    )

    authorities_contacted_input = st.selectbox(
        "What Authority was contacted", ("Ambulance", "Fire", "Other", "Police")
    )

    number_vehicles_invloved = st.number_input(
        "How many vehicles were involved", min_value=1, max_value=4
    )

    property_damage_input = st.radio("Were they Property Damage", ("No", "Yes"))

    bodily_injuries = st.number_input("Bodily Injuries", min_value=0, max_value=2)

    witnesses_input = st.number_input("How many witnesses", min_value=0, max_value=3)

    police_report_input = st.radio("Was a police report made", ("No", "Yes"))

    total_claim_amount_input = st.number_input("What is the total claim amount")

    property_claim_input = st.number_input("What is the property claim amount")

    submitted = st.form_submit_button("Submit")
    if submitted:
        is_insurance_fraud = model.predict(
            construct_input(
                month_as_customer_input,
                customer_age_input,
                policy_state_to_value(policay_state_input),
                policy_deductable_input,
                umbrella_limit_input,
                incident_type_to_value(incident_type_input),
                collision_type_to_value(collision_type_input),
                incidcent_severity_to_value(incident_severity_input),
                authorities_contacted_to_value(authorities_contacted_input),
                number_vehicles_invloved,
                property_damage_to_value(property_damage_input),
                bodily_injuries,
                witnesses_input,
                police_report_to_value(police_report_input),
                total_claim_amount_input,
                property_claim_input,
            )
        )

        print(is_insurance_fraud)

        if is_insurance_fraud[0] == 1:
        
            st.error(f"The system has deteted fraud in {customers_name_input}'s insurance claim")

        else:
            st.success(f"The system did not detect fraud in {customers_name_input}'s insurance claim")

