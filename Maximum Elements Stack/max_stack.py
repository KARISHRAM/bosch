def getMax(operations):
    stack = []
    max_stack = []
    result = []

    for op in operations:
        parts = op.split()

        if parts[0] == "1":  # push
            val = int(parts[1])
            stack.append(val)
            if not max_stack:
                max_stack.append(val)
            else:
                max_stack.append(max(val, max_stack[-1]))

        elif parts[0] == "2":  # pop
            if stack:
                stack.pop()
                max_stack.pop()

        else:  # "3" query max
            if max_stack:
                result.append(max_stack[-1])

    return result


operations = [
    "1 97",
    "2",
    "1 20",
    "2",
    "1 26",
    "1 20",
    "2",
    "3",
    "1 91",
    "3"
]

print("\n".join(map(str, getMax(operations))))
