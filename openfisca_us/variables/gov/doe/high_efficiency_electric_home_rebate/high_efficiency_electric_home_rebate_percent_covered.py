from openfisca_us.model_api import *


class high_efficiency_electric_home_rebate_percent_covered(Variable):
    value_type = float
    entity = Household
    label = "Percent of expenditures covered by high electricity home rebate"
    definition_period = YEAR
    unit = USD

    def formula(household, period, parameters):
        income_ami_ratio = household("household_income_ami_ratio", period)
        p = parameters(period).gov.doe.high_efficiency_electric_home_rebate
        return p.percent_covered.calc(income_ami_ratio)
