import time
from random import random
from tkinter import LEFT, CENTER, END, messagebox, NORMAL, DISABLED
import tkinter as tk
import random
import constant


# def gameOne():
#     global w,h, player,computer, result
#     w=1920  # width
#     h=800   # height
#
#     global total,count
#     count = 0
#     total = 0
#
#     game_window = tk.Tk()
#     game_window.state('zoomed')
#     game_window.geometry('1920x800')
#     game_window.title('Stone Paper Scissor')
#     background1 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Minimal.png')
#     rock_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/r1.png')
#     paper_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/p21.png')
#     scissor_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/s12.png')
#     screen1 = tk.Canvas(game_window,bg='black',width=w, height=h,bd=0,highlightthickness=0)
#     screen1.pack()
#     score_label = tk.Label(screen1,text=f'Total Score: {total}' ,font=('Rye', 15),anchor='nw',fg='#CE6BE0',bg='black')
#     score_label.place(x=1200,y=50)
#     count_label = tk.Label(screen1,text=f'Total Game Played: {count}' ,font=('Rye', 10),anchor='nw',fg='#CE6BE0',bg='black')
#     count_label.place(x=1200,y=100)
#
#     msg = tk.Label(screen1, text='Computer is thinking ....',fg='#CE6BE0',bg='black',anchor='nw', font=('Rye', 10))
#     screen1.create_image(0, 0, image=background1, anchor='nw')
#     screen1.create_text(100,50,text='Rock Paper Scissor Game', fill='#CE6BE0',anchor='nw', font=('Rye', 40))
#     screen1.create_text(200,150,text='Choose Your Options', fill='#CE6BE0',anchor='nw', font=('Rye', 30))
#     screen1.create_text(220,440,text='How to calculate your score...', fill='#CE6BE0',anchor='nw', font=('Rye', 20))
#     screen1.create_text(220,480,text='1. For Every Win you get +100 score.', fill='#CE6BE0',anchor='nw', font=('Rye', 15))
#     screen1.create_text(220,510,text='2. For Every Loss you get -50 score.', fill='#CE6BE0',anchor='nw', font=('Rye', 15))
#     screen1.create_text(220,540,text='3. For Every Draw you get -10 score.', fill='#CE6BE0',anchor='nw', font=('Rye', 15))
#
#
#
#
#
#     def WinOrLoose(player, computer, result):
#         players = player
#         computers = computer
#         results = result
#         msg.place(x=220,y=400)
#         screen1.update()
#         time.sleep(1)
#         screen1.update()
#         screen1.pack_forget()
#         screen2 = tk.Canvas(game_window, bg='black', width=w, height=h, bd=0, highlightthickness=0)
#         screen2.pack()
#         score_label2 = tk.Label(screen2, text=f'Total Score: {constant.score2}', font=('Rye', 15), anchor='nw', fg='#CE6BE0',bg='black')
#         score_label2.place(x=1200, y=50)
#         bac = tk.Label(screen2,image=background1,bd=0, highlightthickness=0)
#         screen2.create_image(0,0,image = background1 ,anchor='nw')
#         # bac.place(x=0, y=0)
#         if results == 'WIN' :
#             total =constant.score + constant.cw
#             constant.score = total
#             constant.score2 = constant.score
#             score_label.config(text=f'Total Score: {total}')
#             screen2.create_text(150,100, text='Congratulations, You Won the Game !!!',fill='#CE6BE0',anchor='nw', font=('Rye', 30))
#         elif results == 'LOOSE' :
#             total = constant.score - constant.cl
#             constant.score = total
#             constant.score2 = constant.score
#             score_label.config(text=f'Total Score: {total}')
#             screen2.create_text(150, 100, text='You LOOSE the Game, Better Luck Next Time !!!',fill='#CE6BE0',anchor='nw', font=('Rye', 30))
#         else:
#             total = constant.score - constant.cd
#             constant.score = total
#             constant.score2 = constant.score
#             score_label.config(text=f'Total Score: {total}')
#             screen2.create_text(150, 100, text="OOPS!!!  it's is a Draw",fill='#CE6BE0',anchor='nw', font=('Rye', 30))
#
#         screen2.create_text(180, 180, text= "You Choice is: "+ players, fill='#CE6BE0',anchor='nw', font=('Rye', 15))
#         if players == 'ROCK':
#             screen2.create_image(180,200, image = rock_icon,anchor='nw')
#         elif players == 'PAPER':
#             screen2.create_image(180, 200, image=paper_icon, anchor='nw')
#         else:
#             screen2.create_image(180, 200, image=scissor_icon, anchor='nw')
#
#         screen2.create_text(580, 180, text= "Computer Choice is: "+ computers, fill='#CE6BE0',anchor='nw', font=('Rye', 15))
#         if computers == 'ROCK':
#             screen2.create_image(580,200, image = rock_icon,anchor='nw')
#         elif computers == 'PAPER':
#             screen2.create_image(580, 200, image=paper_icon, anchor='nw')
#         else:
#             screen2.create_image(580, 200, image=scissor_icon, anchor='nw')
#
#         score_label.config(text=f"Total Score: {total}")
#
#         def reMatch():
#             score_label.config(text=f"Total Score: {total}")
#             screen2.pack_forget()
#             msg.place_forget()
#             screen1.pack()
#
#         rematch = tk.Button(screen2,text='Rematch',command=reMatch,fg='#CE6BE0' ,bg='black',font=('Rye', 18))
#         rematch.place(x=220, y=420)
#         def exits():
#             a = tk.messagebox.askyesno("Exit","You want to Exit the game ?")
#             if a:
#                 game_window.quit()
#
#         rematch = tk.Button(screen2,text='Close',command=exits,fg='#CE6BE0' ,bg='black',font=('Rye', 18))
#         rematch.place(x=420, y=420)
#         score_label2.config(text=f'Total Score: {constant.score2}')
#
#     def chooseRock():
#         count = constant.count + 1
#         constant.count = count
#         count_label.config(text=f'Total Game Played: {count}')
#         player = 'ROCK'
#         list_choice = ['ROCK','PAPER','SCISSOR']
#         computer = random.choice(list_choice)
#         if player == 'ROCK' and computer == 'PAPER':
#             result = 'LOOSE'
#         elif player == 'ROCK' and computer == 'SCISSOR':
#             result = 'WIN'
#         else:
#             result = 'DRAW'
#         WinOrLoose(player, computer ,result)
#
#     rock_button = tk.Button(screen1,image=rock_icon, bg ='black',highlightthickness=0,command=chooseRock)
#     rock_button.place(x=220, y=220)
#     def choosePaper():
#         count = constant.count + 1
#         constant.count = count
#         count_label.config(text=f'Total Game Played: {count}')
#         player = 'PAPER'
#         list_choice = ['ROCK','PAPER','SCISSOR']
#         computer = random.choice(list_choice)
#         if player == 'PAPER' and computer == 'SCISSOR' :
#             result = 'LOOSE'
#         elif player == 'PAPER' and computer == 'ROCK':
#             result = 'WIN'
#         else:
#             result = 'DRAW'
#         WinOrLoose(player, computer ,result)
#
#
#
#     paper_button = tk.Button(screen1,image=paper_icon, bg ='black',highlightthickness=0,command=choosePaper)
#     paper_button.place(x=420, y=220)
#     rock_button.place(x=220, y=220)
#     def chooseScissor():
#         count = constant.count + 1
#         constant.count = count
#         count_label.config(text=f'Total Game Played: {count}')
#         player = 'SCISSOR'
#         list_choice = ['ROCK','PAPER','SCISSOR']
#         computer = random.choice(list_choice)
#         if player == 'SCISSOR' and computer == 'ROCK' :
#             result = 'LOOSE'
#         elif player == 'SCISSOR' and computer == 'PAPER':
#             result = 'WIN'
#         else:
#             result = 'DRAW'
#
#         WinOrLoose(player, computer ,result)
#
#
#     scissor_button = tk.Button(screen1,image=scissor_icon, bg ='black',highlightthickness=0, command=chooseScissor)
#     scissor_button.place(x=620, y=220)
#     game_window.mainloop()
def gameOne():
    global w, h, player, computer, result
    w = 1920  # width
    h = 800  # height

    global total, count
    count = 0
    total = 0

    game_window = tk.Tk()
    game_window.state('zoomed')
    game_window.geometry('1920x800')
    game_window.title('Stone Paper Scissor')
    background1 = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/Minimal.png')
    rock_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/r1.png')
    paper_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/p21.png')
    scissor_icon = tk.PhotoImage(file='C:/Users/skrsg/PycharmProjects/Gaming Applications/PNG/s12.png')

    screen1 = tk.Canvas(game_window, bg='black', width=w, height=h, bd=0, highlightthickness=0)
    screen1.pack()
    score_label = tk.Label(screen1, text=f'Total Score: {total}', font=('Rye', 15), anchor='nw', fg='#CE6BE0',
                           bg='black')
    score_label.place(x=1200, y=50)
    count_label = tk.Label(screen1, text=f'Total Game Played: {count}', font=('Rye', 10), anchor='nw', fg='#CE6BE0',
                           bg='black')
    count_label.place(x=1200, y=100)

    msg = tk.Label(screen1, text='Computer is thinking ....', fg='#CE6BE0', bg='black', anchor='nw', font=('Rye', 10))
    screen1.create_image(0, 0, image=background1, anchor='nw')
    # msg1 = tk.Label(screen1, image=background1)
    # msg1.place(x=0,y=0)
    screen1.create_text(100, 50, text='Rock Paper Scissor Game', fill='#CE6BE0', anchor='nw', font=('Rye', 40))
    screen1.create_text(200, 150, text='Choose Your Options', fill='#CE6BE0', anchor='nw', font=('Rye', 30))
    screen1.create_text(220, 440, text='How to calculate your score...', fill='#CE6BE0', anchor='nw', font=('Rye', 20))
    screen1.create_text(220, 480, text='1. For Every Win you get +100 score.', fill='#CE6BE0', anchor='nw',
                        font=('Rye', 15))
    screen1.create_text(220, 510, text='2. For Every Loss you get -50 score.', fill='#CE6BE0', anchor='nw',
                        font=('Rye', 15))
    screen1.create_text(220, 540, text='3. For Every Draw you get -10 score.', fill='#CE6BE0', anchor='nw',
                        font=('Rye', 15))

    def WinOrLoose(player, computer, result):
        players = player
        computers = computer
        results = result
        msg.place(x=220, y=400)
        screen1.update()
        time.sleep(1)
        screen1.update()
        screen1.pack_forget()
        screen2 = tk.Canvas(game_window, bg='black', width=w, height=h, bd=0, highlightthickness=0)
        screen2.pack()
        score_label2 = tk.Label(screen2, text=f'Total Score: {constant.score2}', font=('Rye', 15), anchor='nw',
                                fg='#CE6BE0', bg='black')
        score_label2.place(x=1200, y=50)
        bac = tk.Label(screen2, image=background1, bd=0, highlightthickness=0)
        screen2.create_image(0, 0, image=background1, anchor='nw')
        # bac.place(x=0, y=0)
        if results == 'WIN':
            total = constant.score + constant.cw
            constant.score = total
            constant.score2 = constant.score
            score_label.config(text=f'Total Score: {total}')
            screen2.create_text(150, 100, text='Congratulations, You Won the Game !!!', fill='#CE6BE0', anchor='nw',
                                font=('Rye', 30))
        elif results == 'LOOSE':
            total = constant.score - constant.cl
            constant.score = total
            constant.score2 = constant.score
            score_label.config(text=f'Total Score: {total}')
            screen2.create_text(150, 100, text='You LOOSE the Game, Better Luck Next Time !!!', fill='#CE6BE0',
                                anchor='nw', font=('Rye', 30))
        else:
            total = constant.score - constant.cd
            constant.score = total
            constant.score2 = constant.score
            score_label.config(text=f'Total Score: {total}')
            screen2.create_text(150, 100, text="OOPS!!!  it's is a Draw", fill='#CE6BE0', anchor='nw', font=('Rye', 30))

        screen2.create_text(180, 180, text="You Choice is: " + players, fill='#CE6BE0', anchor='nw', font=('Rye', 15))
        if players == 'ROCK':
            screen2.create_image(180, 200, image=rock_icon, anchor='nw')
        elif players == 'PAPER':
            screen2.create_image(180, 200, image=paper_icon, anchor='nw')
        else:
            screen2.create_image(180, 200, image=scissor_icon, anchor='nw')

        screen2.create_text(580, 180, text="Computer Choice is: " + computers, fill='#CE6BE0', anchor='nw',
                            font=('Rye', 15))
        if computers == 'ROCK':
            screen2.create_image(580, 200, image=rock_icon, anchor='nw')
        elif computers == 'PAPER':
            screen2.create_image(580, 200, image=paper_icon, anchor='nw')
        else:
            screen2.create_image(580, 200, image=scissor_icon, anchor='nw')

        score_label.config(text=f"Total Score: {total}")

        def reMatch():
            score_label.config(text=f"Total Score: {total}")
            screen2.pack_forget()
            msg.place_forget()
            screen1.pack()

        rematch = tk.Button(screen2, text='Rematch', command=reMatch, fg='#CE6BE0', bg='black', font=('Rye', 18))
        rematch.place(x=220, y=420)

        def exits():
            a = tk.messagebox.askyesno("Exit", "You want to Exit the game ?")
            if a:
                game_window.quit()

        rematch = tk.Button(screen2, text='Close', command=exits, fg='#CE6BE0', bg='black', font=('Rye', 18))
        rematch.place(x=420, y=420)
        score_label2.config(text=f'Total Score: {constant.score2}')

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

    rock_button = tk.Button(screen1, image=rock_icon, bg='black', highlightthickness=0, command=chooseRock)
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

    paper_button = tk.Button(screen1, image=paper_icon, bg='black', highlightthickness=0, command=choosePaper)
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

    scissor_button = tk.Button(screen1, image=scissor_icon, bg='black', highlightthickness=0, command=chooseScissor)
    scissor_button.place(x=620, y=220)
    game_window.mainloop()