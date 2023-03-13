from cx_Freeze import setup, Executable
import glob, os

dir_path = 'build/compiled_files'

files = glob.glob("build/compiled_files/*.pyc")
files = [f for f in files if not f.endswith('main.pyc')]

for dir in os.listdir(dir_path):
    if os.path.isdir(os.path.join(dir_path, dir)):
        files.append(os.path.join(dir_path, dir))

excludes = ["tkinter", "unittest", "email", "html", "http", "pydoc_data", "urllib", "xml", "hashlib", "socket", "ssl"]
includes = ["queue"]
output_dir = "build/app"

build_exe_options = {
    "include_files": files,
    "excludes": excludes,
    "includes": includes,
    'build_exe': output_dir
}

base = None

target = Executable(
    script="src/main.py",
    base=base,
    icon="icon.ico"
)

setup(
    name="PyClickerX",
    version="2.1",
    description="console based autoclicker",
    options={"build_exe": build_exe_options},
    executables=[target]
)
