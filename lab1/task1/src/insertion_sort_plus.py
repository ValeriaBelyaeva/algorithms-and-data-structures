def insertion_sort(to_sort: list)-> (list, list):
    n = len(to_sort)
    swap_id = [1]
    for i in range(1, n):
        key = to_sort[i]
        j = i - 1
        while j >= 0 and key < to_sort[j]:
            to_sort[j + 1] = to_sort[j]
            j -= 1
        swap_id.append(j+2)
        to_sort[j + 1] = key

    return (swap_id, to_sort)


'''inp_file = open("input")
inp = list(map(int, inp_file.readline().split()))
inp_file.close()
out_file = open("output", 'w')
try:
    ans1, ans2 = insertion_sort(inp)
    out1 = ''
    for e in ans1:
        out1 = out1 + str(e) + ' '
    out2 = ''
    for e in ans2:
        out2 = out2 + str(e) + ' '
    out_file.write(out1+'\n'+out2)
except:
    print('we have egor :(')

out_file.close()'''