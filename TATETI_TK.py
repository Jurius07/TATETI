from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("TATETI 1.0")
root.resizable(0,0)
root.geometry("140x235")
root.config(bg="#4C508C")

frame_1=Frame(root)
frame_2=Frame(root)
frame_2.config(bg="#4C508C")

frame_1.pack()
frame_2.pack()

position=StringVar()
tx=True

great_list=['    ']*9


def confirm_position(num):
    global tx
    global great_list
    gamefinished=True
    player=' x ' if tx else ' o '
    try:
        if great_list[int(num)-1]=='    ' and int(num)>=1:
            great_list[int(num)-1]=player
            board_list[int(num)-1].config(text=great_list[int(num)-1])
            tx= not tx
        else:
            messagebox.showinfo('Invalidez','La posicion ya fue jugada \no no existe')
    except:
        messagebox.showinfo('Invalidez','Posicion inexistente')
    
    if (great_list[0] ==  great_list[1] == great_list[2] and great_list[0] !='    ' or 
    great_list[3] ==  great_list[4] == great_list[5] and great_list[3] !='    ' or 
    great_list[6] ==  great_list[7] == great_list[8] and great_list[6] !='    ' or 
    great_list[0] ==  great_list[3] == great_list[6] and great_list[0] !='    ' or 
    great_list[1] ==  great_list[4] == great_list[7] and great_list[1] !='    ' or 
    great_list[2] ==  great_list[5] == great_list[8] and great_list[2] !='    ' or 
    great_list[0] ==  great_list[4] == great_list[8] and great_list[0] !='    ' or 
    great_list[2] ==  great_list[4] == great_list[6] and great_list[2] !='    '):
        messagebox.showinfo('Triunfo','El ganador es: '+'x' if not tx else 'El ganador es: '+'o')
        gamefinished=False
        
    if gamefinished:
        if '    ' not in great_list:
            messagebox.showinfo('Tablas','Empate')

def limpieza():
    global board_list
    global great_list
    for i in board_list:
        i.config(text='    ')
    great_list.clear()
    great_list=['    ']*9
        

############# POSICION 1 ##################

board_1=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_1.grid(row=0,column=0)
board_1.config(text=great_list[0])

############# POSICION 2 ##################


board_2=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_2.grid(row=0,column=1)
board_2.config(text=great_list[1])

############# POSICION 3 ##################

board_3=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_3.grid(row=0,column=2)
board_3.config(text=great_list[2])

############# POSICION 4 ##################

board_4=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_4.grid(row=1,column=0)
board_4.config(text=great_list[3])

############# POSICION 5 ##################

board_5=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_5.grid(row=1,column=1)
board_5.config(text=great_list[4])

############# POSICION 6 ##################

board_6=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_6.grid(row=1,column=2)
board_6.config(text=great_list[5])

############# POSICION 7 ##################

board_7=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_7.grid(row=2,column=0)
board_7.config(text=great_list[6])

############# POSICION 8 ##################

board_8=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_8.grid(row=2,column=1)
board_8.config(text=great_list[7])

############# POSICION 9 ##################

board_9=Label(frame_1,font=("Comic Sans MS",20),
                        fg="white",
                        bg="#111256",
                        justify='center',
                        bd=4,
                        relief="raised")
board_9.grid(row=2,column=2)
board_9.config(text=great_list[8])

########### LISTA DE BOARDS ################

board_list=[board_1,board_2,board_3,board_4,board_5,board_6,board_7,board_8,board_9]

#------------------------------------------------------------------------------

########### LABELS Y BUTTONS DEL SEGUNDO FRAME #################

label_lugar=Label(frame_2,text="POSICION:")
label_lugar.grid(row=0,column=0,pady=5,padx=5)
label_lugar.config(bg="#CACCF0")

ingreso_lugar=Entry(frame_2,width=5,textvariable=position)
ingreso_lugar.grid(row=0,column=1,pady=5)

boton_lugar=Button(frame_2,text="Insertar Posicion",command=lambda:confirm_position(position.get()))
boton_lugar.grid(row=1,column=0,columnspan=2)
boton_lugar.config(bg="#3595BC",fg="white")

boton_limpiar=Button(frame_2,text='Reiniciar Juego',command=lambda:limpieza())
boton_limpiar.grid(row=2,column=0,columnspan=2,pady=5)
boton_limpiar.config(bg="#3595BC",fg="white")


root.mainloop()