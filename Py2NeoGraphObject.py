from py2neo.ogm import (Model, Label, Property, RelatedTo, RelatedFrom)


class Disease(Model):
    __primarykey__ = "name"
    name = Property()
    environment = Property()
    affectfish = Property()
    cause = Property()
    treatment = Property()
    vet_advised = Property()

    alsoknownas = RelatedTo("AKA", "AKA")
    symptoms = RelatedTo("Symptom", "hasSymptom")
    medications = RelatedTo('Medication', 'useMedication')


class AKA(Model):
    name = Property()
    alsoknownas = RelatedFrom(Disease)
    # disease = Related(Disease, 'AKA') << Future


class Symptom(Model):
    name = Property()
    diseases = RelatedTo('Disease', 'isDetectedIn')


class Medication(Model):
    name = Property()
    diseases = RelatedTo('Disease', 'knownTreatment')
