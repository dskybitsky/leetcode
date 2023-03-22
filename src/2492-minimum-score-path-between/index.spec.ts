import { minScore } from "./index";

describe('minScore', () => {
    test('case 1', () => {
        expect(minScore(4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]]))
            .toBe(5);
    });


    test('case 2', () => {
        expect(minScore(4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]]))
            .toBe(2);
    });
});