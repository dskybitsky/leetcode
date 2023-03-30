import { ListNode, swapPairs } from "./index";

describe('swapPairs', () => {
    test('case 1', () => {
        const list = new ListNode(1, new ListNode(2, new ListNode(3, new ListNode(4))));

        expect(swapPairs(list)).toEqual(
            new ListNode(2, new ListNode(1, new ListNode(4, new ListNode(3))))
        )
    });
});