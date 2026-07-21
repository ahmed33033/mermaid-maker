### Get all the existing, generated mermaid files (if they exist)
from glob import glob
from pathlib import Path
from os.path import basename
import os
import json

input_files = json.loads('${{env.input_files}}')
output_files = []

if '${{inputs.output_dir}}' == 'same':
    for file in input_files:
        output_files.append(
            Path(file).with_suffix('.${{inputs.output_file_extension}}').as_posix()
        )
else:
    for file in input_files:
        output_files.append(
            (Path('${{inputs.output_dir}}') / basename(file))
            .with_suffix('.${{inputs.output_file_extension}}')
            .as_posix()
        )

with open(os.environ["GITHUB_OUTPUT"], "a") as file:
    print('output_files=' + json.dumps(output_files), file=file)
