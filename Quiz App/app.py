from tkinter import *
import requests
from PIL import Image, ImageTk


n = 1  
points = 0
answers = []

def proceed():
   
    root.destroy()

    global category
    category = Tk()
    category.geometry("680x430")
    category.minsize(680,430)
    category.maxsize(680,430)
    category.title("Category")

    Label(category,text="Choose the Category for the Quiz:",font="comicsansms 25 bold",bg="bisque").grid(row=0,column=1,columnspan=2,pady=10)

    global var
    var = StringVar()
    var.set("9")

    global categ
    categ = ["General Knowledge","Entertainment: Books","Entertainment: Film","Entertainment: Music","Entertainment: Musicals and Theaters","Entertainment: Television","Entertainment: Video Games","Entertainment: Board Games","Science and Nature","Science: Computers","Science: Mathematics","Mythology","Sports","Geography","History","Politics","Art","Celebrities","Animals","Vehicles","Entertainment: Comics","Science: Gadgets","Entertainment: Japanese Anime and Manga","Entertainment: Cartoons and Animations"]

    for i in range(24):
        if(i%2 == 0):
            k = int(i/2)
            Radiobutton(category,text=f"{categ[i]}",padx=14,variable=var,value=i+9,bg="bisque").grid(row=k+1,column=1,sticky=W,padx=10)
        else:
            k = int(i/2)
            Radiobutton(category,text=f"{categ[i]}",padx=14,variable=var,value=i+9,bg="bisque").grid(row=k+1,column=2,sticky=W,padx=10)



    Button(category,text="Go Back",command=restart,pady=5,padx=3).grid(row=18,column=1,sticky=S,pady=20)
    Button(category,text="Go Next",command=submit,pady=5,padx=3).grid(row=18,column=2,sticky=S,pady=20)

    sbar = Label(category,text="Created by Subhjeet",relief=SUNKEN)
    sbar.grid(row=20,column=1,columnspan=2,pady=15,ipadx=280)

    category.config(bg="bisque")
    category.mainloop()

def restart():
    category.destroy()
    start()

def submit():
    global response
    global categ
    global opt
    response = requests.get(f"https://opentdb.com/api.php?amount=10&category={int(var.get())}&type=multiple")
    opt = categ[int(var.get())-9]
    category.destroy()
    questions()

def questions():
    global n
    global points
    global question
    question = Tk()
    question.geometry("680x400")
    question.title(f"Question Number: {n}")
    
    l = Label(question,text=f"{n}. {response.json()['results'][n-1]['question']}",wraplength=400,bg="bisque")
    l.grid(row=2,column=1,columnspan=2,pady=(100,20))

    options = []
    options.append(response.json()['results'][n-1]['correct_answer'])
    for j in range(3):
        options.append(response.json()['results'][n-1]['incorrect_answers'][j])
    options.sort()

    global ans
    ans = StringVar()
    ans.set("")

    for i in range(4):
        if(i<2):
            Radiobutton(question,text=options[i],variable=ans,value=options[i],wraplength=200,bg="bisque").grid(row=3,column=i+1,sticky=W,padx=(50,10),pady=(20,0))
        else:
            Radiobutton(question,text=options[i],variable=ans,value=options[i],wraplength=200,bg="bisque").grid(row=4,column=i-1,sticky=W,padx=(50,10))
    Button(question,text="Submit",command=solve,pady=5,padx=3).grid(row=5,column=1,columnspan=2,pady=30)

    global opt
    sbar = Label(question,text=f"Chosen Category: {opt}",relief=SUNKEN)
    sbar.grid(row=1,column=1,columnspan=2,ipadx=250)

    question.config(bg="bisque")
    question.mainloop()

def solve():
    global n
    global points
    global answers

    answers.append(ans.get())

    if n<10:
        if(ans.get() == response.json()['results'][n-1]['correct_answer'] ):
            points += 1
        print(ans.get())
        print(response.json()['results'][n-1]['correct_answer'] )
        print(points)
        n += 1 
        question.destroy()
        questions()
    else:
        results()

def results():
    question.destroy()
    global n
    global points
    global result
    global answers
    result = Tk()
    result.geometry("820x580")
    result.minsize(820,580)
    result.maxsize(820,580)
    result.title("Your Score")
    Label(result,text=f"Your Score:",font="comicsansms 25 bold",bg="bisque").grid(row=1,column=1,pady=20,padx=(20,0))
    Label(result,text=f"{points} out of 10",font="comicsansms 25 bold",bg="bisque").grid(row=1,column=2,pady=20,padx=(20,0))
    for i in range(10):
        Label(result,text=response.json()['results'][i]['question'],wraplength=400,justify=LEFT,bg="bisque").grid(row=i+2,column=1,pady=4,sticky=W)
        if (answers[i] == response.json()['results'][i]['correct_answer']):
            Label(result,text=f"You answered {answers[i]} and thats the right answer",wraplength=400,justify=LEFT,bg="bisque").grid(row=i+2,column=2,pady=4,sticky=W)
        else:
            Label(result,text=f"You answered {answers[i]} and the right answer was { response.json()['results'][i]['correct_answer'] }",wraplength=400,justify=LEFT,bg="bisque").grid(row=i+2,column=2,pady=4,sticky=W)
    Button(result,text="Play again",command=playagain,font="comicsansms 18",padx=10).grid(row=17,column=1,pady=20)
    Button(result,text="Exit",command=exit,font="comicsansms 18").grid(row=17,column=2,pady=20,ipadx=10)

    result.config(bg="bisque")
    result.mainloop()

def playagain():
    result.destroy()
    global n
    global points
    n = 1
    points = 0
    start()

def exit():
    result.destroy()

def start():
    #creating the root or the staring window and fixing the size
    global root
    root = Tk()
    root.geometry("650x400")  
    root.minsize(650,400)
    root.maxsize(650,400)  
    root.title("Starting Quiz")

    

    #some labels and buttons 
    l1=Label(root,text="Welcome to the Quiz App",justify=CENTER,font="comicsansms 40 bold",bg="bisque")
    l2=Button(root,text="Start",command=proceed,padx=20,pady=10,font="comicsansms 20 bold",bg="bisque")
    l1.grid(row=0, column=0, pady=(100, 10),padx=80)
    l2.grid(row=1, column=0, pady=(10, 100),padx=200)
    
    #status bar at the bottom
    sbar = Label(root,text="Created by Subhjeet",relief=SUNKEN)
    sbar.grid(row=2,column=0,pady=50,ipadx=260)
    root.config(bg="bisque")
    
    root.mainloop()

if __name__ == '__main__':
    start()
    