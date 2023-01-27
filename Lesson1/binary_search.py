def binary_search(list, item):
    first = 0
    last = len(list) - 1

    while first <= last:
        # Our guess is the midpoint between first and last
        midpoint = (first + last) // 2
        guess = list[midpoint]
        # We found the item
        if guess == item:
            return midpoint
        # Our guess was too high
        if guess > item:
            last = midpoint - 1
        # Our guess was too low
        else:
            first = midpoint + 1
    # Item doesn't exist
    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = binary_search(numbers, 12)
verify(result)
result = binary_search(numbers, 6)
verify(result)
