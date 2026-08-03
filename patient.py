# PATIENT FILE
# This file contains the PatientDetails class.
# It stores patient information to select the issue/test for which an appointment is needed.
# Defining the PatientDetails Class 
class PatientDetails:
   patient_id = 1001         # Class Variable for Auto-Generating Patient ID

# Defining the list of treatment requirements 
treatment_required = ["Acidity","Acid Reflux","Gastric Issues","Bloating",
                           "Blood Test","KFT","LFT","CBC","Lipid Profile"]

# Defining the Appointment Time Range
# Patients can book appointments between 10 AM and 4 PM.
appointment_start_time = "10:00 hrs"
appointment_end_time = "16:00 hrs"
break_start_time = "13:00 hrs"
break_end_time = "14:00 hrs"

# Constructor for Initializing Patient Details
# This function has to be called automatically called whenever a new object is created in PatientDetails Case.
# patient_name, age, gender and treatment_required are provided while creating the Patient object.

def __init__(self, patient_name, age, gender,treatment_required):
 PatientDetails.patient_id += 1 
 self.patient_name = patient_name
 self.age = age
 self.gender = gender
 self.treatment_required = treatment_required

# Function to Display Patient Details
def display_Patient_details(self):
  print("Patient Details:" self.patient_details)
  print("Patient ID:",self.patient_id)
  print("Patient Name:",self.patient_name)
  print("Age:",self.age)
  print("Gender:",self.gender)
  print("Treatment Required:",self.treatment_required)

# Function to Display Appointment Timings
# This informs the patient about the appointment slots ( The Break time has also been mentioned above)

 def show_Appointment_timings(self):
    print(Appointment Timings: "10:00 hrs to 16:00 hrs")
    print(Break Timings : "13:00 hrs to 14:00 hrs")


#  Setter Function for Patient Name
 def set_Patient_name(self,patient_name): 
     try: 
         if len(patient_name) == 0:
            raise ValueError("Patient name cannot be empty.")
            self.patient_name = patient_name  
          except ValueError as e:
                print( "Error:",e)

# Setter Function for Patient Age
# This function ensures that the entered age is numeric and greater than zero.
   def set_Age(self,age):
      try:
           age = int(age)
           if age <= 0:
           raise ValueError("Age must be greater than zero.")
           self.age = age
           except (TypeError, ValueError) as e:
            print("Error:",e)
             
