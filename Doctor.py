#DOCTOR FILE
# Importing datetime and timedelta
from datetime import datetime, timedelta


class DoctorDetails:     # Defining DoctorDetails Base Class
  doctor_id = 1001        # Class Variable for Auto-Generating Doctor ID

  # CONSTRUCTOR FOR INITIALISING DOCTOR DETAILS
  def __init__(self, doctor_name, treatment_speciality):
    self.doctor_id = DoctorDetails.doctor_id  # Assigning current Doctor ID to the object
    DoctorDetails.doctor_id += 1              # Increasing ID for the next Doctor object
    self.doctor_name = doctor_name            # Storing Doctor Name & Speciality
    self.treatment_speciality = treatment_speciality

  # FUNCTION TO DISPLAY DOCTOR DETAILS
  def display_Doctor_details(self):
    print("\nDoctor Details:")
    print("Doctor ID:", self.doctor_id)
    print("Doctor Name:", self.doctor_name)
    print("Treatment Speciality:", self.treatment_speciality)

  # FUNCTION TO DISPLAY DOCTOR APPOINTMENT TIMINGS
  def show_Appointment_timings(self):
    print("\nAppointment Timings: 10:00 hrs - 16:00 hrs")
    print("Break Timings: 13:00 hrs - 14:00 hrs")

  # FUNCTION TO CHECK SLOT AVAILABILITY
  def check_Slot_availability(self, slot_time):
    return slot_time not in self.busy_slots

  # FUNCTION TO SHOW AVAILABLE APPOINTMENT SLOTS.
  # Each Appointment slot is of 30 minutes.
  # Working Hours: 10:00hrs - 16:00 hrs & Break: 13:00 hrs-14:00 hrs
  # Predefined busy slots are removed.
  def show_Available_slots(self, appointment_date):
    if appointment_date is None:
      print("Please enter a valid appointment date before checking slots.")
      return []

    available_slots = []

    # Setting the first slot to the doctor's start time
    current_slot = appointment_date.replace(hour=self.appointment_start_time, minute=0)
    # Setting the final working time of the doctor
    end_time = appointment_date.replace(hour=self.appointment_end_time, minute=0)

    # Generating 30-minutes appointment slots.
    while current_slot < end_time:
      # Here current time is the appointment slot which is dynamic until doctor's last working hour.
      slot_end = current_slot + timedelta(minutes=30)

      # Checking Whether Current Slot Falls During the Doctor's Break Time.
      if (current_slot.hour >= self.break_start_time and current_slot.hour < self.break_end_time):
        # Move to the next 30-minute slot
        current_slot = current_slot + timedelta(minutes=30)
        continue

      # Checking Whether Doctor is Already Busy
      if self.check_Slot_availability(current_slot):
        # Add free slot to available_slots
        available_slots.append((current_slot, slot_end))

      # Move to the Next 30-Minute Slot
      current_slot = current_slot + timedelta(minutes=30)

    # Displaying Available Appointment Slots
    print("\nAvailable Appointment Slots:")
    for i in range(len(available_slots)):
      print(i + 1, ".", available_slots[i][0].strftime("%H:%M"),
            "-", available_slots[i][1].strftime("%H:%M hrs"))

    return available_slots

  # FUNCTION TO BOOK AN APPOINTMENT
  def book_Appointment(self, selected_slot):
    # Checking if selected Slot is already busy
    if selected_slot in self.busy_slots:
      print("This slot is already busy")
    else:
      self.busy_slots.append(selected_slot)     # Add the newly booked slot to busy_slots
      print("Appointment Booked Successfully")


# DERIVED CLASS - GASTROENTEROLOGIST
class Gastroenterologist(DoctorDetails):
  provided_treatments = ["Acidity", "Acid Reflux", "Gastric Issues", "Bloating"]

  def __init__(self, doctor_name):
    super().__init__(doctor_name, "Gastroenterology")  # Calling the constructor of the parent class

    # Doctor's Working Hours & Break time
    self.appointment_start_time = 10
    self.appointment_end_time = 16
    self.break_start_time = 13
    self.break_end_time = 14

    # Predefined Busy Appointment Slots
    self.busy_slots = [datetime(2026, 8, 10, 11, 0), datetime(2026, 8, 10, 14, 0),
              datetime(2026, 8, 11, 15, 0)
              ]


# DERIVED CLASS - PATHOLOGIST
class Pathologist(DoctorDetails):
  provided_treatments = ["Blood Test", "KFT", "LFT", "CBC", "Thyroid Test"]

  def __init__(self, doctor_name):
    super().__init__(doctor_name, "Pathology")

    # Doctor's Working Hours & Break time
    self.appointment_start_time = 10
    self.appointment_end_time = 16
    self.break_start_time = 13
    self.break_end_time = 14

    # Predefined Busy Appointment Slots
    self.busy_slots = [datetime(2026, 8, 10, 10, 0), datetime(2026, 8, 10, 15, 0),
              datetime(2026, 8, 11, 12, 0)
              ]
