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
    })
});