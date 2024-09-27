height_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def water_container(height):
    # brute force method could not beat the time limit.
    # this solution was obtained from:
    # https://leetcode.com/problems/container-with-most-water/solutions/5139915/video-simple-two-pointer-solution
    largest_container = 0
    left = 0
    right = len(height) - 1

    # loop until the left and right pointers overlap
    while left < right:
        # the largest area of the container updates if the distance between the two pointers (width)
        # multiplied by the lowest value (height) is greater than the current value of largest_container.
        largest_container = max(largest_container, (right - left) * min(height[left], height[right]))

        # if the value of left pointer is lower than that of the right then left is incremented,
        # otherwise right is decremented if the opposite is true or they are equal.
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return largest_container


container = water_container(height_list)
print(container)
