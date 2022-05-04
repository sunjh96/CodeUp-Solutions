from itertools import combinations

def isPrime(x):
    if x == 1:
        return True
    else:
        for i in range(2, x//2 + 1):
            if x % i == 0:
                return False
        else:
            return True

def solution(nums):
    ans = 0
    cmb = list(combinations(nums, 3))

    for arr in cmb:
        if isPrime(sum(arr)):
            ans += 1

    return ans
'''
def solution(nums):
    cnt = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1,len(nums)):
                if isPrime(nums[i] + nums[j] + nums[k]) == 1:
                    cnt += 1
    return cnt
'''
print(solution([1, 2, 7, 6, 4]))