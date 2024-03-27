from tkinter import Tk, Frame, Button, Scrollbar, NSEW, Label
import tkinter as tk
from ktcuoiki_python.views import ql_hocphan,ql_dkhp,ql_sinhvien,ql_giatinchi
def create_mainview():
    root = Tk()
    # image = tk.PhotoImage(file="./public/image/nhom10.png")
    root.title('Ứng Dụng Quản Lý Đăng Ký Học Phần')
    root.minsize(height=500, width=500)
    root.resizable(False,False)
    # Title label
    Label(root, text='Ứng Dụng Quản Lý Đăng Ký Học Phần', fg='blue', font=('cambria', 20,'bold'), width=30).grid(row=0, columnspan=7)  # Cải thiện: Merge cells bằng columnspan
    root.iconbitmap("./public/image/nhom10.ico")
    # root.iconphoto(image)
    # Frame
    frame = Frame(root)
    frame.grid(sticky=NSEW)  # Fix the error by adding sticky

    # Buttons
    button2 = Button(frame, text="Quản Lý Học Phần", activebackground="#999999")
    button2.grid(row=0, column=1, padx=5, pady=10)

    button3 = Button(frame, text="Quản Lý Sinh Viên",activebackground="#999999")
    button3.grid(row=0, column=2, padx=5, pady=10)

    button4 = Button(frame, text="Quản Lý Giá Tín Chỉ",activebackground="#999999")
    button4.grid(row=0, column=3, padx=5, pady=10)

    button5 = Button(frame, text="Quản Lý Đăng Ký Học Phần",activebackground="#999999")
    button5.grid(row=0, column=4, padx=5, pady=10)

    # table
    frame_table = Frame(frame, width=100, height=20)
    frame_table.grid(row=1, column=0, columnspan=7, padx=10, pady=10)
    frame_input = Frame(frame)
    frame_input.grid(row=1, column=9, columnspan=3)
    # create_QLSV(frame_table,frame_input)
    # # Scrollbar
    scrollbar = Scrollbar(frame, orient="vertical")  # command=frame_table.yview()
    scrollbar.grid(row=1, column=7, sticky='ns', pady=10)  # Fix the error here

    # Link Listbox with Scrollbar
    # lb.config(yscrollcommand=scrollbar.set)
    # frame_table2 = Frame(frame,width=100,height=20)
    # frame_table2.grid(row=3,column=1,columnspan=7,padx=10,pady=10)
    # lb_frame2 = ql_hocphan.lb_frame(frame_table2)
    # table2 = ql_hocphan.table(frame_table2,lb_frame2)
    # them , xoa , sua

    button8 = Button(frame, text="Thêm",activebackground="#999999")
    button8.grid(row=4, column=9, padx=10, pady=10)

    button9 = Button(frame, text="Xoá",activebackground="#999999")
    button9.grid(row=4, column=10, padx=10, pady=10)

    button10 = Button(frame, text="Sửa",activebackground="#999999")
    button10.grid(row=4, column=11, padx=10, pady=10)
    button2.config(command= lambda : create_QLHP(frame_table, frame_input,root))
    button3.config(command= lambda : create_QLSV(frame_table, frame_input,root))
    button4.config(command= lambda : create_QLGIATC(frame_table,frame_input,root))
    button5.config(command= lambda : create_QLDKHP(frame_table, frame_input,root))
    # button2.config(state= tk.DISABLED)
    root.mainloop()



def create_QLHP(frame_table, frame_input, root):
    clear_frame(frame_table,frame_input)
    lb_frame = ql_hocphan.lb_frame(frame_input)
    table = ql_hocphan.table(frame_table, lb_frame)
    root.update()

def create_QLSV(frame_table,frame_input, root):
    clear_frame(frame_table,frame_input)
    lb_frame = ql_sinhvien.lb_frame(frame_input)
    table = ql_sinhvien.table(frame_table, lb_frame)
    root.update()

def create_QLDKHP(frame_table,frame_input, root):
    clear_frame(frame_table,frame_input)
    lb_frame = ql_dkhp.lb_frame(frame_input)
    table = ql_dkhp.table(frame_table, lb_frame)
    root.update()

def create_QLGIATC(frame_table,frame_input, root):
    clear_frame(frame_table, frame_input)
    lb_frame = ql_giatinchi.lb_frame(frame_input)
    table = ql_giatinchi.table(frame_table, lb_frame)
    root.update()

def clear_frame(frame_table,frame_input):
    try:
        for i in frame_table.winfo_children():
            i.destroy()
        for i in frame_input.winfo_children():
            i.destroy()
    except:
        print("nothing")
create_mainview()