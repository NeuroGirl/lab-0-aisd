nums = input().split(" ")
a = int(nums[0])
b = int(nums[1])
if -10**9 <= a <= 10**9 and -10**9 <= b <= 10**9:
    print(a + b**2)
