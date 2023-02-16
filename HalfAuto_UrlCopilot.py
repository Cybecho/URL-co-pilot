import keyboard
import tkinter as tk
import os
import sys

class URLCopiler:
    instances = []  # to store references to all instances of URLCopiler

    def __init__(self):
        self.result = ""
        URLCopiler.instances.append(self)

    def gotoUrl(self, URL):
        keyboard.press_and_release('ctrl+t')
        keyboard.press_and_release('ctrl+l')
        keyboard.write(URL)
        keyboard.press_and_release('enter')

    def runUrl(self, onKey, URL):
        keyboard.add_hotkey(onKey, lambda: self.gotoUrl(URL))
        print(self)

    def __del__(self):
        print(f"Deleting instance {self}")
        URLCopiler.instances.remove(self)

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def setUrl(entry):
    URL = entry.get()
    return URL

def clearObj():
    print("Reset everything")
    restart()


def submit():
    submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    Key_Ins.runUrl('insert', setUrl(ins_entry))
    Key_Del.runUrl('delete', setUrl(del_entry))
    Key_Home.runUrl('home', setUrl(home_entry))
    Key_End.runUrl('end', setUrl(end_entry))
    Key_Pageup.runUrl('pageup', setUrl(pageup_entry))
    Key_Pagedown.runUrl('pagedown', setUrl(pagedown_entry))
    Key_F1.runUrl('f1', setUrl(f1_entry))
    Key_F2.runUrl('f2', setUrl(f2_entry))
    Key_F3.runUrl('f3', setUrl(f3_entry))
    Key_F4.runUrl('f4', setUrl(f4_entry))
    Key_F6.runUrl('f6', setUrl(f6_entry))
    Key_F7.runUrl('f7', setUrl(f7_entry))
    Key_F8.runUrl('f8', setUrl(f8_entry))
    Key_F9.runUrl('f9', setUrl(f9_entry))
    Key_F10.runUrl('f10', setUrl(f10_entry))
    print("URL 설정 완료")


def exit_program():
    root.destroy()
    sys.exit()

root = tk.Tk()
root.wm_attributes("-topmost", 1) #윈도우 최상위 창 고정
root.title("URL co-pilot Ver1")

#화면해상도 얻기
monitor_height = root.winfo_screenheight()/2.5
monitor_width = root.winfo_screenwidth()/2.5

# Window 사이즈 지정
root.geometry(f"650x350+{int(monitor_width)}+{int(monitor_height)}")

# Create input fields and labels for each hotkey
ins_label = tk.Label(root, text="Ins")
ins_entry = tk.Entry(root)
del_label = tk.Label(root, text="Del")
del_entry = tk.Entry(root)
home_label = tk.Label(root, text="Home")
home_entry = tk.Entry(root)
end_label = tk.Label(root, text="End")
end_entry = tk.Entry(root)
pageup_label = tk.Label(root, text="Page Up")
pageup_entry = tk.Entry(root)
pagedown_label = tk.Label(root, text="Page Down")
pagedown_entry = tk.Entry(root)
f1_label = tk.Label(root, text="F1")
f1_entry = tk.Entry(root)
f2_label = tk.Label(root, text="F2")
f2_entry = tk.Entry(root)
f3_label = tk.Label(root, text="F3")
f3_entry = tk.Entry(root)
f4_label = tk.Label(root, text="F4")
f4_entry = tk.Entry(root)
f5_label = tk.Label(root, text="F5")
f5_entry = tk.Button(root, text="설정금지",width=20,height=1)
f6_label = tk.Label(root, text="F6")
f6_entry = tk.Entry(root)
f7_label = tk.Label(root, text="F7")
f7_entry = tk.Entry(root)
f8_label = tk.Label(root, text="F8")
f8_entry = tk.Entry(root)
f9_label = tk.Label(root, text="F9")
f9_entry = tk.Entry(root)
f10_label = tk.Label(root, text="F10")
f10_entry = tk.Entry(root)
f11_label = tk.Label(root, text="F11")
f11_entry = tk.Button(root, text="설정금지",width=20,height=1)
f12_label = tk.Label(root, text="F12")
f12_entry = tk.Button(root, text="설정금지",width=20,height=1)

#공지사항
notification_label = tk.Label(root, text="URL 새로고침시 URL입력 내용도 초기화 됩니다")
madeby_label = tk.Label(root, text="made by 끼끼도사")

# URL 적용버튼, 프로그램 종료버튼 생성
submit_button = tk.Button(root, text="URL 적용", command=submit, width=30,height=1)
reset_button = tk.Button(root, text="URL 초기화",command=clearObj,width=30,height=1,state=tk.DISABLED)
exit_button = tk.Button(root, text="프로그램 종료", command=exit_program, width=30,height=1)
# Pack labels, input fields, and buttons onto the GUI

ins_label.grid(row=0, column=0)
ins_entry.grid(row=0, column=1)
del_label.grid(row=1, column=0)
del_entry.grid(row=1, column=1)
home_label.grid(row=2, column=0)
home_entry.grid(row=2, column=1)
end_label.grid(row=3, column=0)
end_entry.grid(row=3, column=1)
pageup_label.grid(row=4, column=0)
pageup_entry.grid(row=4, column=1)
pagedown_label.grid(row=5, column=0)
pagedown_entry.grid(row=5, column=1)
f1_label.grid(row=0, column=2)
f1_entry.grid(row=0, column=3)
f2_label.grid(row=1, column=2)
f2_entry.grid(row=1, column=3)
f3_label.grid(row=2, column=2)
f3_entry.grid(row=2, column=3)
f4_label.grid(row=3, column=2)
f4_entry.grid(row=3, column=3)
f5_label.grid(row=4, column=2)
f5_entry.grid(row=4, column=3)
f6_label.grid(row=5, column=2)
f6_entry.grid(row=5, column=3)
f7_label.grid(row=6, column=2)
f7_entry.grid(row=6, column=3)
f8_label.grid(row=7, column=2)
f8_entry.grid(row=7, column=3)
f9_label.grid(row=8, column=2)
f9_entry.grid(row=8, column=3)
f10_label.grid(row=9, column=2)
f10_entry.grid(row=9, column=3)
f11_label.grid(row=10, column=2)
f11_entry.grid(row=10, column=3)
f12_label.grid(row=11, column=2)
f12_entry.grid(row=11, column=3)


submit_button.grid(row=0, column=4)
reset_button.grid(row=1, column=4)
exit_button.grid(row=2, column=4)

notification_label.grid(row=15, column=4)
madeby_label.grid(row=16, column=4)

# Create URLCopiler objects for each hotkey
Key_Ins = URLCopiler()
Key_Del = URLCopiler()
Key_Home = URLCopiler()
Key_End = URLCopiler()
Key_Pageup = URLCopiler()
Key_Pagedown = URLCopiler()
Key_F1 = URLCopiler()
Key_F2 = URLCopiler()
Key_F3 = URLCopiler()
Key_F4 = URLCopiler()
Key_F5 = URLCopiler()
Key_F6 = URLCopiler()
Key_F7 = URLCopiler()
Key_F8 = URLCopiler()
Key_F9 = URLCopiler()
Key_F10 = URLCopiler()
Key_F11 = URLCopiler()
Key_F12 = URLCopiler()

def on_closing():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main loop of the GUI
root.mainloop()

