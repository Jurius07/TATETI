from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.resizable(0,0)
root.title('TATETI 2.0')
root.config(bg="#4C508C")

frame_1=Frame()
frame_1.config(bg="#111256")
frame_1.pack()

frame_2=Frame()
frame_2.config(bg="#4C508C")
frame_2.pack()


font_general=15
tx=True
great_list=['  _  ']*9

def confirm_position(num):
    global tx
    global great_list
    gameFinished=True
    player='  X  ' if tx else '  O  '

    if great_list[num-1]=='  _  ' and num>=1:
        great_list[num-1]=player
        list_buttons[num-1].config(text=great_list[num-1])
        tx=not tx
    else:
        messagebox.showinfo('Invalidez','Posicion ya jugada o inexistente')

    if (great_list[0] ==  great_list[1] == great_list[2] and great_list[0] !='  _  ' or 
    great_list[3] ==  great_list[4] == great_list[5] and great_list[3] !='  _  ' or 
    great_list[6] ==  great_list[7] == great_list[8] and great_list[6] !='  _  ' or 
    great_list[0] ==  great_list[3] == great_list[6] and great_list[0] !='  _  ' or 
    great_list[1] ==  great_list[4] == great_list[7] and great_list[1] !='  _  ' or 
    great_list[2] ==  great_list[5] == great_list[8] and great_list[2] !='  _  ' or 
    great_list[0] ==  great_list[4] == great_list[8] and great_list[0] !='  _  ' or 
    great_list[2] ==  great_list[4] == great_list[6] and great_list[2] !='  _  '):
        messagebox.showinfo('Triunfo','El ganador es: '+'x' if not tx else 'El ganador es: '+'o')
        gamefinished=False

        replexit=messagebox.askyesno('TATETI','Desea volver a jugar?')
        if replexit==True:
            for i in list_buttons:
                i.config(text='  _  ')
            great_list.clear()
            great_list=['  _  ']*9
        else:
            root.destroy()
        

    if gameFinished:
        if '  _  ' not in great_list:
            messagebox.showinfo('Tablas','Empate')

def clean():
    global great_list
    for i in list_buttons:
        i.config(text='  _  ')
    great_list.clear()
    great_list=['  _  ']*9

############## BOTON A POSICION 1 ##########################

button_1=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(1))
button_1.grid(row=0,column=0)
button_1.config(text=great_list[0])

############## BOTON A POSICION 2 ##########################

button_2=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(2))
button_2.grid(row=0,column=1)
button_2.config(text=great_list[1])

############## BOTON A POSICION 3 ##########################

button_3=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(3))
button_3.grid(row=0,column=2)
button_3.config(text=great_list[2])

############## BOTON A POSICION 4 ##########################

button_4=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(4))
button_4.grid(row=1,column=0)
button_4.config(text=great_list[3])

############## BOTON A POSICION 5 ##########################

button_5=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(5))
button_5.grid(row=1,column=1)
button_5.config(text=great_list[4])

############## BOTON A POSICION 6 ##########################

button_6=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(6))
button_6.grid(row=1,column=2)
button_6.config(text=great_list[5])

############## BOTON A POSICION 7 ##########################

button_7=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(7))
button_7.grid(row=2,column=0)
button_7.config(text=great_list[6])

############## BOTON A POSICION 8 ##########################

button_8=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(8))
button_8.grid(row=2,column=1)
button_8.config(text=great_list[7])

############## BOTON A POSICION 9 ##########################

button_9=Button(frame_1,font=("Comic Sans MS",font_general),
                       justify='center',
                       bd=4,
                       relief='raised',
                       fg="white",
                       bg="#111256",command=lambda:confirm_position(9))
button_9.grid(row=2,column=2)
button_9.config(text=great_list[8])

################### LISTA VARIABLES TIPO BUTTON ################################

list_buttons=[button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9]

################## BOTON OPCIONAL PARA LIMPIAR TABLERO ########################

button_clean=Button(frame_2,text="Limpiar tablero(reiniciar)",command=lambda:clean())
button_clean.grid(row=0,column=0,padx=5,pady=5)
button_clean.config(bg="#3595BC",fg="white")


root.mainloop()