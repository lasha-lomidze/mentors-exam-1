# დავალებაში მოცემულია 5 ნორმალური სირთულის და 5 რთული დონის ალგორითმული ამოცანა.
# თითოეულ ამოცანას გააჩნია თავისი პირობა და 3 test case.

# თითოეული ამოცანისთვის უნდა შექმნათ ცალკე პითონის ან js-ის (ამ ორი ენიდან, რომლითაც გინდათ დაწერეთ ამოცანის კოდი) ფაილი და სამივე test case-ზე მიიღოთ იგივე შედეგი.
# შესაძლოა ამოცანამ მოცემულ 3 test case-ზე იგივე შედეგი დააბრუნოს, მაგრამ სხვა მაგალითებზე სწორად არ მუშაობდეს. ასეთ დროს ის შესრულებულად არ ჩაითვლება.

# !!! ყველა ამოცანას უნდა ქონდეს კომენტარები, სადაც ახსნილი იქნება კოდის რა ნაწილი რა დავალებას ასრულებს.

# !!! ამოცანების შესრულებისას დაუშვებელია browser-ის გამოყენება.


# ამოცანები:

# 1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.
# 2. Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
# 3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array.
# 4. Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively.
# 5. Given an array of integers, find all unique pairs of elements that sum to a given target number.
# 6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.
# 7. Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
# 8. Given an array nums of n integers, return all unique triplets [a, b, c] such that a + b + c = 0. The solution set must not contain duplicate triplets.
# 9. Given an array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
# 10. Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Test cases:
# 1. [1, 2, 4, 5] -> 3, [1] -> 2, [2, 3, 1, 5] -> 4
# 2. ["flower", "flow", "flight"] -> "fl", ["dog", "racecar", "car"] -> "", ["apple", "apple", "apple"] -> "apple"
# 3. [3, 2, 3] -> 3, [2, 2, 1, 1, 2] -> 2, [1, 1, 1, 1, 1] -> 1
# 4. 0 -> 0, 5 -> 5, 10 -> 55
# 5. [1, 2, 3, 2, 4], 5 -> [(1, 4), (2, 3)],    [1, 2, 3], 7 -> [],    [-1, 0, 1, 2, -2, 3], 0 -> [(-1, 1), (-2, 2)]
# 6. [1, 2, 3], [4, 5, 6] -> 3.5,    [10, 20], [30, 40, 50] -> 30.0,    [-5, -3, -1], [1, 3, 5] -> 0.0
# 7. "(()))())" -> 4, "((()))" -> 6, ")()())(" -> 4
# 8. [-1, 0, 1, 2, -1, -4] -> [[-1, -1, 2], [-1, 0, 1]],    [1, 2, 3] -> [],    [0, 0, 0, 0] -> [[0, 0, 0]]
# 9. [1, 2, 3, 4] -> [24, 12, 8, 6], [0, 1, 2, 3] -> [6, 0, 0, 0], [0, 0, 1] -> [0, 0, 0]
# 10. ["eat", "tea", "tan", "ate", "nat", "bat"] -> [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],    ["abc", "bac", "cab"] -> [['abc', 'bac', 'cab']],    ["hello", "world", "python"] -> [['hello'], ['world'], ['python']
# the words “gum” and “mug” are anagrams because they are both three-letter words and have the same letters (g, u, and m). Let's look at some more word pairings that are anagrams: “cork” and “rock”




# 1. Given an array containing n-1 numbers taken from the range 1 to n, write a function to find the missing number. There are no duplicates in the array.
def func1(arr):
    n = len(arr)+1
    expect = n*(n+1)//2
    ans = sum(arr)
    return expect-ans 
print(func1([1, 2, 4, 5]))
print(func1([1]))
print(func1([2, 3, 1, 5]))


# 2. Write a function to find the longest common prefix among an array of strings. If there is no common prefix, return an empty string.
def func2(strs):
    if(not strs):
        return ""
    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]
    return prefix
print(func2(["flower", "flow", "flight"]))
print(func2(["dog", "racecar", "car"]))
print(func2(["apple", "apple", "apple"] ))



# 3. Given an array of size n, find the majority element. The majority element is the element that appears more than n // 2 times. You may assume that the array is non-empty and the majority element always exists in the array.
def func3(arr):
    temp = None
    count = 0
    for num in arr:
        if count==0:
            temp = num
            count = 1
        elif num == temp:
            count+=1
        else:
            count -= 1
    return temp
print(func3([3, 2, 3]))
print(func3([2, 2, 1, 1, 2]))
print(func3([1, 1, 1, 1, 1]))



# 4. Write a function to return the nth number in the Fibonacci sequence. Solve it both recursively and iteratively.
def Rfunc4(n):
    if n<=1:
        return n
    return Rfunc4(n-1) + Rfunc4(n-2)
def func4(n):
    temp = 1
    for i in range(2, n+1):
        temp *= i
    return temp
def func4(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
            
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b
print(Rfunc4(0))
print(Rfunc4(5))
print(Rfunc4(10))



# 5. Given an array of integers, find all unique pairs of elements that sum to a given target number.
# def func5(arr, target):
#     seen = set()
#     unique_pairs = set()

#     for num in arr:
#         temp = target - num
#         if temp in seen:
#             unique_pairs.add(tuple(sorted((num, temp))))
#         seen.add(num)
#         return list(unique_pairs)




# 6. Given two sorted arrays nums1 and nums2, return the mean of the two sorted arrays.
def func6(arr1, arr2):
    merged = []
    i, j = 0,0

    while i <len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    total = sum(merged)
    mean = total / len(merged)
    return mean




# 7. Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



# 9. Given an array nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].
def func9(arr):
    length = len(arr)
    output = [1] * length
    left_product = 1
    for i in range(length):
        output[i] = left_product
        lrft_product *= arr[i]
        right_product = arr[i]
        for i in range(length -1, -1, -1):
            output[i] *= right_product
            right_product *= arr[i]
    return output

