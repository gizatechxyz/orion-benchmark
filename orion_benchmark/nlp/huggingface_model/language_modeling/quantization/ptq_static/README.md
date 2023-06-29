Step-by-Step
============

This example load a language translation model and confirm its accuracy and speed based on [WikiText](https://blog.einstein.ai/the-wikitext-long-term-dependency-language-modeling-dataset/) dataset.

# Prerequisite

## 1. Environment
```shell
pip install neural-compressor
pip install -r requirements.txt
```
> Note: Validated ONNX Runtime [Version](/docs/source/installation_guide.md#validated-software-environment).

## 2. Prepare Model

Supported model identifier from [huggingface.co](https://huggingface.co/):

|                 Model Identifier                |
|:-----------------------------------------------:|
|           gpt2          |
|             distilgpt2             |

Use `export.py` script for ONNX model conversion.
Require transformers==3.2.0.

```shell
python export.py --model_name_or_path=gpt2 # or other supported model identifier
```

## 3. Prepare Dataset
Please download [WikiText-2 dataset](https://s3.amazonaws.com/research.metamind.io/wikitext/wikitext-2-raw-v1.zip).

# Run

## 1. Quantization

Quantize model with static quantization:

```bash
bash run_tuning.sh --dataset_location=/path/to/wikitext-2-raw/wiki.test.raw \ 
                   --input_model=path/to/model \ # model path as *.onnx
                   --output_model=path/to/model_tune
```

## 2. Benchmark

```bash
bash run_benchmark.sh --dataset_location=/path/to/wikitext-2-raw/wiki.test.raw \ 
                      --input_model=path/to/model \ # model path as *.onnx
                      --batch_size=batch_size \
                      --mode=performance # or accuracy
```
