# Problem: Longest Substring Without Repeating Characters

## Difficulty: Medium

## Description:
Given a string s, find the length of the longest substring without repeating characters.


## Solution:

I'm gonna use sliding window pattern with dynamic size.

We need to 2 pointer (startIndex and endIndex).

If there's no duplicate letters with current substring I increase endIndex, expanding the substring.

If there's a duplicate I increase the startIndex making sure that the substring has no duplicate in current iteration.



``` javascript

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    let startIndex = 0;
    let endIndex = 1;
    let maxCount = 0;
    if (s.length <= 1) {
        return s.length;
    }
    while (endIndex <= s.length) {
        let substring = s.slice(startIndex, endIndex);
        const current = s[endIndex];
        if (substring.includes(current)) {
            startIndex++;
        } else {
            endIndex++;
        }
        if (endIndex === startIndex) {
            endIndex++;
        }
        maxCount = maxCount > substring.length ? maxCount : substring.length;
    }
    return maxCount;
};

```