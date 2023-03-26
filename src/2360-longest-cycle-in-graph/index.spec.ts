import { longestCycle } from "./index";

describe('longestCycle', () => {
    test('case 1', () => {
        expect(longestCycle([3, 3, 4, 2, 3]))
            .toBe(3);
    });

    test('case 2', () => {
        expect(longestCycle([2, -1, 3, 1]))
            .toBe(-1);
    });
});