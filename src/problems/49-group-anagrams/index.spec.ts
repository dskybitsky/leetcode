import { groupAnagrams } from "./index";

describe('groupAnagrams', () => {
    test('case 1', () => {
        expect(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
            .toEqual([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]);
    });

    test('case 2', () => {
        expect(groupAnagrams(["a", "aa", "aaa"]))
            .toEqual([["a"], ["aa"], ["aaa"]]);
    });
});
