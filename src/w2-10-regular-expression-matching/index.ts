export function isMatch(s: string, p: string): boolean {
    return matchPattern(s, parsePattern(p));
};

function matchPattern(
    s: string,
    p: [string, string][],
    sb = 0,
    se = s.length - 1,
    pb = 0,
    pe = p.length - 1
): boolean {
    while (
        sb < s.length
        && se >= 0
        && pb < p.length
        && pb >= 0
    ) {
        while (p[pb][1] == '' && isMatchChar(s[sb], p[pb][0])) {
            sb++;
            pb++;
            continue;
        }
    
        if (p[pe][1] == '' && isMatchChar(s[se], p[pe][0])) {
            se--;
            pe--;
            continue;
        }

        if (p[pb][1] == '*' || p[pe][1] == '*') {    
            if (p[pb][1] == '*') {
                while (sb <= se && isMatchChar(s[sb], p[pb][0])) {
                    sb++;
                }
                pb++;
            }

            if (p[pe][1] == '*') {
                while (se >= sb && isMatchChar(s[se], p[pe][0])) {
                    se--;
                }
                pe--;
            }

            continue;
        }

        return false;
    }

    return true;
}

function parsePattern(p: string): [string, string][] {
    const res: [string, string][] = [];

    for (var i = 0; i < p.length; i++) {
        if (i < p.length - 1 && p[i + 1] == '*') {
            res.push([p[i], '*']);
            i++;
        } else {
            res.push([p[i], '']);
        }
    }

    return res;
}

function isMatchChar(s: string, p: string): boolean {
    return s == p || p == '.';
}