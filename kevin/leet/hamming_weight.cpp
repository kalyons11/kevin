#include "hamming_weight.h"

int Solution::hammingWeight(uint32_t n)
{
    int result = 0;
    uint32_t mask = 1;

    for (int i = 0; i < 32; i ++) {
        if ((mask & n) != 0) {
            result += 1;
        }
        mask = mask << 1;
    }

    return result;
}
