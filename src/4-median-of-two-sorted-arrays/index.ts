export function findMedianSortedArrays(nums1: number[], nums2: number[]): number {
    if (nums1.length === 0) {
        return findMedianSortedArray(nums2);
    }

    if (nums2.length === 0) {
        return findMedianSortedArray(nums1);
    }

    const overlapping = nums1[0] >= nums2[0] && nums1[0] <= nums2[nums2.length - 1]
        || nums1[nums1.length - 1] >= nums2[0] && nums1[nums1.length - 1] <= nums2[nums2.length - 1];

    if (!overlapping) {
        return findMedianSortedNonOverlappingArrays(nums1, nums2);
    }

    return 0;
};

function findMedianSortedNonOverlappingArrays(nums1: number[], nums2: number[]): number {
    const [leftNums, rightNums] = nums1[0] < nums2[0] ? [nums1, nums2] : [nums2, nums1];

    if (leftNums.length < rightNums.length) {
        return findMedianSortedArray(rightNums, (-1) * leftNums.length);
    }

    if (leftNums.length > rightNums.length) {
        return findMedianSortedArray(leftNums, rightNums.length);
    }

    return (leftNums[leftNums.length - 1] + rightNums[0]) / 2;
}

function findMedianSortedArray(nums: number[], offset = 0): number {
    if (nums.length === 0) {
        return 0;
    }

    const length = nums.length + Math.abs(offset);

    const mid = offset > 0 
        ? Math.floor(length / 2) 
        : Math.floor(length / 2) + offset;

    if (length % 2 === 1) {
        return nums[mid];
    }

    return (nums[mid] + nums[mid - 1]) / 2;
}
