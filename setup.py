import sys
from cx_Freeze import setup,Executable
import os

PYTHON_INSTALL_DIR=os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tcl8.6')
os.environ['TK_LIBRARY']=os.path.join(PYTHON_INSTALL_DIR,'tcl','tk8.6')
include_files=[(os.path.join(PYTHON_INSTALL_DIR,'DLLs','tk86t.dll'),os.path.join('lib','tk86.dll')),
               (os.path.join(PYTHON_INSTALL_DIR,'DLLs','tcl86t.dll'),os.path.join('lib','tcl86.dll'))]
base=None

if sys.platform=='win32':
    base='Win32GUI'
executables=[Executable('Bill.py',base=base,icon=r"C:\Users\shanm\OneDrive\Desktop\My projects\Billing Software\icon.ico",shortcut_name='Billing Software',shortcut_dir='DesktopFolder')]
setup(name='Billing Software Installer',
      version='1.0',
      author='Shanmukh Nath Seleswaram',
      description="My first Software",
      options={'build_exe':{'include_files':include_files}},executables=executables)    
