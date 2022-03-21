from fpdf import FPDF


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

    def pays(self, bill, days_in_house_other_flatmate):
        pay_coefficient = self.days_in_house / (self.days_in_house + days_in_house_other_flatmate)
        pay_share = pay_coefficient * bill.total_expense
        return round(pay_share,3)


class PdfGenerator:
    """
    Creates a PDF report that contains the whole information of the
    tenant/flatmate i.e their names, due payments, their share of the bill
    and the durations of their stay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass


the_bill = Bill(total_expense=2556, period="May 2017")
james = Flatmate("James", 20)
paul = Flatmate("Paul", 30)

print("{} pays {}".format(james.name,james.pays(the_bill, paul.days_in_house)))
print("{} pays {}".format(paul.name,paul.pays(the_bill, james.days_in_house)))

pdf = FPDF()