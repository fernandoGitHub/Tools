import sys
import subprocess as sp
import pkg_resources
import importlib

# Installing packages without !pip
def install_package(package, reload = True):
  '''
  Installs packages without using !pip at the notebook.
  Arguments:
     - package - type: str - name of the package (as it will appear after pip)
     - reload - type: Bool - True for reloading packages after install
  '''
  # Veryfing existing install prior to install
  if is_installed(package):
    print (f'Package: {package} is already installed. Skipping installation')
  else:
    print(f'Installing {package} ...')
    sp.check_call([sys.executable, '-m', 'pip', 'install', package])
    print(f'Package {package} has been successfully installed')

  if reload:
    reload_packages()

def is_installed (package):
  # Getting all the list of packages
  return (package in get_installed_packages())

def get_installed_packages():
  return sorted({pkg.key for pkg in pkg_resources.working_set})

def reload_packages():
  print ('Reloading Packages')
  importlib.reload(pkg_resources)
