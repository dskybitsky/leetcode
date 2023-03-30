export function searchRange(nums: number[], target: number): number[] {
    const targetIndex = findNum(nums, target);

    if (targetIndex < 0) {
        return [-1, -1];
    }

    return [
        findBeginning(nums, target, 0, targetIndex),
        findEnd(nums, target, targetIndex, nums.length - 1),
    ];
};

export function findNum(nums: number[], target: number, from = 0, to = nums.length - 1): number {
    if (from > to) {
        return -1;
    }

    if (from === to) {
        return nums[from] === target ? from : -1;
    }

    const mid = from + Math.floor((to - from) / 2);

    if (nums[mid] === target) {
        return mid;
    }

    if (nums[mid] > target) {
        return findNum(nums, target, from, mid - 1);
    }

    return findNum(nums, target, mid + 1, to);
}

export function findBeginning(nums: number[], target: number, from: number, to: number): number {
    if (from >= to) {
        return to;
    }

    const mid = from + Math.floor((to - from) / 2);

    if (nums[mid] === target) {
        return findBeginning(nums, target, from, mid);
    }

    return findBeginning(nums, target, mid + 1, to);
}

export function findEnd(nums: number[], target: number, from: number, to: number): number {
    if (from >= to) {
        return to;
    }

    const mid = to - Math.floor((to - from) / 2);

    if (nums[mid] === target) {
        return findEnd(nums, target, mid, to);
    }

    return findEnd(nums, target, from, mid - 1);
}