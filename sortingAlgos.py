def bubble(l):
    l_sorted = l.copy()
    for i in range(1, len(l_sorted)):
        for j in range(len(l_sorted)-i):
            if l_sorted[j] > l_sorted[j+1]:
                temp = l_sorted[j+1]
                l_sorted[j+1] = l_sorted[j]
                l_sorted[j] = temp
    return l_sorted

def smarterBubble(l):
    l_sorted = l.copy()
    for i in range(1, len(l_sorted)):
        swapped = False
        for j in range(len(l_sorted)-i):
            if l_sorted[j] > l_sorted[j+1]:
                temp = l_sorted[j+1]
                l_sorted[j+1] = l_sorted[j]
                l_sorted[j] = temp
                swapped = True
        if not swapped:
            return l_sorted
    return l_sorted


def insertion(l):
    l_sorted = [l[0]]
    for i in l[1:]:
        for j_index, j in enumerate(list(l_sorted)):
            if j < i:
                l_sorted.insert(j_index, i)
                break
    return l_sorted[::-1]


