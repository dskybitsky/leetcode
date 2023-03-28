import { mincostTickets } from "./index";

describe('mincostTickets', () => {
    test('case 1', () => {
        expect(mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15]))
            .toBe(11);
    });
});