import os
import shutil
from zipfile import ZipFile

def retrieve_data(data_instructions):
  '''
  Retrieves data from different sources including GitHub and GoogleDrive
  If the file is Zip, then it automatically decompresses it
  Arguments:
     - data instructions (list of 5 element sets) - Every element will provide information for a single operation
        -- base_path (str) - the directory where the specific file will be transferred, not including the filename
        -- file (str) - name of the file to be transferred
        -- base_url (str) - the URL path not including the filename
        -- method (str) - 'Gmail' or 'Github'
        -- remove (boolen) - If true, removes the base path dir before copying again
        
   Example:
     from tools_fernandogithub import ff_data_transfer as ffdt
     data_instructions=list()
     data_instructions.append(('.', 'XML.zip', 'ID_from_Google_share', 'GDrive', False))
     data_instructions.append(('.', 'Hello.txt', 'https://githubfolder/etc', 'Github', True))
     ffdt.retrieve_data(data_instructions)
  '''
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


def clean_directory(directory, skip_logs=True):
  '''
  Cleans all files and all directories in a directory
  Arguments: 
    - directory (string) - the path of the directory to clean
    - skip_logs (boolean) - default: True
  '''
  if not os.path.isdir(directory):
    print(f'folder: {directory} does not exist. Skipping!')
    return
  
  for ent in os.listdir(directory):
    ent = os.path.join(directory, ent)
    if os.path.isdir(ent):
      shutil.rmtree(ent)
    elif not (ent.endswith('.log') and skip_logs):
      os.remove(ent) 
  
  print(f'Cleaned directory: {directory}')

