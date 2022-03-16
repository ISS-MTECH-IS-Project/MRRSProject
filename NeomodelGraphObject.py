#pip install neomodel
from neomodel import (StructuredNode, StringProperty, FloatProperty, StructuredRel, Relationship, RelationshipTo)

# Class Template for using neomodel


class HasSymptomRel(StructuredRel):
    weight = FloatProperty(
        default=1.0
    )
    penalty = FloatProperty(
        default=-0.2
    )


class DetectedInRel(StructuredRel):
    weight = FloatProperty(
        default=1.0
    )


class SuspectedSymptomRel(StructuredRel):
    suspectedLevel = FloatProperty(
        default=1.0
    )


class SuspectedDiseaseRel(StructuredRel):
    confidence = FloatProperty(
        default=1.0
    )


class Disease(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    environment = StringProperty(required=True)
    affectfish = StringProperty()
    cause = StringProperty()
    treatment = StringProperty()
    vet_advised = StringProperty()

    aka = RelationshipTo('AKA', 'AKA')
    symptoms = RelationshipTo('Symptom', 'hasSymptom', model=HasSymptomRel)
    medications = Relationship('Medication', 'useMedication')


class Symptom(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    imageURL = StringProperty()
    question = None
    diseases = RelationshipTo('Disease', 'isDetectedIn', model=DetectedInRel)


class AKA(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    # disease = RelationshipTo(Disease, 'AKA') << Future


class Medication(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    diseases = Relationship('Disease', 'knownTreatment')


class Case(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    suspected_symptoms = RelationshipTo('Symptom', 'suspectedSymptom', model=SuspectedSymptomRel)
    suspected_diseases = RelationshipTo('Symptom', 'suspectedDisease', model=SuspectedDiseaseRel)