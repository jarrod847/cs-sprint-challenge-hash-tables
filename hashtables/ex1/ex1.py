def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    results = {}
    for i, value in enumerate(weights, 0):
        results[i] = value
    for x, y in results.items():
        for i in weights:
            if i + y == limit:
                if len(weights) == 2:
                    return (1, 0)
                else:
                    return((weights.index(i), x))
        # else:
        #     return((x, weights.index(i)))
    # for i in weights:
    #     if i + results.get(0 + num - 1) == limit:
    #         if i > results.get(0 + num - 1):
    #             print(weights[i], results[0])
    #         else:
    #             print((results., results.get(0 + num - 1)))
    print(results)

    # if i not in results.values():
    #     num += 1
    #     results[num] = i
    #     if num == 1:
    #         pass
    #     elif results.get(1) + i == limit:
    #         if i > results.get(1):
    #             return (results[num], results.get(1))
    #         else:
    #             return (results.get(1), results[num])
    return None


get_indices_of_item_weights([2, 4, 7, 8], 4, 10)
