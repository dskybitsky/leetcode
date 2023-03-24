import { divide } from "./index";

describe('divide', () => {
    test('case 1', () => {
        expect(divide(10, 3)).toBe(3);
    });

    test('case 2', () => {
        expect(divide(7, -3)).toBe(-2);
    });

    test('case 3', () => {
        expect(divide(-2147483648, -1)).toBe(2147483647);
    });

    test('case 3', () => {
        expect(divide(4, 2)).toBe(2);
    });
});