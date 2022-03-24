from flat import Bill, Flatmate
from pdf_generator import PdfGenerator,FileShare

period = input("Enter the time period of stay e.g March 2020: ")
total_expense = float(input("Enter the total bill for the period of {} :".format(period)))
the_bill = Bill(total_expense=total_expense, period=period)

flatmate1_name = input("Enter the name of the first_flatmate: ")
flatmate1_days_in_house = int(input("Enter the number of days {} spent in the house: ".format(flatmate1_name)))
flatmate2_name = input("Enter the second of the first_flatmate: ")
flatmate2_days_in_house = int(input("Enter the number of days {} spent in the house: ".format(flatmate2_name)))
flatmate1 = Flatmate(flatmate1_name, flatmate1_days_in_house)
flatmate2 = Flatmate(flatmate2_name, flatmate2_days_in_house)

createPDF = PdfGenerator("{}.pdf".format(the_bill.period))
createPDF.generate(flatmate1, flatmate2, the_bill)

fileshare = FileShare(createPDF.filename)
print(fileshare.uploader())