export class WordDictionary {
    private prefixRoot: TrieNode = new TrieNode();

    constructor() {

    }

    addWord(word: string): void {
        this.insert(this.prefixRoot, word);
    }

    search(word: string): boolean {
        return this.traverse(this.prefixRoot, word)?.isEnd ?? false;
    }

    private insert(root: TrieNode, word: string): void {
        let current = root;

        for (let i = 0; i < word.length; i++) {
            current.lengths.set(word.length - i, true);

            const char = word[i];

            let next = current.children.get(char);

            if (!next) {
                next = new TrieNode();
                current.children.set(char, next);
            }

            if (i === word.length - 1) {
                next.isEnd = true;
            }

            current = next;
        }
    }

    private traverse(root: TrieNode, s: string): TrieNode | null {
        let current = root;

        for (let i = 0; i < s.length; i++) {
            const next = current.children.get(s[i]);

            if (!next) {
                return null;
            }

            current = next;
        }

        return current;
    }
}

class TrieNode {
    public readonly children: Map<string, TrieNode>;
    public readonly lengths: Map<number, boolean>;

    constructor(
        public isEnd: boolean = false
    ) {
        this.children = new Map<string, TrieNode>();
        this.lengths = new Map<number, boolean>();
    }
}