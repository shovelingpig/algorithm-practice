# def f():
#    종료 조건
#    early termination 조건
#    분기1
#    분기2


def print_password(start, find):
    # termination
    if find == L:
        if isOk(answer) == true:
            print(answer)
        return

    # early termination
    if start + L - find > C:
        return

    answer[find] = candidates[start]
    print_password(start + 1, find + 1)
    print_password(start + 1, find)
