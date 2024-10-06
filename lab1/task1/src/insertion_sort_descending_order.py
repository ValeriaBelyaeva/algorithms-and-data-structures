def insertion_sort_reverse(to_sort):
    for i in range(1, len(to_sort)):
        key = to_sort[i]
        j = i - 1
        while j >= 0 and key > to_sort[j]:
            to_sort[j + 1] = to_sort[j]
            j -= 1
        to_sort[j + 1] = key

    return to_sort

inp_file = open("input")
inp = list(map(int, inp_file.readline().split()))
inp_file.close()
out_file = open("output", 'w')
try:
    ans = insertion_sort_reverse(inp)
    out = ''
    for e in ans:
        out = out + str(e) + ' '
    out_file.write(out)
except:
    print('we have egor :(')

out_file.close()