import { findMedianSortedArrays } from './index';

describe('findMedianSortedArrays', () => {
    test('case 1', () => {
        expect(findMedianSortedArrays([1, 3], [2])).toBe(2);
    });

    test('case 2', () => {
        expect(findMedianSortedArrays([1, 3], [2, 4])).toBe(2.5);
    });
});
