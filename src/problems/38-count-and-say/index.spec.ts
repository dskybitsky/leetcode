import { countAndSay } from "./index";

describe('countAndSay', () => {
    test('case 1', () => {
        expect(countAndSay(1)).toEqual('1');
    });

    test('case 2', () => {
        expect(countAndSay(2)).toEqual('11');
    });

    test('case 3', () => {
        expect(countAndSay(3)).toEqual('21');
    });

    test('case 4', () => {
        expect(countAndSay(4)).toEqual('1211');
    });
});