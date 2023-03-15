import { TreeNode, isCompleteTree } from "./index";

describe('isCompleteTree', () => {

    test('case 1', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2,
                    new TreeNode(4),
                    new TreeNode(5),
                ),
                new TreeNode(
                    3,
                    new TreeNode(6)
                )
            )
        )).toBe(true);
    });

    test('case 2', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2,
                    new TreeNode(4),
                    new TreeNode(5),
                ),
                new TreeNode(
                    3,
                    null,
                    new TreeNode(7)
                )
            )
        )).toBe(false);
    });

    test('case 3', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2,
                    new TreeNode(5),
                    new TreeNode(6),
                ),
                new TreeNode(
                    3,
                    new TreeNode(7),
                    new TreeNode(8)
                )
            )
        )).toBe(true);
    });

    test('case 4', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2
                ),
                new TreeNode(
                    3,
                    new TreeNode(7),
                    new TreeNode(8)
                )
            )
        )).toBe(false);
    });

    test('case 5', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2,
                    new TreeNode(5),
                ),
                new TreeNode(
                    3,
                    new TreeNode(7)
                )
            )
        )).toBe(false);
    });

    test('case 6', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2,
                    new TreeNode(5),
                    new TreeNode(6)
                ),
                new TreeNode(
                    3
                )
            )
        )).toBe(true);
    });

    test('case 7', () => {
        expect(isCompleteTree(
            new TreeNode(
                1,
                new TreeNode(
                    2
                )
            )
        )).toBe(true);
    });
})