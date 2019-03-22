#-*- coding: utf-8 -*-


from cx_Freeze import setup, Executable

target = Executable(
    script="yenikapit.py",
    base="Win32GUI",
    compress=False,
    copyDependentFiles=True,
    appendScriptToExe=True,
    appendScriptToLibrary=False,
    icon="icon.ico"
    )

setup(
    name="Yenikapı Teslimat",
    version="1.0",
    description="Opet Teslimatlarını kolay ve düzenli bir hale getiren script benzeri open source uygulama",
    author="Mehmet Eroglu",
    options={"build_exe": options},
    executables=[target]
    )