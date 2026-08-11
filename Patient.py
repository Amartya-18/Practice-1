# PATIENT FILE
# This file contains the PatientDetails class.
# It stores patient information about the patient and the treatment required by the patient.

class PatientDetails:
    patient_id = 1001  # Class variable for auto-generating patient ID

    def __init__(self, patient_name, age, gender, treatment_required):
        # Constructor for initializing patient details
        PatientDetails.patient_id += 1
        self.patient_id = PatientDetails.patient_id
        self.patient_name = patient_name
        self.age = age
        self.gender = gender
        self.treatment_required = treatment_required

    # Function to display patient details
    def display_Patient_details(self):
        print("\nPatient Details:")
        print("Patient ID:", self.patient_id)
        print("Patient Name:", self.patient_name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Treatment Required:", self.treatment_required)

    # Setter function for patient name
    def set_Patient_name(self, patient_name):
        try:
            if len(patient_name) == 0:
                raise ValueError("Patient name cannot be empty.")
            self.patient_name = patient_name
        except ValueError as e:
            print("Error:", e)

    # Setter function for patient age
    def set_Age(self, age):
        try:
            age = int(age)
            if age <= 0:
                raise ValueError("Age must be greater than zero.")
            self.age = age
        except (TypeError, ValueError) as e:
            print("Error:", e)
