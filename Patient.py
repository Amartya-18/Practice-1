# PATIENT FILE
# This file contains the PatientDetails class.
# It stores patient information  about the patient and the treatment required by the patient. 
# Defining the PatientDetails Class 
class PatientDetails:
   patient_id = 1001         # Class Variable for Auto-Generating Patient ID

def __init__(self, patient_name, age, gender,treatment_required):    # Constructor for Initializing Patient Details
# This function (parameterized constructor) has to be called automatically called 
# whenever a new object is created in PatientDetails Class.

# Patient_name, age, gender and treatment_required are provided while creating the Patient object.
 PatientDetails.patient_id += 1 
 self.patient_name = patient_name
 self.age = age
 self.gender = gender
 self.treatment_required = treatment_required

# Functions to Display Patient Details
def display_Patient_details(self):
  print("\n Patient Details:" self.patient_details)
  print("Patient ID:",self.patient_id)
  print("Patient Name:",self.patient_name)
  print("Age:",self.age)
  print("Gender:",self.gender)
  print("Treatment Required:",self.treatment_required)

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

# Setter Function for Patient Age 
 # This function ensures that age is numeric and greater than zero.

def set_Age(self,age):
   try:
         age = int(age)
         if age <= 0:
              raise ValueError("Age must be greater than zero.")
               self.age = age
    except (TypeError, ValueError) as e:
           print("Error:",e)
