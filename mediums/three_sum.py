# this method takes in an array of integers and finds all possible triplet combinations
# that, when added up, amount to 0.
# original solution could not beat the time limit.
# this solution was obtained from: https://leetcode.com/problems/3sum/solutions/5055810/video-two-pointer-solution
number_list = [-1, 0, 1, 2, -1, -4]


def three_sum(nums):
    list_of_lists = []
    # sort the given list of ints to make iteration to the result (0) easier.
    nums.sort()

    # for loop in the range of the length of given list of ints.
    for i in range(len(nums)):
        # if 'i' isn't the starting index and the values from nums[i] and nums[i - 1] equal each other
        # then the loop is pushed into its next iteration because we already obtained the result (or lack thereof)
        # in which num(i) equaled that value in the sorted list of ints.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # the 'j' value increments 1 from the 'i' position.
        j = i + 1
        # the 'k' value is set to the end index of the given list of ints.
        k = len(nums) - 1

        # loops until the 'j' and 'k' values are the same. Nested 'while' loop makes this a bruteforce method.
        while j < k:
            total = nums[i] + nums[j] + nums[k]

            # if the 3 pointers added together is less than 0, then the 'j' pointer is incremented.
            if total < 0:
                j += 1
            # if greater than 0, then the 'k' pointer is decremented.
            elif total > 0:
                k -= 1
            # otherwise the target '0' is met and the triplet combination is appended to the list of lists.
            else:
                list_of_lists.append([nums[i], nums[j], nums[k]])
                j += 1

                # like in the case for 'i', 'j' too is checked for a repeating value.
                while nums[j] == nums[j - 1] and j < k:
                    j += 1

    return list_of_lists


print(three_sum(number_list))

