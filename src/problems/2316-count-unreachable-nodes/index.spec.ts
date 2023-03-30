import { countPairs } from "./index";

describe('countPairs', () => {
    test('case 1', () => {
        expect(countPairs(3, [[0, 1], [0, 2], [1, 2]]))
            .toBe(0);
    });

    test('case 2', () => {
        expect(countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
            .toBe(14);
    });
});