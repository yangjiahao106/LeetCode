#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/23
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = {}
        for s in strs:
            # key = tuple(sorted(s))
            # result[key] = result.get(key, []) + [s]
            if tuple(sorted(s)) in result:
                result[tuple(sorted(s))].append(s)
            else:
                result[tuple(sorted(s))] = [s]
        return list(result.values())


if __name__ == '__main__':
    so = Solution()
    res = so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(res)
