| Model                                 |   Coverage | Missing Operators                                                                                                 |
|---------------------------------------|------------|-------------------------------------------------------------------------------------------------------------------|
| model/bidaf-11-int8.onnx              |    84.8485 | ReduceSum, CategoryMapper, Log, DynamicQuantizeLinear, DynamicQuantizeLSTM                                        |
| model/bertsquad-12-int8.onnx          |    77.7778 | Sqrt, Identity, DynamicQuantizeLinear, ReduceMean, Reciprocal, FusedMatMul                                        |
| model/mnist-12-int8.onnx              |    85.7143 | QLinearAdd                                                                                                        |
| model/mobilenetv2-12-int8.onnx        |    81.8182 | QLinearGlobalAveragePool, QLinearAdd                                                                              |
| model/googlenet-12-int8.onnx          |    72.7273 | AveragePool, QLinearAdd, LRN                                                                                      |
| model/inception-v1-12-int8.onnx       |    60      | QLinearAveragePool, QLinearConcat, Gemm, LRN                                                                      |
| model/resnet50-v1-12-int8.onnx        |    75      | QLinearGlobalAveragePool, QLinearAdd                                                                              |
| model/caffenet-12-int8.onnx           |    77.7778 | QLinearAdd, LRN                                                                                                   |
| model/squeezenet1.0-12-int8.onnx      |    85.7143 | QLinearGlobalAveragePool                                                                                          |
| model/efficientnet-lite4-11-int8.onnx |    77.7778 | QLinearAveragePool, QLinearAdd                                                                                    |
| model/zfnet512-12-int8.onnx           |    77.7778 | QLinearAdd, LRN                                                                                                   |
| model/shufflenet-v2-12-int8.onnx      |    81.8182 | QLinearAdd, ReduceMean                                                                                            |
| model/densenet-12-int8.onnx           |    46.1538 | QLinearGlobalAveragePool, QLinearAdd, QLinearAveragePool, QLinearMul, QLinearConcat, BatchNormalization, Conv     |
| model/bvlcalexnet-12-int8.onnx        |    77.7778 | QLinearAdd, LRN                                                                                                   |
| model/vgg16-12-int8.onnx              |    85.7143 | QLinearAdd                                                                                                        |
| model/arcfaceresnet100-11-int8.onnx   |    70      | BatchNormalization, PRelu, QLinearAdd                                                                             |
| model/ssd-12-int8.onnx                |    90.9091 | NonMaxSuppression, QLinearAdd                                                                                     |
| model/fcn-resnet50-12-int8.onnx       |    90.9091 | QLinearAdd                                                                                                        |
| model/ResNet101-DUC-12-int8.onnx      |   100      |                                                                                                                   |
| model/yolov3-12-int8.onnx             |    82.1429 | QLinearAdd, QLinearLeakyRelu, QLinearConcat, Conv, NonMaxSuppression                                              |
| model/FasterRCNN-12-int8.onnx         |    81.5789 | Floor, QLinearAdd, Sqrt, Log, QLinearSigmoid, RoiAlign, NonMaxSuppression                                         |
| model/ssd_mobilenet_v1_12-int8.onnx   |   100      |                                                                                                                   |
| model/MaskRCNN-12-int8.onnx           |    76.087  | Floor, QLinearAdd, Sqrt, ConvTranspose, Log, And, QLinearSigmoid, RoiAlign, QLinearConcat, Not, NonMaxSuppression |

Average coverage: 80.00107201082231
