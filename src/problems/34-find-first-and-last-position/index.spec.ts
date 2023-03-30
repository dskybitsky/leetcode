import { findBeginning, findEnd, findNum, searchRange } from './index';

describe('searchRange', () => {
    test('case 1', () => {
        expect(searchRange([5, 7, 7, 8, 8, 10], 8))
            .toEqual([3, 4]);
    });
});

describe('Helper Methods', () => {
    describe('findNum', () => {
        test('common case', () => {
            expect(findNum([], 0)).toBe(-1);
    
            expect(findNum([1], 0)).toBe(-1);
            expect(findNum([1], 1)).toBe(0);
            expect(findNum([1], 2)).toBe(-1);
    
            expect(findNum([1, 2], 0)).toBe(-1);
            expect(findNum([1, 2], 1)).toBe(0);
            expect(findNum([1, 2], 2)).toBe(1);
            expect(findNum([1, 2], 3)).toBe(-1);
    
            expect(findNum([1, 2, 3], 0)).toBe(-1);
            expect(findNum([1, 2, 3], 1)).toBe(0);
            expect(findNum([1, 2, 3], 2)).toBe(1);
            expect(findNum([1, 2, 3], 3)).toBe(2);
            expect(findNum([1, 2, 3], 4)).toBe(-1);
        });
    });
    
    describe('findBeginning', () => {
        test('common case', () => {
            expect(findBeginning([3, 3, 3], 3, 0, 0)).toBe(0);
            expect(findBeginning([3, 3, 3], 3, 0, 1)).toBe(0);
            expect(findBeginning([3, 3, 3], 3, 0, 2)).toBe(0);
    
            expect(findBeginning([1, 2, 3, 3, 3], 3, 0, 2)).toBe(2);
            expect(findBeginning([1, 2, 3, 3, 3], 3, 0, 3)).toBe(2);
            expect(findBeginning([1, 2, 3, 3, 3], 3, 0, 4)).toBe(2);
        });
    });
    
    describe('findEnd', () => {
        test('common case', () => {
            expect(findEnd([3, 3, 3], 3, 0, 2)).toBe(2);
            expect(findEnd([3, 3, 3], 3, 1, 2)).toBe(2);
            expect(findEnd([3, 3, 3], 3, 2, 2)).toBe(2);
    
            expect(findEnd([3, 3, 3, 4, 5], 3, 0, 4)).toBe(2);
            expect(findEnd([3, 3, 3, 4, 5], 3, 1, 4)).toBe(2);
            expect(findEnd([3, 3, 3, 4, 5], 3, 2, 4)).toBe(2);
        });
    });
});

