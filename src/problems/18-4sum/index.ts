export function fourSum(nums: number[], target: number): number[][] {
    nums.sort((a, b) => a - b);

    const result: number[][] = [];

    for (let i = 0; i < nums.length - 3; i++) {
        if (i > 0 && nums[i - 1] === nums[i]) {
            continue;
        }

        for (let j = i + 1; j < nums.length - 2; j++) {
            if (j > i + 1 && nums[j - 1] === nums[j]) {
                continue;
            }

            let left = j + 1;
            let right = nums.length - 1;

            while (left < right) {
                const sum = nums[i] + nums[j] + nums[left] + nums[right];

                if (sum === target) {
                    result.push([nums[i], nums[j], nums[left], nums[right]]);
                    
                    while (left < right && nums[left] === nums[left + 1]) {
                        left++;
                    }

                    left++;

                    while (left < right && nums[right] === nums[right - 1]) {
                        right--;
                    }

                    right--;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
            }
        }
    }

    return result;
};