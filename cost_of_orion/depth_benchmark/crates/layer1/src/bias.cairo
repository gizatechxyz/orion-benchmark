use array::{SpanTrait, ArrayTrait};
use orion::operators::tensor::{TensorTrait, FP16x16Tensor, Tensor};
use orion::numbers::{FixedTrait, FP16x16};

fn tensor1() -> Tensor<FP16x16> {
    TensorTrait::<FP16x16>::new(
        array![10].span(),
        array![
            FixedTrait::<FP16x16>::new(1131, false),
            FixedTrait::<FP16x16>::new(21563, false),
            FixedTrait::<FP16x16>::new(70269, true),
            FixedTrait::<FP16x16>::new(33872, true),
            FixedTrait::<FP16x16>::new(49311, false),
            FixedTrait::<FP16x16>::new(60718, true),
            FixedTrait::<FP16x16>::new(15261, true),
            FixedTrait::<FP16x16>::new(61792, true),
            FixedTrait::<FP16x16>::new(52747, false),
            FixedTrait::<FP16x16>::new(45587, false)
        ]
            .span()
    )
}

