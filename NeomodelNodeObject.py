#pip install neomodel
from neomodel import (StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo)

# Class Template for using neomodel

class Disease(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    environment = StringProperty(required=True)
    affectfish = StringProperty()
    cause = StringProperty()
    treatment = StringProperty()
    vet_advised = StringProperty()
    aka = RelationshipTo('AKA', 'AKA')
    symptoms = RelationshipTo('Symptom', 'hasSymptom')
    medications = RelationshipTo('Medication', 'useMedication')

class Symptom(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    diseases = RelationshipTo('Disease', 'isDetectedIn')    

class AKA(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    # disease = RelationshipTo(Disease, 'AKA') << Future

class Medication(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    diseases = RelationshipTo('Disease', 'knownTreatment')