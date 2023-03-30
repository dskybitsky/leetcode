import { ListNode, reverseKGroup, reverseList } from "./index";

describe('reverseKGroup', () => {
    test('case 1', () => {
        expect(reverseKGroup(
            new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))),
            2
        )).toEqual(
            new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(3, new ListNode(5))))),
        )
    });

    test('case 2', () => {
        expect(reverseKGroup(
            new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))),
            3
        )).toEqual(
            new ListNode(3, new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(5))))),
        )
    });

    test('case 3', () => {
        expect(reverseKGroup(
            new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5, new ListNode(6)))))),
            2
        )).toEqual(
            new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(3, new ListNode(6, new ListNode(5)))))),
        )
    });
});

describe('reverseList', () => {
    test('case 1', () => {
        const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

        expect(reverseList(head, head.next.next))
            .toEqual(
                new ListNode(3, new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(5))))),
            );
    });

    test('case 2', () => {
        const head = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5)))));

        expect(reverseList(head, head.next))
            .toEqual(
                new ListNode(2, new ListNode(1, new ListNode(3, new ListNode(4, new ListNode(5))))),
            );
    });
});