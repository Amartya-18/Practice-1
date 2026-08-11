from patient import PatientDetails
from appointment import 
(
    choose_Treatment,
    find_Doctor,
    get_Appointment_date
)

print("\n======================================")
print("Appointment Scheduling System")
print( "======================================")

# Taking Patient Details 
patient_name = input("\nEnter Patient Name: ")
age = int(input("Enter Patient Age: "))
gender = input("Enter Gender: ")

# Patient Selects Treatment 
treatment_required = choose_Treatment()

# Creating a Patient Object 
pat1 = PatientDetails
(
    patient_name,
    age,
    gender,
    treatment_required
)

pat1.display_Patient_details()         # Diplay Patient Details 

# Finding Suitable Doctor 
doctor1 = find_Doctor(pat1.treatment_required)
# Display Doctor Details 
doctor1.display_Doctor_details()       

# Display Doctor's Working hours and break time 
doctor1.show_Appointment_timings()

# Taking Appointment Date
appointment_date = get_Appointment_date()

# Displaying Available Appointment Slots 
available_slots = doctor1.show_Available_slots(appointment_date)

# Taking Appointment Slot Number from the Patient 
selected_slot_number = int(input("\nEnter Appointment Slot Number: "))

# Getting the Appintment Slot 
selected_slot = available_slots[selected_slot_number - 1]

# Booking the Appointment 
doctor1.book_Appointment(selected_slot)

# Displaying Appointment Confirmation 
print("\nAppointment Confirmed")
print("Patient ID:",pat1.patient_id)
print("Patient Name:",pat1.patient_name)
print("Treatment Required:",pat1.treatment_required)

print("Doctor Name:",doctor1.doctor_name)
print("Treatment Speciality:",doctor1.treatment_speciality)

print("Appointment Date:",selected_slot.strftime
      ("%d-%m-%Y") 
     )

print("Appointment Time:",selected_slot.strftime
      ("%H:%M hrs")
      )




