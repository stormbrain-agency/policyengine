from openfisca_core.model_api import *
from openfisca_us.entities import *
from openfisca_us.tools.general import *


class is_usda_elderly(Variable):
    value_type = bool
    entity = Person
    definition_period = YEAR
    documentation = "Is elderly per USDA guidelines"
    label = "USDA elderly"

    def formula(person, period, parameters):
        elderly_age_threshold = parameters(period).usda.elderly_age_threshold
        return person("age", period) >= elderly_age_threshold