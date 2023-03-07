# 1. Maximum Sum Subarray of size k

# arr = [2, 13, 9, 6, 4, 11]
# len(arr) = 6


def max_sum_subarray(arr, k):
    i = 0
    j = 0
    sum = 0
    max_sum = []
    while j < len(arr):
        sum = sum + arr[j]

        # 1. Window size doesn't hit
        if j - i + 1 < k:
            j += 1

        # 2. Window size hits!
        elif j - i + 1 == k:

            # 3. Perform some calculations
            max_sum.append(sum)

            # 4. Maintain window size
            sum = sum - arr[i]
            j += 1
            i += 1
    return max(max_sum)


# print(max_sum_subarray([1, 2, 3, 4], 3))

# ------------------------------------------------

# 2. First Negative Number in every Window of Size K

# Method 1 - Brute Force
def first_neg_brute(arr, k):
    neg_list = []
    for i in range(0, len(arr) - k + 1):
        for j in range(i, i + k):
            if arr[j] < 0:
                neg_list.append(arr[j])
                break
            elif j == i + k - 1:
                neg_list.append(0)
    return neg_list
# print(first_neg_brute([2, -8, -7, 6, 4, -5], 2))

# Method 2 - Sliding Window


def first_neg(arr, k):
    i = 0
    j = 0
    neg_arr = []
    ans_arr = []
    while j < len(arr):
        if arr[j] < 0:
            neg_arr.append(arr[j])

        # 1. Window size doesn't hit
        if j-i+1 < k:
            j += 1

        # 2. Window size hits!
        elif j-i+1 == k:

            # 3. Perform some calculations
            if len(neg_arr) == 0:
                ans_arr.append(0)
            else:
                ans_arr.append(neg_arr[0])

            # 4. Maintain window size
            if arr[i] < 0:
                neg_arr.remove(arr[i])
            j += 1
            i += 1
    return ans_arr
# print(first_neg([-12, -1, -7, 8, -15, 30, 16, 28], 3))
# print(first_neg([2, -8, -7, 6, 4, -5], 2))

# ---------------------------------------------

# Counting occurences of anagrams


def count_ana(str, ptrn):
    i = 0
    j = 0
    k = len(ptrn)
    final_count = 0
    # O(n^2)
    # chars_in_ptrn = {x: ptrn.count(x) for x in ptrn}
    # O(n)
    chars_in_ptrn = {}
    # Creating chars_in_ptrn dict i.e., chars_in_ptrn = {f: 1, o: 1, x: 1}
    for x in range(len(ptrn)):
        chars_in_ptrn[ptrn[x]] = 1 + chars_in_ptrn.get(ptrn[x], 0)
    temp_count = len(chars_in_ptrn)
    while j < len(str):
        # Initial Calc
        if str[j] in chars_in_ptrn:
            chars_in_ptrn[str[j]] -= 1
            if chars_in_ptrn[str[j]] == 0:
                temp_count -= 1
        # Window doesn't hit
        if j-i+1 < k:
            j += 1

        # Window size hits!
        elif j-i+1 == k:
            # Calc
            if temp_count == 0:
                final_count += 1
            # Maintainance
            if str[i] in chars_in_ptrn:
                if chars_in_ptrn[str[i]] == 0:
                    temp_count += 1
                chars_in_ptrn[str[i]] += 1
            i += 1
            j += 1
    return final_count


# print(count_ana('fxorxofuixfo', 'fox'))
# print(count_ana('cbaebabacd', 'abc'))
# print(count_ana('abab', 'ab'))

# ----------------------------------------

# 438. Find All Anagrams in a String


def find_ana(str, ptrn):
    i = 0
    j = 0
    k = len(ptrn)
    final_count_arr = []
    # O(n^2)
    # chars_in_ptrn = {x: ptrn.count(x) for x in ptrn}
    # O(n)
    chars_in_ptrn = {}
    for x in range(len(ptrn)):
        chars_in_ptrn[ptrn[x]] = 1 + chars_in_ptrn.get(ptrn[x], 0)
    temp_count = len(chars_in_ptrn)
    while j < len(str):
        # Initial Calc
        if str[j] in chars_in_ptrn:
            chars_in_ptrn[str[j]] -= 1
            if chars_in_ptrn[str[j]] == 0:
                temp_count -= 1
        # Window doesn't hit
        if j-i+1 < k:
            j += 1

        # Window size hits!
        elif j-i+1 == k:
            # Calc
            # if all(value == 0 for value in chars_in_ptrn.values()):
            if temp_count == 0:
                final_count_arr.append(i)
            # Maintainance
            if str[i] in chars_in_ptrn:
                if chars_in_ptrn[str[i]] == 0:
                    temp_count += 1
                chars_in_ptrn[str[i]] += 1
            i += 1
            j += 1
    return final_count_arr


# print(find_ana("cbaebabacd", "abc"))
# print(find_ana('abab', 'ab'))
