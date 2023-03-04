export function isMatch(s: string, p: string): boolean {
    var i = 0;
    var pi = 0;

    while (i < s.length) {
        if (pi === p.length) {
            return false;
        }

        if (isMatchChar(s[i], p[pi])) {
            i++;
            pi++;
            continue;
        }

        const notLastP = pi < p.length - 2;

        if (notLastP && p[pi + 1] == '*') {
            pi += 2;
            continue;
        }

        if (p[pi] == '*') {
            if (isMatchChar(s[i], p[pi - 1])) {
                i++;
                continue;
            }

            if (!notLastP && isMatchChar(s[i], p[pi + 1])) {
                pi++;
                continue;
            }
        }

        return false;
    }

    var pe = pi;

    pi = p.length - 1;
    i = s.length - 1;

    while (pi >= pe) {
        if (i == 0) {
            return false;
        }
        if (p[pi] == '*') {
            pi -= 2;
            continue;
        }

        if (isMatchChar(s[i], p[pi])) {
            pi--;
            i--;
            continue;
        }

        return false;
    }

    return true;
};

function isMatchChar(s: string, p: string): boolean {
    return s == p || p == '.';
}