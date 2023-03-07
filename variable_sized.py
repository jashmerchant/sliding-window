def find_largest_subarray(arr, k):
    i = 0
    j = 0
    sum = 0
    ans = 0
    while j < len(arr):
        # Initial Calc
        sum += arr[j]

        # Condition doesn't hit
        if sum < k:
            j += 1

        # Condition hits
        elif sum == k:
            # Calculation
            ans = max(ans, j-i+1)
            j += 1

        # Condition exceeds
        elif sum > k:
            while sum > k:
                sum -= arr[i]
                i += 1
            j += 1

    return ans


# print(find_largest_subarray([4, 1, 1, 1, 2, 3, 5], 5))
# print(find_largest_subarray([1, 1, 1], 2))
# print(find_largest_subarray([1, 2, 3], 3))
# print(find_largest_subarray([1], 0))

# Leetcode Premium Hard!
def longest_substring(arr, k):
    i = 0
    j = 0
    counter = 0
    ans = 0
    char_arr = []
    while j < len(arr):
        # Initial Calc
        # if len(set(arr)) < k:
        #     return 1
        char_arr.append(arr[j])
        counter = len(set(char_arr))

        # Condition doesn't meet
        if counter < k:
            j += 1

        # Condition meet
        elif counter == k:
            # Calculate answer
            ans = len(char_arr)
            j += 1

        # Condition exceeds
        elif counter > k:
            while len(set(char_arr)) > k:
                char_arr.remove(arr[i])
                i += 1
            j += 1
    return ans


# print(longest_substring("aabacbebebe", 3))
# print(longest_substring("eceba", 2))
# print(longest_substring("aa", 1))
# print(longest_substring("hq", 2))


def pick_toys(arr):
    i = 0
    j = 0
    counter = 0
    char_arr = []
    ans = 0
    while j < len(arr):
        # Initial Calculations
        if len(set(arr)) < 2:
            return len(arr)
        char_arr.append(arr[j])
        counter = len(set(char_arr))

        # Condition doesn't meet
        if counter < 2:
            j += 1

        elif counter == 2:
            if ans < j-i+1:
                ans = j-i+1

            # ans = max(ans, j-i+1)
            print(f'Ans: {ans}')
            j += 1

        elif counter > 2:
            while len(set(char_arr)) > 2:
                char_arr.remove(arr[i])
                i += 1
            j += 1
    return ans


# print(pick_toys(['a', 'b', 'a', 'c', 'c', 'a', 'b']))
print(pick_toys([0]))
print(pick_toys([1, 1]))
