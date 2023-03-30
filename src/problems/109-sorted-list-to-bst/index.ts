export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
 }
 
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

let current: ListNode | null;
 
export function sortedListToBST(head: ListNode | null): TreeNode | null {
    let n = 0;
    let p = head;

    while (p) {
        p = p.next;
        n++;
    }

    current = head;

    return buildTree(n);
};

function buildTree(n: number): TreeNode | null {
    if (n <= 0) {
        return null;
    }

    const left = buildTree(Math.floor(n / 2));

    const root = new TreeNode(current.val);

    root.left = left;

    current = current.next;

    root.right = buildTree(n - Math.floor(n / 2) - 1);

    return root;
}