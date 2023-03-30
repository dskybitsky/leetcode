export function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    const [nums1st, nums2nd] = nums1.length <= nums2.length 
        ? [nums1, nums2]
        : [nums2, nums1];

    return findMedianOrderedSortedArrays(nums1st, nums2nd);
}

function findMedianOrderedSortedArrays(nums1: number[], nums2: number[]): number {
    if (nums1.length === 0) {
        return findMedianArray(nums2);
    }

    const mid2 = Math.floor(nums2.length / 2);

    if (nums1.length === 1) {
        if (nums2.length === 1) {
            return findMedian2(nums1[0], nums2[0]);
        }

        if (nums2.length % 2 === 1) {
            return findMedian4(nums1[0], nums2[mid2 - 1], nums2[mid2], nums2[mid2 + 1]);
        }

        return findMedian3(nums1[0], nums2[mid2 - 1], nums2[mid2]);
    }

    if (nums1.length === 2) {
        if (nums2.length === 2) {
            return findMedian4(nums1[0], nums1[1], nums2[0], nums2[1]);
        }

        if (nums2.length % 2 === 1) {
            return findMedian3(
                nums2[mid2],
                Math.max(nums1[1], nums2[mid2 - 1]),
                Math.min(nums1[0], nums2[mid2 + 1])
            );
        }

        return findMedian4(
            nums2[mid2 - 1],
            nums2[mid2],
            Math.max(nums1[0], nums2[mid2 - 2]),
            Math.min(nums1[1], nums2[mid2 + 1])
        );
    }

    const idx1 = Math.floor((nums1.length - 1) / 2);
    const idx2 = Math.floor((nums2.length - 1) / 2);

    if(nums1[idx1] <= nums2[idx2]) {
        return findMedianOrderedSortedArrays(
            nums1.slice(idx1),
            nums2.slice(0, nums2.length - idx1)
        );
    }

    return findMedianOrderedSortedArrays(
        nums1.slice(0, nums1.length - idx1),
        nums2.slice(idx1)
    );
};

function findMedian2(num1: number, num2: number): number {
    return (num1 + num2) / 2;
}

function findMedian3(num1: number, num2: number, num3: number): number {
    return (
        num1 + num2 + num3 
        - Math.min(num1, num2, num3)
        - Math.max(num1, num2, num3)
    );
}

function findMedian4(num1: number, num2: number, num3: number, num4: number): number {
    return (
        num1 + num2 + num3 + num4 
        - Math.min(num1, num2, num3, num4)
        - Math.max(num1, num2, num3, num4)
    ) / 2;
}

function findMedianArray(nums: number[]): number {
    if (nums.length === 0) {
        return -1;
    }

    const mid = Math.floor(nums.length / 2);

    if (nums.length % 2 === 1) {
        return nums[mid];
    }

    return (nums[mid] + nums[mid - 1]) / 2;
}
    