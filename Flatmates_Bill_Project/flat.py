"""
    Contains Bill class which initiates the period and total_expenses and also has Flatmate class which calculates
    the total due for each flatmate.
"""


class Bill:
    """
        The Bill class creates an object for
         initializing the total_expense and the exact month & Year of stay (March 2020).
    """

    def __init__(self, total_expense, period):
        self.period = period
        self.total_expense = total_expense


class Flatmate:
    """
        This class creates a Flatmate object that contains
        the details of the tenant/flatmate i.e the name,
        number_of_days_stayed and
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        pay_coefficient = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        pay_share = pay_coefficient * bill.total_expense
        return round(pay_share, 3)
