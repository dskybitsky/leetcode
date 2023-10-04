const assert = require('assert');

class MyHashMap {
    static MAX_BUCKETS = 10000;

    private buckets: ([number, number])[][] = [];

    constructor() {

    }

    put(key: number, value: number): void {
        const bucketId = MyHashMap.getBucket(key);

        if (this.buckets[bucketId] === undefined) {
            this.buckets[bucketId] = [];
        }

        const bucket = this.buckets[bucketId];

        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key)  {
                bucket[i][1] = value;
                return;
            }
        }

        bucket.push([key, value]);
    }

    get(key: number): number {
        const bucketId = MyHashMap.getBucket(key);

        const bucket = this.buckets[bucketId] ?? [];

        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i][0] === key)  {
                return bucket[i][1];
            }
        }

        return -1;
    }

    remove(key: number): void {
        this.put(key, -1);
    }

    private static getBucket(key: number): number {
        return key % MyHashMap.MAX_BUCKETS;
    }
}

const myHash = new MyHashMap()

const myHashMap = new MyHashMap();

myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
assert(myHashMap.get(1) === 1);    // return 1, The map is now [[1,1], [2,2]]
assert(myHashMap.get(3) === -1);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
assert(myHashMap.get(2) === 1);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
assert(myHashMap.get(2) === -1);    // return -1 (i.e., not found), The map is now [[1,1]]

console.log('OK');