import os
import onnx
from collections import defaultdict
from tabulate import tabulate

# Specify the directory you want to search in
directory = '.'

# Find all .onnx files in the directory
onnx_files = [os.path.join(root, file) 
              for root, dirs, files in os.walk(directory) 
              for file in files if file.endswith('-int8.onnx')]

# Initialize a dictionary to store operator counts
operator_counts = defaultdict(int)

# Load each .onnx file and count the operators
model_len = len(onnx_files)
for onnx_file in onnx_files:
    print(f'Counting operators in {onnx_file}')
    model = onnx.load(onnx_file)
    for node in model.graph.node:
        operator_counts[node.op_type] += 1

# Convert the operator counts to a list of tuples and sort by count
operator_counts_list = sorted(
    [(op, count) for op, count in operator_counts.items()],
    key=lambda x: x[1],  # Sort by count
    reverse=True  # Sort in descending order
)

# Print the operator counts in a table
print(tabulate(operator_counts_list, headers=['Operator', 'Count']))