use array::{SpanTrait, ArrayTrait};
use orion::operators::tensor::{TensorTrait, FP16x16Tensor, Tensor};
use orion::numbers::{FixedTrait, FP16x16};
fn tensorn() -> Tensor<FP16x16> {
TensorTrait::<FP16x16>::new(array![10].span(), array![FixedTrait::<FP16x16>::new(40240, false), FixedTrait::<FP16x16>::new(53643, false), FixedTrait::<FP16x16>::new(56630, false), FixedTrait::<FP16x16>::new(38457, true), FixedTrait::<FP16x16>::new(55352, false), FixedTrait::<FP16x16>::new(3760, true), FixedTrait::<FP16x16>::new(44238, false), FixedTrait::<FP16x16>::new(72195, false), FixedTrait::<FP16x16>::new(8617, true), FixedTrait::<FP16x16>::new(3523, true)].span())
}

