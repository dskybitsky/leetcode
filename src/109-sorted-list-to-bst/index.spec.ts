describe('isMatch', () => {
    test('case 1', () => {
        const list = new ListNode(
            -10,
            new ListNode(
                -3,
                new ListNode(
                    0,
                    new ListNode(
                        5,
                        new ListNode(
                            9
                        )
                    )
                )
            )
        );

        expect(sortedListToBST(list)).toEqual(
            new TreeNode(
                0,
                new TreeNode(
                    -3,
                    new TreeNode(
                        -10
                    )
                ),
                new TreeNode(
                    9,
                    new TreeNode(
                        5
                    )
                )
            )
        );
    });


});