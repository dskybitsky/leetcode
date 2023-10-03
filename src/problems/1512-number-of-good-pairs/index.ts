function numIdenticalPairs(nums: number[]): number {
    const index: number[] = [];
    let res = 0;

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];

        res += (index[num] ?? 0);

        index[num] = (index[num] ?? 0) + 1;
    }

    return res;
};

console.log(numIdenticalPairs([1,2,3,1,1,3]));