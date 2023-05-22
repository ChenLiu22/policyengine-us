from policyengine_us.model_api import *


class nj_property_tax_deduction_or_credit_eligible(Variable):
    value_type = bool
    entity = TaxUnit
    label = "New Jersey property tax credit eligibility"
    unit = USD
    definition_period = YEAR
    defined_for = StateCode.NJ

    def formula(tax_unit, period, parameters):
        # Same as deduction eligibility, but also eligible if 65+ or blind/disabled.
        deduction_eligibility = tax_unit(
            "nj_property_tax_deduction_eligible", period
        )

        # If filing jointly, only one spouse needs to be 65+ or blind/disabled.
        blind_head = tax_unit("blind_head", period)
        disabled_head = tax_unit("disabled_head", period)
        blind_spouse = tax_unit("blind_spouse", period)
        disabled_spouse = tax_unit("disabled_spouse", period)
        senior_head = tax_unit("age_head", period) > 65
        senior_spouse = tax_unit("age_spouse", period) > 65
        senior_blind_disabled = (
            blind_head
            + disabled_head
            + blind_spouse
            + disabled_spouse
            + senior_head
            + senior_spouse
        ) > 0

        return deduction_eligibility | senior_blind_disabled
