#!/usr/bin/python3
#Jommal_calc_v01 _ GUI by TKINTER
''' 

حساب الجمّل: وهو حساب من وضع العرب قبل الميلاد بقرون؛ فعندما وضعوا الأبجدية جعلوا ترتيب حروفها على الصورة الآتية: (أ، ب، ج، د، هـ، و، ز، ح، ط، ي، ك، ل، م، ن، س، ع، ف، ص، ق، ر، ش، ت، ث، خ، ذ، ض، ظ، غ). ثم جعلوا لكل حرف من هذه الحروف قيمة عددية وفق الآتي:أ=1 ب=2 ج=3 د=4 هـ=5 و=6 ز=7 ح=8 ط=9 ي=10 ك=20 ل=30 م=40 ن=50 س=60 ع=70 ف=80 ص=90 ق=100 ر=200 ش=300 ت=400 ث=500 خ=600 ذ=700 ض=800 ظ=900 غ=1000

والتاء المربوطة (ـة) تحسب هاء، لأنّها ترسم هاءً وتلفظ عند الوقف هاءً أيضاً. والألف المقصورة تحسب ياء، لأنها ترسم على صورة الياء (ى).
"""
      '''
import tkinter as tk


class JommalCalcV01App:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.main_window.configure(
            background="#870c78",
            height=200,
            relief="flat",
            width=200)
        self.main_window.geometry("800x480")
        self.main_window.resizable(False, False)
        self.main_window.title("حاسبة الجُمّل")
        self.main_frame = tk.Frame(self.main_window)
        self.main_frame.configure(background="#870c78", height=480, width=800)
        self.lbl1 = tk.Label(self.main_frame)
        self.lbl1.configure(
            background="#870c78",
            font="{Arial} 24 {bold underline}",
            foreground="#ffffff",
            justify="center",
            pady=20,
            takefocus=False,
            text='حاسبة الجُمّل')
        self.lbl1.pack(side="top")
        
        self.txt1 = tk.Text(self.main_frame)
        self.txt1.configure(
            font="{Arial} 12 {bold}",
            height=10,
            relief="sunken",
            undo="true",
            width=80,
            wrap="word")
        _text_ = 'أدخل النص'
        #ADDED RTL
        self.txt1.tag_configure('tag-right', justify='right')
        self.txt1.insert('end', 'امسح الكل ثم أدخل النص ' , 'tag-right')
        
        ###
        #self.txt1.insert("0.0", _text_)
        self.txt1.pack(side="top")
        self.btn1 = tk.Button(self.main_frame)
        self.btn1.configure(
            compound="center",
            font="{Arial} 16 {}",
            justify="center",
            relief="ridge",
            text='أحسب النتيجة')
        self.btn1.pack(pady=10, side="top")
        self.btn1.configure(command=self.calc)
        self.res_ent = tk.Entry(self.main_frame)
        self.res_ent_var = tk.StringVar()
        self.res_ent.configure(
            background="#870c78",
            borderwidth=0,
            font="{Arial} 14 {bold}",
            foreground="#ffffff",
            justify="center",
            readonlybackground="#870c78",
            state="readonly",
            validate="none",textvariable=self.res_ent_var,
            width=50)
        self.res_ent.pack(side="top")
        label4 = tk.Label(self.main_frame)
        label4.configure(
            background="#870c78",
            font="{Arial} 9 {italic}",
            foreground="#000000",
            justify="center",
            relief="sunken",
            text='Jommal_calc_v01, 2022, Imdad Pro, imdadpro@gmail.com')
        label4.pack(padx=10, pady=50, side="left")
        self.main_frame.pack(fill="both", side="top")

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def calc(self):
        input=self.txt1.get("1.0",tk.END)
        self.txt1.delete("1.0",tk.END)
        
        x=0
        for i in input :
            if i =="ا" :
              x=x+1
            elif i=="أ" :
              x=x+1
            elif i=="ٱ" :
              x=x+1
            elif i=="إ" :
              x=x+1
            elif i=="ء" :
              x=x+1
            elif i=="ئ" :
              x=x+1
            elif i=="ؤ" :
              x=x+1
            elif i=="ب" :
              x=x+2
            elif i=="آ" :
              x=x+2
            elif i=="ج" :
              x=x+3
            elif i=="د" :
              x=x+4
            elif i=="ه" :
              x=x+5
            elif i=="ة" :
              x=x+5
            elif i=="و" :
              x=x+6
            elif i=="ز" :
              x=x+7
            elif i=="ح" :
              x=x+8
            elif i=="ط" :
              x=x+9
            elif i=="ى" :
              x=x+10
            elif i=="ي" :
              x=x+10
            elif i=="ئ" :
              x=x+10
            elif i=="ك" :
              x=x+20
            elif i=="ل" :
              x=x+30
            elif i=="م" :
              x=x+40
            elif i=="ن" :
              x=x+50
            elif i=="س" :
              x=x+60
            elif i=="ع" :
              x=x+70
            elif i=="ف" :
              x=x+80
            elif i=="ص" :
              x=x+90
            elif i=="ق" :
              x=x+100
            elif i=="ر" :
              x=x+200
            elif i=="ش" :
              x=x+300
            elif i=="ت" :
              x=x+400
            elif i=="ث" :
              x=x+500
            elif i=="خ" :
              x=x+600
            elif i=="ذ" :
              x=x+700
            elif i=="ض" :
              x=x+800
            elif i=="ظ" :
              x=x+900
            elif i=="غ" :
              x=x+1000
        
        self.res_ent_var.set(x)
                #res=self.res_ent_var


if __name__ == "__main__":
    app = JommalCalcV01App()
    app.run()
