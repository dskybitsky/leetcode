import { isMatch } from "./index";

describe('isMatch', () => {
    test('case 1', () => {
        expect(isMatch("aa", "a")).toBe(false);
    });

    test('case 2', () => {
        expect(isMatch("aa", "*")).toBe(true);
    });

    test('case 3', () => {
        expect(isMatch("cb", "?a")).toBe(false);
    })
});