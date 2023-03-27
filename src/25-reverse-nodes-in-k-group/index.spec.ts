import { ListNode, reverseKGroup } from "./index";

describe('reverseKGroup', () => {
    test('case 1', () => {
        expect(reverseKGroup(
            new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))),
            2
        )).toEqual(
            new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(3, new ListNode(5))))),
        )
    });

    test('case 1', () => {
        expect(reverseKGroup(
            new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4, new ListNode(5))))),
            3
        )).toEqual(
            new ListNode(3, new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(5))))),
        )
    });
});