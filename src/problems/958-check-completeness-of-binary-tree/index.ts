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

export function isCompleteTree(root: TreeNode | null): boolean {
    if (root === null) {
        return true;
    }
    
    const queue: TreeNode[] = [];

    queue.push(root);

    let incomplete = false;

    while (queue.length > 0) {
        const size = queue.length;

        for (let i = 0; i < size; i++) {
            const node = queue.shift();

            if (node.left === null && node.right !== null) {
                return false;
            }

            if (node.left !== null) {
                queue.push(node.left);

                if (incomplete) {
                    return false;
                }
            } else {
                incomplete = true;
            }

            if (node.right !== null) {
                queue.push(node.right);

                if (incomplete) {
                    return false;
                }
            } else {
                incomplete = true;
            }
        }
    }

    return true;
}