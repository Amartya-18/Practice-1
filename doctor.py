# DOCTOR FILE
# This file contains the DoctorDetails base class and the derived classes for different doctor specialities.
# The busy appointment slots are predfined for derived doctor class.
# Importing datetime 
from datetime import datetime
# This import function is needed for defining the doctor's predefined busy date and time slots. 
# Defining doctordetails base class - The data members mentioned in the base class 
# will also be inherited in the derived class of doctor's sepciality. 

class DoctorDetails:
  doctor_id = 1001     # Class Variable for Auto-Generating Doctor ID 
    def __init__(self,doctor_name,treatment_speciality,busy_slots):
      self.doctor_id = DoctorDetails.doctor_id
      DoctorDetails.doctor_id += 1
      self.doctor_name = doctor_name
      self.treatment_speciality = (treatment_speciality)
      self.busy_slots = busy_slots
      
# Function to display Doctor's Details 
  def display_Doctor_details(self):
     print("Doctor Details:" DoctorDetails)
     print("Doctor ID:",self.doctor_id)
     print("Doctor Name:",self.doctor_name)
     print("Treatment Speciality:",self.treatment_speciality) 

 def check_Slot_availability(self,selected_slot): 

      if selected_slot == self.busy_slots:
             return False

       else:
             return True

# Function to Book Appointment
  def book_Appointment(self,opted_slot):
  if selected_slot == self.busy_slots:
      print("This slot is already busy.")
  else:
        self.busy_slots != selected_slot
       print("Appointment booked successfully.")

# DERIVED CLASS - GASTROENTEROLOGIST
# This class represents the Gastroenterology speciality.

class Gastroenterologist(DoctorDetails):
  provided_treatments = ["Acidity","Acid Reflux","Gastric Issues","Bloating"]
def __init__(self):

  # DERIVED CLASS  - PATHOLOGIST

class Pathologist(DoctorDetails):
   provided_treatments = ["Blood Test","KFT","LFT","CBC","Thyroid Test"]


