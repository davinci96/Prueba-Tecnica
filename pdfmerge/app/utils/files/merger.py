import os
from PyPDF2 import PdfFileMerger
from flask import current_app

def merger(filename, files):
    temp_folder     = os.path.join(current_app.root_path, 'utils', 'files', 'temp')
    result_folder   = os.path.join(current_app.root_path, 'utils', 'files', 'result')

    os.makedirs(temp_folder, exist_ok=True)
    os.makedirs(result_folder, exist_ok=True)

    output_file     = os.path.join(result_folder, filename)

    for file in os.listdir(result_folder):
        os.remove(os.path.join(result_folder, file))

    merger = PdfFileMerger()

    for pdf in files:
        merger.append(open(pdf, 'rb'))

    with open(output_file, 'wb') as output:
        merger.write(output)

    for file in os.listdir(temp_folder):
        os.remove(os.path.join(temp_folder, file))

    return output_file






