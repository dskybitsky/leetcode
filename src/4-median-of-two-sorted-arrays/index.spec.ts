import { findMedianSortedArrays } from './index';

describe('findMedianSortedArrays', () => {
    test('case 1', () => {
        expect(findMedianSortedArrays([], [])).toBe(0);
    });

    test('case 2', () => {
        expect(findMedianSortedArrays([1, 2], [])).toBe(1.5);
        expect(findMedianSortedArrays([1, 2, 3], [])).toBe(2);
    });

    test('case 3', () => {
        expect(findMedianSortedArrays([], [3, 4])).toBe(3.5);
        expect(findMedianSortedArrays([], [3, 4, 5])).toBe(4);
    });

    test('case 4', () => {
        expect(findMedianSortedArrays([1], [2, 3])).toBe(2);
        expect(findMedianSortedArrays([1], [2, 3, 4])).toBe(2.5);

        expect(findMedianSortedArrays([1, 2], [3])).toBe(2);
        expect(findMedianSortedArrays([1, 2, 3], [4])).toBe(2.5);

        expect(findMedianSortedArrays([1, 2], [3, 4])).toBe(2.5);
        expect(findMedianSortedArrays([3, 4], [1, 2])).toBe(2.5);
    });

    // test('case 1', () => {
    //     expect(findMedianSortedArrays([1, 3], [2])).toBe(2);
    // });

    // test('case 2', () => {
    //     expect(findMedianSortedArrays([1, 3], [2, 4])).toBe(2.5);
    // });
});
