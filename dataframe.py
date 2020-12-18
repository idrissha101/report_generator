import os
import webbrowser
from datetime import date
from datetime import datetime
import pdfkit
from PIL import Image
import pandas as pd
import base64
from pathlib import Path

def outputFiles(items, answers, skips, imageAmount, head, subhead):
	
	dateTimeObj = datetime.now()
	timestampStr = dateTimeObj.strftime("%Y%m%d_%H%M%S")

	question_list = []

	today = date.today()

	data = {    'Items'     :   items,
	            'Contents'  :   answers,
	    }

	df = pd.DataFrame(data)
	df.drop(df.tail(imageAmount).index,inplace=True)

	path1 = os.getcwd() + "\\" + head + "\\" + subhead

	if not os.path.exists(path1):
	    os.makedirs(path1)

	htmlName = path1 + "\\" + subhead + "_" + timestampStr +".html"
	pdfName = path1 + "\\" + subhead + "_" + timestampStr +".pdf"

	html_str = """
	<style>
      .img-container {
        text-align: center;
      }
    </style>
	<h1>"""

	

	f= open(htmlName,"w")
	f.write(html_str)
	f.close()                                                                 

	f= open(htmlName,"a")
	f.write(head + " for " + subhead)
	f.write("""</h1><br>""")
	f.write("<h4>")
	for x in range(0, skips):
		f.write(items[x] + ": ")
		f.write(answers[x] + "<br>")
	f.write("</h4>")

	f.close()

	for x in range(0, skips):
		df = df.drop([x])

	with open(htmlName, 'a') as f:                                            
	    f.write(df.to_html(index=False))
	    f.write("<br><br>")

	if imageAmount > 0:
		print("\n\nGENERATING IMAGES...PLEASE WAIT...")

		for questions in items[-imageAmount:]:
			question_list.append(questions)

		num = 0

		with open(htmlName, 'a') as f:
			for images in answers[-imageAmount:]:
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