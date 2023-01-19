from policyengine_us.model_api import *


class flat_tax(Variable):
    value_type = float
    entity = TaxUnit
    label = "Flat tax"
    unit = USD
    documentation = "Flat income tax on federal AGI."
    definition_period = YEAR

    def formula(tax_unit, period, parameters):
        agi = tax_unit("positive_agi", period)
        p = parameters(period).gov.contrib.ubi_center.flat_tax
        return p.rate * agi
