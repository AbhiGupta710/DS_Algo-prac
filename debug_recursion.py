def bestsum(trg, arr):
    if trg == 0:
        return []
    if trg < 0:
        return None
    shortest = None
    for i in arr:

        rem = trg - i
        rem_comb = bestsum(rem, arr)

        if rem_comb != None:
            ans = rem_comb + [i]

            if shortest == None or len(ans) < len(shortest):
                shortest = ans

    return shortest


print(bestsum(7, [4, 3, 2]))
