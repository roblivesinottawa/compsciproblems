"""
Two sum: given an array of integers, return indices of the two
numbers such that they add up to a specific target.

Example:
nums = [2, 7, 11, 15] = nums[0] + nums[1] = 2+7=9
target = 9

"""




# this solution is from an online bootcamp.
# it uses a for loop and a dictionary to solve the problem.


def two_sum(nums, target):
    d = dict()

    for x in range(len(nums)):
        if target - nums[x] in d:
            # print(d)
            return [d[target - nums[x]], x]
        d[nums[x]] = x
    return -1

_list = [8, 6, 11, 3]
# print(two_sum(_list, 9))

# this is another solution based on a book I read.

"""
arr1 = [1,3,5,6]
target = 8
# this would return indices [1] and [2]

arr2 = [4,7,2,6]
target = 12
# this would return None

"""

"""
we can iterate through the array and use a dictionary to keep track of the values
we want to see. For an element x in the array and a target value, we want 
to see if there is another element in the array that has the
value of target minus x which is called its complement.
we can use a dictionary to keep track of the values and indices of values we have seen so far,
we want to map the value of an element to a corresponding index 
position, for each element in the list, we want to compute the
complement = target - element which is the difference between the
element and the target value. So we chack if the complement is in 
our dictionary.if it is we can return: 

if complement in dictionary:
    return dictionary[complement]

to get the indices of the two elements that sum up to the target. We return an
empty list if two values are not found.

 
"""

arr1 = [1,3,5,6]
target = 8

def twosum(array, target):
    values = dict()

    for x, element in enumerate(array):
        complement = target - element

        if complement in values:
            return [values[complement], x]

        values[element] = x
    
    return [] 

list1 = twosum(arr1, target)
# print(list1)


"""
given an array of integers, return indices of the two numbers
such that they add up to a specific target.

you may assume that each input would have exactly one solution,
and you may not use the same element twice.

example:
    nums = [1, 3, 11, 2, 7]
    target = 9
    return [3, 4]
"""

# using a linear time solution.

nums = [1, 3, 11, 2, 7]
target = 9

def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    
    _dict = dict()
    for i in range(len(nums)):
        if nums[i] in _dict:
            return [_dict[nums[i]], i]
        else:
            _dict[target - nums[i]] = i

print(f"nums = {nums}")
print(f"target = {target}")

print(twoSum(nums, target))



