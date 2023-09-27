var assert = require('assert');

var decodeAtIndex = function(s, k) {
    const n = s.length;
    
    let l = 0;
    let lc = 0;
    let pl = 0

    for (let i = 0; i < n; i++) {
        const c = s[i];
        
        pl = l;

        if (isChar(c)) {
            l += 1;
            lc = i;
        } else {
            cnum = 1;
            
            let j = i;
            
            while (j < n && isNum(s[j])) {
                cnum = cnum * parseInt(s[j]);
                j++;
            }

            l *= cnum;

            i = j - 1;
        }

        if (l === k) {
            return s[lc];
        }

        if (l > k) {
            const newK = k - pl * Math.floor(k / pl);

            if (newK === 0) {
                return s[lc];
            }

            return decodeAtIndex(s, newK);
        }
    }
};

const isNum = (c) => !isChar(c);
const isChar = (c) => (c >= 'a' && c <= 'z');

let res = 0

assert((res = decodeAtIndex('vk6u5xhq9v', 554)) === 'k',  `${res} === 'k'`);

assert((res = decodeAtIndex('a23', 6)) === 'a',  `${res} === 'a'`);

assert((res = decodeAtIndex('vzpp636m8y', 2920)) === 'z',  `'${res}' === 'z'`);
assert(decodeAtIndex('leet2code3', 10) === 'o',  "error");

assert(decodeAtIndex('leet2code3', 12) === 'e',  `'${res}' === 'e'`);
assert(decodeAtIndex('leet2code3', 13) === 'l',  `'${res}' === 'l'`);
assert(decodeAtIndex('leet2code3', 14) === 'e',  `'${res}' === 'e'`);



assert((res = decodeAtIndex('a2b3c4d5e6f7g8h9', 9)) === 'b',  `${res} === 'b'`);

assert(decodeAtIndex('leet2code3', 1) === 'l',  "error");
assert(decodeAtIndex('leet2code3', 10) === 'o',  "error");
assert(decodeAtIndex('leet2code3', 5) === 'l',  "error");

assert(decodeAtIndex('ha22', 5) === 'h',  "error");

console.log("Ok!");