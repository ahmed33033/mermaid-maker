### Get all the input mermaid files
from glob import glob
import os
import json

if os.environ['INPUT_DIR'] == "all":
    input_files_glob_pattern = f'**/*.{os.environ['INPUT_FILE_EXTENSION']}'
else:
    input_files_glob_pattern = '${{inputs.input_dir}}/*.${{inputs.input_file_extension}}'

input_files = []
for file in glob(input_files_glob_pattern, recursive=True):
    input_files.append(file)

with open(os.environ["GITHUB_OUTPUT"], "a") as file:
    print('input_files=' + json.dumps(input_files), file=file)
