import collections


def count_ana(str, ptrn):
    i = 0
    j = 0
    k = len(ptrn)
    final_count = 0
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
                final_count += 1
            # Maintainance
            if str[i] in chars_in_ptrn:
                if chars_in_ptrn[str[i]] == 0:
                    temp_count += 1
                chars_in_ptrn[str[i]] += 1
            i += 1
            j += 1
    return final_count


# print(count_ana('cbaebabacd', 'abc'))  # 2
# print(count_ana('fxorxofuixfo', 'fox'))  # 3
# print(count_ana('abab', 'ab'))  # 3


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


def first_neg(arr, k):
    i = 0
    j = 0
    neg_arr = []
    ans_arr = []
    while j < len(arr):
        if arr[j] < 0:
            neg_arr.append(arr[j])
        # Window doesn't hit
        if j-i+1 < k:
            j += 1
        # Window hit!
        elif j-i+1 == k:
            # Cal
            if len(neg_arr) == 0:
                ans_arr.append(0)
            else:
                ans_arr.append(neg_arr[0])
            # Maintainance
            if arr[i] < 0:
                neg_arr.remove(arr[i])
            j += 1
            i += 1
    return ans_arr


# print(first_neg([-12, -1, -7, 8, -15, 30, 16, 28], 3))
# print(first_neg([2, -8, -7, 6, 4, -5], 2))

# def find_max(arr, k):
#     i = 0
#     j = 0
#     temp_arr = []
#     ans_arr = []
#     while j < len(arr):
#         temp_arr.append(arr[j])
#         # Window doesn't hit
#         if j-i+1 < k:
#             j += 1
#         # Window hits!
#         elif j-i+1 == k:
#             # Calc
#             ans_arr.append(max(temp_arr))
#             # Maintain
#             temp_arr.remove(arr[i])
#             j += 1
#             i += 1
#     return ans_arr

def find_max(arr, k):
    i = 0
    j = 0
    q = collections.deque()
    ans = []
    while j < len(arr):
        # Initial Calc
        while q and arr[q[-1]] < arr[j]:
            q.pop()
        q.append(j)

        # As window slides, remove i value from queue
        if i > q[0]:
            q.popleft()

        # Doesn't hit
        if j-i+1 < k:
            j += 1

        # Hit
        elif j-i+1 == k:

            # Calc
            ans.append(arr[q[0]])

            # Maintain
            i += 1
            j += 1
    return ans


# Note: Above soln with reference from https://www.youtube.com/watch?v=DfljaUwZsOk
print(find_max([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(find_max([1], 1))
print(find_max([1, -1], 1))
