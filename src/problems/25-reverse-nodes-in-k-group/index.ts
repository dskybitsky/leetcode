export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

export function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    let newHead: ListNode | null = null;
    let oldTail: ListNode | null = null;

    let slow = head;
    let fast = slow;

    while (fast) {
        let i = 1;

        while (fast && i < k) {
            i++;
            fast = fast.next;
        }

        if (!fast) {
            break;
        }
        
        const next = fast.next;

        const reverseHead = reverseList(slow, fast);

        if (newHead === null) {
            newHead = reverseHead;
        } else {
            oldTail.next = reverseHead;
        }

        oldTail = slow;

        slow = next;
        fast = slow;
    }

    return newHead;
};

export function reverseList(head: ListNode, tail: ListNode): ListNode {
    if (head === tail) {
        return head;
    }

    const nextHead = head.next;

    head.next = tail.next;
    tail.next = head;

    return reverseList(nextHead, tail);
}