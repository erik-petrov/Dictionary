from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import sys, fileinput
import os

thisFolder = os.path.dirname(os.path.abspath(__file__))
global dec


#print(fileinput.input(file))

def delTranslation(event):
    selection = event.widget.curselection()
    fromSelected = fromList[selection[0]].rstrip('\n')
    toSelected = toList[selection[0]].strip("\n")
    selected2 = f'{fromSelected},{toSelected}'
    translation.configure(text=f'Удалено слово: {fromList[selection[0]]}')
    #with open(os.path.join(thisFolder, dec),'r',encoding='utf-8') as f:
    with open(dec,encoding="utf-8") as f:
        lines = f.readlines()
    #with open(os.path.join(thisFolder, dec),'w',encoding='utf-8') as f:
    with open(dec,"w",encoding="utf-8") as f:
        for i in lines:
            if selected2 == i.rstrip('\n'):
                lines.remove(i)
        for i in lines:
            if lines.index(i) == len(lines)-1:
                i = i.strip('\n')
                f.write(i)
            else:
                f.write(i)
    refresh()

def addTranslation():
    x=0
    word = newTrans.get()
    newTrans.delete(0,END)
    if ',' in word:
        for i in word:
            if i == ',':
                x+=1
    if x == 1:
        #with open(os.path.join(thisFolder, dec),'a',encoding='utf-8') as f:
        with open(dec,"a",encoding="utf-8") as f:
            f.write(f'\n{word}')
            refresh()
    else:
        translation.configure(text='Неверно введенное слово, попробуйте ещё раз.')

def translate(event):
    selection = event.widget.curselection()
    selected = toList[selection[0]]
    selected = selected.rstrip('\n')
    #selected = event.widget.get(selection)
    translation.configure(text=f'Перевод этого слова: {selected}')

def dump():
    global fromList,toList
    fromList,toList = [],[]
    #with open(os.path.join(thisFolder, dec),encoding='utf-8')as f:
    with open(dec,encoding="utf-8") as f:
        lines = f.readlines()
        for i in lines:
            fromI = i.split(',')
            fromList.append(fromI[0])
            toI = i.rsplit(',')
            toList.append(toI[1])
    
def refresh():
    if listbox:
        listbox.delete(0,END)
#    fromList,toList = dump('rus-eng.txt')
    dump()
    for i in fromList:
        listbox.insert(END,i)

#TODO: навести порядок в программе, додумать ещё функции.

main = Tk()
mainMenu = Menu(main)
main.config(menu=mainMenu)
main.title('Словарь')

canvasW = 400
canvasH = 400

w = Canvas(main,width=canvasW,height=canvasH)
w.pack()

translation = Label(main)
w.create_window(200,50,window=translation)

listbox = Listbox(main)
w.create_window(200, 300, window=listbox)

refreshbutton = Button(main,
                        text='Перезагрузить',
                        command=refresh,
                        relief=SUNKEN)
w.create_window(50,50,window=refreshbutton)

newTrans = Entry(main)
w.create_window(350,150,window=newTrans)

transBut = Button(main,command=addTranslation,text='Добавить слово')
w.create_window(230,150,window=transBut)

guide = Label(main,text='При добавлении перевода пишите его в след формате:\n оригинал,перевод')
w.create_window(230,120,window=guide)

dec = askopenfilename()

#open = Button(main,command=add)
#w.create_window(200,400,window=open)

refresh()

#лямбда - функция в 1 строку, 
#позволяет выполнять однострочные действия легко и просто
#listbox.bind('<<ListboxSelect>>',lambda event, toList = toList:
                                    #translate(event,toList))

#отказался от лямбды, сделал списки глобальными
#не знаю насколько это правильно, но оно работает
#newTrans.bind('<Return>',addTranslation)
listbox.bind('<Double-1>',delTranslation)
#кнопки должны быть в <> но не в <<>>
listbox.bind('<<ListboxSelect>>',translate)
main.mainloop()
