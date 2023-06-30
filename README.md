# Orion Model Benchmarking

In this repository you can find a set of benchmarkings with different model architectures from the [ONNX Hub Models repository](https://github.com/onnx/models/tree/main).

## Results

- [ONNX Operators Frequency Usage](./orion_benchmark/operator_usage.md)
- [ONNX Quantized Operators Frequency Usage](./orion_benchmark/quant_operator_usage.md)
- [Orion Compatibility Percentage and Missing Operators with Quantized ONNX Hub models](./orion_benchmark/quant_operator_coverage.md)
- [Orion Compatibility Percentage with ONNX Hub models](./orion_benchmark/operator_coverage.md)

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

## Setup

1. Install dependencies:

```
poetry install
poetry run pip install keyring
poetry run pip install keyrings.google-artifactregistry-auth
```

2. Get `smartonnx` repository configuration:

```
gcloud artifacts print-settings python --project=giza-platform \
    --repository=smartonnx \
    --location=europe-west1
```

3. Install `smartonnx`:

```
pip install --index-url https://europe-west1-python.pkg.dev/giza-platform/smartonnx/simple/ smartonnx
```

## Usage

1. Get ONNX operator usage by frequency:

```python
python orion_benchmark/operator_analytics.py
```

2. Get ONNX operator usage by frequency for quantized models:

```python
python orion_benchmark/quant_operator_analytics.py
```

2. Get model percentage of compatibility with Orion Operators:

```python
python orion_benchmark/operator_coverage.py
```