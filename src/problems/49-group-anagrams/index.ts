export function groupAnagrams(strs: string[]): string[][] {
    const groupMap = new Map<string, string[]>();

    for (let i = 0; i < strs.length; i++) {
        const h = hashWord(strs[i]);

        if (groupMap.has(h)) {
            groupMap.get(h).push(strs[i]);
        } else {
            groupMap.set(h, [strs[i]]);
        }
    }

    return Array.from(groupMap.values());
};


function hashWord(str: string): string {
    let result = Array.from({ length: 26 }, () => 0);

    for (let i = 0; i < str.length; i++) {
        const code = str.charCodeAt(i) - 97;

        result[code]++;
    }

    return result.join(',');
}