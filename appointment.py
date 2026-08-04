from patient import PatientDetails
from doctor import Gastroenterologist, Pathologist
from datetime import datetime

# Creating Objects of derived Doctor Classes
gastro_doctor = Gastroenterologist("Dr. Sharma")
pathology_doctor = Pathologist("Dr. Mehta")

# Getting Treatment options from the Doctor Classes
treatment_options_gastroenterology = (Gastroenterologist.handled_treatments)
treatment_options_pathology = (Pathologist.handled_treatments)

# Combining Treatment Options of Both Specialities
treatment_options = (treatment_options_gastroenterology+treatment_options_pathology) 

# Function to display and select treatment required 
def choose_Treatment():
    print("\nAvailable Treatment Requirements:")
  for treatment in treatment_options:
      print(treatment)
  treatment_required = input("\nEnter Treatment Required: ")

    if treatment_required in treatment_options:
         return treatment_required
   else:
          print("Please enter a valid treatment.")
          return None
       
# Mapping Treatment & Doctor Speciality 
def find_Doctor(treatment_required):
   if treatment_required in treatment_options_gastroenterology:
         return gastro_doctor
      elif treatment_required in treatment_options_pathology:
           return pathology_doctor
 else:
       return None

# Function to get appointment date 

def get_Appointment_date():
 try:
       date_input = input("\nEnter Appointment Date (DD-MM-YYYY):")
       appointment_date = datetime.strptime(date_input,"%d-%m-%Y")
       return appointment_date
except ValueError:
      print("Please enter a valid date in DD-MM-YYYY format.")
      return None

# Functions to find available time slots 

def find_Available_slots(doctor,appointment_date):  #need to call slots_availability method from doctor class
      available_slots = [] 

# Checking Whether the Doctor is Busy ----> no need for this as we are already checking available slots in find_Available_slots method

# FUNCTION TO DISPLAY AND SELECT APPOINTMENT SLOT  ------> no need to display as we are going to do it in slots_availability method in doctor class

  
