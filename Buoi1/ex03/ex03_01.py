def tinh_tong_so_chan(list):
    tong = 0
    for num in list:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("Nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map(int, input_list.split(',')))

tong_chan = tinh_tong_so_chan(numbers)
print("Tổng các số chẵn trong list là:", tong_chan)