import os
import shutil
import time
from pathlib import Path

from giza.commands.transpile import transpile
from smartonnx.backends.cairo.backend import CairoTranspiler
from tabulate import tabulate

directory = 'orion_benchmark/models'

# Find all .onnx files in the directory
onnx_files = [os.path.join(root, file) 
              for root, dirs, files in os.walk(directory) 
              for file in files if file.endswith('-int8.onnx')]

output_folder = "orion_benchmark/cairo_models"

if os.path.exists(output_folder):
    shutil.rmtree(output_folder)

os.mkdir(output_folder)

transpiled_count = 0
transpiled_models = []
for onnx_file in onnx_files:
    model_name = "/".join(onnx_file.split("/")[-2:]).replace(".onnx", "")
    output_model = os.path.join(output_folder, model_name)
    print(f'Transpiling {onnx_file}...')
    # transpile(onnx_file, output_model)
    output_path = Path(output_model)
    try:
        start_time = time.time()
        CairoTranspiler(onnx_file, output_path).transpile()
        end_time = time.time()
        execution_time = end_time - start_time
    except Exception as e:
        shutil.rmtree(output_path)
    else:
        transpiled_count += 1
        transpiled_models.append((model_name, execution_time))
content = tabulate(transpiled_models, headers=['Model', 'Execution time'], tablefmt="github")
content += f'\n\nTranspiled {transpiled_count} models of {len(onnx_files)} total models'

with open("orion_benchmark/cairo_models.md", "w") as f:
    f.write(content)


    