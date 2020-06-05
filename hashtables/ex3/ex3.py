def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    section = {}
    result = []

    for i in arrays:
        for j in i:
            if j in section:
                section[j] += 1
            else:
                section[j] = 1

    for keys in section.keys():
        if section[keys] == len(arrays):
            result.append(keys)

    # for x, y in enumerate(arrays):
    #     section[x] = y

    # num = 0
    # if section[num][num] in section[num + 1]:
    #     result.append(section[num])

    # for i in section.values():
    #     num = 0
    #     if result == []:
    #         result.append(i[num])
    #         num += 1
    #     elif len(result) > 1:
    #         if result[0] == i[num]:
    #             num += 1
    #             return(result)

    return(result)


intersection([[1, 2, 3], [5, 4, 1]])


# if __name__ == "__main__":
#     arrays = []

#     arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
#     arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
#     arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

#     print(intersection(arrays))
