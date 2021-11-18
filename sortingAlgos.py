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


def merge(l):
    if len(l) > 1:
        midpoint = int(len(l) / 2)
        a = l[:midpoint].copy()
        b = l[midpoint:].copy()
        merged_a = merge(a)
        merged_b = merge(b)
        # merge the sorted split lists
        ans = []
        a_index = 0
        b_index = 0
        for index in range(len(l)):
            # one of the lists is empty
            if a_index >= len(merged_a):
                ans += merged_b[b_index:]
                break
            if b_index >= len(merged_b):
                ans += merged_a[a_index:]
                break
            # both lists have elements
            if merged_a[a_index] > merged_b[b_index]:
                ans.append(merged_b[b_index])
                b_index += 1
            else:
                ans.append(merged_a[a_index])
                a_index += 1
        return ans
    else:
        return l

if __name__ == "__main__":
    l = [10, 4, 16, 25, 7, 99]
    sorted_l = merge(l)
    print(sorted_l)