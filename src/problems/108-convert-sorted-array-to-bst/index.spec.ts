import { TreeNode, sortedArrayToBST } from "./index";

describe('sortedArrayToBST', () => {
    test('case 1', () => {
        expect(sortedArrayToBST([-10, -3, 0, 5, 9])).toEqual(
            new TreeNode(
                0,
                new TreeNode(
                    -10,
                    null,
                    new TreeNode(-3)
                ),
                new TreeNode(
                    5,
                    null,
                    new TreeNode(9)
                )
            )
        )
    });
});