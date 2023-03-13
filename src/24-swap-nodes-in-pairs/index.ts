export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

export function swapPairs(head: ListNode | null): ListNode | null {
    if (head === null) {
        return null;
    }

    if (head.next === null) {
        return head;
    }

    let current = head.next.next;

    let newHead = head.next;
    
    newHead.next = head;

    let newTail = newHead.next;

    newTail.next = null;

    while (current !== null && current.next !== null) {
        const p1 = current;
        const p2 = current.next;
        const p3 = current.next.next;

        newTail.next = p2;
        newTail.next.next = p1;
        newTail = newTail.next.next;
        newTail.next = null;    

        current = p3;
    }

    newTail.next = current;

    return newHead;
};