# APPOINTMENT SCHEDULING SYSTEM
#  Importing pickle for file handling used for serialization of appointment details. 

import pickle
from patient import PatientDetails
from doctor import DoctorDetails, Gastroenterologist,Pathologist
from appointment import choose_Treatment,find_Doctor,get_Appointment_date,select_Appointment_slot 

# Provide a concrete implementation for the PatientDetails display method.
def display_Patient_Details(self):
    print("\nPATIENT DETAILS")
    print("----------------")
    print("Patient ID:", getattr(self, 'patient_id', 'N/A'))
    print("Patient Name:", self.patient_name)
    print("Age:", self.age)
    print("Gender:", self.gender)
    print("Treatment Required:", self.treatment_required)

PatientDetails.display_Patient_Details = display_Patient_Details

print("\n======================================")
print("APPOINTMENT SCHEDULING SYSTEM")
print("======================================") 

#TAKING PATIENT DETAILS 
patient_name = input("\nEnter Patient Name: ")
age = int(input("Enter Patient Age: "))
gender = input("Enter Gender: ")  

# PATIENT SELECTS TREATMENT 
# choose_Treatment() displays the treatment options and returns the selected treatment.
treatment_required = choose_Treatment() 

# Creating Patient Object 
pat1 = PatientDetails(patient_name,age,gender,treatment_required) 
pat1.display_Patient_Details()     #Displaying Patient Details

# Finding Suitable Doctor 
# The patient's treatment requirement is mapped to the appropriate doctor's speciality.
doctor1 = find_Doctor(pat1.treatment_required) 

# Displaying Doctor Details 
doctor1.display_Doctor_details()  

# Display Doctor Working Hours and Break Time 
doctor1.show_Appointment_timings() 

# Taking Appointment Date 
appointment_date = get_Appointment_date()  # It keeps asking until valid date is entered.

# Displaying Available slots and taking patient's slot selection & returns slot selected by patient.
selected_slot = select_Appointment_slot(doctor1, appointment_date)
if selected_slot is None:
    print("Appointment could not be booked.")
    raise SystemExit

# Starting Time of the selected slot. 
# select_Appointment_slot() returns(start_time, end_time) 
selected_slot = selected_slot[0]

# BOOKING THE APPOINTMENT 
doctor1.book_Appointment(selected_slot)

# Displaying Appointment Confirmation 
print("\n======================================")
print("     APPOINTMENT CONFIRMED"              )
print("======================================"  )

print("Patient ID:",pat1.patient_id)
print("Patient Name:",pat1.patient_name)
print("Age:",pat1.age)
print("Gender:",pat1.gender)
print("Treatment Required:",pat1.treatment_required)

print("Doctor ID:",doctor1.doctor_id)
print("Doctor Name:",doctor1.doctor_name)
print("Treatment Speciality:",doctor1.treatment_speciality)

print("Appointment Date:",selected_slot.strftime("%d-%m-%Y"))
print("Appointment Time:",selected_slot.strftime("%H:%M hrs"))

