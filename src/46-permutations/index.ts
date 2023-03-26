export function permute(nums: number[], from = 0): number[][] {
    if (from == nums.length) {
        return [];
    }

    if (from === nums.length - 1) {
        return [[nums[from]]];
    }

    const result: number[][] = [];

    const nextPermutes = permute(nums, from + 1);

    for (let i = 0; i < nextPermutes.length; i++) {
        for (let j = 0; j <= nextPermutes[i].length; j++) {
            result.push(insert(nextPermutes[i], j, nums[from]));
        }
    }

    return result;
};

const insert = <T>(arr: T[], index: number, newItem: T) => [
    ...arr.slice(0, index),
    newItem,
    ...arr.slice(index)
]