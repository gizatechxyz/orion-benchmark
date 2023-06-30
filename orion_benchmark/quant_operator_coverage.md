| Model                                 |   Coverage | Missing Operators                                                                                                           |
|---------------------------------------|------------|-----------------------------------------------------------------------------------------------------------------------------|
| model/bidaf-11-int8.onnx              |    72.7273 | Softmax, Sigmoid, Sum, DynamicQuantizeLinear, Log, DynamicQuantizeLSTM, CategoryMapper, Ceil, ReduceSum                             |
| model/bertsquad-12-int8.onnx          |    66.6667 | ReduceMean, Softmax, DynamicQuantizeLinear, FusedMatMul, Tanh, Sqrt, MatMul, Reciprocal, Identity                                   |
| model/mnist-12-int8.onnx              |    85.7143 | QLinearAdd                                                                                                                  |
| model/mobilenetv2-12-int8.onnx        |    81.8182 | QLinearAdd, QLinearGlobalAveragePool                                                                                         |
| model/googlenet-12-int8.onnx          |    63.6364 | AveragePool, QLinearAdd, Softmax, LRN                                                                                          |
| model/inception-v1-12-int8.onnx       |    50      | Softmax, Gemm, QLinearAveragePool, LRN, QLinearConcat                                                                           |
| model/resnet50-v1-12-int8.onnx        |    75      | QLinearAdd, QLinearGlobalAveragePool                                                                                         |
| model/caffenet-12-int8.onnx           |    66.6667 | QLinearAdd, Softmax, LRN                                                                                                      |
| model/squeezenet1.0-12-int8.onnx      |    71.4286 | Softmax, QLinearGlobalAveragePool                                                                                            |
| model/efficientnet-lite4-11-int8.onnx |    66.6667 | QLinearAdd, QLinearAveragePool, Softmax                                                                                       |
| model/zfnet512-12-int8.onnx           |    66.6667 | QLinearAdd, Softmax, LRN                                                                                                      |
| model/shufflenet-v2-12-int8.onnx      |    81.8182 | ReduceMean, QLinearAdd                                                                                                       |
| model/densenet-12-int8.onnx           |    46.1538 | QLinearAdd, QLinearGlobalAveragePool, Conv, QLinearMul, BatchNormalization, QLinearAveragePool, QLinearConcat                     |
| model/bvlcalexnet-12-int8.onnx        |    66.6667 | QLinearAdd, Softmax, LRN                                                                                                      |
| model/vgg16-12-int8.onnx              |    85.7143 | QLinearAdd                                                                                                                  |
| model/arcfaceresnet100-11-int8.onnx   |    70      | QLinearAdd, BatchNormalization, PRelu                                                                                         |
| model/ssd-12-int8.onnx                |    81.8182 | Softmax, Exp, NonMaxSuppression, QLinearAdd                                                                                    |
| model/fcn-resnet50-12-int8.onnx       |    90.9091 | QLinearAdd                                                                                                                  |
| model/ResNet101-DUC-12-int8.onnx      |    75      | Softmax, Sum                                                                                                                 |
| model/yolov3-12-int8.onnx             |    71.4286 | QLinearAdd, Exp, Sigmoid, QLinearLeakyRelu, NonMaxSuppression, Conv, Ceil, QLinearConcat                                           |
| model/FasterRCNN-12-int8.onnx         |    76.3158 | Softmax, Exp, QLinearAdd, Log, NonMaxSuppression, RoiAlign, Floor, Sqrt, QLinearSigmoid                                             |
| model/ssd_mobilenet_v1_12-int8.onnx   |    90.9091 | Exp, Sigmoid                                                                                                                 |
| model/MaskRCNN-12-int8.onnx           |    69.5652 | Softmax, Exp, QLinearAdd, And, Sigmoid, Log, NonMaxSuppression, ConvTranspose, RoiAlign, Floor, Sqrt, QLinearSigmoid, QLinearConcat, Not |