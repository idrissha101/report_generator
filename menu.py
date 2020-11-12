import xlrd
import os
import pandas as pd
from datetime import date
from dataframe import outputFiles
from images import getImages
import sys
from art import text2art

def text_split(text, length):
	lines = []
	if (len(text) > length):
		start = 0
		finish = length - 1
		extra = 0
		while True:
			while True:
				line = text[start:finish]
				if text[finish + 1] == " ":
					finish = finish + 1
					line = text[start:finish]
					lines.append(line)
					break
				else:
					finish = finish + 1
					extra = extra + 1
			start = finish
			finish = finish + 15 - extra
			extra = 0
			if len(text) < finish:
				line = text[start:]
				lines.append(line)
				break
	else:
		lines.append(text)
	return text


def show_exception_and_exit(exc_type, exc_value, tb):
    import traceback
    traceback.print_exception(exc_type, exc_value, tb)
    input("Press key to exit.")
    sys.exit(-1)

def header():
	print("========================================================================================")
	
	if len(title) < 60:
		print(text2art(title, font="small"))
	else:
		for lin in text_split(title, 16):
			print(text2art(lin, font="small"))

	print("========================================================================================\n\n")

def signature():
	print("Tool developed by    : Idris, Shahidan (11952926)")
	print("Tool owner           : {}" . format(owner))
	print("Date Developed       : 12 November 2020")
	if len(title) < 60:
		print("Program              : {}" . format(title))
	else:
		print("Program              : {}" . format(text_split(title,60)[0]))
		i = 1
		for num in range(i, len(text_split(title,60))):
			print("                      {}" . format(text_split(title,60)[num]))
	print("\n")

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

workbook = xlrd.open_workbook("steps.xlsx", encoding_override="cp1252")

worksheet = workbook.sheet_by_name('Sheet1')

questions = []
answers = []
step = ""
starting_read = 1
skipping = 0
imageCount = 0

i = 1
rows = worksheet.nrows - 1

while True:
	if worksheet.cell(i, 0).value == "title":
		title = worksheet.cell(i, 1).value
		starting_read = starting_read + 1
	if worksheet.cell(i, 0).value == "owner":
		owner = worksheet.cell(i, 1).value
		starting_read = starting_read + 1
	if i == rows:
		break
	i = i + 1

clearscreen()
header()
signature()

i = 1

while True:
	if worksheet.cell(i, 0).value == "subheading":
		text = worksheet.cell(i, 1).value + ": "
		questions.append(worksheet.cell(i, 1).value)
		subheading = input(text)
		answers.append(subheading)
		starting_read = starting_read + 1
		skipping = skipping + 1
	if worksheet.cell(i, 0).value == "details":
		text = worksheet.cell(i, 1).value + ": "
		questions.append(worksheet.cell(i, 1).value)
		answers.append(input(text))
		starting_read = starting_read + 1
		skipping = skipping + 1
	if i == rows:
		break
	i = i + 1

questions.append("Date Reported: ")
answers.append(str(today))

clearscreen()
header()
signature()

i = starting_read

while True:
	if worksheet.cell(i, 0).value == "image":
		break
	if worksheet.cell(i, 0).value == xlrd.empty_cell.value:
		text = worksheet.cell(i, 1).value
		print()
		questions.append(text)
		processInput(text, answers)
	elif str(int(worksheet.cell(i, 0).value)).isnumeric():
		text = str(int(worksheet.cell(i, 0).value)) + ". " + worksheet.cell(i, 1).value 
		print(text)
		questions.append(text)
		input()
		processStep(step, answers)
	if i == rows:
		break
	else:
		if not worksheet.cell(i+1, 0).value == xlrd.empty_cell.value:
			clearscreen()
			header()
			signature()
	i = i + 1


while True:
	if worksheet.cell(i, 0).value == "image":
		caption = worksheet.cell(i, 1).value + ": "
		questions.append(worksheet.cell(i, 1).value)
		imageCount = imageCount + 1
	if i == rows:
		break
	i = i + 1

clearscreen()

imageList = []

if imageCount > 0:
	imageList = getImages(questions, imageCount)
	answers = answers + imageList

outputFiles(questions, answers, skipping, imageCount, title, subheading)

# pareto("cyclecount.csv")