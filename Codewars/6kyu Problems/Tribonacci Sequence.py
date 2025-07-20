def tribonacci(signature, n):
    result = signature[:n]
    while len(result) < n:
        result.append(sum(result[-3:]))
    return result
