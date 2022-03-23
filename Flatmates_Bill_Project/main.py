import webbrowser
import os

from fpdf import FPDF

current_path = os.getcwd()

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


class PdfGenerator:
    """
    Creates a PDF report that contains the whole information of the
    tenant/flatmate i.e their names, due payments, their share of the bill
    and the durations of their stay.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        # Initialize FPDF method and add a page

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Adding an icon
        pdf.image(name='house.png', w=50, h=50)
        # Insert Title
        pdf.set_font(family='Arial', style='B', size=25)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert period Label and value
        pdf.set_font(family='Times', style='B',size=18)
        pdf.cell(w=150, h=80, txt="Period: ", border=0)
        pdf.cell(w=150, h=80, txt=bill.period, border=0, align="C", ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=150, h=60, txt=flatmate1.name, border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=150, h=60, txt=str(flatmate1.pays(bill, paul)), border=0, align="C", ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=150, h=60, txt=flatmate2.name, border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=150, h=60, txt=str(flatmate2.pays(bill, james)), border=0, align="C")

        pdf.output(self.filename)
        webbrowser.open(current_path+'\\'+self.filename)


the_bill = Bill(total_expense=2556, period="May 2017")
james = Flatmate("James", 20)
paul = Flatmate("Paul", 30)


createPDF = PdfGenerator(filename="Report.pdf")
createPDF.generate(james, paul, the_bill)
