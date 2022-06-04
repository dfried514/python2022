def countdown(num):
    lst = []
    for x in range(num, -1, -1):
        lst.append(x)
    return lst

def print_and_return(nums):
    print(nums[0])
    return nums[1]

def first_plus_length(nums):
    return nums[0] + len(nums)

def values_greater_than_second(nums):
    if len(nums) < 2:
        return False
    lst = []
    for x in nums:
        if x > nums[1]:
            lst.append(x)
    print(len(lst))
    return lst

def length_and_value(size, value):
    lst = []
    for x in range(size):
        lst.append(value)
    return lst
