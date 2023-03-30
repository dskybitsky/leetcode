import { minReorder } from "./index";

describe('minReorder', () => {
    test('case 1', () => {
        expect(minReorder(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
            .toBe(3);
    });

    test('case 3', () => {
        expect(minReorder(3, [[1, 0], [2, 0]]))
            .toBe(0);
    })
});