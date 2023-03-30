import { maxSatisfaction } from "./index";

describe('maxSatisfaction', () => {
    test('case 1', () => {
        expect(maxSatisfaction([-1,-8,0,5,-9]))
            .toBe(14);
    });

    test('case 2', () => {
        expect(maxSatisfaction([4,3,2]))
            .toBe(20);
    });

    test('case 3', () => {
        expect(maxSatisfaction([-1,-4,-5]))
            .toBe(0);
    });
});