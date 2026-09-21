class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let map = new Map()

        for(let i = 0; i<strs.length; i++){

            // sorted string acts as key for the anagrams
            let key = strs[i].split("").sort().join("")

            // create bucket for new anagrams
            if(!map.has(key)){
                map.set(key,[])
            }

            // add original string to this original anagram
            map.get(key).push(strs[i])
        }

        return Array.from(map.values())
    }
}
