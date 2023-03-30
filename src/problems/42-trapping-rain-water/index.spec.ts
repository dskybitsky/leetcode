import { trap } from "./index";

describe('trap', () => {
    test('case 1', () => {
        expect(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
            .toBe(6);
    });

    test('case 2', () => {
        expect(trap([4, 2, 0, 3, 2, 5]))
            .toBe(9);
    });

    test('case 3', () => {
        expect(trap([9, 6, 8, 8, 5, 6, 3]))
            .toBe(3);
    })
});