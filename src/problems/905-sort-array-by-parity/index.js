var assert = require('assert');

var sortArrayByParity = function(nums) {
    const n = nums.length;

    let last = 0;

    for (let i = 0; i < n; i++) {
        if (nums[i] % 2 === 0) {
            const temp = nums[last];
            nums[last] = nums[i];
            nums[i] = temp;
            last++;
        }
    }

    return nums;
};

console.log(sortArrayByParity([3,1,2,4]));
