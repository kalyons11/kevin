#include <iostream>
#include <assert.h>
#include "hamming_weight.h"

using namespace std;

void baseTestHammingWeight(uint32_t n, int expected) {
    int actual = Solution::hammingWeight(n);
    assert (expected == actual);
}

void testHammingWeightBasic() {
    baseTestHammingWeight(11, 3);
}

void testHammingWeightBig() {
    baseTestHammingWeight(128, 1);
}

void testHammingWeightNegative() {
    baseTestHammingWeight(-3, 31);
}

int main() {
    testHammingWeightBasic();
    testHammingWeightBig();
    testHammingWeightNegative();
    return 0;
}
