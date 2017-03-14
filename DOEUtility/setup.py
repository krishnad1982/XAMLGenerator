import sys
from cx_Freeze import setup, Executable

company_name="IRESS"
product_name="DOESkinManager"
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "SkinManager",            # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]DoeUtility.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os","sys","PyQt5.QtWidgets","PyQt5.QtGui","PyQt5.QtWidgets","xml.dom","csv","shutil","Config","builtins","json"],
                     "include_files":["./images","./skins","./storage","config.json"],
                      "excludes": ["tkinter"],
                     "icon": "./images/appicon.ico",
                     }

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {
    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': False,
    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
    'data':msi_data,
    }


# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "SkinManager",
        author="IRESS",
        version = "1.0.0",
        description = "Iress DOE Skin Manager!",
        options = {"bdist_msi":bdist_msi_options,"build_exe": build_exe_options},
        executables = [Executable("DoeUtility.py", base=base)],
        requires=['PyQt5', 'cx_Freeze', 'json']
        )