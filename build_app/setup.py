from cx_Freeze import setup, Executable
import glob, os, pkgutil, Xlib.ext, Xlib.keysymdef

dir_path = 'build/compiled_files'

files = glob.glob('build/compiled_files/*.pyc')
files = [f for f in files if not f.endswith('main.pyc')]

for dir in os.listdir(dir_path):
    if os.path.isdir(os.path.join(dir_path, dir)):
        files.append(os.path.join(dir_path, dir))

excludes = ['tkinter', 'unittest', 'email', 'html', 'http', 'pydoc_data', 'urllib', 'xml', 'hashlib', 'ssl']
includes = ['queue', 'pynput.keyboard._xorg', 'pynput.mouse._xorg']
output_dir = 'build/app'

xlib_ext_modules = pkgutil.iter_modules(Xlib.ext.__path__)
xlib_keysymdef_modules = pkgutil.iter_modules(Xlib.keysymdef.__path__)

for importer, modname, ispkg in xlib_ext_modules:
    includes.append(f'Xlib.ext.{modname}')

for importer, modname, ispkg in xlib_keysymdef_modules:
    includes.append(f'Xlib.keysymdef.{modname}')

build_exe_options = {
    'include_files': files,
    'excludes': excludes,
    'includes': includes,
    'build_exe': output_dir
}

target = Executable(
    script='src/main.py',
    base='Console',
    icon='icon.ico'
)

setup(
    name='PyClickerX',
    version='4',
    description='console based autoclicker',
    options={'build_exe': build_exe_options},
    executables=[target]
)
