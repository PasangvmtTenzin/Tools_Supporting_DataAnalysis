def mask_sum(data, mask):
    res = 0
    for val, mask_val in zip(data, mask):
       if mask_val != 0:
            res += val
    return res

def test_mask_sum():
    assert mask_sum(data=[], mask=[]) == 0 # type: ignore
    assert mask_sum([1]*5, [1]*5) == 5

def test_mask_sum_zeros():
    assert mask_sum([1]*5, [0]*5) == 0
