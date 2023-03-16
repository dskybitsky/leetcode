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

export function buildTree(
    inorder: number[], 
    postorder: number[],
    inorderLeft = 0,
    inorderRight = inorder.length - 1,
    postorderLeft = 0,
    postorderRight = postorder.length - 1
): TreeNode | null {
    if (postorderLeft > postorderRight) {
        return null;
    }

    const rootVal = postorder[postorderRight];

    const inorderSplitIndex = inorder.indexOf(rootVal);

    const leftInorder = inorder.slice(0, inorderSplitIndex);
    const rightInorder = inorder.slice(inorderSplitIndex + 1);

    const leftPostorder = postorder.slice(0, inorderSplitIndex);
    const rightPostorder = postorder.slice(inorderSplitIndex, postorder.length - 1);

    const root = new TreeNode(rootVal);
    
    root.left = buildTree(leftInorder, leftPostorder);
    root.right = buildTree(rightInorder, rightPostorder);

    return root;
};