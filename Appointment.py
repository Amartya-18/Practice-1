#APPOINTMENT FILE 
from doctor import Gastroenterologist, Pathologist
from datetime import datetime 
from patient import PatientDetails 

# Creating Doctor Objects 
gastro_doctor = Gastroenterologist("Dr. Sharma")
pathology_doctor = Pathologist("Dr. Mehta")

# GETTING TREATMENT OPTIONS FROM THE DOCTOR'S CLASSES
# The treatment list is already defined in doctor.py.
treatment_options_gastroenterology = Gastroenterologist.provided_treatments
treatment_options_pathology = Pathologist.provided_treatments
# Combining Treatment Options 
treatment_options = treatment_options_gastroenterology + treatment_options_pathology

# FUNCTION TO DISPLAY AND SELECT TREATMENT
# The patient selects a treatment using its number.
def choose_Treatment():
    print("\nAvailable Treatment Options:")
    print("\nGastroenterology:")
    print("1. Acidity")
    print("2. Acid Reflux")
    print("3. Gastric Issues")
    print("4. Bloating")

    print("\nPathology / Diagnostic Tests:")
    print("5. Blood Test")
    print("6. KFT")
    print("7. LFT")
    print("8. CBC")
    print("9. Thyroid Test")

    try:
        selected_treatment_number = int(input("\nEnter Treatment Option Number: "))
        if selected_treatment_number == 1:
            return "Acidity"
        elif selected_treatment_number == 2:
            return "Acid Reflux"
        elif selected_treatment_number == 3:
            return "Gastric Issues"
        elif selected_treatment_number == 4:
            return "Bloating"
        elif selected_treatment_number == 5:
            return "Blood Test"
        elif selected_treatment_number == 6:
            return "KFT"
        elif selected_treatment_number == 7:
            return "LFT"
        elif selected_treatment_number == 8:
            return "CBC"
        elif selected_treatment_number == 9:
            return "Thyroid Test"
        else:
            print("Please enter a valid treatment option number.")
            return None
    except ValueError:
        print("Invalid Selection")
        return None

# Function to Map Treatment to Doctor
def find_Doctor(treatment_required):
    if treatment_required in treatment_options_gastroenterology:
        return gastro_doctor
    elif treatment_required in treatment_options_pathology:
        return pathology_doctor
    else:
        return None

# FUNCTION TO GET APPOINTMENT DATE 
def get_Appointment_date():
    while True:
        try:
            date_input = input("\nEnter Appointment Date (DD-MM-YYYY): ")
            return datetime.strptime(date_input, "%d-%m-%Y")
        except ValueError:
            print("Please enter a valid date in DD-MM-YYYY format.")

# Function to select an appointment slot
# This function expects a doctor object and a valid appointment date.
def select_Appointment_slot(doctor, appointment_date):
    if appointment_date is None:
        print("Please enter a valid date before selecting a slot.")
        return None

    available_slots = doctor.show_Available_slots(appointment_date)
    if not available_slots:
        print("No appointment slots are available.")
        return None

    try:
        selected_slot_number = int(input("\nEnter Appointment Slot Number: "))
        if 1 <= selected_slot_number <= len(available_slots):
            return available_slots[selected_slot_number - 1]
        else:
            print("Please enter a valid appointment slot number.")
            return None
    except ValueError:
        print("Invalid Selection")
        return None
