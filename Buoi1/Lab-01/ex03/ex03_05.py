def dem_so_lan_xuat_hien(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict
input_string = input("Nhập danh sách từ, cách nhau bằng dấu: ")
word_list = input_string.split()

result = dem_so_lan_xuat_hien(word_list)
print("số lần xuất hiện của các phần tử:", result)