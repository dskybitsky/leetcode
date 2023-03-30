class TrieNode {
    public readonly children: Map<string, TrieNode>;

    constructor(
        public isEnd: boolean = false
    ) {
        this.children = new Map<string, TrieNode>();
    }
}

export class Trie {
    private root: TrieNode | null;

    constructor() {
        this.root = new TrieNode();
    }

    insert(word: string): void {
        let current = this.root;

        for (let i = 0; i < word.length; i++) {
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

    search(word: string): boolean {
        const last = this.traverse(word);

        return last?.isEnd ?? false;
    }

    startsWith(prefix: string): boolean {
        const last = this.traverse(prefix);

        return last !== null;
    }

    private traverse(s: string): TrieNode | null {
        let current = this.root;

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
