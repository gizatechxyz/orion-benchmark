
## Depth Benchmark

The aim of this benchmark is to test the scaling of Orion with respect to number of model layers.

### Model Summary
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
The table below shows the benchmark results at varying depths. 
It's using [Platinum Prover](https://github.com/lambdaclass/lambdaworks_stark_platinum).

| Depth | Cairo VM execution time (s) | Proving time (s) | Verification time (s) |
| ----- | --------------------------- | ---------------- | --------------------- |
| 1     | 0.5706441                   | 32.94817         | 0.0002777805          |
| 5     | 2.080153                    | 138.54219        | 1.131792917           |
| 10    | 4.0620766                   | 313.24823        | 2.362478041           |

### How to add new depth to the benchmark?

1. Change `DEPTH` const in `src/inference.cairo`.
    ```
    const DEPTH: u32 = 1000;
    ```
2. Compile project:
    ```
    > scarb build  
    > starknet-sierra-compile -- target/dev/bench_OrionRunner.sierra.json target/dev/bench.casm.json
    ```
3. Prove the program with Giza-CLI:
    ```
    giza prove target/dev/bench.casm.json --size XL
    ```
4. Update README.