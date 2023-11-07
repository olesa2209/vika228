# a = [1, 2, 3, 4, 5, 6]
# a.reverse()
# print(a)


# lst = [1, 2, 3, 4, 5, 6]
# def change(lst):
#     first = lst[0]
#     last = lst[-1]
#     lst[0] = last
#     lst[-1] = first
#     return lst

# print(change(lst))


# def to_list(*args):
#     return list (args)
# lst = to_list(1, 2, 3, 4, 5, 6)
# print(lst)

s = [1, 2, 3, 4, 5, 7]
def useless(s):
    if len(s) > 0:
        max_num = max(s)
        return max_num / len(s)
    else:
        return None

print(useless(s))
    
    