import { ListNode, mergeKLists, mergeTwoLists } from "./index";

describe('mergeKLists', () => {
    test('case 1', () => {
        const lists = [
            new ListNode(1, new ListNode(4, new ListNode(5))),
            new ListNode(1, new ListNode(3, new ListNode(4))),
            new ListNode(2, new ListNode(6)),
        ];

        expect(mergeKLists(lists)).toEqual(
            new ListNode(1, 
                new ListNode(1, 
                    new ListNode(2, 
                        new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5, new ListNode(6)))))
                    )
                )
            )
        )
    });
});

describe('mergeTwoLists', () => {
    test('case 1', () => {
        const lists = [
            new ListNode(1, new ListNode(4, new ListNode(5))),
            new ListNode(1, new ListNode(3, new ListNode(4))),
            new ListNode(2, new ListNode(6)),
        ];

        expect(mergeTwoLists(
            new ListNode(1, new ListNode(4, new ListNode(5))),
            new ListNode(1, new ListNode(3, new ListNode(4))),
        )).toEqual(
            new ListNode(1, 
                new ListNode(1,
                    new ListNode(3, new ListNode(4, new ListNode(4, new ListNode(5))))
                )
            )
        )
    });
});