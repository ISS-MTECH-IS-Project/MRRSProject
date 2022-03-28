#pip install neomodel
from neomodel import (StructuredNode, ArrayProperty, UniqueIdProperty, StringProperty, FloatProperty, StructuredRel, Relationship,
                      RelationshipTo, RelationshipFrom)

# Class Template for using neomodel


class HasSymptomRel(StructuredRel):
    name = StringProperty()
    weight = FloatProperty(
        default=1.0
    )
    penalty = FloatProperty(
        default=-0.2
    )


class DetectedInRel(StructuredRel):
    name = StringProperty()
    weight = FloatProperty(
        default=1.0
    )


class SuspectedSymptomRel(StructuredRel):
    name = StringProperty()
    suspectedLevel = FloatProperty(
        default=1.0
    )


class SuspectedDiseaseRel(StructuredRel):
    name = StringProperty()
    confidence = FloatProperty(
        default=0.0
    )


class IsSuspectedInCase(StructuredRel):
    name = StringProperty()


class Disease(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    environment = StringProperty()
    affectfish = StringProperty()
    cause = StringProperty()
    treatment = StringProperty()
    vet_advised = StringProperty()

    aka = RelationshipTo('AKA', 'AKA')
    symptoms = RelationshipTo('Symptom', 'hasSymptom', model=HasSymptomRel)
    medications = RelationshipTo('Medication', 'useMedication')


class Symptom(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    description = StringProperty()
    type = StringProperty()
    tm_token = ArrayProperty()
    category1 = StringProperty()
    category2 = StringProperty()
    category3 = StringProperty()
    imageurl = StringProperty()
    question = StringProperty()
    # confidence <= removing this as topic modelling can return dict(name:confidence)and inflate from there when required
    diseases = RelationshipTo('Disease', 'isDetectedIn', model=DetectedInRel)


class AKA(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    # disease = RelationshipTo(Disease, 'AKA') << Future


class Medication(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    vet_or_OTC = StringProperty()
    description = StringProperty(required=True)
    treatment_desc = StringProperty()
    complicate_fish = StringProperty()
    danger_human = StringProperty()
    danger_plant = StringProperty()
    danger_invertebrates = StringProperty()
    diseases = RelationshipTo('Disease', 'knownTreatment')


class CaseInc(StructuredNode):
    name = StringProperty(required=True)
    case_chathistory = ArrayProperty()
    case_token = ArrayProperty()
    suspected_symptoms = RelationshipTo('Symptom', 'suspectedSymptom', model=SuspectedSymptomRel)
    suspected_diseases = RelationshipTo('Disease', 'suspectedDisease', model=SuspectedDiseaseRel)