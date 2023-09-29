import os
import onnx
from datetime import datetime
from collections import Counter
from tabulate import tabulate
from supported_operatorr_list import SUPPORTED_OPERATORS


# Specify the directory you want to search in
directory = 'orion_benchmark/models'

# Find all .onnx files in the directory
onnx_files = [os.path.join(root, file) 
              for root, dirs, files in os.walk(directory) 
              for file in files if file.endswith('-int8.onnx')]

# Step 3: Load each ONNX file and analyze the operators
operator_coverage_list = []
for onnx_file in onnx_files:
    # print(f'Analyzing operators in {onnx_file}')
    file_path = onnx_file
    model = onnx.load(file_path)
    
    # Collecting operator types in the ONNX model's graph
    operator_types = [node.op_type for node in model.graph.node]
    operator_types = set(operator_types)
    operator_counts = Counter(operator_types)
    
    # Calculate the percentage coverage of operators    
    implemented_operator_count = sum(operator_counts[op] for op in operator_types if op in SUPPORTED_OPERATORS)
    not_implemented_operator_set = operator_types - set(SUPPORTED_OPERATORS)
    total_operator_count = sum(operator_counts.values())
    percentage_coverage = (implemented_operator_count / total_operator_count) * 100 if total_operator_count > 0 else 0
    operator_coverage_list.append(("/".join(onnx_file.split("/")[-2:]), percentage_coverage, ", ".join(not_implemented_operator_set)))

average_coverage = sum([x[1] for x in operator_coverage_list]) / len(operator_coverage_list)

current_time = datetime.now().strftime('%d/%m/%Y')
print(tabulate(operator_coverage_list, headers=['Model', f'Coverage ({current_time})', 'Missing Operators'], tablefmt="github"))
print(f'\nAverage coverage: {average_coverage}')

