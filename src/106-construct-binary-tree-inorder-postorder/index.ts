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

export function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    if (!postorder.length) {
        return null;
    }

    const rootVal = postorder[postorder.length - 1];

    const inorderSplitIndex = inorder.indexOf(rootVal);

    const leftInorder = inorder.slice(0, inorderSplitIndex);
    const rightInorder = inorder.slice(inorderSplitIndex + 1);

    const leftPostorder = [];
    const rightPostorder = [];

    for (let i = postorder.length - 2; i >= 0; i--) {
        const index = leftInorder.indexOf(postorder[i]);

        if (index < 0) {
            rightPostorder.unshift(postorder[i]);
        } else {
            leftPostorder.unshift(postorder[i]);
        }
    }

    const root = new TreeNode(rootVal);
    
    root.left = buildTree(leftInorder, leftPostorder);
    root.right = buildTree(rightInorder, rightPostorder);

    return root;
};