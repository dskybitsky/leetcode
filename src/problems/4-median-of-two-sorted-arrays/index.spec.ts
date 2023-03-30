import { findMedianSortedArrays } from './index';

describe('findMedianSortedArrays', () => {
    test('case 1', () => {
        expect(findMedianSortedArrays([], [])).toBe(-1);
        expect(findMedianSortedArrays([], [1])).toBe(1);
        expect(findMedianSortedArrays([], [1, 2])).toBe(1.5);
        expect(findMedianSortedArrays([], [1, 2, 3])).toBe(2);
    });

    test('case 2', () => {
        expect(findMedianSortedArrays([1], [2])).toBe(1.5);
        expect(findMedianSortedArrays([1], [2, 3])).toBe(2);
        expect(findMedianSortedArrays([1], [1, 2, 3])).toBe(1.5);
    });

    test('case 3', () => {
        expect(findMedianSortedArrays([1, 2], [3, 4])).toBe(2.5);
        expect(findMedianSortedArrays([1, 2], [3, 4, 5])).toBe(3);
        expect(findMedianSortedArrays([1, 2], [3, 4, 5, 6])).toBe(3.5);
        expect(findMedianSortedArrays([2, 3], [4, 5, 6, 7])).toBe(4.5);
    });

    test('case 4', () => {
        expect(findMedianSortedArrays([1, 2, 3], [3, 4, 5])).toBe(3);
        expect(findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7])).toBe(4);
        expect(findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7])).toBe(4);
        expect(findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7, 8])).toBe(4.5);
        expect(findMedianSortedArrays([1, 2, 3], [4, 5, 6, 7, 8])).toBe(4.5);
        expect(findMedianSortedArrays([1, 5, 6], [2, 3, 4, 7, 8])).toBe(4.5);
        expect(findMedianSortedArrays([2, 2, 4, 4], [2, 2, 4, 4])).toBe(3);
        expect(findMedianSortedArrays([1, 4, 5, 6], [2, 3, 7, 8])).toBe(4.5);
    });
});
