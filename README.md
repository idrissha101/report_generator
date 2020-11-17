# Report Generator Tool
This tool is a user-customizable report generation tool. It is derived from the ICT Fixture PM Report Generation Tool used at SIMS. This software is built using Python. The tool reads the questions/steps that need to be recorded in the report from an Excel file. The Excel file can be edited by users for any questions/steps they require. The different questions are labeled by the input types, these different input types will display and process the answers of these questions differently.

## Installation
### Basic usage only
For users who want to run the tool (not intending to develop/build the software), clone the following files/folders:
- **menu.exe** *(Main Executable File for the program)*
- **wkhtmltopdf** *(Folder containing executables and binaries to enable HTML-to-PDF conversion)*
- **steps.xlsx** *(Excel file containing user-defined questions/steps, in which the program reads from)*

Make sure all 3 files/folders are placed in the same directory. The report generator tool is built to detect and use the files/folders at the same directory.

### For developers
Should you wish to develop/modify the code, clone the following files/folders:
- **menu.py** *(Script running the collection of questions/steps from Excel file, displays questions/steps, collects input from reporters, runs the other sub-scripts)*
- **menu.spec** *(Spec file used to generate executable file for the tool using PyInstaller)*
- **images.py** *(Script running the GUI to collect images. The images will be rendered at the end of the report)*
- **dataframe.py** *(Data compilation into pandas DataFrame, HTML and PDF file generation)*
- **report_generator_env.yml** *(Anaconda environment used to develop the tool. Optional, but encouraged as it will reduce problems when developing the tool)*
- **steps.xlsx** *(Excel file containing user-defined questions/steps, in which the program reads from)*
- **wkhtmltopdf** *(Folder containing executables and binaries to enable HTML-to-PDF conversion)*

#### Libraries and Versions
- Python == 3.6.8
- pip == 20.2.4
- setuptools == 50.3.2
- pandas == 1.1.3
- pdfkit == 0.6.1
- Pillow == 8.0.2
- PySimpleGUI == 4.30.0
- pyinstaller == 4.0
- ipython == 7.16.1
- matplotlib == 3.2.2
- pycairo == 1.20.0
- PySide2 == 5.15.1
- tornado == 6.0.4
- xlrd == 1.2.0
- xlwt == 1.3.0

Some of the libraries may not be necessary in developing and generating the executable file for the report generator tool, however, these are what worked for me throughout the development/debugging process. You are strongly encouraged to follow the versions mentioned in the list, as using a different version may cause bugs/issues in developing/running the tool. Most of the libraries can be obtained through a [pip installation](https://pip.pypa.io/en/stable/), else a quick Google search should get you the libraries you need.

```
pip install matplotlib==3.2.2
```

You will also need to have an installation of wkhtmltopdf. This can be downloaded and installed from [this link](https://wkhtmltopdf.org/downloads.html).

When running the tool using Python, you would need to run the ***menu.py*** script. Do this on a Command Prompt or Anaconda Prompt.

```
python menu.py
```

#### If you want to build your own executable file
The executable file is generated using PyInstaller. Before running the ***pyinstaller*** command to generate the .exe file, we must first create ***menu.spec***. This is needed to specify the additional binaries that ***pyinstaller*** needs to create the .exe file. Refer to [this link](https://pyinstaller.readthedocs.io/en/stable/spec-files.html) for reference on how to create the file. Once the .spec file is created, edit the file in a text editor. In *binaries*, insert a tuple as follows: ('path_to_wkhtmltopdf.exe','.'). The final .spec file should look something like this:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['menu.py'],
             pathex=['C:\\Users\\usr\\Documents\\fixturePMReportTerminal'],
             binaries=[('C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe','.')],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='menu',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
```

This step would not be necessary if you have already cloned the ***menu.spec*** file at the start. To generate the .exe, enter the following in a Command Prompt or Anaconda Prompt.

```bash
pyinstaller menu.spec
```

## Usage
### Excel File (steps.xlsx)
The Excel File contains the questions/steps that should be displayed by the tool. These questions/steps can be modified/added by the user. Each question/step is labeled with its own input tag (***input_tag*** in the Excel).

#### Input Tags and their functions
##### owner (required)
There should only be ONE statement with this input tag. Users should enter the owner of this report (e.g. a department head, a module engineer in charge of the process etc). The name of the owner is displayed within the header of the program, along with other built-in details (developer name, date developed).

##### title (required)
There should only be ONE statement with this input tag. The statement for this input tag is the title of the report to be generated. An example would be a report of a set of procedures for cleaning an equipment. The statement for this input tag would be something like "Cleaning Report". The title is displayed within the header of the program.

##### subheading (required)
There should only be ONE statement with this input tag. The statement for this input tag should indicate the subgroup in which this report applies to. Using the example from ***title***, the subheading statement should be "Equipment X". The subheading will be displayed in the HTML and PDF reports as part of the header. From the example mentioned, if the statements earlier were given, the header of the HTML and PDF reports would be "Cleaning Report for Equipment X" (<title> for <subheading>).

##### details (optional)
There can be multiple statements using this input tag. The statements for this input tag do not appear in the dataframe table in the HTMl and PDF reports, rather they are displayed above the table. This input tag is useful if the user wants to highlight more important information regarding the report (e.g. Name, ID, and Department of the reporter, Shipment Order related to the report) or displaying information that is not directly related to the contents of the report (not part of the steps/procedures)

##### numbers (1, 2, 3...) (optional)
There can be multiple statements using this input tag. Placing a number as an input tag indicates the steps in the report. Statements with numbers as input tags will be displayed in the report as **steps to be completed/done**. In the tool, the reporter would need to **press ENTER** to indicate the step is completed.

##### empty cell (no input tag) (optional)
There can be multiple statements using this input tag. Statements with no input tag are used to request the reporter to input text data. This type of input is usually placed between ***numbers***, needing reporters to give more details after they have completed a step (e.g. Replaced spring for an equipment. How many springs replaced?). 

##### image (optional)
There can be multiple statements using this input tag. Statements with this input tag will not appear in the tool menu (Terminal display), rather it will appear in the GUI at the end. This input tag is used when reporters are required to upload images related to the steps they have completed for the report (e.g. Image of Before/After). The statements with this input tag will be the captions for the images uploaded by the reporter, which will be rendered and displayed at the end of the HTML and PDF reports.

#### Formatting of Excel File
The tool is programmed to read the Excel file in an order of top-to-bottom. It is strongly advised (if not compulsory) to **keep the order and formatting of the Excel file and its input tags** so that the tool will run correctly. 

Keep the input tags in the following sequence:
- owner
- title
- subheading
- details
- number (with corresponding empty cell where necessary)
- image

### Report Form (menu.py)
The program starts with the Terminal displaying the header, which contains the description of the program. The description includes an ASCII Art of ***title***, developer name (myself), ***owner***, and ***title*** as program name.

The form starts with requesting ***details***. The remaining parts of the Report Form is based on the steps/procedures specified by the user in ***steps.xlsx****. Statements with ***numbers*** input tags will be displayed and require reporters to hit ENTER to indicate completed, statements with ***empty cells*** will ask the reporter to key-in text input.

At the end of the form, the image retrieval tool GUI will appear if there are statements in ***steps.xlsx*** with ***images*** input tags (else, the program will proceed to output generation).

### Image Retrieval GUI (images.py)
The GUI will show the statements with ***images*** input tags in a GUI. This is used to request the reporter to upload images for each statement/caption. On the GUI menu, there are 2 options: ***Done*** and ***Clear Input***. ***Clear Input*** clears all the image uploads on the menu. Once the images are uploaded and confirmed, click ***Done*** to proceed to the next step.

The image file locations provided are converted into Base64, which will later be rendered into images and placed into the report HTML and PDF.

### DataFrame and Report Output Generation (dataframe.py)
This part of the script collects the list of questions and answers from the Report Tool and creates a DataFrame. From the DataFrame, a HTML file is generated to show the report. The HTML file has been included with slight formatting (headers) and some CSS (to centre align the images and captions at the end of the report). The images obtained and converted into Base64 earlier are rendered after the DataFrame table (at the end of the report), with the captions specified by ***images*** input tags in ***steps.xlsx***.

Using ***pdfkit*** and ***wkhtmltopdf***, a PDF file is produced from the HTML report.

## Contributing and Bug Reporting
For contributions, development, and issues, please contact [shahidan.idris@intel.com (until 18 December 2020)](mailto:shahidan.idris@intel.com) or [shahidan.utp@gmail.com](mailto:shahidan.utp@gmail.com).
