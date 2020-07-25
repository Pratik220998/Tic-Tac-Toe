import turtle as x
import random as r
import sys
if sys.version_info[0]>2:
    import tkinter as tk
    from tkinter.simpledialog import askstring as askstring
    from tkinter.simpledialog import askinteger as askinteger
    from tkinter.messagebox import showerror as showerror
    from tkinter.messagebox import showinfo as showinfo
    from tkinter.messagebox import askyesno as askyesno
elif sys.version_info[0]<3:
    import Tkinter as tk
    from tkSimpleDialog import askstring as askstring
    from tkSimpleDialog import askinteger as askinteger
    from tkMessageBox import showerror as showerror
    from tkMessageBox import showinfo as showinfo
    from tkMessageBox import askyesno as askyesno


#(2) TKINTER AND TURTLE MODULE INITIALIZATION 
root=tk.Tk()
root.overrideredirect(1)
root.withdraw()
root.focus()
root.lift()


window = x.Screen()
window.screensize(1920, 1080)
window.setup(width=1.0, height=1.0, startx=None, starty=None)


#(3) GLOBAL VARIABLES DECLARATION
showinfo("WELCOME !","\t     WELCOME TO THE TIC-TAC-TOE GAME!\n\t    ")
void=None

choice=askinteger("CHOOSE YOUR OPPONENT!!","Would you like to play against SYSTEM or against a FRIEND?\n\n\tENTER \"1\" TO PLAY AGAINST YOUR FRIEND!\n\t\t             OR\n\t\"2\" TO PLAY AGAINT THE SYSTEM")
if choice!=1 and choice!=2:
    showerror("ERROR!","YOU HAVE CHOOSEN A WRONG RESPONSE!!\nYOU HAVE ONE MORE TRY TO CHOOSE THE RIGHT CHOICE OR THE GAME WILL QUIT BY DEFAULT!")
    choice=askinteger("CHOOSE YOUR OPPONENT!!","Would you like to play against SYSTEM or against a FRIEND?\n\n\tENTER \"2\" TO PLAY AGAINT THE SYSTEM\n\t\t             OR\n\t\"1\" TO PLAY AGAINST YOUR FRIEND!")
    if int(choice)!=1 and int(choice)!=2:
        showerror("ERROR!!","YOU HAVE INPUTTED THE WRONG OPTION TWICE!\n\tQUITTING GAME BY DEFAULT!\nKINDLY RESTART THE GAME AGAIN TO PLAY!")
        quit()
 

if choice==1:
    temp1=askstring("ENTER NAME!","ENTER THE NAME OF PLAYER 1 - ")
    temp2=askstring("ENTER NAME!","ENTER THE NAME OF PLAYER 2 - ")
    if type(temp1)==type(void) or type(temp2)==type(void):
        f=askyesno("ATTENTION!","YOU HAVE CHOSEN TO CANCEL THE GAME!\nDO YOU REALLY WANT TO END THE GAME?")
        if f==True:
            showinfo("THANK YOU!","THANK YOU FOR TRYING THE TIC-TAC-TOE GAME!")	
            quit()
        else:
            showinfo("ATTENTION!","THIS IS THE LAST CHANCE FOR ENTERING YOUR NAMES\nAND CONTINUING THE GAME!")
            temp1=askstring("ENTER NAME!","KINLDY ENTER THE NAME OF PLAYER 1 - ")
            temp2=askstring("ENTER NAME!","KINDLY ENTER THE NAME OF PLAYER 2 - ")
            if type(temp1)==type(void) or type(temp2)==type(void):
                showerror("ATTENTION!","YOU HAVE CHOSEN TO CANCEL THE GAME ABRUPTLY!\nQUITTING THE GAME BY DEFAULT!\nRESTART THE GAME TO PLAY AGAIN!")
                quit()
    while len(temp1)<1 and len(temp2)<1:
        showerror("ATTENTION!","Name of both players has to be at least one character long! Kindly re-enter! ")
        temp1=askstring("ENTER NAME!","KINLDY ENTER THE NAME OF PLAYER 1 - ")
        temp2=askstring("ENTER NAME!","KINDLY ENTER THE NAME OF PLAYER 2 - ")
    name1=temp1.upper();name2=temp2.upper()
    font_list=[12,24]
    font_size1=len(name1);font_size2=len(name2)
    if font_size1>8 or font_size2>8:
        Font=font_list[0]
    else:
        Font=font_list[1]
    showinfo("ATTENTION!","\t       %s VS %s\n\nKINDLY WAIT TILL THE GAME SETUP IS COMPLETED!"%(name1,name2))
elif choice==2:
    level="EASY"
    """
    quality=askinteger("CHOOSE LEVEL!","CHOOSE THE LEVEL OF HARDNESS OF THE GAME!\n\t1)ENTER \"1\" FOR 'EASY' LEVEL GAMES.\n\t2)ENTER \"2\" FOR 'HARD' LEVEL GAMES.")
    if quality==1:
        level="EASY"
    elif quality==2:
        level="HARD"
    else:
        showerror("WRONG INPUT!","PLEASE ENTER EITHER 1 or 2 ONLY!!\nTHIS IS THE LAST CHANCE TO ENTER THE CORRECT OPTION!")
        quality=askinteger("CHOOSE LEVEL!","CHOOSE THE LEVEL OF HARDNESS FOR THE GAME!\n\t1)ENTER \"1\" FOR 'EASY' LEVEL GAMES.\n\t2)ENTER \"2\" FOR 'HARD' LEVEL GAMES.")
        if quality==1:
            level="EASY"
        elif quality==2:
            level="HARD"
        else:
            showerror("WRONG INPUT!","YOU HAVE INPUTTED THE WRONG OPTION TWICE!\nQUITTING THE GAME BY DEFAULT!!")
    """
    temp1=askstring("ENTER NAME!","ENTER YOUR NAME - ")
    name1=temp1.upper()
    name2="SYSTEM"
    font_list=[12,24]
    font_size1=len(name1);
    if font_size1>8:
        Font=font_list[0]
    else:
        Font=font_list[1]
    showinfo("ATTENTION!","\t       %s VS %s\n\nKINDLY WAIT TILL THE GAME SETUPS FOR YOU!"%(name1,name2))


########################################################################################################################################################################

    
#(4) MAIN-CLASS BEGINS HERE
class ttt:
#INITIALIZING    
    def __init__(self,t=None,trial=0,game=0,check=0,change="INIT",count1=0,count2=0,game1=0,game2=0,Ngames=0,letter1="",letter2="",swap="",player1="",player2="",board=[],main=[],top=[],mid=[],bot=[],diag1=[],diag2=[],col1=[],col2=[],col3=[]):
        self.t=t;       
        self.trial=0;self.game=0;self.check=0;self.count1=0;self.count2=0;self.game1=0;self.game2=0;
        self.Ngames=0;self.change="INIT";
        self.letter1=letter1;self.letter2=letter2;self.swap=swap;self.player1=player1;self.player2=player2
        self.main=[];
        self.board=[i for i in range(1,10)]
        self.top=["-" for i in range(3)];
        self.mid=["-" for i in range(3)];
        self.bot=["-" for i in range(3)];
        self.col1=["-" for i in range(3)];
        self.col2=["-" for i in range(3)];
        self.col3=["-" for i in range(3)];
        self.diag1=["-" for i in range(3)];
        self.diag2=["-" for i in range(3)];
        self.scoreboard()



#MAKING THE SCOREBOARD        
    def scoreboard(self):
        self.t=x.clone()
        self.t.speed(10);self.t.pu();self.t.goto(300,300);self.t.pd();self.t.width(3)
        for i in range(2):
            self.t.fd(350);self.t.lt(90);self.t.fd(45);self.t.lt(90)
        self.t.fd(10)
        if choice==1:
            self.t.write(name1,font=("Ariel",Font,"bold"))
            self.t.fd(165);self.t.lt(90);self.t.fd(45);self.t.bk(45);self.t.rt(90);self.t.fd(10)
            self.t.write(name2,font=("Ariel",Font,"bold"))
        elif choice==2:
            self.t.write(name1,font=("Ariel",Font,"bold"))
            self.t.fd(165);self.t.lt(90);self.t.fd(45);self.t.bk(45);self.t.rt(90);self.t.fd(10)
            self.t.write(name2,font=("Ariel",Font,"bold"))
        self.t.goto(300,300);self.t.goto(300,-300);self.t.goto(650,-300);self.t.goto(650,300);self.t.goto(475,300);self.t.goto(475,-210)
        self.t.pu()
        self.t.goto(300,-250)
        self.t.pd()
        self.t.fd(350);self.t.bk(350);self.t.fd(10)
        self.t.write("TOTAL SCORE - ",font=("Ariel",24,"bold"))
        self.t.bk(10)
        self.t.goto(300,-210);self.t.goto(650,-210)
        self.t.pu()
        self.t.goto(475,-250)
        self.t.pd()
        self.t.goto(475,-300)
        self.t.pu()
        self.t.goto(300,250)
        self.t.ht()
        showinfo("\t\tRULES!","Here are the rules and info of playing the game - \n\n1.)The basic rules of Tic-Tac-Toe apply in this game too (consecutive X or 0 thrice in a row, column or diagonals to win).\n\n2.)Type the number of the place where you want to place your X or 0 (eg: type 1 to make an X in first place in the tic-tac-toe set-up)\n\n3.) The game will be considered a TIE only if all the 9 boxes are filled.\n\n4.)Click on cancel option on pop-up boxes to quit the game!\n\n\t\tTHAT'S ALL!! BEST OF LUCK IN THE GAME!")
        self.Ngames=askinteger("No. of Games?","How many games would you like to?\n(Note : Choose from the range 1 to 10 only!)")
        if type(self.Ngames)==type(void):
            a=askyesno("ATTENTION!","DO YOU REALLY WANT TO QUIT RIGHT NOW?")
            if a==True:
                self.score()
            elif a==False:
                showinfo("ATTENTION!","CONTINUING THE GAME FROM WHERE WE LEFT\nTHIS IS THE LAST TRY TO CHOOSE NUMBER OF GAMES - ")
                self.Ngames=askinteger("No. of Games?","How many games would you like to?\n(Note : Choose from the range 1 to 10 only!)")
                if type(self.Ngames)==type(void):
                    showerror("ATTENTION!","QUITTING THE GAME SINCE YOU HAVE CHOSEN TO PRESS CANCEL TWICE ABRUPTLY!")
                    quit()	
        while self.Ngames<1 or self.Ngames>10:
            showerror("ERROR!","WRONG INPUT TRY AGAIN!")
            self.Ngames=askinteger("No. of Games?","How many games would you like to play?\n(Note : Choose from the range 1 to 10 only!)")	
        self.ttt_board()



#MAKING THE TTT BOARD         
    def ttt_board(self):
        x.clear();x.color("black")
        x.home();x.width(5);x.pu()
        #SETTING UP HORIZONTAL LINES 
        x.speed(10);
        x.goto(-300,0);x.pd();x.color("green");x.write("1",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220,0);x.fd(5);x.color("green");x.write("2",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220+80,0);x.fd(5);x.color("green");x.write("3",font=("Ariel",8,"italic"));x.color("black")
        x.goto(-220+80+80,0);x.pu()
        x.goto(-300,-80);x.pd();x.color("green");x.write("4",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220,-80);x.fd(5);x.color("green");x.write("5",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220+80,-80);x.fd(5);x.color("green");x.write("6",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220+80+80,-80);x.pu()
        x.goto(-300,-80-80);
        x.goto(-230,-80-80);x.color("green");x.write("7",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220,-80-80);x.fd(5);x.color("green");x.write("8",font=("Ariel",8,"italic"));x.color("black");
        x.goto(-220+80,-80-80);x.fd(5);x.color("green");x.write("9",font=("Ariel",8,"italic"));x.color("black");
        #SETTING UP VERTICAL LINES
        x.pu()
        x.goto(-220,80);x.pd();x.goto(-220,-80-80);x.pu()
        x.goto(-220+80,80);x.pd();x.goto(-220+80,-80-80)
        x.ht();
        #x.done()
        self.input()


#RESETTING THE TTT BOARD
    def reset(self):	
        x.reset()
        self.ttt_board()


#CHOOSING X OR 0        
    def input(self):
        void=None
        if choice==1:
            self.main=[i for i in range(1,10)]
            self.top=["-" for i in range(3)];
            self.mid=["-" for i in range(3)];
            self.bot=["-" for i in range(3)];
            self.col1=["-" for i in range(3)];
            self.col2=["-" for i in range(3)];
            self.col3=["-" for i in range(3)];
            self.diag1=["-" for i in range(3)];
            self.diag2=["-" for i in range(3)];
            if self.change=="INIT":
                pass;
            choose=[name1,name2,name1,name2,name1,name2,name1,name2,name1,name2]       
            r.shuffle(choose)
            self.c=r.choice(choose)
            showinfo("ATTENTION!","THE GAME IS GOING TO RANDOMLY SELECT THE FIRST PLAYER TO MOVE RIGHT NOW, AFTER THIS EACH PLAYER WILL GET CHANCE ALTERNATIVELY!!")
            showinfo("FIRST PLAYER CHOSEN IS - !","THE GAME HAS RANDOMLY SELECTED THE FIRST PLAYER TO MOVE AND THE FIRST PLAYER IS - \n\n\t\t%s"%(self.c))
            #NAME 1 INITIALIZATION
            if self.c==name1:
                self.player1=self.c
                self.player2=name2
            #NAME 2 INITIALIZATION    
            elif self.c==name2:
                self.player1=self.c
                self.player2=name1
            self.letter1=askstring("\tX OR 0?","%s would you like to pick \"X or x\" or \"0\"?? \n\n(Note - Please pick number \"0\" {zero} not letter \"O\")"%(self.c))
            if type(self.letter1)==type(void):
                a=askyesno("ATTENTION!","DO YOU REALLY WANT TO QUIT RIGHT NOW?")
                if a==True:
                    self.score()
                elif a==False:
                    showinfo("ATTENTION!","CONTINUING THE GAME FROM WHERE WE LEFT.\n(i.e., choosing a player randomly to move first!)")
                    self.input()
            if self.letter1.upper()=="X":
                self.letter2="0".upper()			
                showinfo("ATTENTION!","%s is \"%s\" (obviously)"%(self.player2,self.letter2))
            if self.letter1=="0":
                self.letter2="X".upper()
                showinfo("ATTENTION!","%s is \"%s\" (obviously)"%(self.player2,self.letter2))
            while self.letter1.upper()!="X" and self.letter1.upper()!="0":
                showerror("\tERROR!","YOU HAVE PICKED UP THE WRONG INPUT! YOU HAVE ONE LAST TRY TO PICK THE RIGHT CHOICE!!")
                self.letter1=askstring("\tX OR 0?","%s would you like to pick \"X/x\" or \"0\"?? \n\n(Note - Please pick number \"0\" {zero} not letter \"O\")"%(self.c))
                if self.letter1.upper()=="X":
                    self.letter2="0"
                    showinfo("ATTENTION!","%s, YOU ARE \"0\" (obviously)"%(self.player2))
                elif self.letter1=="0":
                    self.letter2="X"
                    showinfo("ATTENTION!","%s, YOU ARE \"X\" (obviously)"%(self.player2))
                else:
                    showerror("ERROR!!","YOU HAVE ENTERED WRONG INPUT TWICE! QUITTING THE GAME BY DEFAULT!")
                    self.score()
            self.letter1=self.letter1.upper()
            self.play_with_friend1()
        if choice==2:
            self.main=[i for i in range(1,10)]
            self.top=["-" for i in range(3)];
            self.mid=["-" for i in range(3)];
            self.bot=["-" for i in range(3)];
            self.col1=["-" for i in range(3)];
            self.col2=["-" for i in range(3)];
            self.col3=["-" for i in range(3)];
            self.diag1=["-" for i in range(3)];
            self.diag2=["-" for i in range(3)];
            choose=[name1,name2,name1,name2,name1,name2,name1,name2,name1,name2]       
            r.shuffle(choose)
            self.c=r.choice(choose)
            showinfo("ATTENTION!","THE GAME IS GOING TO RANDOMLY SELECT THE FIRST PLAYER TO MOVE RIGHT NOW!")
            showinfo("FIRST PLAYER CHOSEN IS - !","THE GAME HAS RANDOMLY SELECTED THE FIRST PLAYER TO MOVE AND THE FIRST PLAYER IS - \n\n\t\t%s"%(self.c))
            #NAME 1 INITIALIZATION
            if self.c==name1:
                self.player1=name1
                self.player2=name2
                self.letter1=askstring("\tX OR 0?","%s would you like to pick \"X or x\" or \"0\"?? \n\n(Note - Please pick number \"0\" {zero} not letter \"O\")"%(self.c))
                self.letter1=self.letter1.upper()
                if type(self.letter1)==type(void):
                    a=askyesno("ATTENTION!","DO YOU REALLY WANT TO QUIT RIGHT NOW?")
                    if a==True:
                        self.score()
                    elif a==False:
                        showinfo("ATTENTION!","CONTINUING THE GAME FROM WHERE WE LEFT.\n(i.e., choosing a player randomly to move first!)")
                        self.input()
                if self.letter1.upper()=="X":
                    self.letter2="0"			
                    showinfo("ATTENTION!","%s is \"%s\" (obviously)"%(self.player2,self.letter2))
                if self.letter1=="0":
                    self.letter2="X"
                    showinfo("ATTENTION!","%s is \"%s\" (obviously)"%(self.player2,self.letter2))
                while self.letter1.upper()!="X" and self.letter1.upper()!="0":
                    showerror("\tERROR!","YOU HAVE PICKED UP THE WRONG INPUT! YOU HAVE ONE LAST TRY TO PICK THE RIGHT CHOICE!!")
                    self.letter1=askstring("\tX OR 0?","%s would you like to pick \"X/x\" or \"0\"?? \n\n(Note - Please pick number \"0\" {zero} not letter \"O\")"%(self.c))
                    if self.letter1.upper()=="X":
                        self.letter2="0"
                        showinfo("ATTENTION!","%s, YOU ARE \"0\" (obviously)"%(self.player2))
                    elif self.letter1=="0":
                        self.letter2="X"
                        showinfo("ATTENTION!","%s, YOU ARE \"X\" (obviously)"%(self.player2))
                    else:
                        showerror("ERROR!!","YOU HAVE ENTERED WRONG INPUT TWICE! QUITTING THE GAME BY DEFAULT!")
                        self.score()
                self.play_with_friend1()
            #NAME 2 INITIALIZATION    
            elif self.c==name2:
                self.main=[i for i in range(1,10)]
                self.top=["-" for i in range(3)];
                self.mid=["-" for i in range(3)];
                self.bot=["-" for i in range(3)];
                self.col1=["-" for i in range(3)];
                self.col2=["-" for i in range(3)];
                self.col3=["-" for i in range(3)];
                self.diag1=["-" for i in range(3)];
                self.diag2=["-" for i in range(3)];
                meh=["X","0","X","0","X","0","X","0"]
                r.shuffle(meh)
                self.player1=name1
                self.player2=name2
                self.letter2=r.choice(meh)
                showinfo("SYSTEM CHOSE!","THE SYSTEM HAS CHOSEN -> %s"%(self.letter2))
                if self.letter2=="X":
                    self.letter1="0"			
                    showinfo("ATTENTION!","%s is \"%s\" (obviously)"%(self.player1,self.letter1))
                if self.letter2=="0":
                    self.letter1="X"
                    showinfo("ATTENTION!","%s is \"%s\" (obviously)"%(self.player1,self.letter1))
                self.play_with_sys()
        


#MOVING POSITIONS OF X OR 0 ON THE TTT BOARD            
    def p1(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-280,20);x.pd();x.goto(-240,60);x.pu();x.goto(-280,60);x.pd();x.goto(-240,20);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-260,20);x.pd();x.circle(20);x.ht()
        x.pu()
    def p2(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-200,20);x.pd();x.goto(-160,60);x.pu();x.goto(-200,60);x.pd();x.goto(-160,20);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-180,20);x.pd();x.circle(20);x.ht()
        x.pu()
    def p3(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-120,20);x.pd();x.goto(-80,60);x.pu();x.goto(-120,60);x.pd();x.goto(-80,20);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-100,20);x.pd();x.circle(20);x.ht()
        x.pu()
    def p4(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-280,-60);x.pd();x.goto(-240,-20);x.pu();x.goto(-280,-20);x.pd();x.goto(-240,-60);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-260,-60);x.pd();x.circle(20);x.ht()
        x.pu()
    def p5(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-200,-60);x.pd();x.goto(-160,-20);x.pu();x.goto(-200,-20);x.pd();x.goto(-160,-60);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-180,-60);x.pd();x.circle(20);x.ht()
        x.pu()
    def p6(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-120,-60);x.pd();x.goto(-80,-20);x.pu();x.goto(-120,-20);x.pd();x.goto(-80,-60);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-100,-60);x.pd();x.circle(20);x.ht()
        x.pu()
    def p7(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-280,-140);x.pd();x.goto(-240,-100);x.pu();x.goto(-280,-100);x.pd();x.goto(-240,-140);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-260,-140);x.pd();x.circle(20);x.ht()
        x.pu()
    def p8(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-200,-140);x.pd();x.goto(-160,-100);x.pu();x.goto(-200,-100);x.pd();x.goto(-160,-140);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-180,-140);x.pd();x.circle(20);x.ht()
        x.pu()
    def p9(self):
        if self.swap=="X":
            x.speed(10);x.color("red");x.width(2)
            x.pu();x.goto(-120,-140);x.pd();x.goto(-80,-100);x.pu();x.goto(-120,-100);x.pd();x.goto(-80,-140);x.ht()
        else:
            x.speed(20);x.color("blue");x.width(2)
            x.pu();x.goto(-100,-140);x.pd();x.circle(20);x.ht()
        x.pu()


#POSITION OF TURTLE ON THE SCOREBOARD
    #VERTICALLY MOVES UP AND DOWN THE SCOREBOARD AND INITIATES -> SELF.points FUNCTION 
    def pos(self):
        self.t.pu()
        self.t.color("gray")
        if self.game==1:
            self.t.goto(300,250)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==2:
            self.t.goto(300,200)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==3:
            self.t.goto(300,150)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==4:
            self.t.goto(300,100)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==5:
            self.t.goto(300,50)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==6:
            self.t.goto(300,0)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==7:
            self.t.goto(300,-50)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==8:
            self.t.goto(300,-100)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==9:
            self.t.goto(300,-150)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()
        elif self.game==10:
            self.t.goto(300,-200)
            if self.check==1:
                self.points()
            elif self.check==0:
                self.tie()



#WIN THE GAME ->            
    def win(self):
        c1="red"
        c2="blue"
    #TOP CASES!!
        #TOP ROW IS ALL "X"
        if self.top[0]=="X" and self.top[1]=="X" and self.top[2]=="X":       			
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                elif self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #TOP ROW IS ALL "0"
        elif self.top[0]=="0" and self.top[1]=="0" and self.top[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - X AND LOSSES			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #MID CASES!!
        #MID ROW IS ALL "X"
        if self.mid[0]=="X" and self.mid[1]=="X" and self.mid[2]=="X":       
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #MID ROW IS ALL "0"
        elif self.mid[0]=="0" and self.mid[1]=="0" and self.mid[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - X AND LOSES)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-40);x.pd();x.goto(-70,-40);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #BOTTOM CASES!!
        #BOTTOM ROW IS ALL "X"
        if self.bot[0]=="X" and self.bot[1]=="X" and self.bot[2]=="X":       
            self.main=[];self.check=1;self.game+=1;
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-290,40);x.pd();x.goto(-70,40);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #BOTTOM ROW IS ALL "0"                
        elif self.bot[0]=="0" and self.bot[1]=="0" and self.bot[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()	
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))		
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - X AND LOSSES)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-290,-120);x.pd();x.goto(-70,-120);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #COLUMN 1 CASES!!
        #COLUMN-1 IS ALL "X"
        if self.col1[0]=="X" and self.col1[1]=="X" and self.col1[2]=="X":       
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #COLUMN-1 IS ALL "0"
        elif self.col1[0]=="0" and self.col1[1]=="0" and self.col1[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()	
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))		
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - X AND LOSES)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-260,70);x.pd();x.goto(-260,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #COLUMN 2 CASES
        #COLUMN-2 IS ALL "X"
        if self.col2[0]=="X" and self.col2[1]=="X" and self.col2[2]=="X":       
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #COLUMN-2 ROW IS ALL "0"
        elif self.col2[0]=="0" and self.col2[1]=="0" and self.col2[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-180,70);x.pd();x.goto(-180-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - 0 AND WINS)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-180,70);x.pd();x.goto(-180,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #COLUMN 3 CASES
        #COLUMN-3 IS ALL "X"
        if self.col3[0]=="X" and self.col3[1]=="X" and self.col3[2]=="X":       
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-100,70);x.pd();x.goto();x.ht-100,-150()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #COLUMN-3 IS ALL "0"
        elif self.col3[0]=="0" and self.col3[1]=="0" and self.col3[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - 0 AND WINS)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-100,70);x.pd();x.goto(-100,-150);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #DIAGONAL 1 CASES
        #DIAGONAL-1 IS ALL "X"
        if self.diag1[0]=="X" and self.diag1[1]=="X" and self.diag1[2]=="X":       
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))	
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #DIAGONAL-1 IS ALL "0"
        elif self.diag1[0]=="0" and self.diag1[1]=="0" and self.diag1[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()		
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))		
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - 0 AND WINS)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-300,80);x.pd();x.goto(-60,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
    #DIAGONAL 2 CASES
        #DIAGONAL-2 IS ALL "X"
        if self.diag2[0]=="X" and self.diag2[1]=="X" and self.diag2[2]=="X":       
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:                  
                if self.letter1=="X":		#NAME 1 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND LOSES			(NAME 2 WINS WITH X)	
                    x.width(4);x.color(c1);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		
                if self.letter1=="X":		#NAME 2 PICKS - X AND WINS
                    x.width(4);x.color(c1);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND LOSSES			(NAME 1 WINS WITH X)
                    x.width(4);x.color(c1);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();
        #DIAGONAL-2 IS ALL "0"
        elif self.diag2[0]=="0" and self.diag2[1]=="0" and self.diag2[2]=="0":     
            self.main=[];self.check=1;self.game+=1
            if self.player1==name1:			                  
                if self.letter1=="0":		#NAME 1 PICKS - 0 AND WINS
                    x.width(4);x.color(c2);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()	
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))		
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                elif self.letter1=="X":		#NAME 1 PICKS - X AND LOSSES			(NAME 2 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))				
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                self.pos();
            elif self.player1==name2:		 
                if self.letter1=="0":		#NAME 2 PICKS - 0 AND WINS			(
                    x.width(4);x.color(c2);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player1),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player1,self.player1,self.player2))			
                    self.game1="0"
                    self.game2="1"
                    self.count2+=1
                if self.letter1=="X":		#NAME 2 PICKS - 0 AND WINS)			(NAME 1 WINS WITH 0)
                    x.width(4);x.color(c2);x.pu();x.goto(-60,80);x.pd();x.goto(-300,-160);x.ht()
                    showinfo("%s WON!"%(self.player2),"THE WINNER IS -> %s!!\n\n%s got 1 point while %s got 0 point"%(self.player2,self.player2,self.player1))
                    self.game1="1"
                    self.game2="0"
                    self.count1+=1
                self.pos();



#TIE GAME ->
    def tie(self):
        showinfo("ATTENTION!","THIS GAME SESSION IS A points. BOTH %s AND %s SCORE A ZERO (0)"%(self.player1,self.player2))
        self.t.pu();self.t.fd(75);self.t.pd();self.t.write("0",font=("Ariel",24,"bold"));
        self.t.pu();self.t.fd(175);self.t.pd();self.t.write("0",font=("Ariel",24,"bold"));self.t.pu()
        self.new_game()



#POINTS - MAIN SCOREBOARD FUNCTION IF ANY PLAYER WINS
    def points(self):                           #self.game1 -> Name1 scores a point
        self.t.speed(5)                         #self.game2 -> Name2 scores a point
        self.t.pu();self.t.fd(75);self.t.pd;self.t.write(self.game1,font=("Ariel",24,"bold"));self.t.pu();self.t.fd(175);self.t.pd();self.t.write(self.game2,font=("Ariel",24,"bold"));self.t.pu()        
        self.new_game()                         #self.count1 & self.count2 -> Total scoreS of Name1 and Name2



#NEW GAME OR NOT
    def new_game(self):
        if self.game%2==0:
            self.change=True;
        else:
            self.change=False;
        if self.game==self.Ngames:
            self.score()
        if self.game!=10:
            q=askyesno("ATTENTION!","DO YOU WANT TO PLAY A NEW GAME ?")
            if q==True:
                showinfo("ATTENTION!","NEW GAME IS ABOUT TO START!")
                self.reset()
            else:
                self.score()



#FINAL SCORE OF PARTICIPANTS                
    def score(self):                
        if self.game==0:
            showerror("ATTENTION!","YOU HAVEN'T PLAYED ANY GAME! THE FINAL SCORE IS - \n\n\tZERO!\n\n\tFor both the players!")
            quit()
        if self.game==self.Ngames:
            self.t.pu();self.t.color("red");self.t.goto(300,-295);self.t.fd(75);self.t.pd();self.t.write(self.count1,font=("Ariel",24,"bold"));
            self.t.pu();self.t.fd(175);self.t.pd();self.t.write(self.count2,font=("Ariel",24,"bold"));
            if self.count1>self.count2:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\n%s is the winner!!\n\nThe number of total moves taken to win : %s"%(self.player1,str(self.count1),self.player2,str(self.count2),name1,self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            elif self.count2>self.count1:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\n%s is the winner!!\n\nThe number of total moves taken to win : %s"%(self.player1,str(self.count1),self.player2,str(self.count2),name2,self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            elif self.count1==self.count2:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\nThe match is a draw (%s-%s).\n\nThe number of total moves taken : %s\n\nBETTER LUCK NEXT TIME!"%(self.player1,str(self.count1),self.player2,str(self.count2),str(self.count1),str(self.count2),self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            quit()	
        if self.game==10:
            self.t.pu();self.t.color("red");self.t.goto(300,-295);self.t.fd(75);self.t.pd();self.t.write(self.count1,font=("Ariel",24,"bold"));
            self.t.pu();self.t.fd(175);self.t.pd();self.t.write(self.count2,font=("Ariel",24,"bold"));
            if self.count1>self.count2:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\n%s is the winner!!\n\nThe number of total moves taken to win : %s"%(self.player1,str(self.count1),self.player2,str(self.count2),name1,self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            elif self.count2>self.count1:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\n%s is the winner!!\n\nThe number of total moves taken to win : %s"%(self.player1,str(self.count1),self.player2,str(self.count2),name2,self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            elif self.count1==self.count2:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\nThe match is a draw (%s-%s).\n\nThe number of total moves taken : %s\n\nBETTER LUCK NEXT TIME!"%(self.player1,str(self.count1),self.player2,str(self.count2),str(self.count1),str(self.count2),self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            quit()
        else:
            self.t.pu();self.t.color("red");self.t.goto(300,-295);self.t.fd(75);self.t.pd();self.t.write(self.count1,font=("Ariel",24,"bold"));
            self.t.pu();self.t.fd(175);self.t.pd();self.t.write(self.count2,font=("Ariel",24,"bold"));
            if self.count1>self.count2:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\n%s is the winner!!\n\nThe number of total moves taken to win : %s"%(self.player1,str(self.count1),self.player2,str(self.count2),name1,self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            elif self.count2>self.count1:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\n%s is the winner!!\n\nThe number of total moves taken to win : %s"%(self.player1,str(self.count1),self.player2,str(self.count2),name2,self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            elif self.count1==self.count2:
                showinfo("FINAL RESULTS!","%s scored : %s\nwhile %s scored : %s.\n\nThe match is a draw (%s-%s).\n\nThe number of total moves taken : %s\n\nBETTER LUCK NEXT TIME!"%(self.player1,str(self.count1),self.player2,str(self.count2),str(self.count1),str(self.count2),self.trial))
                showinfo("THANK YOU!","THANK YOU FOR PLAYING THE TIC-TAC-TOE GAME!")
            quit()	



#PLAYER 1 MOVES            
    def play_with_friend1(self):
        void=None           #pos1 = positions that PLAYER 1 choses.
        self.check=0
        while self.main!=[]:
            key1=1
            self.trial+=1
            while key1!=0:
                pos1=askinteger("MOVE : %d"%(self.trial),"%s, Kindly choose where you want to place \"%s\" - "%(self.player1,self.letter1))
                self.swap=self.letter1
                try:
                    if type(pos1)!=int:
                        Quit=askyesno("ATTENTION!","DO YOU REALLY WANT TO QUIT?")
                        if Quit==True:
                            showinfo("THANK YOU!","THANK YOU FOR PLAYING WITH US!\nQUITTING THE GAME AS PER YOUR REQUEST!")
                            self.score()
                        else:
                            if type(pos1)==type(void):
                                self.play_with_friend1()
                            else:
                                self.main.remove(pos1)
                    else:
                        self.main.remove(pos1)
                    if pos1==1:
                        self.p1()
                        self.top[0]=self.swap
                        self.col1[0]=self.swap
                        self.diag1[0]=self.swap
                        self.win()
                        break
                    elif pos1==2:           
                        self.p2()
                        self.top[1]=self.swap
                        self.col2[0]=self.swap
                        self.win()
                        break
                    elif pos1==3:
                        self.p3()
                        self.top[2]=self.swap
                        self.col3[0]=self.swap
                        self.diag2[0]=self.swap
                        self.win()
                        break
                    elif pos1==4:       
                        self.p4()
                        self.mid[0]=self.swap
                        self.col1[1]=self.swap
                        self.win()
                        break
                    elif pos1==5:
                        self.p5()
                        self.mid[1]=self.swap
                        self.col2[1]=self.swap
                        self.diag1[1]=self.swap
                        self.diag2[1]=self.swap
                        break
                    elif pos1==6:       
                        self.p6()
                        self.mid[2]=self.swap
                        self.col3[1]=self.swap
                        self.win()
                        break
                    elif pos1==7:
                        self.p7()
                        self.bot[0]=self.swap
                        self.col1[2]=self.swap
                        self.diag2[2]=self.swap
                        self.win()
                        break
                    elif pos1==8:       
                        self.p8()
                        self.bot[1]=self.swap
                        self.col2[2]=self.swap
                        self.win()
                        break
                    elif pos1==9:
                        self.p9()
                        self.bot[2]=self.swap
                        self.col3[2]=self.swap
                        self.diag1[2]=self.swap
                        self.win()
                        break
                except ValueError:
                    showerror("ERROR!","WRONG INPUT!\nPOSITION - %d is either already occupied OR out of range from 1 to 9!\nPLEASE TRY AGAIN! - "%(pos1))
            if self.main==[] and self.check==0:
                self.game+=1
                self.pos()
            else:
                if choice==1:
                    self.play_with_friend2()
                elif choice==2:
                    self.play_with_sys()




#PLAYER 2 MOVES                
    def play_with_friend2(self):
        void=None           #pos2 = positions that PLAYER 2 choses.
        self.check=0
        while self.main!=[]:
            key2=1
            while key2!=0:
                self.trial+=1
                pos2=askinteger("MOVE : %d"%(self.trial),"%s, Kindly choose where you want to place \"%s\" - "%(self.player2,self.letter2))
                self.swap=self.letter2
                try:
                    if type(pos2)!=int:
                        Quit=askyesno("ATTENTION!","DO YOU REALLY WANT TO QUIT?")
                        if Quit==True:
                            showinfo("THANK YOU!","THANK YOU FOR PLAYING WITH US!\nQUITTING THE GAME AS PER YOUR REQUEST!")
                            self.score()
                        else:
                            if type(pos2)==type(void):
                                self.play_with_friend2()
                            else:        
                                self.main.remove(pos2)
                    else:
                        self.main.remove(pos2)
                    if pos2==1:
                        self.p1()
                        self.top[0]=self.swap
                        self.col1[0]=self.swap
                        self.diag1[0]=self.swap
                        self.win()
                        break
                    elif pos2==2:       
                        self.p2()
                        self.top[1]=self.swap
                        self.col2[0]=self.swap
                        self.win()
                        break
                    elif pos2==3:
                        self.p3()
                        self.top[2]=self.swap
                        self.col3[0]=self.swap
                        self.diag2[0]=self.swap
                        self.win()
                        break
                    elif pos2==4:       
                        self.p4()
                        self.mid[0]=self.swap
                        self.col1[1]=self.swap
                        self.win()
                        break
                    elif pos2==5:
                        self.p5()
                        self.mid[1]=self.swap
                        self.col2[1]=self.swap
                        self.diag1[1]=self.swap
                        self.diag2[1]=self.swap
                        self.win()
                        break
                    elif pos2==6:       
                        self.p6()
                        self.mid[2]=self.swap
                        self.col3[1]=self.swap
                        self.win()
                        break
                    elif pos2==7:       
                        self.p7()
                        self.bot[0]=self.swap
                        self.col1[2]=self.swap
                        self.diag2[2]=self.swap
                        self.win()
                        break
                    elif pos2==8:       
                        self.p8()
                        self.bot[1]=self.swap
                        self.col2[2]=self.swap
                        self.win()
                        break
                    elif pos2==9:
                        self.p9()
                        self.bot[2]=self.swap
                        self.col3[2]=self.swap
                        self.diag1[2]=self.swap
                        self.win()
                        break
                except ValueError:
                    showerror("ERROR!","WRONG INPUT!\nPOSITION - %d is either already occupied OR out of range from 1 to 9!\nPLEASE TRY AGAIN! - "%(pos2))
            if self.main==[] and self.check==0:
                self.game+=1
                self.pos()
            else:               
                self.play_with_friend1()


    def play_with_sys(self):
        self.check=0
        void=None
        pos2=self.player2;
        if level=="EASY":
            while self.main!=[]:
                key2=1
                while key2!=0:
                    self.trial+=1
                    r.shuffle(self.main)
                    pos2=r.choice(self.main)
                    showinfo("MOVE : %d"%(self.trial),"THE SYSTEM HAS CHOSEN TO MOVE AT POSITION -> %d"%(pos2))
                    self.swap=self.letter2
                    self.main.remove(pos2)
                    if pos2==1:
                        self.p1()
                        self.top[0]=self.swap
                        self.col1[0]=self.swap
                        self.diag1[0]=self.swap
                        self.win()
                        break
                    elif pos2==2:       
                        self.p2()
                        self.top[1]=self.swap
                        self.col2[0]=self.swap
                        self.win()
                        break
                    elif pos2==3:
                        self.p3()
                        self.top[2]=self.swap
                        self.col3[0]=self.swap
                        self.diag2[0]=self.swap
                        self.win()
                        break
                    elif pos2==4:       
                        self.p4()
                        self.mid[0]=self.swap
                        self.col1[1]=self.swap
                        self.win()
                        break
                    elif pos2==5:
                        self.p5()
                        self.mid[1]=self.swap
                        self.col2[1]=self.swap
                        self.diag1[1]=self.swap
                        self.diag2[1]=self.swap
                        self.win()
                        break
                    elif pos2==6:       
                        self.p6()
                        self.mid[2]=self.swap
                        self.col3[1]=self.swap
                        self.win()
                        break
                    elif pos2==7:       
                        self.p7()
                        self.bot[0]=self.swap
                        self.col1[2]=self.swap
                        self.diag2[2]=self.swap
                        self.win()
                        break
                    elif pos2==8:       
                        self.p8()
                        self.bot[1]=self.swap
                        self.col2[2]=self.swap
                        self.win()
                        break
                    elif pos2==9:
                        self.p9()
                        self.bot[2]=self.swap
                        self.col3[2]=self.swap
                        self.diag1[2]=self.swap
                        self.win()
                        break
                if self.main==[] and self.check==0:
                    self.game+=1
                    self.pos()
                else:               
                    self.play_with_friend1()
        


        
#(5) END
ttt()
x.done()
window.bye()


"""
window.exitonclick()==True:
	window.bye()
	quit()
"""