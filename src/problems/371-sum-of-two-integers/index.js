var assert = require('assert');

var getSum = function(a, b) {
    if ((a & b) == 0) {
        return a ^ b;
    }

    const xor = a ^ b;
    const carry = (a & b) << 1;

    return getSum(xor, carry);
};

assert(getSum(1, 2) == 3, "(1, 2) == 3");