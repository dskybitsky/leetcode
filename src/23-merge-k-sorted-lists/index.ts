export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val);
        this.next = (next===undefined ? null : next);
    }
}

export function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    if (lists.length === 0) {
        return null;
    }

    if (lists.length === 1) {
        return lists[0];
    }

    const mergedLists: Array<ListNode | null> = [];

    for (let i = 0; i < lists.length; i += 2) {
        mergedLists.push(
            i < lists.length - 1 
                ? mergeTwoLists(lists[i], lists[i + 1])
                : lists[i]
        );
    }

    return mergeKLists(mergedLists);
};

export function mergeTwoLists(head1: ListNode | null, head2: ListNode | null) {
    if (head1 === null) {
        return head2;
    }

    if (head2 === null) {
        return head1;
    }

    const head = head1.val <= head2.val ? head1 : head2;

    head.next = head1.val <= head2.val ? mergeTwoLists(head1.next, head2) : mergeTwoLists(head1, head2.next);

    return head;
}