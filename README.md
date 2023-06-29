# Orion Model Benchmarking

In this repository you can find a set of benchmarkings with different model architectures from the [ONNX Hub Models repository](https://github.com/onnx/models/tree/main).

## Results

- [ONNX Operators Frequency Usage](./orion_benchmark/operator_usage.md)
- [ONNX Quantized Operators Frequency Usage](./orion_benchmark/quant_operator_usage.md)

## Development

1. Clone ONNX Hub Models repository:

```
git clone https://github.com/onnx/models.git
```

2. Install Git LFS

```
brew install git-lfs
```

3. Setup Git LFS

```
git lfs install
```

4. Fetch models:

```
git lfs fetch
```

5. Checkout models:

```
git lfs checkout
```

6. Get ONNX operator usage by frequency:

```python
python orion_benchmark/operator_analytics.py
```

7. Get ONNX operator usage by frequency for quantized models:

```python
python orion_benchmark/quant_operator_analytics.py
```