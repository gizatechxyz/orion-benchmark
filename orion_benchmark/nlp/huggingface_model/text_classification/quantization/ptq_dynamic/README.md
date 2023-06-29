Step-by-Step
============

This example load a language translation model and confirm its accuracy and speed based on [GLUE data](https://gluebenchmark.com/).

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
|           Intel/bert-base-uncased-mrpc          |
|             Intel/roberta-base-mrpc             |
|           Intel/xlm-roberta-base-mrpc           |
|            Intel/camembert-base-mrpc            |
| distilbert-base-uncased-finetuned-sst-2-english |
|         Alireza1044/albert-base-v2-sst2         |
|        Intel/MiniLM-L12-H384-uncased-mrpc       |
|      philschmid/MiniLM-L6-H384-uncased-sst2     |
|     bert-base-cased-finetuned-mrpc              |
|        Intel/electra-small-discriminator-mrpc   |
|         M-FAC/bert-mini-finetuned-mrpc          |
|           Intel/xlnet-base-cased-mrpc           |
|            Intel/bart-large-mrpc                |
|             Intel/deberta-v3-base-mrpc          |

```bash
python export.py --model_name_or_path=Intel/bert-base-uncased-mrpc \ # or other supported model identifier
```

## 3. Prepare Dataset
Download the GLUE data with `prepare_data.sh` script.

```shell
export GLUE_DIR=/path/to/glue_data
export TASK_NAME=MRPC # or SST

bash prepare_data.sh --data_dir=$GLUE_DIR --task_name=$TASK_NAME
```

# Run

## 1. Quantization

Dynamic quantization:

```bash
bash run_tuning.sh --input_model=path/to/model \ # model path as *.onnx
                   --output_model=path/to/model_tune \ # model path as *.onnx
                   --dataset_location=path/to/glue/data
```

## 2. Benchmark

```bash
bash run_benchmark.sh --input_model=path/to/model \ # model path as *.onnx
                      --dataset_location=path/to/glue/data \ 
                      --batch_size=batch_size \ 
                      --mode=performance # or accuracy
```
