"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

def longestPrefix(strs: list[str]) -> str:
    if not strs:
        return ""
    
    for i in range(len(min(strs, key=len))): # for i in the range of the length of the shortest word in the list.
        if len(set(str[i] for str in strs)) > 1: # if the set of prefixes in the range [0:i] is more than one (i.e. there are multiple prefixes)
            return strs[0][:i] # return the prefix
    return min(strs, key=len) # else the shortest word is the common prefix


print(longestPrefix(["dog","racecar","car"]))