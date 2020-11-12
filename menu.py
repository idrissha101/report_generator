import xlrd
import os
import pandas as pd
from datetime import date
from dataframe import outputFiles
from images import getImages
from cyclecount_pareto import pareto
import sys

def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

def header():
	print("""====================================================================================================================\n\n
  ___ ___ _____   ___ _____  _______ _   _ ___ ___ 
 |_ _/ __|_   _| | __|_ _\ \/ |_   _| | | | _ | __|
  | | (__  | |   | _| | | >  <  | | | |_| |   | _| 
 |___\___| |_|   |_| |___/_/\_\ |_|  \___/|_|_|___|
                                                   
  _    _____   _____ _      _   ___ __  __   ___ ___ ___  ___  ___ _____ 
 | |  | __\ \ / | __| |    / | | _ |  \/  | | _ | __| _ \/ _ \| _ |_   _|
 | |__| _| \ V /| _|| |__  | | |  _| |\/| | |   | _||  _| (_) |   / | |  
 |____|___| \_/ |___|____| |_| |_| |_|  |_| |_|_|___|_|  \___/|_|_\ |_|  
                                                                         
                                                                                                              
		\n\n====================================================================================================================\n""")

def signature():
	print("""
		Developed by    : Idris, Shahidan
		Date Developed  : 10/27/2020
		Program         : ICT Fixture Level 1 PM Report Generation Tool
		\n""")

def clearscreen():
	os.system("cls")

def processStep(answer, listy):
	answer = input("\nPress Enter if this step is DONE...   ")
	if answer == "":
		listy.append("Done")
	else:
		processStep(answer, listy)

def processInput(question, listans):
	answer = input(question + " ")
	listans.append(answer)

sys.excepthook = show_exception_and_exit

today = date.today()

workbook = xlrd.open_workbook("steps_Level1.xlsx", encoding_override="cp1252")

worksheet = workbook.sheet_by_name('Sheet1')

questions = []
answers = []
step = ""

i = 1
rows = worksheet.nrows - 1
clearscreen()
header()
signature()

text = "WWID: "
questions.append(text)
ans = input(text)
answers.append(ans)

text = "Fixture Name: "
questions.append(text)
ans = input(text)
answers.append(ans)

text = "Fixture ID: "
questions.append(text)
ans = input(text)
answers.append(ans)

questions.append("Date Reported: ")
answers.append(str(today))

clearscreen()
header()
signature()

while True:
	if worksheet.cell(i, 0).value == xlrd.empty_cell.value:
		text = worksheet.cell(i,1).value
		print()
		questions.append(text)
		processInput(text, answers)
	else:
		text = str(int(worksheet.cell(i, 0).value)) + ". " + worksheet.cell(i, 1).value 
		print(text)
		questions.append(text)
		processStep(step, answers)
	if i == rows:
		break
	else:
		if not worksheet.cell(i+1, 0).value == xlrd.empty_cell.value:
			clearscreen()
			header()
			signature()
	i = i + 1


clearscreen()

imageList = []

imageList = getImages()

questions.append('Top Cover (1) Before')
questions.append('Top Cover (1) After')
questions.append('Top Cover (2) Before')
questions.append('Top Cover (2) After')
questions.append('Bottom Cover (1) Before')
questions.append('Bottom Cover (1) After')
questions.append('Bottom Cover (2) Before')
questions.append('Bottom Cover (2) After')

answers = answers + imageList

outputFiles(questions, answers)

pareto("cyclecount.csv")