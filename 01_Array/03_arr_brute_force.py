def two_sum(nums, target):
    """
    Find indices of two numbers in the list `nums` that add up to `target`.

    Args:
        nums (list): List of integers.
        target (int): Target sum.

    Returns:
        list: Indices of the two numbers or None if no solution exists.
    """
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            print(i, j)  # Debugging print statement
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

if __name__ == "__main__":
    # Hardcoded test case
    nums = [2, 7, 10, 19]
    target = 9

    # Call the two_sum function
    result = two_sum(nums, target)

    # Print the result
    if result is not None:
        print(f"Indices of the two numbers that add up to {target}: {result}")
    else:
        print("No two numbers add up to the target value.")

# 실행 커맨드
# python 03_arr_brute_force.py