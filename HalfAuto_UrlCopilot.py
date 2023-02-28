import keyboard
import tkinter as tk
import os
import sys
import time

#메인 부모 클래스
class URLCopiler:
    instances = []  # to store references to all instances of URLCopiler

    def __init__(self):
        self.result = ""
        URLCopiler.instances.append(self)

    def gotoUrl(self, URL):
        #time.sleep(0.03) #약간의 딜레이를 넣어야 F4를 눌렀을때 오류가 안생김 근데 이러면 F1이 문제생김
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

#키 F4 만을 위한 자식클래스
class URLCopiler_F4(URLCopiler):

    def gotoUrl(self, URL):
        time.sleep(0.03) #약간의 딜레이를 넣어야 F4를 눌렀을때 오류가 안생김
        keyboard.press_and_release('ctrl+t')
        keyboard.press_and_release('ctrl+l')
        keyboard.write(URL)
        keyboard.press_and_release('enter')

class URLCopiler_dot(URLCopiler):

    def gotoUrl(self, URL):
        keyboard.write('12121212')

def restart():
    os.execl(sys.executable, sys.executable, *sys.argv)

def setUrl(entry):
    URL = entry.get()
    return URL

#초기화 함수
def clearObj():
    print("Reset everything")
    restart()



################################################################

#각 키별로 개별 URL 설정

def submit_Ins():
    ins_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_Ins.runUrl('insert', setUrl(ins_entry))
    print("URL 설정 완료")

def submit_Del():
    del_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_Del.runUrl('delete', setUrl(del_entry))
    print("URL 설정 완료")

def submit_Home():
    home_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_Home.runUrl('home', setUrl(home_entry))
    print("URL 설정 완료")

def submit_End():
    end_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_End.runUrl('end', setUrl(end_entry))
    print("URL 설정 완료")

def submit_Pageup():
    pageup_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_Pageup.runUrl('pageup', setUrl(pageup_entry))
    print("URL 설정 완료")

def submit_Pagedown():
    pagedown_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_Pagedown.runUrl('pagedown', setUrl(pagedown_entry))
    print("URL 설정 완료")

def submit_F1():
    f1_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F1.runUrl('f1', setUrl(f1_entry))
    print("URL 설정 완료")

def submit_F2():
    f2_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F2.runUrl('f2', setUrl(f2_entry))
    print("URL 설정 완료")

def submit_F3():
    f3_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F3.runUrl('f3', setUrl(f3_entry))
    print("URL 설정 완료")

def submit_F4():
    f4_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F4.runUrl('f4', setUrl(f4_entry))
    print("URL 설정 완료")

def submit_F6():
    f6_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F6.runUrl('f6', setUrl(f6_entry))
    print("URL 설정 완료")

def submit_F7():
    f7_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F7.runUrl('f7', setUrl(f7_entry))
    print("URL 설정 완료")

def submit_F8():
    f8_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F8.runUrl('f8', setUrl(f8_entry))
    print("URL 설정 완료")

def submit_F9():
    f9_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F9.runUrl('f9', setUrl(f9_entry))
    print("URL 설정 완료")

def submit_F10():
    f10_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_F10.runUrl('f10', setUrl(f10_entry))
    print("URL 설정 완료")

def submit_dot():
    dot_submit_button.config(state=tk.DISABLED) #한번 눌리면 초기화
    reset_button.config(state=tk.NORMAL)
    
    Key_dot.runUrl('alt + shift', setUrl(dot_entry))

################################################################

def exit_program():
    root.destroy()
    sys.exit()

root = tk.Tk()
root.wm_attributes("-topmost", 1) #윈도우 최상위 창 고정
root.title("URL co-pilot Ver2")

#화면해상도 얻기
monitor_height = root.winfo_screenheight()/2.5
monitor_width = root.winfo_screenwidth()/2.5

# Window 사이즈 지정
root.geometry(f"820x380+{int(monitor_width)}+{int(monitor_height)}")

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
dot_label = tk.Label(root, text="alt + shift")
dot_entry = tk.Entry(root)
f1_label = tk.Label(root, text="F1")
f1_entry = tk.Entry(root)
f2_label = tk.Label(root, text="F2")
f2_entry = tk.Entry(root)
f3_label = tk.Label(root, text="F3")
f3_entry = tk.Entry(root)
f4_label = tk.Label(root, text="F4")
f4_entry = tk.Entry(root)
f5_label = tk.Label(root, text="F5")
f5_entry = tk.Button(root, text="설정금지",width=20,height=1,state=tk.DISABLED)
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
f11_entry = tk.Button(root, text="설정금지",width=20,height=1,state=tk.DISABLED)
f12_label = tk.Label(root, text="F12")
f12_entry = tk.Button(root, text="설정금지",width=20,height=1,state=tk.DISABLED)

#공지사항
notification_label = tk.Label(root, text="URL 새로고침시 입력한 내용 전체가 초기화됨")
madeby_label = tk.Label(root, text="made by 끼끼도사")

# 프로그램 종료버튼 생성
reset_button = tk.Button(root, text="URL 초기화",command=clearObj,width=30,height=1,state=tk.DISABLED)
exit_button = tk.Button(root, text="프로그램 종료", command=exit_program, width=30,height=1)

# 각 키마다 URL 적용버튼
ins_submit_button = tk.Button(root, text="Ins 적용", command=submit_Ins, width=10,height=1)
del_submit_button = tk.Button(root, text="Del 적용", command=submit_Del, width=10,height=1) 
home_submit_button = tk.Button(root, text="Home 적용", command=submit_Home, width=10,height=1) 
end_submit_button = tk.Button(root, text="End 적용", command=submit_End, width=10,height=1) 
pageup_submit_button = tk.Button(root, text="PgUp 적용", command=submit_Pageup, width=10,height=1) 
pagedown_submit_button = tk.Button(root, text="PgDown 적용", command=submit_Pagedown, width=10,height=1) 

f1_submit_button = tk.Button(root, text="F1 적용", command=submit_F1, width=10,height=1)
f2_submit_button = tk.Button(root, text="F2 적용", command=submit_F2, width=10,height=1)
f3_submit_button = tk.Button(root, text="F3 적용", command=submit_F3, width=10,height=1)
f4_submit_button = tk.Button(root, text="F4 적용", command=submit_F4, width=10,height=1)
f6_submit_button = tk.Button(root, text="F6 적용", command=submit_F6, width=10,height=1)
f7_submit_button = tk.Button(root, text="F7 적용", command=submit_F7, width=10,height=1)
f8_submit_button = tk.Button(root, text="F8 적용", command=submit_F8, width=10,height=1)
f9_submit_button = tk.Button(root, text="F9 적용", command=submit_F9, width=10,height=1)
f10_submit_button = tk.Button(root, text="F10 적용", command=submit_F10, width=10,height=1)

dot_submit_button = tk.Button(root, text="..단축키에 12121212 적용", command=submit_dot, width=20,height=1)

'''
#우측정렬
f1_submit_button.configure(anchor="e", justify="right")
f2_submit_button.configure(anchor="e", justify="right")
f3_submit_button.configure(anchor="e", justify="right")
f4_submit_button.configure(anchor="e", justify="right")
f6_submit_button.configure(anchor="e", justify="right")
f7_submit_button.configure(anchor="e", justify="right")
f8_submit_button.configure(anchor="e", justify="right")
f9_submit_button.configure(anchor="e", justify="right")
f10_submit_button.configure(anchor="e", justify="right")
'''

# GUI 버튼 및 텍스트 배치부분

ins_label.grid(row=0, column=0)
ins_entry.grid(row=0, column=1)
ins_submit_button.grid(row=0, column=2)

del_label.grid(row=1, column=0)
del_entry.grid(row=1, column=1)
del_submit_button.grid(row=1, column=2)

home_label.grid(row=2, column=0)
home_entry.grid(row=2, column=1)
home_submit_button.grid(row=2, column=2)

end_label.grid(row=3, column=0)
end_entry.grid(row=3, column=1)
end_submit_button.grid(row=3, column=2)

pageup_label.grid(row=4, column=0)
pageup_entry.grid(row=4, column=1)
pageup_submit_button.grid(row=4, column=2)

pagedown_label.grid(row=5, column=0)
pagedown_entry.grid(row=5, column=1)
pagedown_submit_button.grid(row=5, column=2)

dot_label.grid(row=6, column=0)
#dot_entry.grid(row=6, column=1)
dot_submit_button.grid(row=6, column=1)

f1_label.grid(row=0, column=3)
f1_entry.grid(row=0, column=4)
f1_submit_button.grid(row=0, column=5)

f2_label.grid(row=1, column=3)
f2_entry.grid(row=1, column=4)
f2_submit_button.grid(row=1, column=5)

f3_label.grid(row=2, column=3)
f3_entry.grid(row=2, column=4)
f3_submit_button.grid(row=2, column=5)

f4_label.grid(row=3, column=3)
f4_entry.grid(row=3, column=4)
f4_submit_button.grid(row=3, column=5)

f5_label.grid(row=4, column=3)
#f5_entry.grid(row=4, column=4)
#submit 버튼 필요없음

f6_label.grid(row=5, column=3)
f6_entry.grid(row=5, column=4)
f6_submit_button.grid(row=5, column=5)

f7_label.grid(row=6, column=3)
f7_entry.grid(row=6, column=4)
f7_submit_button.grid(row=6, column=5)

f8_label.grid(row=7, column=3)
f8_entry.grid(row=7, column=4)
f8_submit_button.grid(row=7, column=5)

f9_label.grid(row=8, column=3)
f9_entry.grid(row=8, column=4)
f9_submit_button.grid(row=8, column=5)

f10_label.grid(row=9, column=3)
f10_entry.grid(row=9, column=4)
f10_submit_button.grid(row=9, column=5)

f11_label.grid(row=10, column=3)
#f11_entry.grid(row=10, column=4)
#submit 버튼 필요없음

f12_label.grid(row=11, column=3)
#f12_entry.grid(row=11, column=4)
#submit 버튼 필요없음

reset_button.grid(row=0, column=6)
exit_button.grid(row=1, column=6)

notification_label.grid(row=15, column=6)
madeby_label.grid(row=16, column=6)

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
Key_F4 = URLCopiler_F4()
Key_F5 = URLCopiler()
Key_F6 = URLCopiler()
Key_F7 = URLCopiler()
Key_F8 = URLCopiler()
Key_F9 = URLCopiler()
Key_F10 = URLCopiler()
Key_F11 = URLCopiler()
Key_F12 = URLCopiler()

#단순하게 12121212만 치는놈
Key_dot = URLCopiler_dot()

def on_closing():
    root.destroy()
    sys.exit()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the main loop of the GUI
root.mainloop()

