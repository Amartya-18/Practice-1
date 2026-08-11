# DOCTOR FILE
# The busy appointment slots are predfined for derived doctor class.
# Importing datetime: This import function is needed for defining the doctor's predefined busy date and time slots. 
from datetime import datetime
# Defining doctordetails base class - The data members mentioned in the base class will also be inherited in the derived class of doctor's sepciality. 

class DoctorDetails:
  doctor_id = 1001     # Class Variable for Auto-Generating Doctor ID 
  # Constructor for Initialising doctor's details 
    def __init__(self,doctor_name,treatment_speciality):
      self.doctor_id = DoctorDetails.doctor_id
      DoctorDetails.doctor_id += 1
      self.doctor_name = doctor_name
      self.treatment_speciality = (treatment_speciality)
      
# Function to display Doctor's Details 
  def display_Doctor_details(self):
     print("\nDoctor Details:" DoctorDetails)
     print("Doctor ID:",self.doctor_id)
     print("Doctor Name:",self.doctor_name)
     print("Treatment Speciality:",self.treatment_speciality) 
    
#Function to check Slot Availibility 
 #If the selected slot is already present in busy_slots,the function returns False, otherwise it returns true. 

def check_Slot_availability(self,selected_slot):  #doing the same work as book_Appointment(need to check once)
    if selcted_slot in self.busy_slots:
      return False
    else:
      return True

# Function to display doctor appointment timings. 
# This displays predfeined working hours and break timings of the doctor. 

def show_Appointment_timings(self):
  print("Appointment Timings : 10:00 hrs - 16:00 hrs")
  print("Break Timings : 13:00 hrs - 14:00 hrs") 

# Function to show available appointment slots . This function uses: 
# 1. Doctor's predefined working hours  2. Doctor's predfined Break time  & 3. Doctor's predefined busy slots 

def show_available_slots(self,appointment_date):
avaialable_slots =[]                  # Creating an empty list where appointments will be stored

# Generating Appointment Slots as per Doctor's predfined working hours. 
 for hour in range(self.appointment_start_time,self.appointment_end_time):
   
# Creating an Appointment Slot - The Selected appointment date is combined with the current working hour. 
appointment_slot = appointment_date.replace(hour=hour,minute=0)

# Checking Whether the stated hour is during break Time 
 if (hour >= self.break_start_time and hour < self.break_end_time):   # Copied Command
        continue
# Displaying Available Appointment Slots

print("\nAvailable Appointment Slots:")

for i in range(len(available_slots)):
print(i + 1,".",
      available_slots[i].strftime
      ("%H:%M hrs")
     )

# Returning the Available Slots
# appointment.py will use this list so that the patient can select one of the displayed slots.
  return available_slots
# Function to Book an appointment 
def book_Appointment(self,selected_slot):

# Checking Whether the Slot is Already Busy
  if selected_slot in self.busy_slots:
      print("This slot is already busy.")
 else:
         self.busy_slots.append(selected_slot)      # Adding the Selected Slot to Busy Slots - Once booked, the slot becomes unavailable. 
     print("Appointment Booked Successfully.")

# DERIVED CLASS - GASTROENTEROLOGIST
# This class represents the Gastroenterology speciality.

class Gastroenterologist(DoctorDetails):
  provided_treatments = ["Acidity","Acid Reflux","Gastric Issues","Bloating"]
# Treatments Handled by Gastroenterologist and the above issues are mapped to gastroenterology speciality. 

def __init__(self,doctor_name):                          # Constructor for Gastroenterologist
   super().__init__(doctor_name,"Gastroenterology")         # Calling Constructor of Parent DoctorDetails Class
# doctor_name comes from object creation.
# Gastroenterology is predefined because this derived class is represented as a speciality.

# Defining Doctor's Working Hours 
  self.appointment_start_time = 10  
  self.appointment_end_time = 16 

# Defining Doctor's Break Time 
  self.break_start_time = 13 
  self.break_end_time = 14 

# Defining Predefined Busy Slots - These are the date & time slots during which gastroenterologist is already occupied. 
#  datetime format : datetime(year, month, day, hour, minute)

 self.busy_slots = [datetime(2026, 8, 10, 11, 0),
                    datetime(2026, 8, 10, 14, 0), 
                    datetime(2026, 8, 11, 15, 0)]

# DERIVED CLASS  - PATHOLOGIST
class Pathologist(DoctorDetails):
   provided_treatments = ["Blood Test","KFT","LFT","CBC","Thyroid Test"]
# Treatments Handled by Pathologists and the mentioned issues are mapped to Pathology speciality. 
def __init__(self,doctor_name):

  # Calling the Constructor of DoctorDetails
 super().__init__(doctor_name,"Pathology")
# Defining Appointment Timings for the derived Gatroenterologist class.  
  self.appointment_start_time = 10  
  self.appointment_end_time = 16 
  self.break_start_time = 13 
  self.break_end_time = 14 

 # Defining Predefined Busy Slots for Pathologist
  self.busy_slots = [ datetime(2026, 8, 10, 10, 0),
                    datetime(2026, 8, 10, 15, 0),
                    datetime(2026, 8, 11, 12, 0)]

