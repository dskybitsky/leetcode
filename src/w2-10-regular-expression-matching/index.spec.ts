import { isMatch } from "./index";

describe('isMatch', () => {
    it ('checks basic strings', () => {
        expect(isMatch('a', 'a')).toBe(true);
    })
});
