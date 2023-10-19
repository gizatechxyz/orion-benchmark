
## Depth Benchmark

The aim of this benchmark is to test the scaling of Orion with respect to number of model layers.

### Model Architecture
```
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         [(None, 200)]             0         
_________________________________________________________________
layer1 (Dense)               (None, 10)                2010      
_________________________________________________________________
layern (Dense)               (None, 10)                110       
=================================================================
Total params: 2,120
_________________________________________________________________
```

### Results
The table below shows the benchmark results at varying depths:

| Depth | Proof Cairo VM execution time | Proof proving time |
| ----- | ----------------------------- | ------------------ |
| 1     | 0.5706441                     | 32.94817           |
| 5     | 2.080153                      | 138.54219          |
| 10    | 4.0620766                     | 313.24823          |
