from tkinter import *
from tkinter import messagebox
from random import choice, randint, randrange
import datetime
import mysql.connector
import os
from PIL import Image, ImageTk

sqlcon = mysql.connector.connect(host='localhost', user='root', password='1234', autocommit=True)
cursor = sqlcon.cursor()
Users = Passes = []
sportmenu = sportmenu1 = sportmenu2 = concertmenu = concertmenu1 = concertmenu2 = mov = mov1 = mov2 = mov3 = mainmenu = menufornew = menuforold = menuforgotpass = Main = trainmenu = trainmenu1 = trainmenu2 = transport1 = event1 = taximenu = cabmenu = cabmenu1 = busmenu = busmenu1 = busmenu2 = airmenu = airmenu1 = airmenu2 = Tk()
User = "Guest"


nopass = [i for i in range(1, 21)]
nopass1 = [i for i in range(1, 51)]
dates1 = [datetime.datetime.today() + datetime.timedelta(days=x) for x in range(0, 365)]
dates = [i.strftime("%d-%m_%Y") for i in dates1]
logo = Image.open('Images/bookmyseat.png')
smologo = Image.open('Images/bookmyseatsmall.png')
icologo = 'Images/bookmyseat.ico'


def startup():
    L = ["Create Database if not exists Project",
         "Use Project",
         "Create table if not exists Passwords (Username varchar(30) Primary key, Password varchar(30) )"]
    for i in L:
        cursor.execute(i)
    recordsfetch()
    global trainlist, cablist, color, trainlist1, trainlist2, flightlist, cricketlistint, cricketlistipl
    global nbalist, nbavenue, cricvenueipl, cricvenueint, footballteamlist, footballvenue, buslist, mini, suv
    global flightclass, flightbrand, theatre, movies, lang, art
    trainlist = read_text_file('table data/trainlist.txt')
    cablist = read_text_file('table data/cablist.txt')
    color = read_text_file('table data/color.txt')
    trainlist1 = read_text_file('table data/trainlist1.txt')
    trainlist2 = read_text_file('table data/trainlist2.txt')
    flightlist = read_text_file('table data/flightlist.txt')
    cricketlistint = read_text_file('table data/cricketlistint.txt')
    cricketlistipl = read_text_file('table data/cricketlistipl.txt')
    nbalist = read_text_file('table data/nbalist.txt')
    nbavenue = read_text_file('table data/nbavenue.txt')
    cricvenueipl = read_text_file('table data/cricvenueipl.txt')
    cricvenueint = read_text_file('table data/cricvenueint.txt')
    footballteamlist = read_text_file('table data/footballteamlist.txt')
    footballvenue = read_text_file('table data/footballvenue.txt')
    buslist = read_text_file('table data/buslist.txt')
    mini = read_text_file('table data/mini.txt')
    suv = read_text_file('table data/suv.txt')
    flightclass = read_text_file('table data/flightclass.txt')
    flightbrand = read_text_file('table data/flightbrand.txt')
    theatre = read_text_file('table data/theatre.txt')
    movies = {}
    movies_data = read_text_file('table data/movies.txt')
    for line in movies_data:
        movie, details_1, details_2 = line.split(',')
        movies[movie] = [details_1, details_2]
    lang = read_text_file('table data/lang.txt')
    art = read_text_file('table data/art.txt')

def read_text_file(filename):
    with open(filename, 'r') as file:
        data = file.read().splitlines()
    return data

def create_folder(folder_name,parent_folder="Tickets"):
    folder_path = os.path.join(parent_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
def recordsfetch():
    global Users, Passes
    cursor.execute("Select * from Passwords")
    Records = cursor.fetchall()
    Users, Passes = [i[0] for i in Records], [i[1] for i in Records]


def new():
    global menufornew, smologo, icologo
    des()
    menufornew = Tk()
    menufornew.state('zoomed')
    menufornew.title('Registration')
    menufornew.configure(bg="black")
    menufornew.wm_iconbitmap(icologo)
    name, password, password1 = StringVar(menufornew), StringVar(menufornew), StringVar(menufornew)
    tempolist = [["Username", name, 'pink', 'red'], ["Password", password, 'white', 'black'],
                 ["Confirm Password", password1, 'pink', 'red']]
    logo1 = ImageTk.PhotoImage(smologo, master=menufornew)
    L1 = Label(menufornew, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(pady=5)
    Label(menufornew, text="Account Registration", font=('calibre', 50, 'bold', 'underline'), fg='white',
          bg='black').pack(pady=3, fill=X)
    for i in tempolist:
        Label(menufornew, text=i[0], font=('calibre', 30, 'bold'), fg=i[2], bg='black').pack(pady=2, fill=X)
        if i[0] == "Username":
            Entry(menufornew, textvariable=i[1], font=('calibre', 30, 'bold'), bg=i[2], fg=i[3]).pack(pady=3, fill=X)
        else:
            Entry(menufornew, textvariable=i[1], font=('calibre', 30, 'bold'), show='*', bg=i[2], fg=i[3]).pack(
                pady=3, fill=X)
    Label(menufornew,bg='black').pack(pady=3)
    Button(menufornew, text="Enter", font=('calibre', 30, 'normal'), relief=RAISED,
           command=lambda: submitr(name.get(), password.get(), password1.get()), bg='white', fg='black',
           activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(menufornew, text="Go Back", font=('calibre', 30, 'normal'), relief=RAISED, command=lambda: back(1),
           bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
def old():
    global menuforold, smologo, icologo
    des()
    menuforold = Tk()
    menuforold.state('zoomed')
    menuforold.title('Login')
    menuforold.configure(bg="black")
    menuforold.wm_iconbitmap(icologo)
    name, password = StringVar(menuforold), StringVar(menuforold)
    tempolist = [["Username", name, 'pink', 'red'], ["Password", password, 'white', 'black']]
    logo1 = ImageTk.PhotoImage(smologo, master=menuforold)
    L1 = Label(menuforold, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(pady=5)
    Label(menuforold, text="Login Menu\n", font=('calibre', 50, 'bold', 'underline'), fg='white', bg='black').pack(
        pady=8, fill=X)
    for i in tempolist:
        Label(menuforold, text=i[0], font=('calibre', 30, 'bold'), fg=i[2], bg='black').pack(pady=5, fill=X)
        if i[0] == "Username":
            Entry(menuforold, textvariable=i[1], font=('calibre', 30, 'bold'), bg=i[2], fg=i[3]).pack(pady=8, fill=X)
        else:
            Entry(menuforold, textvariable=i[1], font=('calibre', 30, 'bold'), show='*', bg=i[2], fg=i[3]).pack(
                pady=8, fill=X)
    Button(menuforold, text="Forgot Password", font=('calibre', 30, 'normal'), relief=RAISED, command=forget,
           bg='white', fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(menuforold, text="     Submit    ", font=('calibre', 30, 'normal'), relief=RAISED,
           command=lambda: submitl(name.get(), password.get()), bg='white', fg='black', activebackground='pink',
           activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(menuforold, text="    Go back    ", font=('calibre', 30, 'normal'), relief=RAISED, command=lambda: back(1),
           bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def show(var):
    if var == 1:
        new()
        mainmenu.withdraw()
    elif var == 2:
        old()
        mainmenu.withdraw()
    else:
        messagebox.showerror("Error", "Choose one of the options.")


def back(a):
    des()
    if a == 1:
        mainmenu1()
    elif a == 2:
        menu1()
    elif a == 3:
        transport()
    elif a == 4:
        event()


def forget():
    global menuforgotpass, smologo, icologo
    des()
    menuforgotpass = Tk()
    menuforgotpass.wm_iconbitmap(icologo)
    menuforgotpass.state('zoomed')
    menuforgotpass.title('Forgot Password')
    menuforgotpass.configure(bg="black")
    logo1 = ImageTk.PhotoImage(smologo, master=menuforgotpass)
    L1 = Label(menuforgotpass, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(pady=5)
    name, password, password1 = StringVar(menuforgotpass), StringVar(menuforgotpass), StringVar(menuforgotpass)
    tempolist = [["Username", name, 'pink', 'red'], ["Password", password, 'white', 'black'],
                 ["Confirm Password", password1, 'pink', 'red']]
    Label(menuforgotpass, text="Reset Password", font=('calibre', 40, 'bold', 'underline'), fg='white',
          bg='black').pack(pady=5, fill=X)
    for i in tempolist:
        Label(menuforgotpass, text=i[0], font=('calibre', 25, 'bold'), fg=i[2], bg='black').pack(pady=2, fill=X)
        if i[0] == "Username":
            Entry(menuforgotpass, textvariable=i[1], font=('calibre', 25, 'bold'), bg=i[2], fg=i[3]).pack(pady=3,
                                                                                                          fill=X)
        else:
            Entry(menuforgotpass, textvariable=i[1], font=('calibre', 25, 'bold'), show='*', bg=i[2], fg=i[3]).pack(
                pady=3, fill=X)
        Label(menuforgotpass, bg='black').pack(pady=3, fill=X)
    Button(menuforgotpass, text='Submit', command=lambda: update(name.get(), password.get(), password1.get()),
           font=('calibre', 30, 'normal'), relief=RAISED, bg='white', fg='black', activebackground='pink',
           activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(menuforgotpass, text="Go back", font=('calibre', 30, 'normal'), relief=RAISED, command=lambda: back(1),
           bg='white', fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def update(name, password, password1):
    global Users, Passes, User, menuforgotpass
    if name in Users:
        if password == password1:
            cursor.execute("Update Passwords set Password='{}' where Username='{}'".format(password, name))
            Passes[Users.index(name)] = password
            M1 = messagebox.showinfo("Success", "Successfully Updated!")
            if M1:
                M2 = messagebox.askyesno("Login", "Do you want to login with the same?")
                if M2:
                    User = name
                    back(2)
                else:
                    back(1)
        else:
            messagebox.showerror("Error", "Passwords do not match.")
    else:
        M4 = messagebox.askyesno("Username is not in use", "Username does not exist. Do you want to retry again ?")
        if M4 is False:
            back(1)


def submitr(name, password, password1):
    global Users, Passes, User, menufornew
    if name not in Users:
        if password == password1:
            cursor.execute("Insert into Passwords values('{}','{}')".format(name, password))
            Users.append(name)
            Passes.append(password)
            M1 = messagebox.showinfo("Success", "Successfully Registered!")
            if M1 == "ok":
                M2 = messagebox.askyesno("Login", "Do you want to login with the same?")
                if M2:
                    User = name
                    back(2)
                else:
                    back(1)
        else:
            messagebox.showerror("Error", "Passwords do not match.")
    else:
        M4 = messagebox.askyesno("Username is already in use",
                                 "Username already exists. Do you want to login instead ?")
        if M4:
            des()
            old()
        else:
            back(1)


def submitl(name, password):
    global Users, Passes, User, menuforold
    if name in Users:
        if password == Passes[Users.index(name)]:
            User = name
            M1 = messagebox.showinfo("Success", "Successfully Logged in!")
            if M1 == "ok":
                back(2)
        else:
            messagebox.showerror("Incorrect Password",
                                 " Incorrect Password Entered. Please check the details once again.")
    else:
        M3 = messagebox.askyesno("Username doesn't exist",
                                 "Username doesn't exist in database. Please check the details once again. Do you want to register instead?")
        if M3:
            des()
            new()


def des():
    global sportmenu, sportmenu1, sportmenu2, concertmenu, concertmenu1, concertmenu2, mov3, mov1, mov2, mov, airmenu1, airmenu, airmenu2, mainmenu, menufornew, menuforold, menuforgotpass, Main, transport1, event1, taximenu, cabmenu, cabmenu1, trainmenu, trainmenu1, trainmenu2, busmenu, busmenu1, busmenu2
    menufornew.withdraw()
    menuforold.withdraw()
    menuforgotpass.withdraw()
    Main.withdraw()
    transport1.withdraw()
    event1.withdraw()
    taximenu.withdraw()
    cabmenu.withdraw()
    trainmenu.withdraw()
    cabmenu1.withdraw()
    trainmenu1.withdraw()
    trainmenu2.withdraw()
    mainmenu.withdraw()
    busmenu.withdraw()
    busmenu1.withdraw()
    busmenu2.withdraw()
    airmenu.withdraw()
    airmenu1.withdraw()
    airmenu2.withdraw()
    mov.withdraw()
    mov1.withdraw()
    mov2.withdraw()
    mov3.withdraw()
    concertmenu.withdraw()
    concertmenu1.withdraw()
    concertmenu2.withdraw()
    sportmenu.withdraw()
    sportmenu1.withdraw()
    sportmenu2.withdraw()


def mainmenu1():
    global mainmenu, logo, icologo
    des()
    mainmenu = Tk()
    mainmenu.state('zoomed')
    mainmenu.title('BookMySeat')
    mainmenu.configure(bg="black")
    mainmenu.wm_iconbitmap(icologo)
    var = IntVar(mainmenu)
    logo1 = ImageTk.PhotoImage(logo, master=mainmenu)
    L1 = Label(mainmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack()
    Label(mainmenu, text="Greetings Dear User!", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(pady=2,
                                                                                                           fill=X,
                                                                                                           expand=True)
    Label(mainmenu, text="Welcome to BookMySeat!", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(pady=8,
                                                                                                             fill=X,
                                                                                                             expand=True)
    Radiobutton(mainmenu, text="I don't have an account (Registration Menu)", variable=var, value=1,
                font=('calibre', 20, 'normal'), fg='white',
                bg='black', activeforeground="red", activebackground='pink', selectcolor='red').pack(pady=5)
    Radiobutton(mainmenu, text="I have an account (Login Menu)", variable=var, value=2,
                font=('calibre', 20, 'normal'), fg='white',
                bg='black', activeforeground="red", activebackground='pink', selectcolor='red').pack(pady=5)
    Button(mainmenu, text="  Go  ", relief=RAISED, command=lambda: show(var.get()), font=('calibre', 30, 'bold'),
           bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(mainmenu, text=" Quit ", relief=RAISED, command=mainmenu.withdraw, font=('calibre', 30, 'bold'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def menu1():
    global User, Main, logo, icologo
    des()
    Main = Tk()
    Main.state('zoomed')
    Main.title('BookMySeat')
    Main.configure(bg="black")
    Main.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(logo, master=Main)
    L1 = Label(Main, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    text1 = "Greetings %s" % User
    Label(Main, text=text1, font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP, fill=X, expand=True)
    Label(Main, text='Welcome to BookMySeat!', font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                         fill=X,
                                                                                                         expand=True)
    Label(Main, bg='black').pack(side=TOP, fill=X, expand=True)
    Label(Main, bg='black').pack(side=TOP, fill=X, expand=True)
    Button(Main, text="Tickets for Travelling", relief=RAISED, command=transport,
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=Y, expand=True)
    Button(Main, text="  Tickets for Events  ", relief=RAISED, command=event, font=('calibre', 30, 'normal'),
           bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=Y, expand=True)
    Label(Main, bg='black').pack(side=TOP)
    Label(Main, bg='black').pack(side=TOP)
    Button(Main, text="Quit", relief=RAISED, command=lambda: back(1), font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=Y, expand=True)


def transport():
    global Main, User, transport1, smologo, icologo
    des()
    transport1 = Tk()
    transport1.state('zoomed')
    transport1.title('BookMySeat - Transport')
    transport1.configure(bg="black")
    transport1.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=transport1)
    L1 = Label(transport1, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(transport1, text="Transport Menu\n", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                         fill=X)
    Button(transport1, text="I want to book a CAB", relief=RAISED, command=taxi,
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Button(transport1, text="I want to book a TRAIN ticket", relief=RAISED, command=train,
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Button(transport1, text="I want to book a BUS ticket", relief=RAISED, command=bus, font=('calibre', 30, 'normal'),
           bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Button(transport1, text="I want to book a FLIGHT ticket", relief=RAISED, command=air,
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Label(transport1, bg='black').pack(side=TOP)
    Label(transport1, bg='black').pack(side=TOP)
    Button(transport1, text="Go back", relief=RAISED, command=lambda: back(2),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)


def event():
    global Main, User, event1, smologo, icologo
    des()
    event1 = Tk()
    event1.state('zoomed')
    event1.title('BookMySeat - Events')
    event1.configure(bg="black")
    event1.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=event1)
    L1 = Label(event1, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(event1, text="Events Menu\n", font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP, fill=X)
    Button(event1, text="I want to book a ticket to a MOVIE", relief=RAISED, command=movie,
           font=('calibre', 30, 'normal'), bg='plum1', fg='firebrick4', activebackground='pink',
           activeforeground='red').pack(side=TOP)
    Button(event1, text="I want to book a ticket to a CONCERT", relief=RAISED, command=concert,
           font=('calibre', 30, 'normal'), bg='plum1', fg='firebrick4', activebackground='pink',
           activeforeground='red').pack(side=TOP)
    Button(event1, text="I want to book a ticket to a SPORTS EVENT", relief=RAISED, command=sports,
           font=('calibre', 30, 'normal'), bg='plum1', fg='firebrick4', activebackground='pink',
           activeforeground='red').pack(side=TOP)
    Label(event1, bg='black').pack(side=TOP)
    Label(event1, bg='black').pack(side=TOP)
    Button(event1, text="Go back", relief=RAISED, command=lambda: back(2), font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)


def movie():
    global mov, User, smologo, icologo
    des()
    mov = Tk()
    mov.state('zoomed')
    mov.title('BookMySeat - Movie')
    mov.configure(bg="black")
    mov.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=mov)
    L1 = Label(mov, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    n, m, d, e = StringVar(mov), StringVar(mov), StringVar(mov), IntVar(mov)
    Label(mov, text="Movie Menu", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(pady=8, fill=X)
    Label(mov, text="Movie", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(mov, n, *[i for i in movies]).pack(pady=5, fill=X, expand=True)
    Label(mov, text="Theatre", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(mov, m, *theatre).pack(pady=5, fill=X, expand=True)
    Label(mov, text="Date of airing", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(mov, d, *dates).pack(pady=5, fill=X, expand=True)
    Label(mov, text="No. of Seats", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(mov, e, *nopass1).pack(pady=5, fill=X, expand=True)
    Label(mov, bg='black').pack(side=TOP)
    Button(mov, text="Book", relief=RAISED, command=lambda: movie2(n.get(), m.get(), d.get(), e.get()),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(mov, text="Go Back", relief=RAISED, command=lambda: back(4),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def movie2(M, T, d, n):
    global mov1, User, smologo, icologo
    if M and T and d and n:
        des()
        mov1 = Tk()
        mov1.state('zoomed')
        mov1.title('BookMySeat - Movie')
        mov1.configure(bg="black")
        mov1.wm_iconbitmap(icologo)
        logo1 = ImageTk.PhotoImage(smologo, master=mov1)
        L1 = Label(mov1, image=logo1, borderwidth=0, highlightthickness=0)
        L1.image = logo1
        L1.pack(side=TOP)
        t = "%s Movie Ticket Booking" % M
        Label(mov1, text=t, font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(
            side=TOP, fill=X)
        Label(mov1, bg='black').pack(side=TOP)
        v, A, B = movies[M], StringVar(mov1), StringVar(mov1)
        if v[0] == "3D":
            Radiobutton(mov1, text="2-D", variable=A, value="2D",
                        font=('calibre', 30, 'normal'), fg='white',
                        bg='black', activeforeground="red", activebackground='pink', selectcolor='red').pack(
                side=TOP)
            Radiobutton(mov1, text="3-D", variable=A, value="3D",
                        font=('calibre', 30, 'normal'), fg='white',
                        bg='black', activeforeground="red", activebackground='pink', selectcolor='red').pack(
                side=TOP)
        Label(mov1, text="Language", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        if v[1] != "English":
            OptionMenu(mov1, B, *lang).pack(side=TOP, fill=X, expand=True)
        else:
            tempolist = lang + ["English"]
            OptionMenu(mov1, B, *tempolist).pack(side=TOP, fill=X, expand=True)
        Label(mov1, bg='black').pack(side=TOP)
        Label(mov1, bg='black').pack(side=TOP)
        Button(mov1, text="Book", relief=RAISED, command=lambda: movie3(M, T, d, n, A.get(), B.get()),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
        Button(mov1, text="Go Back", relief=RAISED, command=lambda: back(4),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    else:
        messagebox.showerror("ERROR", "Please ensure that all of the entries are filled.")


def movie3(M, T, d, n, V, L):
    global mov2, User, smologo, icologo
    if L:
        if V != "3D":
            V = "2D"
        des()
        mov2 = Tk()
        mov2.state('zoomed')
        mov2.title('BookMySeat - Movie - Food Menu')
        mov2.configure(bg="black")
        mov2.wm_iconbitmap(icologo)
        logo1 = ImageTk.PhotoImage(smologo, master=mov2)
        L1 = Label(mov2, image=logo1, borderwidth=0, highlightthickness=0)
        L1.image = logo1
        L1.pack(side=TOP)
        P, C, D, N = IntVar(mov2), IntVar(mov2), IntVar(mov2), IntVar(mov2)
        Label(mov2, text="BookMySeat - Movie - Food Menu", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(
            side=TOP, fill=X)
        Label(mov2, bg='black').pack(side=TOP)
        Label(mov2, text="No. of Popcorn", font=('calibre', 30, 'bold'), fg='pink', bg='black').pack(
            side=TOP)
        OptionMenu(mov2, P, *nopass).pack(side=TOP, fill=X, expand=True)
        Label(mov2, text="No. of Coke", font=('calibre', 30, 'bold'), fg='pink', bg='black').pack(
            side=TOP)
        OptionMenu(mov2, C, *nopass).pack(side=TOP, fill=X, expand=True)
        Label(mov2, text="No. of Donuts", font=('calibre', 30, 'bold'), fg='pink', bg='black').pack(
            side=TOP)
        OptionMenu(mov2, D, *nopass).pack(side=TOP, fill=X, expand=True)
        Label(mov2, text="No. of Nachos", font=('calibre', 30, 'bold'), fg='pink', bg='black').pack(
            side=TOP)
        OptionMenu(mov2, N, *nopass).pack(side=TOP, fill=X, expand=True)
        Label(mov2, bg='black').pack(side=TOP)
        Label(mov2, bg='black').pack(side=TOP)
        Button(mov2, text="Book", relief=RAISED,
               command=lambda: movie4(M, T, d, n, V, L, P.get(), C.get(), D.get(), N.get()),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
        Button(mov2, text="Go Back", relief=RAISED, command=lambda: back(4),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    else:
        messagebox.showerror("ERROR", "Please ensure that all of the entries are filled.")


def movie4(M, T, d, n, V, L, P, C, D, E):
    global mov3, User, smologo, icologo
    bookedmsg = "You have successfully booked movie ticket/s for " + M + " in " + T + " in " + L + " language.\nClick yes to download the ticket in form of text file."
    M1 = messagebox.askyesno("Success", bookedmsg)
    if M1:
        des()
        mov3 = Tk()
        mov3.state('zoomed')
        mov3.title('TICKET')
        mov3.configure(bg="black")
        mov3.wm_iconbitmap(icologo)
        logo1 = ImageTk.PhotoImage(smologo, master=mov3)
        L1 = Label(mov3, image=logo1, borderwidth=0, highlightthickness=0)
        L1.image = logo1
        L1.pack(side=TOP)
        create_folder(User)
        filename = "Tickets/"+ User + "/Movie-"+ whattime() + ".txt"
        with open(filename, "w+") as file:
            Cost, n = str((300 * (n + P)) + (100 * (C + D + E))), str(n)
            file.writelines(["Dear " + User + "!", "\nThank you for using BookMySeat's booking facility!",
                             "\nMovie Name: " + M, "\nTheatre: " + T, "\nDate: " + d,
                             "\nNo of Seats booked: " + n,
                             "\nView Mode: " + V,
                             "\nLanguage: " + L,
                             "\nNo.of Popcorn ordered: " + str(P),
                             "\tNo.of Cokes ordered: " + str(C),
                             "\nNo.of Donuts ordered: " + str(D),
                             "\tNo.of Nachos ordered: " + str(E),
                             "\nAmount to be paid: " + Cost])
            file.seek(0)
            filetext = file.read()
        Label(mov3, text="TICKET", font=('calibre', 20, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
        Label(mov3, bg='black').pack(side=TOP)
        Label(mov3, text=filetext, font=('calibre', 20, 'normal'), fg='Black', bg='White').pack(side=TOP,
                                                                                                fill=X)
        Label(mov3, text="Ticket is saved in suitable directory with name: ",
              font=('calibre', 20, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
        Label(mov3, text=filename, font=('calibre', 20, 'bold'), fg="Red", bg='black').pack(side=TOP, fill=X)
        Label(mov3, bg='black').pack(side=TOP, fill=X)
        Button(mov3, text="Done", relief=RAISED, command=lambda: back(4), font=('calibre', 30,
                                                                                'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
    else:
        back(4)


def concert():
    global concertmenu, User, smologo, icologo
    des()
    concertmenu = Tk()
    concertmenu.state('zoomed')
    concertmenu.title('BookMySeat - Concert')
    concertmenu.configure(bg="black")
    concertmenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=concertmenu)
    L1 = Label(concertmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    n, m, o = StringVar(concertmenu), StringVar(concertmenu), StringVar(concertmenu)
    Label(concertmenu, text="Concert Menu\n", font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                        fill=X)
    Label(concertmenu, bg='black').pack(side=TOP)
    Label(concertmenu, text="Artist / Band", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(concertmenu, n, *art).pack(side=TOP, fill=X, expand=True)
    Label(concertmenu, bg='black').pack(side=TOP)
    Label(concertmenu, text="Venue of Concert", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(concertmenu, m, *trainlist).pack(side=TOP, fill=X, expand=True)
    Label(concertmenu, bg='black').pack(side=TOP)
    Label(concertmenu, text="Date of Concert", font=('calibre', 30, 'normal'), fg='white', bg='black').pack(side=TOP)
    OptionMenu(concertmenu, o, *dates).pack(side=TOP, fill=X, expand=True)
    Label(concertmenu, bg='black').pack(side=TOP)
    Label(concertmenu, bg='black').pack(side=TOP)
    Button(concertmenu, text="Book", relief=RAISED, command=lambda: concert1(n.get(), m.get(), o.get()),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(concertmenu, text="Go Back", relief=RAISED, command=lambda: back(4),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def concert1(n, m, o):
    global User, smologo, concertmenu1, icologo
    if n and m and o:
        des()
        concertmenu1 = Tk()
        concertmenu1.state('zoomed')
        concertmenu1.title('BookMySeat - Concert')
        concertmenu1.configure(bg="black")
        concertmenu1.wm_iconbitmap(icologo)
        logo1 = ImageTk.PhotoImage(smologo, master=concertmenu1)
        L1 = Label(concertmenu1, image=logo1, borderwidth=0, highlightthickness=0)
        L1.image = logo1
        L1.pack(side=TOP)
        seat = ["VIP Area", "Balcony", "Premium Sofas", "General"]
        p, q, r = StringVar(concertmenu1), IntVar(concertmenu1), IntVar(concertmenu1)
        Label(concertmenu1, text="Concert Menu\n", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                             fill=X)
        Label(concertmenu1, bg='black').pack(side=TOP)
        Label(concertmenu1, text="Seating Area", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(concertmenu1, p, *seat).pack(pady=3, fill=X, expand=True)
        Label(concertmenu1, bg='black').pack(side=TOP)
        Label(concertmenu1, text="No. of Seats", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(concertmenu1, q, *nopass).pack(pady=3, fill=X, expand=True)
        Label(concertmenu1, bg='black').pack(side=TOP)
        Radiobutton(concertmenu1, text="Exclude Snacks and Beverages", variable=r, value=0,
                    font=('calibre', 30, 'normal'), fg='white',
                    bg='black', activeforeground="red", activebackground='pink', selectcolor='red').pack(
            pady=3)
        Radiobutton(concertmenu1, text="Include Snacks and Beverages", variable=r, value=1,
                    font=('calibre', 30, 'normal'), fg='white',
                    bg='black', activeforeground="red", activebackground='pink', selectcolor='red').pack(
            pady=8)
        Button(concertmenu1, text="Book", relief=RAISED, command=lambda: concert2(n, m, o, p.get(), q.get(), r.get()),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
        Button(concertmenu1, text="Go Back", relief=RAISED, command=lambda: back(4),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    else:
        messagebox.showerror("ERROR", "Please ensure that all of the entries are filled.")


def concert2(n, m, o, p, q, r):
    global concertmenu2, User, smologo, icologo
    if p and q:
        bookedmsg = "You have successfully booked ticket/s to a concert by " + n + " in " + m + " on " + o + ".\nClick yes to download the ticket in form of text file."
        M1 = messagebox.askyesno("Success", bookedmsg)
        if M1:
            des()
            concertmenu2 = Tk()
            concertmenu2.state('zoomed')
            concertmenu2.title('TICKET')
            concertmenu2.configure(bg="black")
            concertmenu2.wm_iconbitmap(icologo)
            logo1 = ImageTk.PhotoImage(smologo, master=concertmenu2)
            L1 = Label(concertmenu2, image=logo1, borderwidth=0, highlightthickness=0)
            L1.image = logo1
            L1.pack(side=TOP)
            create_folder(User)
            filename = "Tickets/"+ User + "/Concert-"+ whattime() + ".txt"
            with open(filename, "w+") as file:
                Cost, q = str(q * (500 + (r * 200))), str(q)
                if r == 0:
                    s = " (no snacks) "
                else:
                    s = " (includes snacks)"
                file.writelines(["Dear " + User + "!", "\nThank you for using BookMySeat's booking facility!",
                                 "\nArtist / Band Name: " + n, "\nVenue: " + m, "\nDate: " + o,
                                 "\nNo of Seats booked: " + q,
                                 "\nSeating Area: " + p,
                                 "\nAmount to be paid: " + Cost + s])
                file.seek(0)
                filetext = file.read()
            Label(concertmenu2, text="TICKET", font=('calibre', 30, 'bold'), fg='White', bg='black').pack(side=TOP,
                                                                                                          fill=X)
            Label(concertmenu2, bg='black').pack(side=TOP)
            Label(concertmenu2, text=filetext, font=('calibre', 20, 'normal'), fg='Black', bg='White').pack(side=TOP,
                                                                                                            fill=X)
            Label(concertmenu2, bg='black').pack(side=TOP)
            Label(concertmenu2, bg='black').pack(side=TOP)
            Label(concertmenu2, text="Ticket is saved in suitable directory with name: ",
                  font=('calibre', 20, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(concertmenu2, text=filename, font=('calibre', 20, 'bold'), fg="Red", bg='black').pack(side=TOP,
                                                                                                        fill=X)
            Label(concertmenu2, bg='black').pack(side=TOP, fill=X)
            Button(concertmenu2, text="Done", relief=RAISED, command=lambda: back(4), font=('calibre', 30,
                                                                                            'normal'), bg='white',
                   fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
        else:
            back(4)
    else:
        messagebox.showerror("ERROR", "Please ensure that all of the entries are filled.")


def sports():
    global sportmenu, User, smologo, icologo
    des()
    sportmenu = Tk()
    sportmenu.state('zoomed')
    sportmenu.title('BookMySeat - Sports Events')
    sportmenu.configure(bg="black")
    sportmenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=sportmenu)
    L1 = Label(sportmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(sportmenu, text="Sports Menu\n", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                     fill=X)
    Label(sportmenu, bg='black').pack(side=TOP)
    Button(sportmenu, text="Cricket Matches", relief=RAISED, command=lambda: sports1('Cricket Matches Menu', 'Cricket'),
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Button(sportmenu, text="Football Matches ", relief=RAISED,
           command=lambda: sports1('Football Matches Menu', 'Football'),
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Button(sportmenu, text="Basketball Matches ", relief=RAISED,
           command=lambda: sports1('Basketball Matches Menu', 'Basketball'),
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Label(sportmenu, bg='black').pack(side=TOP)
    Button(sportmenu, text="Go Back", relief=RAISED, command=lambda: back(4),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X, expand=True)


def sports1(t, t1):
    global sportmenu1, User, smologo, icologo
    des()
    sportmenu1 = Tk()
    sportmenu1.state('zoomed')
    sportmenu1.title('BookMySeat - Sports Events')
    sportmenu1.configure(bg="black")
    sportmenu1.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=sportmenu1)
    L1 = Label(sportmenu1, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(sportmenu1, text=t, font=('calibre', 35, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                        fill=X)
    Label(sportmenu1, bg='black').pack(side=TOP)
    if t == "Basketball Matches Menu":
        list1, list2 = nbalist, nbavenue
    elif t == 'Football Matches Menu':
        list1, list2 = footballteamlist, footballvenue
    elif t == "Cricket Matches Menu":
        Button(sportmenu1, text="Book Tickets for IPL", relief=RAISED,
               command=lambda: sports1('IPL Matches Menu', 'IPL'),
               font=('calibre', 30, 'normal'), bg='plum1',
               fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
        Button(sportmenu1, text="Book Tickets for International Cricket Matches", relief=RAISED,
               command=lambda: sports1('International Cricket Matches Menu', 'International Cricket'),
               font=('calibre', 30, 'normal'), bg='plum1',
               fg='firebrick4', activebackground='pink', activeforeground='red').pack(
            side=TOP)
        Label(sportmenu1, bg='black').pack(side=TOP)
        Button(sportmenu1, text="Go Back", relief=RAISED, command=lambda: back(4),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X, expand=True)
        return
    elif t == 'IPL Matches Menu':
        list1, list2 = cricketlistipl, cricvenueipl
    else:
        list1, list2 = cricketlistint, cricvenueint
    n, m, o, v, p = StringVar(sportmenu1), StringVar(sportmenu1), StringVar(sportmenu1), StringVar(sportmenu1), IntVar(
        sportmenu1)
    OptionMenu(sportmenu1, n, *list1).pack(side=TOP, fill=X, expand=True)
    Label(sportmenu1, text="VS", font=('calibre', 20, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(sportmenu1, m, *list1).pack(side=TOP, fill=X, expand=True)
    Label(sportmenu1, bg='black').pack(side=TOP)
    Label(sportmenu1, text="Date", font=('calibre', 20, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(sportmenu1, o, *dates).pack(side=TOP, fill=X, expand=True)
    Label(sportmenu1, bg='black').pack(side=TOP)
    Label(sportmenu1, text="Stadium", font=('calibre', 20, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(sportmenu1, v, *list2).pack(side=TOP, fill=X, expand=True)
    Label(sportmenu1, bg='black').pack(side=TOP)
    Label(sportmenu1, text="No of Tickets to be booked", font=('calibre', 20, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(sportmenu1, p, *nopass).pack(side=TOP, fill=X, expand=True)
    Label(sportmenu1, bg='black').pack(side=TOP)
    Button(sportmenu1, text="Book", relief=RAISED,
           command=lambda: sports2(n.get(), m.get(), o.get(), v.get(), p.get(), t1),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(sportmenu1, text="Go Back", relief=RAISED, command=lambda: back(4),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def sports2(Team1, Team2, Date, Stadium, Tickets, Sport):
    global sportmenu2, User, smologo, icologo
    if Team1 and Team2 and Date and Tickets and Stadium and Sport:
        if Team1 != Team2:
            bookedmsg = "You have successfully booked ticket/s for " + Sport + " Match between " + Team1 + " and " + Team2 + " which takes place on " + Date + " in " + Stadium + ".\nClick yes to download the ticket in form of text file."
            M1 = messagebox.askyesno("Success", bookedmsg)
            if M1:
                des()
                sportmenu2 = Tk()
                sportmenu2.state('zoomed')
                sportmenu2.title('TICKET')
                sportmenu2.configure(bg="black")
                sportmenu2.wm_iconbitmap(icologo)
                logo1 = ImageTk.PhotoImage(smologo, master=sportmenu2)
                L1 = Label(sportmenu2, image=logo1, borderwidth=0, highlightthickness=0)
                L1.image = logo1
                L1.pack(side=TOP)
                create_folder(User)
                filename = "Tickets/"+ User + "/"+ Sport + "-" + whattime() + ".txt"
                with open(filename, "w+") as file:
                    if Sport[-1] == "l":
                        r = 6500
                    else:
                        r = 3000
                    Cost, Tickets = str(r * Tickets), str(Tickets)
                    file.writelines(["Dear " + User + "!", "\nThank you for using BookMySeat's booking facility!",
                                     "\nTicket for a/an  " + Sport + " Match between " + Team1 + " and " + Team2,
                                     "\nStadium: " + Stadium, "\nDate: " + Date,
                                     "\nNo of Seats booked: " + Tickets,
                                     "\nAmount to be paid: " + Cost])
                    file.seek(0)
                    filetext = file.read()
                Label(sportmenu2, text="TICKET", font=('calibre', 30, 'bold'), fg='White', bg='black').pack(side=TOP,
                                                                                                            fill=X)
                Label(sportmenu2, bg='black').pack(side=TOP)
                Label(sportmenu2, text=filetext, font=('calibre', 20, 'normal'), fg='Black', bg='White').pack(side=TOP,
                                                                                                              fill=X)
                Label(sportmenu2, bg='black').pack(side=TOP)
                Label(sportmenu2, bg='black').pack(side=TOP)
                Label(sportmenu2, text="Ticket is saved in suitable directory with name: ",
                      font=('calibre', 20, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
                Label(sportmenu2, text=filename, font=('calibre', 20, 'bold'), fg="Red", bg='black').pack(side=TOP,
                                                                                                          fill=X)
                Label(sportmenu2, bg='black').pack(side=TOP, fill=X)
                Button(sportmenu2, text="Done", relief=RAISED, command=lambda: back(4), font=('calibre', 30,
                                                                                              'normal'), bg='white',
                       fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
            else:
                back(4)
        else:
            messagebox.showerror("ERROR", "Please ensure that Team 1 and Team 2 aren't the same.")

    else:
        messagebox.showerror("ERROR", "Please ensure that all of the entries are filled.")


def train():
    global trainmenu, User, smologo, icologo
    des()
    trainmenu = Tk()
    trainmenu.state('zoomed')
    trainmenu.title('BookMySeat - Train')
    trainmenu.configure(bg="black")
    trainmenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=trainmenu)
    L1 = Label(trainmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(trainmenu, text="Train Ticket Booking", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                            fill=X)
    n, m = StringVar(trainmenu), StringVar(trainmenu)
    Label(trainmenu, text="Train from: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(trainmenu, n, *trainlist).pack(side=TOP, fill=X, expand=True)
    Label(trainmenu, bg='black').pack(side=TOP)
    Label(trainmenu, text="Train to: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(trainmenu, m, *trainlist).pack(side=TOP, fill=X, expand=True)
    Label(trainmenu, bg='black').pack(side=TOP)
    Label(trainmenu, bg='black').pack(side=TOP)
    Button(trainmenu, text="Book", relief=RAISED, command=lambda: train2(n.get(), m.get()),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(trainmenu, text="Go Back", relief=RAISED, command=lambda: back(3),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def train2(f, t):
    global trainmenu1, User, smologo, icologo
    if f == t:
        messagebox.showerror("ERROR", "Please ensure that pickup and drop point are different.")
    elif f and t:
        des()
        trainmenu1 = Tk()
        trainmenu1.state('zoomed')
        trainmenu1.title('BookMySeat - Train')
        trainmenu1.configure(bg="black")
        trainmenu1.wm_iconbitmap(icologo)
        logo1 = ImageTk.PhotoImage(smologo, master=trainmenu1)
        L1 = Label(trainmenu1, image=logo1, borderwidth=0, highlightthickness=0)
        L1.image = logo1
        L1.pack(side=TOP)
        Label(trainmenu1, text="Train Ticket Booking", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(
            side=TOP, fill=X)
        n, m, o, p = StringVar(trainmenu1), StringVar(trainmenu1), IntVar(trainmenu1), StringVar(trainmenu1)
        templist = [["Reservation Quota: ", n, trainlist1], ["Reservation Class: ", m, trainlist2],
                    ["No of Passengers: ", o, nopass], ["Date of Arrival/Departure: ", p, dates]]
        for i in templist:
            Label(trainmenu1, text=i[0], font=('calibre', 30, 'normal'), fg='white',
                  bg='black').pack(side=TOP)
            OptionMenu(trainmenu1, i[1], *i[2]).pack(side=TOP, fill=X, expand=True)
        Label(trainmenu1, bg='black').pack(side=TOP)
        Label(trainmenu1, bg='black').pack(side=TOP)
        Button(trainmenu1, text="Book", relief=RAISED,
               command=lambda: train3(n.get(), m.get(), f, t, o.get(), p.get()),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
        Button(trainmenu1, text="Go Back", relief=RAISED, command=lambda: back(3), font=('calibre', 30, 'normal'),
               bg='white', fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X,
                                                                                             expand=True)
    else:
        messagebox.showerror("ERROR", "Please ensure that pickup and drop point are selected.")


def train3(cat, cla, f, t, n, d):
    global User, trainmenu2, smologo, icologo
    if cat and cla and f and t and n and d:
        bookedmsg = "You have successfully booked train ticket/s from " + f + " to " + t + ".\nClick yes to download the ticket in form of text file."
        M = messagebox.askyesno("Success", bookedmsg)
        if M:
            des()
            create_folder(User)
            filename = "Tickets/"+ User + "/Train-"+ whattime() + ".txt"
            with open(filename, "w+") as file:
                Fare, pnr, trainno = str(150 * n), str(randint(1000000000, 9999999999)), str(randint(100000, 999999))
                file.writelines(["Dear " + User + "!", "\nThank you for using BookMySeat's reservation facility!",
                                 "\nPNR No: " + pnr, "\nTrain No: " + trainno, "\nReservation Quota: " + cat,
                                 "\nReservation Class: " + cla, "\nPickup Location: " + f + "\nDrop Location: " + t,
                                 "\nScheduled Arrival: " + d, "\nAmount to be paid: " + Fare])
                file.seek(0)
                filetext = file.read()
            trainmenu2 = Tk()
            trainmenu2.state('zoomed')
            trainmenu2.title("Ticket")
            trainmenu2.configure(bg="black")
            trainmenu2.wm_iconbitmap(icologo)
            logo1 = ImageTk.PhotoImage(smologo, master=trainmenu2)
            L1 = Label(trainmenu2, image=logo1, borderwidth=0, highlightthickness=0)
            L1.image = logo1
            L1.pack(side=TOP)
            Label(trainmenu2, text="TICKET", font=('calibre', 30, 'bold'), fg='White', bg='black').pack(side=TOP,
                                                                                                        fill=X)
            Label(trainmenu2, bg='black').pack(side=TOP)
            Label(trainmenu2, text=filetext, font=('calibre', 20, 'normal'), fg='Black', bg='White').pack(side=TOP,
                                                                                                          fill=X)
            Label(trainmenu2, bg='black').pack(side=TOP)
            Label(trainmenu2, text="Ticket is saved in suitable directory with name: ",
                  font=('calibre', 30, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(trainmenu2, text=filename, font=('calibre', 25, 'bold'), fg="Red", bg='black').pack(side=TOP, fill=X)
            Button(trainmenu2, text="Done", relief=RAISED, command=lambda: back(3), font=('calibre', 30,
                                                                                          'normal'), bg='white',
                   fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
        else:
            back(3)
    else:
        messagebox.showerror("ERROR",
                             "Please ensure that all of the options are chosen and the number of passengers is not zero.")


def bus():
    global busmenu, User, smologo, icologo
    des()
    busmenu = Tk()
    busmenu.state('zoomed')
    busmenu.title('BookMySeat - Bus')
    busmenu.configure(bg="black")
    busmenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=busmenu)
    L1 = Label(busmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(busmenu, text="Bus Ticket Booking", font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                        fill=X)
    n, m = StringVar(busmenu), StringVar(busmenu)
    Label(busmenu, text="Bus from: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(busmenu, n, *trainlist).pack(side=TOP, fill=X, expand=True)
    Label(busmenu, text="Bus to: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(busmenu, m, *trainlist).pack(side=TOP, fill=X, expand=True)
    Label(busmenu, bg='black').pack(side=TOP)
    Label(busmenu, bg='black').pack(side=TOP)
    Label(busmenu, bg='black').pack(side=TOP)
    Button(busmenu, text="Book", relief=RAISED, command=lambda: bus1(n.get(), m.get()),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X,
                                                                             expand=True)
    Button(busmenu, text="Go Back", relief=RAISED, command=lambda: back(3),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X,
                                                                             expand=True)


def bus1(f, t):
    global busmenu1, User, smologo, icologo
    if f == t:
        messagebox.showerror("ERROR", "Please ensure that pickup and drop point are different.")
    elif f and t:
        des()
        busmenu1 = Tk()
        busmenu1.state('zoomed')
        busmenu1.title('BookMySeat - Bus')
        busmenu1.configure(bg="black")
        busmenu1.wm_iconbitmap(icologo)
        logo1 = ImageTk.PhotoImage(smologo, master=busmenu1)
        L1 = Label(busmenu1, image=logo1, borderwidth=0, highlightthickness=0)
        L1.image = logo1
        L1.pack(side=TOP)
        Label(busmenu1, text="Bus Ticket Booking", font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                             fill=X)
        n, m, o, p = StringVar(busmenu1), IntVar(busmenu1), IntVar(busmenu1), StringVar(busmenu1)
        Label(busmenu1, text="Bus Type: ", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(busmenu1, n, *buslist).pack(side=TOP, fill=X, expand=True)
        Label(busmenu1, text="No. of Window Seats: ", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(busmenu1, m, *nopass).pack(side=TOP, fill=X, expand=True)
        Label(busmenu1, text="No. of Non-Window Seats: ", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(busmenu1, o, *nopass1).pack(side=TOP, fill=X, expand=True)
        Label(busmenu1, text="Date of Arrival/Departure: ", font=('calibre', 30, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(busmenu1, p, *dates).pack(side=TOP, fill=X, expand=True)
        Label(busmenu1, bg='black').pack(side=TOP)
        Label(busmenu1, bg='black').pack(side=TOP)
        Label(busmenu1, bg='black').pack(side=TOP)
        Button(busmenu1, text="Book", relief=RAISED,
               command=lambda: bus2(n.get(), m.get(), f, t, o.get(), p.get()),
               font=('calibre', 30, 'normal'), bg='white',
               fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X,
                                                                                 expand=True)
        Button(busmenu1, text="Go Back", relief=RAISED, command=lambda: back(3), font=('calibre', 30, 'normal'),
               bg='white', fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X,
                                                                                             expand=True)
    else:
        messagebox.showerror("ERROR", "Please ensure that pickup and drop point are selected.")


def bus2(ty, ws, f, t, nws, d):
    global User, busmenu2, smologo, icologo
    if ty and f and t and d and (ws or nws):
        bookedmsg = "You have successfully booked bus ticket/s from " + f + " to " + t + ".\nClick yes to download the ticket in form of text file."
        M = messagebox.askyesno("Success", bookedmsg)
        if M:
            des()
            create_folder(User)
            filename = "Tickets/"+ User + "/Bus-"+ whattime() + ".txt"
            with open(filename, "w+") as file:
                Fare, pnr, bno = str((150 * ws) + (100 * nws)), str(randint(1000000000, 9999999999)), str(
                    randint(100000, 999999))
                file.writelines(["Dear " + User + "!", "\nThank you for using BookMySeat's reservation facility!",
                                 "\nPNR No: " + pnr, "\nBus No: " + bno, "\nBus Type: " + ty,
                                 "\nNo of Window Seats booked: " + str(ws),
                                 "\tNo of Non-Window Seats booked: " + str(nws),
                                 "\nPickup Location: " + f + "\tDrop Location: " + t,
                                 "\nScheduled Arrival: " + d, "\nAmount to be paid: " + Fare])
                file.seek(0)
                filetext = file.read()
            busmenu2 = Tk()
            busmenu2.state('zoomed')
            busmenu2.title("Ticket")
            busmenu2.configure(bg="black")
            busmenu2.wm_iconbitmap(icologo)
            logo1 = ImageTk.PhotoImage(smologo, master=busmenu2)
            L1 = Label(busmenu2, image=logo1, borderwidth=0, highlightthickness=0)
            L1.image = logo1
            L1.pack(side=TOP)
            Label(busmenu2, text="TICKET", font=('calibre', 25, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(busmenu2, bg='black').pack(side=TOP)
            Label(busmenu2, text=filetext, font=('calibre', 20, 'normal'), fg='Black', bg='White').pack(side=TOP,
                                                                                                        fill=X)
            Label(busmenu2, bg='black').pack(side=TOP)
            Label(busmenu2, text="Ticket is saved in suitable directory with name: ",
                  font=('calibre', 25, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(busmenu2, text=filename, font=('calibre', 25, 'bold'), fg="Red", bg='black').pack(side=TOP, fill=X)
            Button(busmenu2, text="Done", relief=RAISED, command=lambda: back(3), font=('calibre', 30,
                                                                                        'normal'), bg='white',
                   fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
        else:
            back(3)
    else:
        messagebox.showerror("ERROR",
                             "Please ensure that all of the options are chosen and make sure either of the entries for no of seats are selected.")


def air():
    global airmenu, User, smologo, icologo
    des()
    airmenu = Tk()
    airmenu.state('zoomed')
    airmenu.title('BookMySeat - Flights')
    airmenu.configure(bg="black")
    airmenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=airmenu)
    L1 = Label(airmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    Label(airmenu, text="Flight Ticket Booking\n", font=('calibre', 40, 'bold'), fg='pink', bg='black').pack(side=TOP,
                                                                                                             fill=X)
    Button(airmenu, text="Domestic Flights ", relief=RAISED, command=lambda: air1('Domestic'),
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Button(airmenu, text="International Flights ", relief=RAISED, command=lambda: air1('International'),
           font=('calibre', 30, 'normal'), bg='plum1',
           fg='firebrick4', activebackground='pink', activeforeground='red').pack(side=TOP)
    Label(airmenu, bg='black').pack(side=TOP)
    Button(airmenu, text="Go Back", relief=RAISED, command=lambda: back(3),
           font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X, expand=True)


def air1(n):
    global airmenu1, User, smologo, icologo
    des()
    airmenu1 = Tk()
    airmenu1.state('zoomed')
    airmenu1.title('BookMySeat - Flights')
    airmenu1.configure(bg="black")
    airmenu1.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=airmenu1)
    L1 = Label(airmenu1, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    t = n + " Flight Ticket Booking\n"
    if n == 'International':
        airlist = flightlist
    else:
        airlist = trainlist
    Label(airmenu1, text=t, font=('calibre', 30, 'bold'), fg='pink', bg='black').pack(side=TOP, fill=X)
    m, o, p, q, d, ws, nws = StringVar(airmenu1), StringVar(airmenu1), StringVar(airmenu1), StringVar(
        airmenu1), StringVar(airmenu1), IntVar(airmenu1), IntVar(airmenu1)
    tempolist = [["Choose the airlines: ", m, flightbrand], ["Choose Class: ", o, flightclass], ["From: ", p, airlist],
                 ["To: ", q, airlist], ["Date: ", d, dates], ["No. of Window Seats: ", ws, nopass],
                 ["No. of Non-Window Seats: ", nws, nopass1]]
    for i in tempolist:
        Label(airmenu1, text=i[0], font=('calibre', 10, 'normal'), fg='white',
              bg='black').pack(side=TOP)
        OptionMenu(airmenu1, i[1], *i[2]).pack(side=TOP, fill=X, expand=True)
    Button(airmenu1, text="Book", relief=RAISED,
           command=lambda: air2(n, m.get(), o.get(), p.get(), q.get(), d.get(), ws.get(), nws.get()),
           font=('calibre', 20, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(airmenu1, text="Go Back", relief=RAISED, command=lambda: back(3), font=('calibre', 20, 'normal'),
           bg='white', fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def air2(n, m, o, p, q, d, ws, nws):
    global User, airmenu2, smologo, icologo
    if m and o and p and q and d and (ws or nws):
        bookedmsg = "You have successfully booked flight ticket/s from " + p + " to " + q + ".\nClick yes to download the ticket in form of text file."
        M = messagebox.askyesno("Success", bookedmsg)
        if M:
            des()
            create_folder(User)
            filename = "Tickets/"+ User + "/Air-"+ whattime() + ".txt"
            with open(filename, "w+") as file:
                Fare, gtno, fno = str(2000 + (1000 * ws) + (750 * nws)), str(randint(1, 20)), chr(
                    randrange(97, 97 + 26)) + "-" + str(randint(1000, 9999))
                if n == "International":
                    Fare = str(int(Fare) + 1750)
                file.writelines(["Dear " + User + "!", "\nThank you for using BookMySeat's reservation facility!",
                                 "\nSuccessfully booked a/an %s flight ticket" % n,
                                 "\nFlight No: " + fno, "\nGate No: " + gtno, "\nAirlines: " + m, "\nClass: " + o,
                                 "\nNo of Window Seats booked: " + str(ws),
                                 "\tNo of Non-Window Seats booked: " + str(nws),
                                 "\nOrigin: " + p + "\tDestination: " + q,
                                 "\nDate: " + d, "\nAmount to be paid: " + Fare])
                file.seek(0)
                filetext = file.read()
            airmenu2 = Tk()
            airmenu2.state('zoomed')
            airmenu2.title("Ticket")
            airmenu2.configure(bg="black")
            airmenu2.wm_iconbitmap(icologo)
            logo1 = ImageTk.PhotoImage(smologo, master=airmenu2)
            L1 = Label(airmenu2, image=logo1, borderwidth=0, highlightthickness=0)
            L1.image = logo1
            L1.pack(side=TOP)
            Label(airmenu2, text="TICKET", font=('calibre', 25, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(airmenu2, bg='black').pack(side=TOP)
            Label(airmenu2, text=filetext, font=('calibre', 15, 'normal'), fg='Black', bg='White').pack(side=TOP,
                                                                                                        fill=X)
            Label(airmenu2, bg='black').pack(side=TOP)
            Label(airmenu2, text="Ticket is saved in suitable directory with name: ",
                  font=('calibre', 25, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(airmenu2, text=filename, font=('calibre', 25, 'bold'), fg="Red", bg='black').pack(side=TOP, fill=X)
            Label(airmenu2, bg='black').pack(side=TOP, fill=X)
            Button(airmenu2, text="Done", relief=RAISED, command=lambda: back(3), font=('calibre', 30,
                                                                                        'normal'), bg='white',
                   fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
        else:
            back(3)
    else:
        messagebox.showerror("ERROR",
                             "Please ensure that all of the options are chosen and make sure either of the entries for no of seats are selected.")


def taxi():
    global taximenu, User, smologo, icologo
    des()
    taximenu = Tk()
    taximenu.state('zoomed')
    taximenu.title('BookMySeat - Cab')
    taximenu.configure(bg="black")
    taximenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=taximenu)
    L1 = Label(taximenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    n = StringVar(taximenu)
    Label(taximenu, text="Cab Booking\n", font=('calibre', 50, 'bold'), fg='pink', bg='black').pack(side=TOP, fill=X)
    Label(taximenu, bg='black').pack(side=TOP)
    Label(taximenu, text="Choose the vehicle: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    n.set('Auto - 2')
    OptionMenu(taximenu, n, *['Auto - 2', 'Mini - 4', 'SUV - 6', 'Rental - 5']).pack(side=TOP, fill=X, expand=True)
    Button(taximenu, text="Go Back", relief=RAISED, command=lambda: back(2), font=('calibre', 20, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=BOTTOM, fill=X)
    Button(taximenu, text="Book", relief=RAISED, command=lambda: taxi1(n.get()), font=('calibre', 20, 'normal'),
           bg='white', fg='black', activebackground='pink', activeforeground='red').pack(side=BOTTOM, fill=X)


def whattime():
    now = datetime.datetime.now()
    dt_string = now.strftime("%d-%B-%Y-%I-%M%p")
    return dt_string


def taxi1(cab):
    global User, cabmenu, smologo, icologo
    des()
    cabmenu = Tk()
    cabmenu.state('zoomed')
    cab1, cab = cab.rstrip(" -2465"), cab.rstrip(" -2465")
    cabmenu.title('BookMySeat - ' + cab)
    cabmenu.configure(bg="black")
    cabmenu.wm_iconbitmap(icologo)
    logo1 = ImageTk.PhotoImage(smologo, master=cabmenu)
    L1 = Label(cabmenu, image=logo1, borderwidth=0, highlightthickness=0)
    L1.image = logo1
    L1.pack(side=TOP)
    cab += " Menu"
    n, m = StringVar(cabmenu), StringVar(cabmenu)
    Label(cabmenu, text=cab, font=('calibre', 50, 'bold'), fg='pink',
          bg='black').pack(side=TOP, fill=X)
    Label(cabmenu, bg='black').pack(side=TOP)
    Label(cabmenu, bg='black').pack(side=TOP)
    Label(cabmenu, text="Choose the pickup point: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(cabmenu, n, *cablist).pack(side=TOP, fill=X)
    Label(cabmenu, bg='black').pack(side=TOP)
    Label(cabmenu, bg='black').pack(side=TOP)
    Label(cabmenu, text="Choose the drop point: ", font=('calibre', 30, 'normal'), fg='white',
          bg='black').pack(side=TOP)
    OptionMenu(cabmenu, m, *cablist).pack(side=TOP, fill=X)
    Label(cabmenu, bg='black').pack(side=TOP)
    Label(cabmenu, bg='black').pack(side=TOP)
    Button(cabmenu, text="Book", relief=RAISED, command=lambda: taxi2(cab1, n.get(), m.get()),
           font=('calibre', 30, 'normal'), bg='white', fg='black', activebackground='pink',
           activeforeground='red').pack(side=LEFT, fill=X, expand=True)
    Button(cabmenu, text="Go Back", relief=RAISED, command=lambda: back(3), font=('calibre', 30, 'normal'), bg='white',
           fg='black', activebackground='pink', activeforeground='red').pack(side=LEFT, fill=X, expand=True)


def taxi2(cab1, pickup, drop):
    global User, cabmenu1, color, suv, mini, smologo, icologo
    if pickup == drop:
        messagebox.showerror("ERROR", "Please ensure that pickup and drop point are different.")
    else:
        bookedmsg = "You have successfully booked a " + cab1 + " from " + pickup + " to " + drop + ".\nClick yes to download the ticket in form of text file."
        M = messagebox.askyesno("Success", bookedmsg)
        if M:
            des()
            create_folder(User)
            filename = "Tickets/"+ User + "/"+ cab1 + "-" + whattime() + ".txt"
            with open(filename, "w+") as file:
                Fare = "50"
                if cab1 != "Auto":
                    cab = choice(color)
                    if cab1 == "SUV":
                        cab = cab + " " + choice(suv)
                        Fare = "150"
                    else:
                        cab = cab + " " + choice(mini)
                        Fare = "120"
                    cab1 = cab
                file.writelines(
                    ["Pickup Location: " + pickup + "\nDrop Location: " + drop, "\nVehicle arriving soon: " + cab1,
                     "\nAmount to be paid: " + Fare])
                file.seek(0)
                file1 = file.read()
            cabmenu1 = Tk()
            cabmenu1.state('zoomed')
            cabmenu1.title("Ticket")
            cabmenu1.configure(bg="black")
            cabmenu1.wm_iconbitmap(icologo)
            logo1 = ImageTk.PhotoImage(smologo, master=cabmenu1)
            L1 = Label(cabmenu1, image=logo1, borderwidth=0, highlightthickness=0)
            L1.image = logo1
            L1.pack(side=TOP)
            Label(cabmenu1, text="TICKET", font=('calibre', 30, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(cabmenu1, bg='black').pack(side=TOP)
            Label(cabmenu1, text=file1, font=('calibre', 30, 'normal'), fg='Black', bg='White').pack(side=TOP, fill=X)
            Label(cabmenu1, bg='black').pack(side=TOP)
            Label(cabmenu1, bg='black').pack(side=TOP)
            Label(cabmenu1, text="Ticket is saved in suitable directory with name: ",
                  font=('calibre', 30, 'bold'), fg='White', bg='black').pack(side=TOP, fill=X)
            Label(cabmenu1, text=filename, font=('calibre', 30, 'bold'), fg="Red", bg='black').pack(side=TOP, fill=X)
            Label(cabmenu1, bg='black').pack(side=TOP, fill=X)
            Button(cabmenu1, text="Done", relief=RAISED, command=lambda: back(3), font=('calibre', 30,
                                                                                        'normal'), bg='white',
                   fg='black', activebackground='pink', activeforeground='red').pack(side=TOP, fill=X)
        else:
            back(3)


startup()
mainmenu1()
