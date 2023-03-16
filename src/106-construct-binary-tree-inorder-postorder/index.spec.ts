import { TreeNode, buildTree } from "./index";

describe('buildTree', () => {
    test('case 1', () => {
        expect(buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))
            .toEqual(
                new TreeNode(
                    3,
                    new TreeNode(9),
                    new TreeNode(
                        20,
                        new TreeNode(15),
                        new TreeNode(7)
                    )
                )
            );
    });

    test('case 3', () => {
        expect(buildTree([2, 3, 1], [3, 2, 1]))
            .toEqual(
                new TreeNode(
                    1,
                    new TreeNode(
                        2,
                        null,
                        new TreeNode(3)
                    ),
                )
            );
    });

    test('case 4', () => {
        expect(buildTree([3, 2, 1], [3, 2, 1]))
            .toEqual(
                new TreeNode(
                    1,
                    new TreeNode(
                        2,
                        new TreeNode(3)
                    ),
                )
            );
    });
});