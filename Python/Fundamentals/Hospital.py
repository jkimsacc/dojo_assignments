class Patient(object):
    """docstring forPatient."""
    def __init__(self, id_number, name, allergies, bed = None):
        self.id_number = id_number
        self.name = name
        self.allergies = allergies
        self.bed = bed

class Hospital(object):
    """docstring forHospital."""
    def __init__(self, hospital_name, capacity, patients =[]):
        self.patients = patients
        self.hospital_name = hospital_name
        self.capacity = capacity

    def admit(self, patient):
        self.patients.append(patient)
        if len(self.patients) <= 100:
            patient.bed = len(self.patients)
        print "admitted", patient
        return self

    def discharge(self, patient):
        self.patients.remove(patient)
        patient.bed = None
        print "discharged"
        return self



hospital1 = Hospital("St.Joseph", 100)
joseph = Patient(123123,"Joseph", "idiots")
# print hospital1.hospital_name, hospital1.capacity
# print joseph.name
# print hospital1.admit(joseph).patients[0].bed
hospital1.admit(joseph).admit(joseph).discharge(joseph)
