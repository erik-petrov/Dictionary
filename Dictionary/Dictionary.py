from tkinter import *
import os

thisFolder = os.path.dirname(os.path.abspath(__file__))

#def fileread(file):
#    mylist = []
#    with open(os.path.join(thisFolder, file),encoding='utf-8') as f:
#        lines = f.readlines()
#        for i in lines:
#            temp = i.split(',')
#            mylist.append(temp[0])
#    return mylist

def delTranslation(event):
    selection = event.widget.curselection()
    selected = toList[selection[0]]
    selected = selected.rstrip('\n')
    
    pass

def addTranslation():
    word = newTrans.get()
    newTrans.delete(0,END)
    with open(os.path.join(thisFolder,'rus-eng.txt'),'a',encoding='utf-8') as f:
        f.write(f'\n{word}')

def translate(event):
    selection = event.widget.curselection()
    selected = toList[selection[0]]
    selected = selected.rstrip('\n')
    #selected = event.widget.get(selection)
    translation.configure(text=f'Перевод этого слова: {selected}')

def dump(file):
    global fromList,toList
    fromList,toList = [],[]
    with open(os.path.join(thisFolder, file),encoding='utf-8')as f:
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
    dump('rus-eng.txt')
    for i in fromList:
        listbox.insert(END,i)

#TODO: сделать кнопку для удаления перевода, навести порядок в программе, додумать ещё функции.

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
w.create_window(350,50,window=newTrans)

transBut = Button(main,command=addTranslation,text='Добавить слово')
w.create_window(230,50,window=transBut)

refresh()

#лямбда - функция в 1 строку, 
#позволяет выполнять однострочные действия легко и просто
#listbox.bind('<<ListboxSelect>>',lambda event, toList = toList:
                                    #translate(event,toList))

#отказался от лямбды, сделал списки глобальными
#не знаю насколько это правильно, но оно работает
newTrans.bind('<<Return>>',addTranslation)
listbox.bind('<<3>>',delTranslation)
listbox.bind('<<ListboxSelect>>',translate)
main.mainloop()
