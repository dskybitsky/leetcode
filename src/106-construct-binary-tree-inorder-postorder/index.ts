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
    inorderFrom = 0,
    inorderTo = inorder.length - 1,
    postorderFrom = 0,
    postorderTo = postorder.length - 1
): TreeNode | null {
    if (inorderFrom > inorderTo || postorderFrom > postorderTo) {
        return null;
    }

    const rootVal = postorder[postorderTo];

    const inorderSplitIndex = inorder.indexOf(rootVal);

    const inorderOffset = inorderSplitIndex - inorderFrom;

    const leftInorderFrom = inorderFrom;
    const leftInorderTo = inorderSplitIndex - 1;

    const leftPostorderFrom = postorderFrom;
    const leftPostorderTo = postorderFrom + inorderOffset - 1;

    const rightInorderFrom = inorderSplitIndex + 1;
    const rightInorderTo = inorderTo;

    const rightPostorderFrom = postorderFrom + inorderOffset;
    const rightPostorderTo = postorderTo - 1;

    const root = new TreeNode(rootVal);
    
    root.left = buildTree(inorder, postorder, leftInorderFrom, leftInorderTo, leftPostorderFrom, leftPostorderTo);
    root.right = buildTree(inorder, postorder, rightInorderFrom, rightInorderTo, rightPostorderFrom, rightPostorderTo);

    return root;
};