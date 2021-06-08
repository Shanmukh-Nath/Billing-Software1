import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Admin\AppData\Local\Programs\Python\Python37\tcl\tk8.6"

executables = [cx_Freeze.Executable("Bill.py", base=base, icon="Bill.ico")]


cx_Freeze.setup(
    name = "Billing Software",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["Bill.ico",'tcl86t.dll','tk86t.dll', '__pycache__','.idea','venv']}},
    version = "0.1",
    description = "Tkinter Application",
    executables = executables
    )
