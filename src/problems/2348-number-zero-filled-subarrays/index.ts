export function zeroFilledSubarray(nums: number[]): number {
    if (nums.length === 0) {
        return 0;
    }

    let result = 0;
    let zeroStart = -1;

    for (let i = 0; i < nums.length; i++) {
        if (
            nums[i] === 0 
            && (i === 0 || nums[i - 1] !== 0)
        ) {
            zeroStart = i;
        }

        if (nums[i] !== 0 && i > 0 && nums[i - 1] === 0) {
            result += countSubarraysInArray(i - zeroStart);
            zeroStart = -1;
        }
    }

    if (zeroStart >= 0) {
        result += countSubarraysInArray(nums.length - zeroStart);
    }

    return result;
};

function countSubarraysInArray(n: number): number {
    return (1 + n) * n / 2;
}