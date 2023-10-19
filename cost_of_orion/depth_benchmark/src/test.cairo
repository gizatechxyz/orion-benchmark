use orion::operators::tensor::{TensorTrait, FP16x16Tensor, Tensor};
use orion::operators::nn::{NNTrait, FP16x16NN};
use orion::numbers::FP16x16;
use layer1::weights::tensor1 as w1;
use layer1::bias::tensor1 as b1;
use layern::weights::tensorn as wn;
use layern::bias::tensorn as bn;
use bench::functions as f;
use bench::input::input;

const DEPTH: u32 = 10000;

#[test]
#[available_gas(2000000000000)]
fn test_() {
    let mut x = input();
    let mut i = 1;
    loop {
        if i == 1 {
            x = f::lin(x, w1(), b1());
            x = f::relu(x);
        } else {
            let mut x = f::lin(x, wn(), bn()); // Shadowing to avoid overflow
            x = f::relu(x);
        }

        if i == DEPTH {
            break;
        };

        i += 1;
    };
}

