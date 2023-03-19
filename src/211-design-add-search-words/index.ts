export class WordDictionary {
    private root: TrieNode = new TrieNode();

    constructor() {

    }

    addWord(word: string): void {
        let current = this.root;

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

    search(word: string, root: TrieNode = this.root): boolean {
        let current = root;

        for (let i = 0; i < word.length; i++) {
            if (word[i] === '.') {
                for (const [key, value] of current.children) {
                    if (this.search(word.substring(i + 1), value)) {
                        return true;
                    }
                }

                return false;
            }

            const next = current.children.get(word[i]);

            if (!next) {
                return false;
            }

            current = next;
        }

        return current.isEnd;
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