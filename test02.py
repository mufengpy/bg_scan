need_dic = [1, 1, 0, 0, 0, 0]

file_line_tuple = (1853, 821, 1152, 630, 418, 1066)

# print(need_dic, '\n', file_line_tuple)

need_dic_line_nums = sum([file_line_tuple[index] for index, item in enumerate(need_dic) if item is 1])

print(need_dic_line_nums)

# for index, item in enumerate(need_dic):
#     # print(index , item)
#     if item is 1:
#         print('当前index item', index, item)
#     #     # file_line_tuple[index]
