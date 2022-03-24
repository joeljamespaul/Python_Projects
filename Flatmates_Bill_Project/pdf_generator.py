import os
import webbrowser
from filestack import Client
from fpdf import FPDF

current_path = os.getcwd()


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

        # Adding an icon
        pdf.image(name='files/house.png', w=50, h=50)
        # Insert Title
        pdf.set_font(family='Arial', style='B', size=25)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Insert period Label and value
        pdf.set_font(family='Times', style='B', size=18)
        pdf.cell(w=150, h=80, txt="Period: ", border=0)
        pdf.cell(w=150, h=80, txt=bill.period, border=0, align="C", ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=150, h=60, txt=flatmate1.name, border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=150, h=60, txt=str(flatmate1.pays(bill, flatmate2)), border=0, align="C", ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=16)
        pdf.cell(w=150, h=60, txt=flatmate2.name, border=0)
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=150, h=60, txt=str(flatmate2.pays(bill, flatmate1)), border=0, align="C")
        os.chdir('Reports')
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class FileShare:

    def __init__(self, filepath, apikey="AFvlWGbtTT92QIZw5Limbz"):
        self.filepath = filepath
        self.apikey = apikey

    def uploader(self):
        client = Client(self.apikey)

        report_file_link = client.upload(filepath=self.filepath)
        return report_file_link.url
