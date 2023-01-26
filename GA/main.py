import random
import time
import Mysql
from tkinter import LEFT, CENTER, END, messagebox, NORMAL, DISABLED, W, VERTICAL, BOTH
import tkinter as tk
import mysql.connector
import proctection
import userdata
import rps
import score
import printdata as p
import constant
global x,x1,x2,x3,x4,x5


# Connect to MySQL Workbench -------------------------------
mydb = mysql.connector.connect(host=Mysql.h,user=Mysql.u,password=Mysql.pas,port=Mysql.po,database=Mysql.dat)
mycursor = mydb.cursor()
mycursor.execute("select username from gaming_application")
users1 = mycursor.fetchall()
for l in users1:
    U = (''.join(str(e) for e in l))
    proctection.GAusername.append(U)
#-----------------------------------------------------------
class Canvas_Frame:
    def __init__(self):
        self.gamingApplicationWindow = tk.Tk()
        self.gamingApplicationWindow.state('zoomed')
        self.gamingApplicationWindow.title('Gaming Application')
        self.gamingApplicationWindow.geometry('1920x800')
        image = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/D2.png')
        canvasScreen_1 = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
        canvasScreen_1.pack()
        canvasScreen_1.create_image(0, 0, image=image, anchor='nw')
        canvasScreen_1.create_text(770, 200, text="Welcome", fill='#FFBC00', font=('Lucida Calligraphy', 35))
        canvasScreen_1.create_text(775, 280, text="To", fill='#FFBC00', font=('Lucida Calligraphy', 35))
        canvasScreen_1.create_text(760, 360, text="Gaming World", fill='#FFBC00', font=('Lucida Calligraphy', 35))
        canvasScreen_1.create_text(1400, 710, text="Developed by:", fill='#0022d2', font=('Lucida Calligraphy', 20))
        canvasScreen_1.create_text(1380, 750, text="Sudhanshu & Divya ", fill='#0022d2', font=('Lucida Calligraphy', 20))
        image2 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/ss4.png')
        canvas_2_Login_Page = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
        # canvas2 is user login page.................
        canvas_Entry_New_User_Details = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
        # canvas3 is created new username and Password.................
        # canvas_login_successfull = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
        # canvas4 use when login username password is successfully .................
        canvas_Choose_Username_Password = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
        # canvas5 select new username and password.....................

        image3 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/pp.png')
        image4 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/ik.png')
        image5 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/cr (2).png')
        image6 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/close (2).png')
        image7 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Black Wallpaper 4K - WallpaperSafari.png')
        image8 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/voyager2 (1).png')
        image9 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/pioneer11.png')
        image10 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/stp (4).png')
        image11 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/ttt1.png')
        image12 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/tic1 (1).png')
        image13 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/rock-paper-scissors (4).png')
        image14= tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/mprofile.png')
        image15 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/fprofile.png')
        image16 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/tprofile.png')
        image17 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/duser.png')
        image18 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/exit2.png')
        image19 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/userslist.png')
        background21 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/k3.png')
        vsimage = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Ryuk.png')
        vsprofile = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Studying.png')
        userdelete = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Do.png')
        tleaderbord = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Berserk.png')
        rpsleaderbord = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/aKhMhFy.png')
        #

        #
        dd=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
        mm=['January','February','March','April','May','June','July','August','September','October','November','December']
        yy=[]
        for  i in range (1980,2030):
            yy.append(i)

        cross = tk.Label(canvas_2_Login_Page, image=image6)
        cross1 = tk.Label(canvas_2_Login_Page, image=image6)

        def onClick():
            canvasScreen_1.create_text(755, 650, text="Processing To Next Screen...", fill='#b86b23', font=('Lucida Calligraphy', 20))
            canvasScreen_1.update()
            time.sleep(2)
            canvasScreen_1.pack_forget()
            canvas_2_Login_Page.pack(fill="both", expand=True)
            canvas_2_Login_Page.create_image(0, 0, image=image3, anchor='nw')
            canvas_2_Login_Page.create_image(300, 100, image=image4, anchor='nw')
            canvas_2_Login_Page.create_text(550, 150, text="Username", fill='#000000', font=('Rubik Distressed', 20))
            canvas_2_Login_Page.create_text(550, 250, text="Password", fill='#000000', font=('Rubik Distressed', 20))
# -----------------------------------------------------------------------------------------------------------------------------------------------------
            def create_new_user():
                canvas_2_Login_Page.pack_forget()
                canvas_Entry_New_User_Details.pack(fill="both", expand=True)
                canvas_Entry_New_User_Details.create_image(0, 0, image=image8, anchor='nw')
                user_firstname = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))
                user_lastname = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))
                user_year = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))
                user_month = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))
                user_date = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))
                user_gender = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))
                user_email = tk.Entry(canvas_Entry_New_User_Details, font=('Rye', 15))

                canvas_Entry_New_User_Details.create_text(550, 150, text="First Name", fill='#000000', font=('Rye', 20))
                canvas_Entry_New_User_Details.create_text(550, 200, text="Last Name", fill='#000000', font=('Rye', 20))
                canvas_Entry_New_User_Details.create_text(550, 250, text="Age", fill='#000000', font=('Rye', 20))
                canvas_Entry_New_User_Details.create_text(550, 300, text="Gender", fill='#000000', font=('Rye', 20))
                canvas_Entry_New_User_Details.create_text(520, 350, text="Email Address", fill='#000000', font=('Rye', 20))

                clicked = tk.IntVar()
                clicked.set(9)
                drop = tk.OptionMenu(canvas_Entry_New_User_Details, clicked, *dd)
                drop5 = canvas_Entry_New_User_Details.create_window(660, 235, anchor='nw', window=drop)
                clicked1 = tk.StringVar()
                clicked1.set("September")
                drop1 = tk.OptionMenu(canvas_Entry_New_User_Details, clicked1, *mm)
                drop6 = canvas_Entry_New_User_Details.create_window(720, 235, anchor='nw', window=drop1)
                clicked2 = tk.IntVar()
                clicked2.set(2000)
                drop2 = tk.OptionMenu(canvas_Entry_New_User_Details, clicked2, *yy)
                drop7 = canvas_Entry_New_User_Details.create_window(830, 235, anchor='nw', window=drop2)
                user_firstname1 = canvas_Entry_New_User_Details.create_window(660, 135, anchor='nw', window=user_firstname)
                user_lastname1 = canvas_Entry_New_User_Details.create_window(660, 185, anchor='nw', window=user_lastname)
                user_gender1 = canvas_Entry_New_User_Details.create_window(660, 285, width=70, anchor='nw', window=user_gender)
                canvas_Entry_New_User_Details.create_text(950, 300, text="(eg: male = M,female = F)", fill='#000000', font=('Rye', 15))
                user_email1 = canvas_Entry_New_User_Details.create_window(660, 335, width=250, anchor='nw', window=user_email)

                def chk():
                    if len(user_firstname.get()) > 3:
                        x=1
                    else:
                        x=0
                    if len(user_lastname.get()) > 3:
                        x1=1
                    else:
                        x1=0
                    if user_gender.get() == 'T' or user_gender.get() == 'M' or user_gender.get() == 'F' or user_gender.get() == 't' or user_gender.get() == 'm' or user_gender.get() == 'f':
                        x2=1
                    else:
                        x2=0
                    if (len(str(user_email.get())) > 3) and  (user_email.get().__contains__('@')) and (user_email.get().__contains__('gmail.com')):
                        x3=1
                    else:
                        x3=0

                    if x+x1+x2+x3 !=4:
                        messagebox.showerror('Error','Please Enter Valid Details')
                        return x+x1+x2+x3
                    else:
                        return x+x1+x2+x3

                def user_next():
                    y = chk()
                    if y  == 4:
                        canvas_Entry_New_User_Details.pack_forget()
                        canvas_Choose_Username_Password.pack()
                        canvas_Choose_Username_Password.create_image(0, 0, image=image9, anchor='nw')
                        canvas_Choose_Username_Password.create_text(750, 150, text="Select Username", fill='#000000', font=('Rye', 20))
                        canvas_Choose_Username_Password.create_text(750, 280, text="Select Password", fill='#000000', font=('Rye', 20))
                        canvas_Choose_Username_Password.create_text(750, 410, text="Confirm Password", fill='#000000', font=('Rye', 20))
                        user_username = tk.Entry(canvas_Choose_Username_Password, font=('Rye', 15), width=18)
                        user_username1 = canvas_Choose_Username_Password.create_window(628, 200, anchor='nw', window=user_username)
                        user_password = tk.Entry(canvas_Choose_Username_Password, font=('Rye', 15), width=18)
                        user_password1 = canvas_Choose_Username_Password.create_window(628, 330, anchor='nw', window=user_password)
                        user_password2 = tk.Entry(canvas_Choose_Username_Password, font=('Rye', 15), width=18)
                        user_password3 = canvas_Choose_Username_Password.create_window(628, 460, anchor='nw', window=user_password2)
                        user_password.insert(0,'Create Password')
                        user_username.insert(0,'Choose Username')
                        user_password2.insert(0,'Confirm password')
                    try:
                        def user_clear(e):
                            user_creates.config(state=DISABLED)
                            canvas_Choose_Username_Password.update()
                            if user_password.get() == 'Create Password' or user_password2.get() == 'Confirm password':
                                user_password.delete(0, END)
                                user_password2.delete(0, END)
                                user_password.config(show='*')
                                user_password2.config(show='*')
                                canvas_Choose_Username_Password.update()

                    except Exception:
                        print('')
                    try:
                        user_password.bind("<Button-1>", user_clear)
                        user_password2.bind("<Button-1>", user_clear)
                    except Exception:
                        print('')

                    def user_disable(e):
                        canvas_Choose_Username_Password.update()
                        user_creates.config(state=DISABLED)
                        if len(user_username.get()) == 15:
                            user_username.delete(0, END)
                        canvas_Choose_Username_Password.update()
                    user_username.bind("<Button-1>", user_disable)

                    def user_check():
                        if user_password.get() == user_password2.get():
                            user_creates.config(state=NORMAL)
                        else:
                            messagebox.askretrycancel('Retry',"Password did not match")
                        if len(user_password.get()) == 0 or len(user_password.get()) == 0 or len(user_username.get())<3:
                            user_creates.config(state=DISABLED)
                            messagebox.askretrycancel('Retry', "Username and Password are Invalid")
                        if len(user_password.get())>10:
                            user_creates.config(state=DISABLED)
                            messagebox.askretrycancel('Retry', "Username and Password are Invalid")
                        if len(user_username.get())>10:
                            user_creates.config(state=DISABLED)
                            messagebox.askretrycancel('Retry', "Username and Password are Invalid")
                        print('check')

                    user_check = tk.Button(canvas_Choose_Username_Password, text='check', font=('Rye', 12), width=10, command=user_check)
                    user_check = canvas_Choose_Username_Password.create_window(610, 545, anchor='nw', window=user_check)
                    def user_create():
                        # print(user_username.get(),user_password.get(),user_password2.get(),user_firstname.get(),user_lastname.get(),user_email.get()
                        #       ,clicked.get(),clicked1.get(),clicked2.get(),user_gender.get())
                        mycursor.execute('select username from gaming_application')
                        sql_usernames = mycursor.fetchall()
                        sUsers = []
                        userValidity = False
                        for l in sql_usernames:
                            s_user = (''.join(str(e) for e in l))
                            sUsers.append(s_user)
                        # print(sUsers)
                        for p in sUsers:
                            if p == user_username.get():
                                userValidity = True
                                tk.messagebox.showwarning('Invalid Username','Username Already Exist')
                                user_creates.config(state=DISABLED)
                        if not userValidity:
                            try:
                                mycursor.execute("""insert into gaming_application (username, passwords, name) values ('%s','%s','%s')""" %(user_username.get() ,user_password.get() ,user_firstname.get()))
                                mydb.commit()
                                proctection.GAusername.append(user_username.get())
                                print('username added to database')
                                # mycursor.execute("""CREATE TABLE %s (UserName varchar(10),FirstName varchar(30),LastName varchar(30),Gender varchar(15),DOB varchar(30),EmailAddress varchar(50))""" % user_username.get())
                                # mydb.commit()
                                print("table created")
                                if user_gender.get() == 'F' or  user_gender.get() =='f':
                                   userdata.genderMorF ='Female'
                                elif user_gender.get() == 'M' or user_gender.get() == 'm':
                                    userdata.genderMorF = 'Male'
                                else:
                                    userdata.genderMorF = 'Transgender'
                                userdata.ageDD = str(clicked.get()) +"/"+ str(clicked1.get()) +"/" + str(clicked2.get())
                                print(userdata.ageDD)
                                # mycursor.execute("""insert into %s (UserName, FirstName, LastName, Gender, DOB, EmailAddress) values ('%s','%s','%s','%s','%s','%s') """ %(user_username.get(),user_username.get(),user_firstname.get(),user_lastname.get(),userdata.genderMorF,userdata.ageDD,user_email.get()))
                                # mydb.commit()
                                mycursor.execute("""insert into user_registration (UserName, FirstName, LastName, Gender, DOB, EmailAddress) values ('%s','%s','%s','%s','%s','%s') """ % (user_username.get(), user_firstname.get(), user_lastname.get(),userdata.genderMorF, userdata.ageDD, user_email.get()))
                                mydb.commit()
                                print('data enter successfully')
                            except Exception:
                                print('error')
                            tk.messagebox.showinfo('Congratulation!',"Account Created Successfully")
                            canvas_Choose_Username_Password.pack_forget()
                            canvas_2_Login_Page.pack()
                            print('create')
                    user_creates = tk.Button(canvas_Choose_Username_Password, text='Create', font=('Rye', 12), width=10, command=user_create, state=DISABLED)
                    user_create = canvas_Choose_Username_Password.create_window(760, 545, anchor='nw', window=user_creates)
                    print('next')

                user_next = tk.Button(canvas_Entry_New_User_Details, text='Next', font=('Rye', 12), width=10, command=user_next)
                user_next = canvas_Entry_New_User_Details.create_window(730, 385, anchor='nw', window=user_next)
                def user_previous():
                    canvas_Entry_New_User_Details.pack_forget()
                    canvas_2_Login_Page.pack()
                user_previous = tk.Button(canvas_Entry_New_User_Details, text='Back', font=('Rye', 12), width=10, command=user_previous)
                user_previous = canvas_Entry_New_User_Details.create_window(600, 385, anchor='nw', window=user_previous)


            create_btn = tk.Button(canvas_2_Login_Page, image=image5, bd=0, highlightthickness=0, command=create_new_user)
            create_btn_window = canvas_2_Login_Page.create_window(470, 410, anchor='nw', window=create_btn)
            my_username = tk.Entry(canvas_2_Login_Page, font=('Rubik Distressed', 15))
            my_password = tk.Entry(canvas_2_Login_Page, font=('Rubik Distressed', 15))

            my_username.insert(0,'username')
            my_password.insert(0,'password')

            u_window = canvas_2_Login_Page.create_window(480, 180, anchor='nw', window=my_username)
            p_window = canvas_2_Login_Page.create_window(480, 280, anchor='nw', window=my_password)

            def login_success():
                sucess = False
                for U in proctection.GAusername:
                    mycursor.execute("""select passwords from gaming_application where username = '%s'""" %U)
                    users3 = mycursor.fetchall()
                    for l in users3:
                        Pa = (''.join(str(e) for e in l))
                    if my_username.get() == U and my_password.get() == Pa:
                        sucess = True
                        canvas_2_Login_Page.pack_forget()
                        canvas_login_successfull = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920,height=800, bd=0, highlightthickness=0)
                        canvas_login_successfull.pack(fill="both", expand=True)
                        canvas_login_successfull.create_image(0, 0, image=image7, anchor='nw')
                        canvas_login_successfull.create_text(750,50,text=f"Welcome {my_username.get()} to Gaming World",fill='#EA8AE8',font=('Perpetua Titling MT', 25))
                        # canvas_login_successfull.create_text(750,50,text=f" {my_username.get()}",fill='#72E79B',font=('Perpetua Titling MT', 25))
                        # canvas_login_successfull.create_text(1050,50,text=f" to Gaming World",fill='#EA8AE8',font=('Perpetua Titling MT', 25))

                        def challanger():
                            vs = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
                            vs.pack()
                            vs.create_image(0, 0, image=vsimage, anchor='nw')
                            vs.create_text(800, 50, text="Welcome to Tic-Tac-Toe Game", fill="#D2EAE0",
                                           font=('Rye', 40))
                            vs.create_text(400, 200, text="X belong to Player 1.", fill="#D2EAE0", font=('Rye', 30))
                            vs.create_text(1100, 200, text="O belong to Player 2.", fill="#D2EAE0", font=('Rye', 30))
                            vs.create_text(300, 280, text=f"Player 1 Username: {my_username.get()}", fill="#D2EAE0", font=('Rye', 20))
                            vs.create_text(1000, 280, text="Enter Player 2 Username:", fill="#D2EAE0", font=('Rye', 20))
                            player2Username = tk.Entry(self.gamingApplicationWindow, bg='#6E7874', fg="#D2EAE0", width=10,font=('Rye', 20))
                            vs.create_window(1300, 280, window=player2Username)
                            def vsuser2back():
                                vs.pack_forget()
                                canvas_login_successfull.pack()
                            def starttictoe():
                                vs.pack_forget()
                                gameTwo()

                            def verifyuser():
                                mycursor.execute('select username from gaming_application')
                                sql_usernames = mycursor.fetchall()
                                sUsers = []
                                userValidityPlayer = False
                                for l in sql_usernames:
                                    s_user = (''.join(str(e) for e in l))
                                    sUsers.append(s_user)
                                for p in sUsers:
                                    if p == player2Username.get():
                                        userValidityPlayer = True
                                        score.player2name = player2Username.get()
                                        vsstart.config(state=NORMAL)
                                        player2Username.config(state=DISABLED)
                                if player2Username.get() == my_username.get():
                                    player2Username.config(state=NORMAL)
                                    tk.messagebox.showerror("Error", "You Can not play Yourself..")
                                    vsstart.config(state=DISABLED)
                                if not userValidityPlayer:
                                    tk.messagebox.showerror("Error","Username Not Found ..")
                                    vsstart.config(state=DISABLED)



                            vsback = tk.Button(vs, text="Back", font=('Rye', 13),command=vsuser2back)
                            vsstart = tk.Button(vs, text="Start", font=('Rye', 13),command=starttictoe,state=DISABLED)
                            vscheck = tk.Button(vs, text="verify", font=('Rye', 13),command=verifyuser)
                            vsstart.place(x=1000, y=350)
                            vsback.place(x=500, y=350)
                            vscheck.place(x=1400, y=262)


                        def stonePaper():
                            canvas_login_successfull.pack_forget()

                            # -------------------------------------------------------------------------------------------------
                            def gameOne():
                                global w, h, player, computer, result
                                w = 1920  # width
                                h = 800  # height

                                global total, count
                                count = 0
                                total = 0
                                background1 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Minimal.png')
                                rock_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/r1.png')
                                paper_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/p21.png')
                                scissor_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/s12.png')
                                p.rock_paper_score = 0
                                mycursor.execute("""select sps_score from gaming_application where username='%s'""" % my_username.get())
                                a = mycursor.fetchone()
                                aa = (''.join(str(e) for e in a))
                                p.rock_paper_score = int(aa)
                                # print(p.rock_paper_score)

                                screen1 = tk.Canvas(self.gamingApplicationWindow, bg='black', width=w, height=h, bd=0,
                                                    highlightthickness=0)
                                screen1.pack()
                                score_label = tk.Label(screen1, text=f'Total Score: {total}', font=('Rye', 15),
                                                       anchor='nw', fg='#CE6BE0', bg='black')
                                score_label.place(x=1200, y=50)
                                score_label4 = tk.Label(screen1, text=f'{my_username.get()} Highest Score: {p.rock_paper_score}', font=('Rye', 15),
                                                       anchor='nw', fg='#CE6BE0', bg='black')
                                score_label4.place(x=1200, y=150)
                                count_label = tk.Label(screen1, text=f'Total Game Played: {count}', font=('Rye', 10),
                                                       anchor='nw', fg='#CE6BE0', bg='black')
                                count_label.place(x=1200, y=100)

                                msg = tk.Label(screen1, text='Computer is thinking ....', fg='#CE6BE0', bg='black',
                                               anchor='nw', font=('Rye', 10))
                                screen1.create_image(0, 0, image=background1, anchor='nw')
                                screen1.create_text(100, 50, text='Rock Paper Scissor Game', fill='#CE6BE0',
                                                    anchor='nw', font=('Rye', 40))
                                screen1.create_text(200, 150, text=f'Choose Your Options ', fill='#CE6BE0', anchor='nw',font=('Rye', 30))
                                screen1.create_text(650, 150, text=f'{my_username.get()} ', fill='#72E79B', anchor='nw',font=('Rye', 30))
                                screen1.create_text(220, 440, text='How to calculate your score...', fill='#CE6BE0',
                                                    anchor='nw', font=('Rye', 20))
                                screen1.create_text(220, 480, text='1. For Every Win you get +100 score.',
                                                    fill='#CE6BE0', anchor='nw', font=('Rye', 15))
                                screen1.create_text(220, 510, text='2. For Every Loss you get -50 score.',
                                                    fill='#CE6BE0', anchor='nw', font=('Rye', 15))
                                screen1.create_text(220, 540, text='3. For Every Draw you get -10 score.',
                                                    fill='#CE6BE0', anchor='nw', font=('Rye', 15))

                                def WinOrLoose(player, computer, result):
                                    players = player
                                    computers = computer
                                    results = result
                                    msg.place(x=220, y=400)
                                    screen1.update()
                                    time.sleep(1)
                                    screen1.update()
                                    screen1.pack_forget()
                                    screen2 = tk.Canvas(self.gamingApplicationWindow, bg='black', width=w, height=h,
                                                        bd=0, highlightthickness=0)
                                    screen2.pack()
                                    score_label2 = tk.Label(screen2, text=f'Total Score: {constant.score2}',
                                                            font=('Rye', 15), anchor='nw', fg='#CE6BE0', bg='black')
                                    score_label2.place(x=1200, y=50)
                                    score_label3 = tk.Label(screen2, text=f'{my_username.get()} Highest Score: {p.rock_paper_score}',
                                                            font=('Rye', 15), anchor='nw', fg='#CE6BE0', bg='black')
                                    score_label3.place(x=1200, y=100)

                                    bac = tk.Label(screen2, image=background1, bd=0, highlightthickness=0)
                                    screen2.create_image(0, 0, image=background1, anchor='nw')
                                    # bac.place(x=0, y=0)
                                    if results == 'WIN':
                                        total = constant.score + constant.cw
                                        constant.score = total
                                        constant.score2 = constant.score
                                        score_label.config(text=f'Total Score: {total}')
                                        score_label4.config(text=f'{my_username.get()} Highest Score: {p.rock_paper_score}')
                                        screen2.create_text(150, 100, text='Congratulations, You Won the Game !!!',
                                                            fill='#CE6BE0', anchor='nw', font=('Rye', 30))
                                        if total > p.rock_paper_score:
                                            p.rock_paper_score = total
                                            mycursor.execute("""update gaming_application set sps_score =%s ,total_score = (ttt_score + sps_score) where username = '%s'""" %(total,my_username.get()))
                                            mydb.commit()
                                    elif results == 'LOOSE':
                                        total = constant.score - constant.cl
                                        constant.score = total
                                        constant.score2 = constant.score
                                        score_label.config(text=f'Total Score: {total}')
                                        score_label4.config(text=f'{my_username.get()} Highest Score: {p.rock_paper_score}')
                                        screen2.create_text(150, 100,
                                                            text='You LOOSE the Game, Better Luck Next Time !!!',
                                                            fill='#CE6BE0', anchor='nw', font=('Rye', 30))
                                        if total > p.rock_paper_score:
                                            p.rock_paper_score = total
                                            mycursor.execute("""update gaming_application set sps_score =%s ,total_score = (ttt_score + sps_score) where username = '%s'""" %(total,my_username.get()))
                                            mydb.commit()
                                    else:
                                        total = constant.score - constant.cd
                                        constant.score = total
                                        constant.score2 = constant.score
                                        score_label.config(text=f'Total Score: {total}')
                                        score_label4.config(text=f'{my_username.get()} Highest Score: {p.rock_paper_score}')
                                        screen2.create_text(150, 100, text="OOPS!!!  it's is a Draw", fill='#CE6BE0',
                                                            anchor='nw', font=('Rye', 30))
                                        if total > p.rock_paper_score:
                                            p.rock_paper_score = total
                                            mycursor.execute("""update gaming_application set sps_score =%s ,total_score = (ttt_score + sps_score) where username = '%s'""" %(total,my_username.get()))
                                            mydb.commit()

                                    screen2.create_text(180, 180, text="You Choice is: " + players, fill='#CE6BE0',
                                                        anchor='nw', font=('Rye', 15))
                                    if players == 'ROCK':
                                        screen2.create_image(180, 200, image=rock_icon, anchor='nw')
                                    elif players == 'PAPER':
                                        screen2.create_image(180, 200, image=paper_icon, anchor='nw')
                                    else:
                                        screen2.create_image(180, 200, image=scissor_icon, anchor='nw')

                                    screen2.create_text(580, 180, text="Computer Choice is: " + computers,
                                                        fill='#CE6BE0', anchor='nw', font=('Rye', 15))
                                    if computers == 'ROCK':
                                        screen2.create_image(580, 200, image=rock_icon, anchor='nw')
                                    elif computers == 'PAPER':
                                        screen2.create_image(580, 200, image=paper_icon, anchor='nw')
                                    else:
                                        screen2.create_image(580, 200, image=scissor_icon, anchor='nw')

                                    score_label.config(text=f"Total Score: {total}")
                                    score_label4.config(text=f'{my_username.get()} Highest Score: {p.rock_paper_score}')

                                    def reMatch():
                                        score_label.config(text=f"Total Score: {total}")
                                        score_label4.config(text=f'{my_username.get()} Highest Score: {p.rock_paper_score}')
                                        screen2.pack_forget()
                                        msg.place_forget()
                                        screen1.pack()

                                    rematch = tk.Button(screen2, text='Rematch', command=reMatch, fg='#CE6BE0',
                                                        bg='black', font=('Rye', 18))
                                    rematch.place(x=220, y=420)

                                    def exits():
                                        a = tk.messagebox.askyesno("Exit", "You want to Exit the game ?")
                                        if a:
                                            constant.score = 0
                                            constant.count = 0
                                            constant.score2 = 0
                                            screen2.pack_forget()
                                            canvas_login_successfull.pack()

                                            # self.gamingApplicationWindow.quit()

                                    rematch = tk.Button(screen2, text='Close', command=exits, fg='#CE6BE0', bg='black',
                                                        font=('Rye', 18))
                                    rematch.place(x=420, y=420)
                                    score_label2.config(text=f'Total Score: {constant.score2}')
                                    score_label3.config(text=f'{my_username.get()} Highest Score: {p.rock_paper_score}')

                                def chooseRock():
                                    count = constant.count + 1
                                    constant.count = count
                                    count_label.config(text=f'Total Game Played: {count}')
                                    player = 'ROCK'
                                    list_choice = ['ROCK', 'PAPER', 'SCISSOR']
                                    computer = random.choice(list_choice)
                                    if player == 'ROCK' and computer == 'PAPER':
                                        result = 'LOOSE'
                                    elif player == 'ROCK' and computer == 'SCISSOR':
                                        result = 'WIN'
                                    else:
                                        result = 'DRAW'
                                    WinOrLoose(player, computer, result)

                                rock_button = tk.Button(screen1, image=rock_icon, bg='black', highlightthickness=0,
                                                        command=chooseRock)
                                rock_button.place(x=220, y=220)

                                def choosePaper():
                                    count = constant.count + 1
                                    constant.count = count
                                    count_label.config(text=f'Total Game Played: {count}')
                                    player = 'PAPER'
                                    list_choice = ['ROCK', 'PAPER', 'SCISSOR']
                                    computer = random.choice(list_choice)
                                    if player == 'PAPER' and computer == 'SCISSOR':
                                        result = 'LOOSE'
                                    elif player == 'PAPER' and computer == 'ROCK':
                                        result = 'WIN'
                                    else:
                                        result = 'DRAW'
                                    WinOrLoose(player, computer, result)

                                paper_button = tk.Button(screen1, image=paper_icon, bg='black', highlightthickness=0,
                                                         command=choosePaper)
                                paper_button.place(x=420, y=220)
                                rock_button.place(x=220, y=220)

                                def chooseScissor():
                                    count = constant.count + 1
                                    constant.count = count
                                    count_label.config(text=f'Total Game Played: {count}')
                                    player = 'SCISSOR'
                                    list_choice = ['ROCK', 'PAPER', 'SCISSOR']
                                    computer = random.choice(list_choice)
                                    if player == 'SCISSOR' and computer == 'ROCK':
                                        result = 'LOOSE'
                                    elif player == 'SCISSOR' and computer == 'PAPER':
                                        result = 'WIN'
                                    else:
                                        result = 'DRAW'

                                    WinOrLoose(player, computer, result)

                                scissor_button = tk.Button(screen1, image=scissor_icon, bg='black',
                                                           highlightthickness=0, command=chooseScissor)
                                scissor_button.place(x=620, y=220)

                            # -------------------------------------------------------------------------------------------------
                            gameOne()

                        def gameTwo():
                            global w, h, player, computer, result, player1score, player2score, game_count
                            game_count = 0
                            player1score = 0
                            player2score = 0
                            win_score = 100
                            loose_score = 50
                            draw_score = 10
                            w = 1920  # width
                            h = 800  # height
                            screen21 = tk.Canvas(self.gamingApplicationWindow, bg='black', width=w, height=h, bd=0,highlightthickness=0)
                            screen21.pack()
                            mycursor.execute("""select ttt_score from gaming_application where username='%s'""" %my_username.get())
                            a = mycursor.fetchone()
                            aa = (''.join(str(e) for e in a))
                            p.tic_tac_scorep1 = int(aa)
                            mycursor.execute("""select ttt_score from gaming_application where username='%s'""" %score.player2name)
                            b = mycursor.fetchone()
                            aa = (''.join(str(e) for e in b))
                            p.tic_tac_scorep2 = int(aa)
                            screen21.create_image(0, 0, image=background21, anchor='nw')
                            screen21.create_text(350, 20, text="Welcome to Tic Tac Toe Game", font=('Rye', 30),anchor='nw', fill='#6FDAA6')
                            screen21.update()
                            total_score_player1 = tk.Label(screen21, text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}",font=('Rye', 15), anchor='nw', fg='#6FDAA6', bg='black')
                            total_score_player2 = tk.Label(screen21, text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}",font=('Rye', 15), anchor='nw', fg='#6FDAA6', bg='black')
                            total_game_played = tk.Label(screen21, text=f"Total Game Played: {game_count}",font=('Rye', 10), anchor='nw', fg='#6FDAA6', bg='black')
                            total_score_player1.place(x=1000, y=100)
                            total_score_player2.place(x=1000, y=150)
                            total_game_played.place(x=1000, y=200)


                            clicked = True
                            counTing = 0
                            turn_lable = tk.Label(screen21, text=f"The Player 1: {my_username.get()} Turn", font=('Rye', 20), anchor='nw',
                                                  fg='#6FDAA6', bg='black')
                            turn_lable.place(x=405, y=130)

                            def disable_all_buttons():
                                b1.config(state=DISABLED)
                                b2.config(state=DISABLED)
                                b3.config(state=DISABLED)

                                b4.config(state=DISABLED)
                                b5.config(state=DISABLED)
                                b6.config(state=DISABLED)

                                b7.config(state=DISABLED)
                                b8.config(state=DISABLED)
                                b9.config(state=DISABLED)

                            def checkIfWon():
                                global winner
                                winner = False
                                if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
                                    b1.config(bg="green")
                                    b2.config(bg="green")
                                    b3.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe", f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute("""update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" %(player1score,my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute("""update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" %(player2score,score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
                                    b4.config(bg="green")
                                    b5.config(bg="green")
                                    b6.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
                                    b7.config(bg="green")
                                    b8.config(bg="green")
                                    b9.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
                                    b1.config(bg="green")
                                    b4.config(bg="green")
                                    b7.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
                                    b2.config(bg="green")
                                    b5.config(bg="green")
                                    b8.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
                                    b3.config(bg="green")
                                    b6.config(bg="green")
                                    b9.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
                                    b1.config(bg="green")
                                    b5.config(bg="green")
                                    b9.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
                                    b3.config(bg="green")
                                    b5.config(bg="green")
                                    b7.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 1: {my_username.get()} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe", f"congratulation Player 1: {my_username.get()} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + win_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 - loose_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                #         -----------------------------------------------------------------
                                elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
                                    b1.config(bg="green")
                                    b2.config(bg="green")
                                    b3.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute("""update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                            player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
                                    b4.config(bg="green")
                                    b5.config(bg="green")
                                    b6.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
                                    b7.config(bg="green")
                                    b8.config(bg="green")
                                    b9.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
                                    b1.config(bg="green")
                                    b4.config(bg="green")
                                    b7.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
                                    b2.config(bg="green")
                                    b5.config(bg="green")
                                    b8.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
                                    b3.config(bg="green")
                                    b6.config(bg="green")
                                    b9.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
                                    b1.config(bg="green")
                                    b5.config(bg="green")
                                    b9.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
                                    b3.config(bg="green")
                                    b5.config(bg="green")
                                    b7.config(bg="green")
                                    winner = True
                                    turn_lable.config(text=f"congratulation Player 2: {score.player2name} won")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe",
                                                           f"congratulation Player 2: {score.player2name} won")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 - loose_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(
                                        text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + win_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(
                                        text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                                if score.counTings == 9 and winner == False:
                                    # print(counTing)
                                    turn_lable.config(text="It's a Draw")
                                    tk.messagebox.showinfo(" Tic-Tac-Toe", f"It's a Draw between {my_username.get()} and {score.player2name}")
                                    disable_all_buttons()
                                    score.gc = score.gc + 1
                                    game_count = score.gc
                                    total_game_played.config(text=f"Total Game Played: {game_count}")
                                    score.p1 = score.p1 + draw_score
                                    player1score = score.p1
                                    if player1score > p.tic_tac_scorep1:
                                        p.tic_tac_scorep1 = player1score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player1score, my_username.get()))
                                        mydb.commit()
                                    total_score_player1.config(text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                    score.p2 = score.p2 + draw_score
                                    player2score = score.p2
                                    if player2score > p.tic_tac_scorep2:
                                        p.tic_tac_scorep2 = player2score
                                        mycursor.execute(
                                            """update gaming_application set ttt_score =%s , total_score = (ttt_score + sps_score) where username = '%s'""" % (
                                                player2score, score.player2name))
                                        mydb.commit()
                                    total_score_player2.config(text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")

                            def b_click(b):
                                global clicked, counTing

                                if b["text"] == " " and clicked == True:
                                    turn_lable.config(text=f"The Player 2: {score.player2name} Turn")
                                    b["text"] = "X"
                                    clicked = False
                                    counTing += 1
                                    score.counTings = counTing

                                    # print(counTing)
                                    checkIfWon()
                                elif b["text"] == " " and clicked == False:
                                    turn_lable.config(text=f"The Player 1: {my_username.get()} Turn")
                                    b["text"] = "O"
                                    clicked = True
                                    counTing += 1
                                    score.counTings = counTing
                                    # print(counTing)
                                    checkIfWon()
                                else:
                                    tk.messagebox.showerror(" Tic Tac Toe",
                                                            "hey ! the box is already selected \nPick another box")

                            def rematch():
                                turn_lable.config(text=f"The Player 1: {my_username.get()} Turn")
                                global b1, b2, b3, b4, b5, b6, b7, b8, b9
                                global clicked, counTing
                                clicked = True
                                counTing = 0
                                score.counTings = counTing
                                b1 = tk.Button(screen21, text=" ", font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b1))
                                b2 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b2))
                                b3 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b3))

                                b4 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b4))
                                b5 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b5))
                                b6 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b6))

                                b7 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b7))
                                b8 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b8))
                                b9 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b9))

                                b1.place(x=500, y=200)
                                b2.place(x=590, y=200)
                                b3.place(x=680, y=200)

                                b4.place(x=500, y=296)
                                b5.place(x=590, y=296)
                                b6.place(x=680, y=296)

                                b7.place(x=500, y=392)
                                b8.place(x=590, y=392)
                                b9.place(x=680, y=392)

                            def reset1():
                                score.p1 = 0
                                score.p2 = 0
                                score.gc = 0
                                player1score = 0
                                player2score = 0
                                game_count = 0
                                total_score_player2.config(text=f"Player 2: {score.player2name} Score: {player2score} Highest Score: {p.tic_tac_scorep2}")
                                total_score_player1.config(text=f"Player 1: {my_username.get()} Score: {player1score} Highest Score: {p.tic_tac_scorep1}")
                                total_game_played.config(text=f"Total Game Played: {game_count}")
                                turn_lable.config(text=f"The Player 1: {my_username.get()} Turn")
                                global b1, b2, b3, b4, b5, b6, b7, b8, b9
                                global clicked, counTing
                                clicked = True
                                counTing = 0
                                b1 = tk.Button(screen21, text=" ", font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b1))
                                b2 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b2))
                                b3 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b3))

                                b4 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b4))
                                b5 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b5))
                                b6 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b6))

                                b7 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b7))
                                b8 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b8))
                                b9 = tk.Button(screen21, text=' ', font=('Rye', 15), heigh=3, width=6, bg='#99B7B3',
                                               command=lambda: b_click(b9))

                                b1.place(x=500, y=200)
                                b2.place(x=590, y=200)
                                b3.place(x=680, y=200)

                                b4.place(x=500, y=296)
                                b5.place(x=590, y=296)
                                b6.place(x=680, y=296)

                                b7.place(x=500, y=392)
                                b8.place(x=590, y=392)
                                b9.place(x=680, y=392)

                            def close():
                                ans = tk.messagebox.askyesno("Tic-Tac-Toe","Do you Want to Exit the Game")
                                if ans:
                                    score.p1 = 0
                                    score.p2 = 0
                                    score.gc = 0
                                    score.counTings = 0
                                    screen21.pack_forget()
                                    canvas_login_successfull.pack()

                            reset = tk.Button(screen21, text='Reset', font=('Rye', 15), bg='#99B7B3', command=reset1)
                            rematch = tk.Button(screen21, text='Rematch', font=('Rye', 15), bg='#99B7B3',
                                                command=rematch)
                            close = tk.Button(screen21, text='Close', font=('Rye', 15), bg='#99B7B3', command=close)

                            reset.place(x=500, y=520)
                            rematch.place(x=600, y=520)
                            close.place(x=750, y=520)
                            reset1()



                        def gameTicTac():
                            canvas_login_successfull.pack_forget()
                            challanger()



                        rops = tk.Button(canvas_login_successfull,image=image10,command=stonePaper)
                        rops.place(x=200,y=180)
                        canvas_login_successfull.create_text(260,340,text="  Rock Paper \n   Scissor",fill='#EA8AE8',font=('Perpetua Titling MT', 15))
                        ttt = tk.Button(canvas_login_successfull, image=image11,command=gameTicTac)
                        ttt.place(x=500, y=180)
                        canvas_login_successfull.create_text(560, 330, text="Tic-tac-toe", fill='#EA8AE8', font=('Perpetua Titling MT', 15))
                        def leadershipstonepaper():
                            rps_leaderbord = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1600, height=800, bd=0,
                                                       highlightthickness=0)
                            rps_leaderbord.pack()
                            rps_leaderbord.create_image(0, 0, image=rpsleaderbord, anchor='nw')
                            rps_leaderbord.create_text(50, 50, text="Welcome to Stone-Paper-Scissor  Leadership Bord",
                                                       anchor=W, fill='#BBD9E2', font=('Rye', 30))
                            rps_leaderbord.create_text(150, 120, text="\U0001F449 Top 10 Highest Scoring Player",
                                                       anchor=W, fill='#BFE182', font=('Rye', 20))
                            rps_leaderbord.create_text(50, 180, text="Rank", anchor=W, fill='#BBD9E2', font=('Rye', 20))
                            rps_leaderbord.create_text(250, 180, text="Username", anchor=W, fill='#BBD9E2',
                                                       font=('Rye', 20))
                            rps_leaderbord.create_text(500, 180, text="Name", anchor=W, fill='#BBD9E2',
                                                       font=('Rye', 20))
                            rps_leaderbord.create_text(750, 180, text="Stone-Paper-Scissor Score", anchor=W,
                                                       fill='#BBD9E2', font=('Rye', 20))
                            mycursor.execute("select count(*) from gaming_application")
                            countuser = mycursor.fetchone()
                            z = (''.join(str(e) for e in countuser))
                            noofUser = int(z)
                            p.username = []
                            p.name = []
                            p.rpsscore = []
                            mycursor.execute(
                                "select username,name,sps_score from gaming_application order by sps_score DESC")
                            listuser = mycursor.fetchall()
                            for u, n, ts in listuser:
                                p.username.append(u)
                                p.name.append(n)
                                p.rpsscore.append(ts)
                            x = 1
                            if noofUser >= 10:
                                a = 240
                                while x <= 10:
                                    rps_leaderbord.create_text(50, a, text=f"{x}", anchor=W, fill='#BBD9E2',
                                                               font=('Rye', 20))
                                    rps_leaderbord.create_text(250, a, text=f"{p.username[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    rps_leaderbord.create_text(500, a, text=f"{p.name[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    rps_leaderbord.create_text(750, a, text=f"{p.rpsscore[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    a += 50
                                    x += 1
                            else:
                                a = 240
                                while x <= noofUser:
                                    rps_leaderbord.create_text(50, a, text=f"{x}", anchor=W, fill='#BBD9E2',
                                                               font=('Rye', 20))
                                    rps_leaderbord.create_text(250, a, text=f"{p.username[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    rps_leaderbord.create_text(500, a, text=f"{p.name[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    rps_leaderbord.create_text(750, a, text=f"{p.tttscore[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    a += 50
                                    x += 1

                            def backtousers():
                                rps_leaderbord.pack_forget()
                                canvas_login_successfull.pack()

                            backtouser = tk.Button(rps_leaderbord, text="Back", anchor=W, fg='#AE6DB1', bg="black",
                                                   font=('Rye', 15), command=backtousers)
                            backtouser.place(x=800, y=100)

                        def leadershipstone():
                            canvas_login_successfull.pack_forget()
                            leadershipstonepaper()
                        ledrrps = tk.Button(canvas_login_successfull, image=image13,command=leadershipstone)
                        ledrrps.place(x=800, y=180)
                        canvas_login_successfull.create_text(870, 340, text="Rock Paper Scissor\n Leadership Board", fill='#EA8AE8', font=('Perpetua Titling MT', 15))
                        def leadershipTicToe():
                            tic_leaderbord = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1600, height=800, bd=0,
                                                       highlightthickness=0)
                            tic_leaderbord.pack()
                            tic_leaderbord.create_image(0, 0, image=tleaderbord, anchor='nw')
                            tic_leaderbord.create_text(50, 50, text="Welcome to Tic-Tac-Toc Game Leadership Bord",
                                                       anchor=W, fill='#BBD9E2', font=('Rye', 40))
                            tic_leaderbord.create_text(150, 120, text="\U0001F449 Top 10 Highest Scoring Player",
                                                       anchor=W, fill='#BFE182', font=('Rye', 20))
                            tic_leaderbord.create_text(50, 180, text="Rank", anchor=W, fill='#BBD9E2', font=('Rye', 20))
                            tic_leaderbord.create_text(250, 180, text="Username", anchor=W, fill='#BBD9E2',
                                                       font=('Rye', 20))
                            tic_leaderbord.create_text(500, 180, text="Name", anchor=W, fill='#BBD9E2',
                                                       font=('Rye', 20))
                            tic_leaderbord.create_text(750, 180, text="Tic-Tac-Toe Score", anchor=W, fill='#BBD9E2',
                                                       font=('Rye', 20))
                            mycursor.execute("select count(*) from gaming_application")
                            countuser = mycursor.fetchone()
                            z = (''.join(str(e) for e in countuser))
                            noofUser = int(z)
                            p.username = []
                            p.name = []
                            p.tttscore = []
                            mycursor.execute(
                                "select username,name,ttt_score from gaming_application order by ttt_score DESC")
                            listuser = mycursor.fetchall()
                            for u, n, ts in listuser:
                                p.username.append(u)
                                p.name.append(n)
                                p.tttscore.append(ts)
                            x = 1
                            if noofUser >= 10:
                                a = 240
                                while x <= 10:
                                    tic_leaderbord.create_text(50, a, text=f"{x}", anchor=W, fill='#BBD9E2',
                                                               font=('Rye', 20))
                                    tic_leaderbord.create_text(250, a, text=f"{p.username[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    tic_leaderbord.create_text(500, a, text=f"{p.name[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    tic_leaderbord.create_text(750, a, text=f"{p.tttscore[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    a += 50
                                    x += 1
                            else:
                                a = 240
                                while x <= noofUser:
                                    tic_leaderbord.create_text(50, a, text=f"{x}", anchor=W, fill='#BBD9E2',
                                                               font=('Rye', 20))
                                    tic_leaderbord.create_text(250, a, text=f"{p.username[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    tic_leaderbord.create_text(500, a, text=f"{p.name[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    tic_leaderbord.create_text(750, a, text=f"{p.tttscore[x - 1]}", anchor=W,
                                                               fill='#BBD9E2', font=('Rye', 20))
                                    a += 50
                                    x += 1

                            def backtousers():
                                tic_leaderbord.pack_forget()
                                canvas_login_successfull.pack()

                            backtouser = tk.Button(tic_leaderbord, text="Back", anchor=W, fg='#AE6DB1', bg="black",
                                                   font=('Rye', 15), command=backtousers)
                            backtouser.place(x=800, y=100)


                        def leadershipTic():
                            canvas_login_successfull.pack_forget()
                            leadershipTicToe()
                        ledrttt = tk.Button(canvas_login_successfull, image=image12,command=leadershipTic)
                        ledrttt.place(x=1100, y=180)
                        canvas_login_successfull.create_text(1190, 340, text=" Tic-tac-toe\nLeadership Board", fill='#EA8AE8', font=('Perpetua Titling MT', 15))
                        mycursor.execute("""select gender from user_registration where UserName = '%s'"""%my_username.get())
                        gen1 = mycursor.fetchall()
                        def profiles():
                            canvas_login_successfull.pack_forget()
                            userProfile = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1920, height=800, bd=0, highlightthickness=0)
                            userProfile.pack()
                            # -----------------------------
                            try:
                                mycursor.execute("""select * from gaming_application where username = '%s'"""%my_username.get())
                                users1 = mycursor.fetchall()
                                for Uname, Paswrd, Fname, ticscore, spscore, tscore in users1:
                                    # U = (''.join(str(e) for e in l))
                                    starpass = []
                                    for i in range(len(Paswrd)):
                                        if i < len(Paswrd) - 2:
                                            starpass += '*'
                                        else:
                                            starpass += Paswrd[i]
                                        starpass = (''.join(str(e) for e in starpass))
                                        p.username = Uname
                                        p.password = starpass
                                        p.firstname = Fname
                                        p.tic_tac_score = ticscore
                                        p.rock_paper_score = spscore
                                        p.total_score = tscore

                                mycursor.execute("""select * from user_registration where UserName = '%s'""" %my_username.get())
                                users1 = mycursor.fetchall()
                                for Uname, Fname, Lname, Gendr, dob, Eml in users1:
                                    p.lastname = Lname
                                    p.gender = Gendr
                                    p.dob = dob
                                    p.email = Eml
                            except Exception:
                                print("Error")
                            # -------------------------------

                            userProfile.create_image(0, 0, image=vsprofile, anchor='nw')
                            userProfile.create_text(600, 50, text="Welcome to Gaming World", fill="#CEEF84",font=('Rye', 40))

                            userProfile.create_rectangle(100, 200, 1150, 600, outline='red')
                            userProfile.create_text(110, 180, text=f"Profile of Username: {p.username} ", anchor=W, fill="#E9BE7E", font=('Rye', 20))
                            userProfile.create_text(130, 230, text=f"NAME: {p.firstname} {p.lastname}", anchor=W, fill="#E9BE7E",font=('Rye', 20))
                            userProfile.create_text(130, 290, text=f"FIRST NAME: {p.firstname}\t LAST NAME: {p.lastname}", anchor=W,fill="#E9BE7E", font=('Rye', 20))
                            userProfile.create_text(130, 350, text=f"GENDER: {p.gender}\t\t DOB: {p.dob}", anchor=W, fill="#E9BE7E",font=('Rye', 20))
                            userProfile.create_text(130, 410, text=f"EMAIL: {p.email}", anchor=W, fill="#E9BE7E",font=('Rye', 20))
                            userProfile.create_text(130, 470, text=f"USERNAME: {p.username}\t\t PASSWORD: {p.password}", anchor=W,fill="#E9BE7E", font=('Rye', 20))
                            userProfile.create_text(130, 540, text=f"TOTAL SCORE: {p.total_score}", anchor=W, fill="#E9BE7E",font=('Rye', 20))
                            def profileToLogins():
                                userProfile.pack_forget()
                                canvas_login_successfull.pack()

                            profileToLogin = tk.Button(userProfile,text="Back", font=('Rye', 20), anchor=W, bg="Black", fg='white',command=profileToLogins)
                            profileToLogin.place(x=100, y=620)


                        for l in gen1:
                            gen = (''.join(str(e) for e in l))
                        if gen == "Male":
                            profile = tk.Button(canvas_login_successfull, image=image14,command=profiles)
                            profile.place(x=350, y=400)
                        elif gen == "Female":
                            profile = tk.Button(canvas_login_successfull, image=image15,command=profiles)
                            profile.place(x=350, y=400)
                        else:
                            profile = tk.Button(canvas_login_successfull, image=image16,command=profiles)
                            profile.place(x=350, y=400)
                        canvas_login_successfull.create_text(410, 560, text=f"{my_username.get()}\nProfile", fill='#EA8AE8',font=('Perpetua Titling MT', 15))
                        if my_username.get() == "admin":
                            def deleteUserDetais():
                                adminDelete = tk.Canvas(self.gamingApplicationWindow, bg='black', width=1600, height=800, bd=0,
                                                        highlightthickness=0)
                                adminDelete.pack()
                                adminDelete.create_image(0, 0, image=userdelete, anchor='nw')
                                adminDelete.create_text(200, 50, text="Delete User In Gaming World", anchor=W,
                                                        fill='#4CF1EA', font=('Rye', 40))
                                adminDelete.create_text(200, 150, text="Enter Username: ", anchor=W, fill='#4CF1EA',
                                                        font=('Rye', 20))
                                adminDelete.create_text(110, 215, text="Enter Admin Password: ", anchor=W,
                                                        fill='#4CF1EA', font=('Rye', 20))
                                e_user = tk.Entry(adminDelete, fg='#DE64EC', font=('Rye', 15))
                                e_user.place(x=450, y=140)
                                a_pass = tk.Entry(adminDelete, fg='#DE64EC', font=('Rye', 15), state=DISABLED)
                                a_pass.config(show="*")
                                a_pass.place(x=450, y=200)

                                def vusername():
                                    mycursor.execute(
                                        """select username from gaming_application where username = '%s'""" % e_user.get())
                                    unAme = mycursor.fetchall()
                                    fnd = False
                                    for name in unAme:
                                        u = (''.join(str(e) for e in name))
                                        if u != 'admin':
                                            if u == e_user.get():
                                                fnd = True
                                                e_user.config(state=DISABLED)
                                                a_pass.config(state=NORMAL)
                                    if not fnd:
                                        tk.messagebox.showerror('Delete Users', 'Username Not Found')

                                def apassword():
                                    mycursor.execute(
                                        """select passwords from gaming_application where username = 'admin'""")
                                    apassw = mycursor.fetchall()
                                    fnd = False
                                    for apass in apassw:
                                        u = (''.join(str(e) for e in apass))
                                        if u == a_pass.get():
                                            fnd = True
                                            a_pass.config(state=DISABLED)
                                            Dusers.config(state=NORMAL)
                                    if not fnd:
                                        tk.messagebox.showerror('Delete Users', 'Password does not match')

                                def deleteuser():
                                    try:
                                        mycursor.execute(
                                            """delete from gaming_application where username='%s'""" % e_user.get())
                                        mydb.commit()
                                        mycursor.execute(
                                            """delete from user_registration where UserName='%s';""" % e_user.get())
                                        mydb.commit()
                                        print("delete")
                                        tk.messagebox.showinfo("Delete User", "User Delete Successfully")
                                    except Exception:
                                        print("error")

                                def backToAdmin():
                                    e_user.config(state=NORMAL)
                                    adminDelete.pack_forget()
                                    canvas_login_successfull.pack()

                                verify = tk.Button(adminDelete, text="Verify", anchor=W, font=('Rye', 11),
                                                   command=vusername)
                                verify.place(x=740, y=140)
                                aPass = tk.Button(adminDelete, text="Verify", anchor=W, font=('Rye', 11),
                                                  command=apassword)
                                aPass.place(x=740, y=200)
                                Dusers = tk.Button(adminDelete, text="Delete User", anchor=W, font=('Rye', 15),
                                                   state=DISABLED, command=deleteuser)
                                Dusers.place(x=500, y=260)
                                back = tk.Button(adminDelete, text="Back", anchor=W, font=('Rye', 15),command=backToAdmin)
                                back.place(x=400, y=260)

                            def detilsUserDelete():
                                canvas_login_successfull.pack_forget()
                                deleteUserDetais()

                            duser = tk.Button(canvas_login_successfull, image=image17,command=detilsUserDelete)
                            duser.place(x=650, y=400)

                            def listsUsers():
                                canvas_login_successfull.update()
                                p.x=1
                                p.y = 11
                                main_frame = tk.Frame(self.gamingApplicationWindow, bg="black")
                                main_frame.pack(fill=BOTH, expand=1)
                                adminUserList = tk.Canvas(main_frame, bg='black', width=1600, height=1000, bd=0,
                                                          highlightthickness=0)
                                adminUserList.pack()
                                mydb = mysql.connector.connect(host=Mysql.h, user=Mysql.u, password=Mysql.pas,
                                                               port=Mysql.po, database=Mysql.dat)
                                mycursor = mydb.cursor()
                                mycursor.execute("select count(*) from gaming_application")
                                users1 = mycursor.fetchone()
                                u = (''.join(str(e) for e in users1))
                                countusers = int(u)
                                print(countusers)
                                text2 = tk.Label(main_frame, text="\t\t\t\t\t\t\t\t\t\t\t\t\t", anchor=W, bg='black',
                                                 fg="#CEEF84", font=('Rye', 80))
                                text2.place(x=0, y=0)
                                text = tk.Label(main_frame, text="List of Users in Gaming World", anchor=W, bg='black',
                                                fg="#CEEF84", font=('Rye', 40))
                                text.place(x=100, y=10)
                                global x, y, a, b, z
                                a = 160
                                b = 220
                                mycursor.execute(
                                    "select username,name,total_score from gaming_application order by username asc")
                                users1 = mycursor.fetchall()
                                p.uname =[]
                                p.fname=[]
                                p.Tscore=[]
                                for Uname, Fname, Tscore in users1:
                                    p.uname.append(Uname)
                                    p.fname.append(Fname)
                                    p.Tscore.append(Tscore)
                                text2 = tk.Label(main_frame, text=f"Username", anchor=W, bg='black', fg='#4CF1EA',
                                                 font=('Rye', 20))
                                text3 = tk.Label(main_frame, text=f"Name", anchor=W, bg='black', fg='#A3F15D',
                                                 font=('Rye', 20))
                                text4 = tk.Label(main_frame, text=f"Total Score", anchor=W, bg='black', fg='#DE64EC',
                                                 font=('Rye', 20))
                                text2.place(x=100, y=100)
                                text3.place(x=410, y=100)
                                text4.place(x=710, y=100)
                                while p.x <= countusers:
                                    adminUserList.create_rectangle(100, a, 1150, b, outline='red')
                                    adminUserList.create_text(55, a + 27, text=f'{p.x}.', anchor=W, fill='#4CF1EA',
                                                              font=('Rye', 20))
                                    adminUserList.create_text(110, a + 27, text=f"{p.uname[p.x - 1]}", anchor=W,
                                                              fill='#4CF1EA', font=('Rye', 20), tags="e")
                                    adminUserList.create_text(410, a + 27, text=f"{p.fname[p.x - 1].upper()}", anchor=W,
                                                              fill='#A3F15D', font=('Rye', 20), tags="e")
                                    adminUserList.create_text(760, a + 27, text=f"{p.Tscore[p.x - 1]}", anchor=W,
                                                              fill='#DE64EC', font=('Rye', 20), tags="e")
                                    a = b + 10
                                    b = a + 50
                                    p.x += 1
                                myScroll = tk.Scrollbar(main_frame, orient=VERTICAL, command=adminUserList.yview,
                                                        width=30, highlightbackground='green')
                                myScroll.place(x=1500, y=300)
                                adminUserList.configure(yscrollcommand=myScroll.set)
                                adminUserList.bind('<Configure>', lambda e: adminUserList.configure(
                                    scrollregion=adminUserList.bbox("all")))
                                second_frame = tk.Frame(adminUserList)
                                adminUserList.create_window((0, 0), window=second_frame, anchor="nw")
                                def backtoMenus():
                                    main_frame.forget()
                                    canvas_login_successfull.pack()

                                backtoMenu = tk.Button(main_frame,text="Back",fg='#D37FA6',bg='black',anchor=W,font=('Rye', 15),command=backtoMenus)
                                backtoMenu.place(x=1200, y=50)

                            def adminuserlists():
                                canvas_login_successfull.pack_forget()
                                listsUsers()

                            canvas_login_successfull.create_text(710, 560, text="Delete Users\nAccount", fill='#EA8AE8',font=('Perpetua Titling MT', 15))
                            listuser = tk.Button(canvas_login_successfull, image=image19,command=adminuserlists)
                            listuser.place(x=1250, y=400)
                            canvas_login_successfull.create_text(1310, 560, text="list of  Users\nAccount", fill='#EA8AE8',font=('Perpetua Titling MT', 15))
                        def backtologin():
                            my_username.delete(0,END)
                            my_password.delete(0,END)
                            my_password.config(show="")
                            my_username.insert(0, 'username')
                            my_password.insert(0, 'password')
                            canvas_login_successfull.pack_forget()
                            canvas_2_Login_Page.pack()
                        exitlogout = tk.Button(canvas_login_successfull, image=image18,command=backtologin)
                        exitlogout.place(x=950, y=400)
                        canvas_login_successfull.create_text(1010, 540, text="Log out", fill='#EA8AE8',font=('Perpetua Titling MT', 15))



                if sucess:
                    sucess=False
                    print(sucess)
                else:
                    tk.messagebox.showwarning('Warning', 'Incorrect Username or Password')
            #     -----------------------------------------------------------------------


            login_btn = tk.Button(canvas_2_Login_Page, text='Log in', font=('Rubik Distressed', 15), width=10, command=login_success)
            login_btn_window = canvas_2_Login_Page.create_window(480, 340, anchor='nw', window=login_btn)

            def entry_clear(e):
                canvas_2_Login_Page.update()
                if my_username.get() == 'username' or my_password.get() == 'password':
                    my_username.delete(0,END)
                    my_password.delete(0,END)
                    my_password.config(show='*')
                    canvas_2_Login_Page.update()

            my_username.bind("<Button-1>",entry_clear)
            my_password.bind("<Button-1>", entry_clear)

            print('end')

        btn = tk.Button(canvasScreen_1, image=image2, bg='#b86b23', command=onClick)
        btn.place(x=730, y=510)
        self.gamingApplicationWindow.mainloop()

# class ends and intentness of class start
c = Canvas_Frame()
