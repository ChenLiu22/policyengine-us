from policyengine_us.model_api import *


class taxable_employment_income(Variable):
    value_type = float
    entity = Person
    label = "Taxable employment income"
    unit = USD
    documentation = "Employment income less payroll deductions."
    definition_period = YEAR
    adds = ["employment_income"]
    subtracts = "gov.irs.income.gross_income.pre_tax_contributions"
