
import sys
from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] ="C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Igor\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executable = [
        Executable(script="Iniciar.py", base=base, icon="imagem/logoicone3.ico")
]

buildOptions = dict(
        packages = ["tkinter"],
        includes = ["tkinter","matplotlib","os","random","sys","functools","clipboard"],
        include_files = ["logoicone4.ico","gerador.py"],
        include_msvcr = True,
        excludes = []
)




setup(
    name = "GNUScasinos",
    version = "1.0",
    description = "Simulador de casinos",
    options = dict(build_exe = buildOptions),
    executables = executable
 )
