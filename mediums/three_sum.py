# this method takes in an array of integers and finds all possible triplet combinations
# that, when added up, amount to 0.
number_list = [34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]


def three_sum(nums):
    list_of_lists = []
    left_counter = 0
    middle_counter = 1
    right_counter = 2
    end_flag = False

    # looks for at least a list length of 3, otherwise an empty list is returned.
    try:
        left = nums[0]
        middle = nums[1]
        right = nums[2]
    except:
        return []

    # if the length of the list is 3 then only 1 check for a triplet combination is necessary.
    if len(nums) == 3:
        if left + middle + right == 0:
            list_of_lists.append([left, middle, right])
            return list_of_lists
        # empty list is returned if there's no possible combination.
        else:
            return list_of_lists

    # absolutely some of the most disgusting code I've ever written. Conditional hell! I should be ashamed
    # of myself... and yet it works.
    while not end_flag:
        # if the sum of all 3 pointers equals 0 and the conditional hell gauntlet is passed (regardless of order,
        # the triplet combination is not already in the list of lists) then the triplets are appended.
        if (left + middle + right == 0 and [left, middle, right] not in list_of_lists and [left, right, middle]
                not in list_of_lists and [middle, left, right] not in list_of_lists and [middle, right, left]
                not in list_of_lists and [right, middle, left] not in list_of_lists and [right, left, middle]
                not in list_of_lists):
            list_of_lists.append([left, middle, right])
            # if the right pointer is not at the end, then increment it and assign.
            if right_counter != len(nums) - 1:
                right_counter += 1
                right = nums[right_counter]
            # if the right pointer reached the end of the list, decrement the left pointer and assign,
            # then reset the right pointer to be 1 ahead of the middle pointer.
            elif left != nums[0]:
                left_counter -= 1
                left = nums[left_counter]
                right_counter = middle_counter + 1
                right = nums[right_counter]
            # if both right and left pointers have reached their end points, x is incremented and both pointers are
            # assigned to 1 ahead and 1 behind the middle pointer index and assignment respectively.
            else:
                middle_counter += 1
                middle = nums[middle_counter]
                # flag is tripped and the while loop is ended if the middle counter is equal to the index
                # of 2 before the length of the given int list (nums).
                if middle_counter == len(nums) - 1:
                    end_flag = True
                    break
                right_counter = middle_counter + 1
                right = nums[right_counter]
                left_counter = middle_counter - 1
                left = nums[left_counter]
        elif right_counter != len(nums) - 1:
            right_counter += 1
            right = nums[right_counter]
        elif left != nums[0]:
            left_counter -= 1
            left = nums[left_counter]
            right_counter = middle_counter + 1
            right = nums[right_counter]
        else:
            middle_counter += 1
            middle = nums[middle_counter]
            if middle_counter == len(nums) - 1:
                end_flag = True
                print(nums[middle_counter])
                break
            right_counter = middle_counter + 1
            right = nums[right_counter]
            left_counter = middle_counter - 1
            left = nums[left_counter]

    return list_of_lists


solution = three_sum(number_list)
print(solution)
