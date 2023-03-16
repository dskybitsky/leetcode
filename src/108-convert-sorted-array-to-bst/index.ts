export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.left = (left===undefined ? null : left);
        this.right = (right===undefined ? null : right);
    }
}

export function sortedArrayToBST(nums: number[], from = 0, to = nums.length - 1): TreeNode | null {
    if (from > to) {
        return null;
    }

    const mid = from + Math.floor((to - from) / 2);

    const root = new TreeNode(nums[mid]);

    root.left = sortedArrayToBST(nums, from, mid - 1);
    root.right = sortedArrayToBST(nums, mid + 1, to);

    return root;
};
