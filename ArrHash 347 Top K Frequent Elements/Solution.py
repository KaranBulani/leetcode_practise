'''
Time complexity: O(3n + k) which is O(n + k) but k is always less than n, we can just say O(n)
                 O(n) for count
                 O(n) for empty count_bucket
                 O(distinct n) which is O(n) for inserting count_dict to count_bucket
                 O(k) to add in res
Space complexity: O(2n + res) which is O(n + res) but res is always less than n, we can just say O(n)
                  O(n) for count
                  O(n) for empty count_bucket
                  res which we are returning
'''

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_dict = {}
        for num in nums:
            count_dict[num] = 1 + count_dict.get(num, 0)

        # Bucket where index = frequency, and value = list of numbers with that frequency
        count_bucket = [[] for _ in range(len(nums)) ]
        for key, value in count_dict.items():
            count_bucket[value - 1].append(key) ##when all 1 then count will be n but list goes from 0..n-1 hence v-1

        res = []

        for i in range(len(nums) - 1, -1, -1):

            # No need to explicitly check if count_bucket[i] is empty.
            # The inner for loop will simply skip over empty lists.
            if not count_bucket[i]:
                continue
            for value in count_bucket[i]:

                # You could also use count_bucket[i].pop() here,
                # but since all values at this frequency level are equally frequent,
                # the order doesn't matter. Appending directly is cleaner and non-destructive.
                res.append(value)
                if len(res) == k:
                    return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1,1,1,2,2,2,3,3]#[1]
    k = 2 #1
    result = solution.topKFrequent(nums, k)
    print(result)
