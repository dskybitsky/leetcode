import { Trie } from "./index";

describe('Trie', () => {
    test('case 1', () => {
        const trie = new Trie();

        trie.insert("apple");

        expect(trie.search("apple")).toBe(true);
        expect(trie.search("app")).toBe(false);
        expect(trie.startsWith("app")).toBe(true);

        trie.insert("app");

        expect(trie.search("app")).toBe(true);
    });

    test('case 2', () => {
        const trie = new Trie();

        expect(trie.search("a")).toBe(false);
    })
})