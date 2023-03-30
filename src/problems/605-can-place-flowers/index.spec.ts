import { canPlaceFlowers } from "./index";

describe('canPlaceFlowers', () => {
    test('case 1', () => {
        expect(canPlaceFlowers([1, 0, 0, 0, 1], 1)).toBe(true);
    });

    test('case 2', () => {
        expect(canPlaceFlowers([1, 0, 0, 0, 1], 2)).toBe(false);
    })
});