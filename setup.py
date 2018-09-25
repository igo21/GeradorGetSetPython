from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("gerador.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "Gerador de Get/Set",
    options = options,
    version = "1.0",
    description = 'Este software foi feito com muito carinho para aqueles que precisam gerar get/set',
    executables = executables
)