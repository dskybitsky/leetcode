import { zeroFilledSubarray } from './index';

describe('zeroFilledSubarray', () => {
    test('case 1', () => {
        expect(zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4])).toBe(6);
    });

    test('case 2', () => {
        expect(zeroFilledSubarray([0, 0, 0, 2, 0, 0])).toBe(9);
    })
});