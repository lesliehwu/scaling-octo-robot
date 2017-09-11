from random import randint

class Patient(object):
    def __init__(self,idn,name,allergies):
        self.idn = idn
        self.name = name
        self.allergies = allergies
        self.bedn = None

class Hospital(object):
    def __init__(self,patients,name,capacity):
        self.patients = patients
        self.name = name
        self.capacity = capacity

    def admit(self,patient):
        if len(self.patients) >= self.capacity:
            print "Hospital is full"
        else:
            self.patients.append(patient)
            patient.bedn = randint(1,500)
            print "Patient added"
        return self
        
    def discharge(self,patient_idn):
        for patient in self.patients:
            if patient.idn == patient_idn:
                self.patients.remove(patient)
                patient.bedn = None

sadie = Patient(1,"sadie","baths")
brownie = Patient(2,"brownie","hunger")
deedle = Patient(3,"deedle","leedle")
my_list = []

lhopital = Hospital(my_list,"lhopital",5)
lhopital.admit(sadie).admit(brownie).admit(deedle).discharge(3)
print my_list[0]
print my_list[1]
