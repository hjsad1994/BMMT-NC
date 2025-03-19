from QuanLySinhVien import QuanLySinhVien
qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*****************************Menu*************************")
    print("**  1. Them Sinh Vien.                                  **")
    print("**  2. Cap nhat thong tin sinh vien boi ID.             **")
    print("**  3. Xoa sinh vien boi ID.                            **")
    print("**  4. Tim kiem sinh vien theo ten.                     **")
    print("**  5. Sap xep sinh vien theo diem trung binh.          **")
    print("**  6. Sap xeo sinh vien theo chuyen nghanh.            **")
    print("**  7. Hien thi danh sach sinh vien.                    **")
    print("**  0. Thoat                                            **")
    print("**********************************************************")
    
    key = int (input("Nhap tuy chon: "))
    if (key == 1):
        print("\n1. Them Sinh Vien.")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
    elif (key == 2):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Them Sinh Vien.")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xoa Sinh Vien.")
            print("\nNhap ID: ")
            ID = int(input())
            if (qlsv.deleteByID(ID)):
                print("\nSinh Vien co id =", ID, "Da bi xoa.")
            else:
                print("\nSinh Vien co id =", ID, "Khong ton tai.")
        else:
            print("\nDanh sach sinh vien trong!")
        print("\nThem sinh vien thanh cong!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten.")
            print("\nNhap ten de tim kiem: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 5):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 6):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 7):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien trong!")
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh.")
        break
    else:
        print("\nKhong co chuc nang nay!")
        print("\n Hay chon lai chuc nang!")