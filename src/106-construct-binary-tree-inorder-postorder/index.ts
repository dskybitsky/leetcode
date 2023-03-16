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

    const leftPostorder = postorder.slice(0, leftInorder.length);
    const rightPostorder = postorder.slice(leftInorder.length, postorder.length - 1);

    const root = new TreeNode(rootVal);
    
    root.left = buildTree(leftInorder, leftPostorder);
    root.right = buildTree(rightInorder, rightPostorder);

    return root;
};