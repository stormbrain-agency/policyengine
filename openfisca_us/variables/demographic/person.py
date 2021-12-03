from openfisca_core.model_api import *
from openfisca_us.entities import *


class person_id(Variable):
    value_type = int
    entity = Person
    label = u"Unique reference for this person"
    definition_period = ETERNITY


class people(Variable):
    value_type = float
    entity = Person
    label = u"People represented"
    definition_period = YEAR
    default_value = 1.0


class person_weight(Variable):
    value_type = float
    entity = Person
    label = u"Person weight"
    definition_period = YEAR


class age(Variable):
    value_type = float
    entity = Person
    label = u"Age"
    definition_period = YEAR


class AgeGroup(Enum):
    CHILD = "Child"
    WORKING_AGE = "Working-age"
    SENIOR = "Senior"


class age_group(Variable):
    value_type = Enum
    possible_values = AgeGroup
    default_value = AgeGroup.WORKING_AGE
    entity = Person
    label = u"Age group"
    definition_period = YEAR

    def formula(person, period, parameters):
        return select(
            [
                person("is_child", period),
                person("is_wa_adult", period),
                person("is_senior", period),
            ],
            [AgeGroup.CHILD, AgeGroup.WORKING_AGE, AgeGroup.SENIOR],
        )


class is_child(Variable):
    value_type = bool
    entity = Person
    label = u"Is a child"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("age", period) < 18


class is_wa_adult(Variable):
    value_type = bool
    entity = Person
    label = u"Is a working-age adult"
    definition_period = YEAR

    def formula(person, period, parameters):
        age = person("age", period)
        return (age >= 18) & (age < 65)


class is_senior(Variable):
    value_type = bool
    entity = Person
    label = u"Is a senior"
    definition_period = YEAR

    def formula(person, period, parameters):
        return person("age", period) >= 65


class is_citizen(Variable):
    value_type = bool
    entity = Person
    label = u"Is a U.S. citizen"
    definition_period = YEAR