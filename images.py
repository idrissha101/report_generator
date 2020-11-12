import PySimpleGUI as sg

def getImages():
	
	image_list = []

	sg.theme('DarkAmber')   # Add a touch of color
	
	# All the stuff inside your window.
	layout = [
	    [ sg.Text('Select Top Cover (1) Before image', size=(30,1))], 
	    [ sg.In(size=(80,1),key='topcover1before'),sg.FileBrowse(target='topcover1before')],
	    [ sg.Text('Select Top Cover (1) After image', size=(30,1))],
	    [ sg.In(size=(80,1),key='topcover1after'),sg.FileBrowse(target='topcover1after')], 
	    [ sg.Text('Select Top Cover (2) Before image', size=(30,1))],
	    [ sg.In(size=(80,1),key='topcover2before'),sg.FileBrowse(target='topcover2before')],
	    [ sg.Text('Select Top Cover (2) After image', size=(30,1))],
	    [ sg.In(size=(80,1),key='topcover2after'),sg.FileBrowse(target='topcover2after')],
	    [ sg.Text('Select Bottom Cover (1) Before image', size=(30,1))], 
	    [ sg.In(size=(80,1),key='bottomcover1before'),sg.FileBrowse(target='bottomcover1before')],
	    [ sg.Text('Select Bottom Cover (1) After image', size=(30,1))],
	    [ sg.In(size=(80,1),key='bottomcover1after'),sg.FileBrowse(target='bottomcover1after')], 
	    [ sg.Text('Select Bottom Cover (2) Before image', size=(30,1))],
	    [ sg.In(size=(80,1),key='bottomcover2before'),sg.FileBrowse(target='bottomcover2before')],
	    [ sg.Text('Select Bottom Cover (2) After image', size=(30,1))],
	    [ sg.In(size=(80,1),key='bottomcover2after'),sg.FileBrowse(target='bottomcover2after')],

	    [ sg.Button('Done'), sg.Button('Clear Input') ]
	]

	# Create the Window
	window = sg.Window('ICT FIXTURE PM REPORT - IMAGE RETRIEVAL', layout)
	# Event Loop to process "events" and get the "values" of the inputs
	while True:
	    event, values = window.read()

	    if event == sg.WIN_CLOSED or event == 'Done': # if user closes window or clicks cancel
	        break

	    if event=='Clear Input':
	       values['topcover1before'],values['topcover1after'],values['topcover2before'],values['topcover2after']='','','',''
	       values['bottomcover1before'],values['bottomcover1after'],values['bottomcover2before'],values['bottomcover2after']='','','',''

	       window['topcover1before'].update('')
	       window['topcover1after'].update('')
	       window['topcover2before'].update('')
	       window['topcover2after'].update('')
	       window['bottomcover1before'].update('')
	       window['bottomcover1after'].update('')
	       window['bottomcover2before'].update('')
	       window['bottomcover2after'].update('')

	image_list.append(values['topcover1before'])
	image_list.append(values['topcover1after'])
	image_list.append(values['topcover2before'])
	image_list.append(values['topcover2after'])
	image_list.append(values['bottomcover1before'])
	image_list.append(values['bottomcover1after'])
	image_list.append(values['bottomcover2before'])
	image_list.append(values['bottomcover2after'])

	window.close()

	return image_list