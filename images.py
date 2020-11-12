import PySimpleGUI as sg

def getImages(fullQuestions, imageQuantity):
	
	image_list = []
	image_captions = []
	key_and_target = []

	sg.theme('DarkAmber')   # Add a touch of color

	for items in fullQuestions[-imageQuantity:]:
		image_captions.append(items)
		items = items.replace(" ", "")
		items = items.lower()
		key_and_target.append(items)

	# All the stuff inside your window.
	layout = []
	for i in range(0, len(image_captions)):
		layout += [ sg.Text(image_captions[i], size=(30,1))],
		layout += [ sg.In(size=(80,1),key=key_and_target[i]),sg.FileBrowse(target=key_and_target[i])],
	
	layout += [[ sg.Button('Done'), sg.Button('Clear Input') ]]

	# Create the Window
	window = sg.Window('IMAGE RETRIEVAL', layout)
	# Event Loop to process "events" and get the "values" of the inputs
	while True:
	    event, values = window.read()

	    if event == sg.WIN_CLOSED or event == 'Done': # if user closes window or clicks cancel
	        break

	    if event=='Clear Input':
	    	for i in range(0, len(image_captions)):
	    		values[key_and_target[i]] = ''

	    	for i in range(0, len(image_captions)):
	    		window[key_and_target[i]].update('')

	for i in range(0, len(image_captions)):
		image_list.append(values[key_and_target[i]])

	window.close()

	return image_list