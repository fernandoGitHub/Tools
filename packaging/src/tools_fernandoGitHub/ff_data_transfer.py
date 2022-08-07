import os
import shutil
from zipfile import ZipFile

def retrieve_data(data_instructions):
  for data_instruction in data_instructions:
    base_path, file, base_url, method, remove = data_instruction

    if os.path.isdir(base_path) and remove and (base_path != '.'):
      print(f'Removing directory tree: {base_path} ...')
      shutil.rmtree(base_path)

    if not os.path.isdir(base_path):
      print(f'Creating directory: {base_path} ...')
      os.mkdir(base_path)

    if not file == None:
      file_path = os.path.join(base_path, file)

      if os.path.isfile(file_path):
        if not remove:
          print(f'{file_path} already exists, skipping retrieve ...')
        else:
          print(f'Removing file: {file_path} ...')
          os.remove(file_path)
      else:
        if method == 'GDrive':
          print(f'Fetching from Google Drive: {file} ...')
          os.system(f'! gdown {base_url}') 
          os.replace(os.path.join('.', file), file_path)

        elif method == 'Github':
          print(f"Fetching from GitHub: {file} ...")
          url_path  = os.path.join(base_url, file)
          file_name = wget.download(url_path)
          os.replace(os.path.join('.', file), file_path)

      if file.lower().endswith('zip'):
        print(f"Extracting files in {file} ...")
        with ZipFile(file_path, 'r') as zippy:
          zippy.extractall(base_path)
		  
def clean_dir(dir):
  for ent in os.listdir(dir):
    ent = os.path.join(dir, ent)
    if os.path.isdir(ent):
      shutil.rmtree(ent)
    else:
      os.remove(ent) 
  
  print(f'Cleaned directory {dir}')

