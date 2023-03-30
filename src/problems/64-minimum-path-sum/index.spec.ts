import { minPathSum } from "./index";

describe('minPathSum', () => {
    test('case 1', () => {
        expect(minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
            .toBe(7);
    });

    test('case 2', () => {
        expect(minPathSum([[1, 2, 3], [4, 5, 6]]))
            .toBe(12);
    });
});