#[starknet::contract]
mod OrionRunner {
    use orion::operators::tensor::{TensorTrait, FP16x16Tensor, Tensor};
    use orion::operators::nn::{NNTrait, FP16x16NN};
    use orion::numbers::FP16x16;
    use layer1::weights::tensor1 as w1;
    use layer1::bias::tensor1 as b1;
    use layern::weights::tensorn as wn;
    use layern::bias::tensorn as bn;
    use bench::functions as f;
    use bench::input::input;

    #[storage]
    struct Storage {
        id: u8,
    }

    const DEPTH: u32 = 50;

    #[external(v0)]
    fn main(self: @ContractState) {
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
}
