# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    compFile = dict(files=files, queries=queries)

    for x in compFile.get('files'):
        if (x[-3:]) in compFile.get('queries'):
            result.append(x)
        else:
            continue

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
