import pickle                #  pickle is used for serialization and deserialization.
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
# Association between Doctor & Patient. 
#  The Patient and Doctor are separate objects, but they interact during the appointment booking process.

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
doctor1.book_Appointment(selected_slot)                      # Asscoiating the selected slot with doctor 

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

appointment_details = 
{
    "Patient ID": pat1.patient_id,
    "Patient Name": pat1.patient_name,
    "Treatment Required": pat1.treatment_required,
    "Doctor ID": doctor1.doctor_id,
    "Doctor Name": doctor1.doctor_name,
    "Treatment Speciality": doctor1.treatment_speciality,
    "Appointment Date": selected_slot.strftime("%d-%m-%Y"),
    "Appointment Time": selected_slot.strftime("%H:%M hrs")
}


# File Handling - Serialization
# The appointment_details dictionary is converted into a storable form and written into appointments.dat.
with open("appointments.dat","ab") as file:          # "a" means append, so previous appointments are not deleted & b means binary.
  pickle.dump(appointment_details,file)
  print("\nAppointment details saved successfully.")
    
# Deserialization 
# The appointments.dat file is opened in binary read mode.
# Each previously stored appointment record is read using pickle.load() and displayed.
print("Saved Appointment Records")

with open("appointments.dat","rb") as file:     # "rb" means read binary
    while True:
        try:
            saved_appointment = pickle.load(file)
    
 # Displaying the Deserialized Appointment

 print("\nPatient ID:",saved_appointment["Patient ID"])
 print("Patient Name:",saved_appointment["Patient Name"])
 print("Treatment Required:",saved_appointment["Treatment Required"])
 
 print("Doctor ID:",saved_appointment["Doctor ID"])
 print("Doctor Name:",saved_appointment["Doctor Name"])
 print("Treatment Speciality:",saved_appointment["Treatment Speciality"])

 print("Appointment Date:",saved_appointment[ "Appointment Date"])
 print("Appointment Time:",saved_appointment["Appointment Time"])

except Error:                       
             break


