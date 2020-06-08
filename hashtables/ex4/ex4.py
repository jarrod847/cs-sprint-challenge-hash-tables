def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    numbers = {}
    num = 0
    for x, y in enumerate(a, 0):
        numbers[x] = y

    result = []
    while num != len(numbers):
        print(numbers[num])
        if numbers[num] == 0:
            num += 1

        elif numbers[num] > 0:
            if numbers[num] in result:
                num += 1
            elif numbers[num] * -1 in numbers.values():
                result.append(abs(numbers[num]))
                num += 1
            else:
                num += 1

        elif numbers[num] < 0:
            if abs(numbers[num]) in result:
                num += 1

            elif abs(numbers[num]) in a:
                result.append(abs(numbers[num]))
                num += 1

    # elif numbers[num] > 0:
    #     if int('-' + str(numbers[num])) in a:
    #         result.append(abs(numbers[num]))
    # while len(numbers) != num:
    #     if numbers[num] < 0:
    #         if abs(numbers[num]) in a:
    #             result.append(abs(numbers[num])

    #     elif numbers[num] > 0:
    #         if int('-' + str(numbers[num])) in a:
    #             result.append(numbers[num])

    #     return num += 1
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
