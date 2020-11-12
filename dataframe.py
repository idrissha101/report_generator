import os
import webbrowser
from datetime import date
from datetime import datetime
import pdfkit
from PIL import Image
import pandas as pd
import base64
from pathlib import Path

def outputFiles(items, answers):
	
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S)")

	question_list = []

	today = date.today()

	def make_clickable(val):
	    return '<a href="{}">{}</a>'.format(val,val)

	def highlight_vals(val, min=20000, max=40000):
	    if val >= min and val < max:
	        return ''
	    elif val >= max:
	        return ''
	    elif val < min:
	        return ''

	data = {    'Items'     :   items,
	            'Contents'  :   answers,
	    }

	df = pd.DataFrame(data)
	df.drop(df.tail(8).index,inplace=True)

	df = df.replace('0', 'None')
	df = df.replace('', 'None')

	path1 = os.getcwd() + "\\" + "Level1" + "\\" + answers[2]

	if not os.path.exists(path1):
	    os.makedirs(path1)

	csvName = path1 + "\\" + answers[2] + "_" + str(today) + ".csv"
	htmlName = path1 + "\\" + answers[2] + "_" + str(today) + ".html"
	pdfName = path1 + "\\" + answers[2] + "_" + str(today) + ".pdf"
	df.to_csv(csvName, index=False)

	html_str = """
	<style>
      .img-container {
        text-align: center;
      }
    </style>
	<h1>ICT Fixture LEVEL 1 PM Report for """

	f= open(htmlName,"w")                                                     
	f.write(html_str + answers[1] + " (" + answers[2] + ")</h1>" + "<strong>Reported by: </strong>" + answers[0] + "<br>" + "<strong>Fixture Name: </strong>" + answers[1] + "<br>" + "<strong>Fixture ID: </strong>" + answers[2] + "<br>" + "<strong>Date Reported: </strong>" + str(answers[3]) + "<br><br>")

	f.close()                                                                 

	df = df.drop([0, 1, 2, 3])

	# TODO: Debug the "format make_clickable" thing to allow clickable image link
	with open(htmlName, 'a') as f:                                            
	    f.write(df.to_html(index=False))
	    f.write("<br><br>")

	print("\n\nGENERATING IMAGES...PLEASE WAIT...")

	for questions in items[-8:]:
		question_list.append(questions)

	num = 0

	with open(htmlName, 'a') as f:
		for images in answers[-8:]:
			if not images == '':
				data_uri = base64.b64encode(open(images, 'rb').read()).decode('utf-8')
				img_tag = '<div class="img-container"><img src="data:image/png;base64,{0}" width=500>'.format(data_uri)
				f.write(img_tag)
				f.write("<br><strong><em>" + question_list[num] + "</em></strong><br><br></div>")
			num = num + 1

	path_wkhtmltopdf = r"wkhtmltopdf\bin\wkhtmltopdf.exe"
	config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
	pdfkit.from_file(htmlName, pdfName, configuration=config)

	os.startfile(Path(pdfName))

	counterFile = "cyclecount.csv"

	cycleData = {	'timeStamp' 	: [dateTimeObj],
					'fixtureName'	: [answers[1]],
					'fixtureId'		: [answers[2]],
					'cycleCount'	: [answers[8]]
			}

	df2 = pd.DataFrame(cycleData)

	if not os.path.exists(counterFile):
		df2.to_csv(counterFile, index=False)
	elif os.path.exists(counterFile):
		df = pd.read_csv(counterFile)
		df = df.append(df2, ignore_index=True)
		df = df.sort_values(by=['fixtureId', 'timeStamp'], ascending=False)
		df.to_csv(counterFile, index=False)