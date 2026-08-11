# Appointment File
# This file connects the Patient and Doctor classes.
from patient import PatientDetails                      # Importing Patient Details from patient.py
from doctor import Gastroenterologist, Pathologist      # Importing the derived doctor classes from doctor.py
from datetime import datetime                           # Importing date and time for Appointment date

# Creating Objects of derived Doctor Classes
gastro_doctor = Gastroenterologist("Dr. Sharma")
pathology_doctor = Pathologist("Dr. Mehta")

# Getting Treatment options from the Doctor Classes
treatment_options_gastroenterology = (Gastroenterologist.provided_treatments)
treatment_options_pathology = (Pathologist.provided_treatments)

# Combining Treatment Options of Both Specialities
treatment_options = (treatment_options_gastroenterology+treatment_options_pathology)

# Function to display and select treatment required 
def choose_Treatment():
    print("\nAvailable Treatment Requirements:")
  
for treatment in treatment_options:
      print(treatment)
  treatment_required = input("\nEnter Treatment Required: ")

 # Checking Whether Entered Treatment Exists in the List
    if treatment_required in treatment_options:
         return treatment_required
   else:
          print("Please enter a valid treatment.")
          return None

# Function to map a treatment to doctor 
def find_Doctor(treatment_required):
   if treatment_required in treatment_options_gastroenterology:           # Checking Gastroenterology Treatments
         return gastro_doctor
      elif treatment_required in treatment_options_pathology:             # Checking Pathology Treatments
           return pathology_doctor
 else:
       return None                                                        # In case no matching doctor is found. 

# Function to get appointment date 
def get_Appointment_date():
 try:
       date_input = input("\nEnter Appointment Date (DD-MM-YYYY):")
  # Converting String into datetime Object
       appointment_date = datetime.strptime
      (date_input,"%d-%m-%Y")
       return appointment_date
except ValueError:
      print("Please enter a valid date in DD-MM-YYYY format.")
      return None
# Function to display and select Appointment Slot -The Doctor class calculates the available slots.
# This function only handles the patient's selection.

def choose_Appointment_slot(doctor,appointment_date):
    
# Asking the Selected Doctor for Available Slots
available_slots = doctor.show_Available_slots(appointment_date)

# Checking Whether Any Slots are Available
  if len(available_slots) == 0:
      return None
# Taking Appointment Slot Number from Patient
try:
      selected_slot_number = int(input("\nEnter Appointment Slot Number: "))
# Checking Whether the Entered Number is Valid
    if ( 
       selected_slot_number >= 1
        and selected_slot_number <= len(available_slots)
        ):
# Converting Patient's Number into List Index 
 selcted_slot = available_slots[selected_slot_number - 1]
  return selected_slot
 
 except ValueError:
          print("Please enter a valid number.")
          return None
