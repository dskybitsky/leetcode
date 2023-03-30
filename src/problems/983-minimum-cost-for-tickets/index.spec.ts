import { mincostTickets } from "./index";

describe('mincostTickets', () => {
    test('case 1', () => {
        expect(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
            .toBe(11);
    });

    test('case 2', () => {
        expect(mincostTickets(
            [1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28],
            [3, 13, 45]
        )).toBe(44);
    });
});