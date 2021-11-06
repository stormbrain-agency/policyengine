from openfisca_core.model_api import *
from openfisca_us.entities import *
from openfisca_us.tools.general import *


class ccdf_county_cluster(Variable):
    value_type = int
    entity = Household
    label = u"County Cluster for CCDF"
    definition_period = ETERNITY

    def formula(household, period, parameters):
        county = household("county", period).decode_to_str()
        cluster_mapping = parameters(period).benefit.ccdf.county_cluster
        return cluster_mapping[county]
