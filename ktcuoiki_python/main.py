from tkinter import Tk, Frame, Button, Listbox, Scrollbar, NSEW, Label
from ktcuoiki_python.views import ql_hocphan
root = Tk()
root.title('Ứng Dụng Quản Lý Đăng Ký Học Phần')
root.minsize(height=500, width=500)

# Title label
Label(root, text='Ứng Dụng Quản Lý Đăng Ký Học Phần', fg='blue', font=('cambria', 20), width=30).grid(row=0, columnspan=7) # Cải thiện: Merge cells bằng columnspan

# Frame
frame = Frame(root)
frame.grid(sticky=NSEW)  # Fix the error by adding sticky

# Buttons
button2 = Button(frame, text="Quản Lý Học Phần")
button2.grid(row=1, column=1, padx=5, pady=10)

button3 = Button(frame, text="Quản Lý Đăng Ký Học Phần")
button3.grid(row=1, column=2, padx=5, pady=10)

button4 = Button(frame, text="Quản Lý Giá Học Phần")
button4.grid(row=1, column=3, padx=5, pady=10)

button5 = Button(frame, text="Danh Sách Đăng Ký Học Phần")
button5.grid(row=1, column=4, padx=5, pady=10)



# Listbox
frame_table = Frame(frame, width=100, height=20)
frame_table.grid(row=3, column=0, columnspan=7, padx=10, pady=10)


lb_frame = ql_hocphan.lb_frame(frame_table)
table = ql_hocphan.table(frame_table,lb_frame)
# # Scrollbar
scrollbar = Scrollbar(frame, orient="vertical" )#command=frame_table.yview()
scrollbar.grid(row=3, column=7, sticky='ns', pady=10)  # Fix the error here

# Link Listbox with Scrollbar
# lb.config(yscrollcommand=scrollbar.set)

# them , xoa , sua
button8 = Button(frame, text="Thêm")
button8.grid(row=4, column=9, padx=10, pady=10)

button9 = Button(frame, text="Xoá")
button9.grid(row=4, column=10, padx=10, pady=10)

button10 = Button(frame, text="Sửa")
button10.grid(row=4, column=11, padx=10, pady=10)


root.mainloop()