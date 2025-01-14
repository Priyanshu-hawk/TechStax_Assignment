import gdown
import os

os.makedirs("dataset", exist_ok=True)

output = "dataset/road_aci_ds.zip"

url = "https://drive.google.com/file/d/1edKrdWNOcgbAo2JtckX-PEyM0FdEq4EG/view?usp=drive_link"
gdown.download(url=url, output=output, fuzzy=True)

from zipfile import ZipFile
with ZipFile(output, 'r') as zip_ref:
    zip_ref.extractall("dataset/")