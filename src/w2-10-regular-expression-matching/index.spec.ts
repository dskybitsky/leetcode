import { isMatch } from "./index";

describe('isMatch', () => {
    test ('plain strings', () => {
        expect(isMatch('a', 'a')).toBe(true);
        expect(isMatch('a', 'b')).toBe(false);
        expect(isMatch('abc', 'a')).toBe(false);
        expect(isMatch('a', 'abc')).toBe(false);
        expect(isMatch('abc', 'abc')).toBe(true);
        expect(isMatch('aa', 'a')).toBe(false);
        expect(isMatch('a', 'aa')).toBe(false);
        expect(isMatch('aaa', 'aaaa')).toBe(false);
        expect(isMatch('aa', 'aa')).toBe(true);
    });

    test ('dot chars', () => {
        expect(isMatch('a', '.')).toBe(true);
        expect(isMatch('ab', '.b')).toBe(true);
        expect(isMatch('abc', 'a.c')).toBe(true);
        expect(isMatch('a', '..')).toBe(false);
        expect(isMatch('abc', '.b.')).toBe(true);
    });

    test('wildcard', () => {
        expect(isMatch('aaa', 'a*')).toBe(true);
        expect(isMatch('aaa', 'a*a')).toBe(true);
        expect(isMatch('aaa', 'aa*')).toBe(true);
        expect(isMatch('aaa', 'b*a*')).toBe(true);
        expect(isMatch('aaa', 'b*')).toBe(false);
    });

    test('cases', () => {
        expect(isMatch('a', 'ab*')).toBe(true);
        expect(isMatch('aaa', 'ab*ac*a')).toBe(true);
        expect(isMatch('a', '.*')).toBe(true);
        expect(isMatch('mississippi', 'mis*is*ip*.')).toBe(true);
    })
});
