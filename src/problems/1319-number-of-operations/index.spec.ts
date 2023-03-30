import { makeConnected } from "./index";

describe('makeConnected', () => {
    test('case 1', () => {
        expect(makeConnected(4, [[0, 1], [0, 2], [1, 2]]))
            .toBe(1);
    });

    test('case 2', () => {
        expect(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]))
            .toBe(2);
    });

    test('case 3', () => {
        expect(makeConnected(6, [[0, 1], [0, 2], [0, 3], [1, 2]]))
            .toBe(-1);
    });

    test('case 4', () => {
        expect(makeConnected(5, [[0, 1], [0, 2], [3, 4], [2, 3]]))
            .toBe(0);
    });

    test('case 5', () => {
        expect(makeConnected(12, [[1,5],[1,7],[1,2],[1,4],[3,7],[4,7],[3,5],[0,6],[0,1],[0,4],[2,6],[0,3],[0,2]]))
            .toBe(4);
    });
});