import time
import tkinter
import mysql.connector as mc
from tkinter import *
from tkinter import ttk


# mydb = mc.connect(host = 'localhost', user = 'libmansys', passwd = 'libmansys', database = 'lib')
# mycursor = mydb.cursor()


#Main Window
window = Tk()
state = 'start'
###############################################################################################################################################################################
#Main Frame
frame_1 = Frame(window)
frame_1.grid(row= 0, column= 0, padx=10, pady= (5,20))
###############################################################################################################################################################################

###############################################################################################################################################################################
#LabelFrame to store accno and classno
library_info_frame = LabelFrame(frame_1, text='Library Information', padx= 20, pady= 15)
library_info_frame.grid(row= 0, column= 0, columnspan= 2, padx= 20, pady= (10,0), sticky= 'news')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store accno
acc_no_frame = Frame(library_info_frame)
acc_no_frame.grid(row=0,column=0,padx=(0,7.5))
acc_no_label = Label(acc_no_frame, text= 'Accession Number').grid(row=0,column=0)
# mycursor.execute('select accno from library')
# accno = [i for i in mycursor]
acc_no_entry = Entry(acc_no_frame)
# acc_no_entry.insert(END,int(accno[-1][0])+1)
acc_no_entry.config(state= DISABLED)
acc_no_entry.grid(row=1,column=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store classno
class_no_frame = Frame(library_info_frame)
class_no_frame.grid(row=0,column=1,padx=(7.5,0))
class_no_label = Label(class_no_frame, text= 'Class Number').grid(row=0,column=0)
class_no_entry = Entry(class_no_frame)
class_no_entry.grid(row=1,column=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
###############################################################################################################################################################################



###############################################################################################################################################################################
#LabelFrame to store book info
book_info_frame = LabelFrame(frame_1, text='Book Information', padx= 20, pady= 15)
book_info_frame.grid(row= 1, column= 0, columnspan= 2, padx= 20, pady= (10,0), sticky= 'news')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store title
title_frame = Frame(book_info_frame)
title_frame.grid(row= 0, column= 0, padx= (0,7.5))
title_label = Label(title_frame, text= 'Title').grid(row= 0, column= 0)
title_entry = Entry(title_frame)
title_entry.grid(row= 1, column= 0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store author name
author_name_frame = Frame(book_info_frame)
author_name_frame.grid(row= 1, column= 0, padx= (0,7.5), pady= (5,0))
author_name_label = Label(author_name_frame, text= 'Author Name').grid(row= 0, column= 0)
author_name_entry = Entry(author_name_frame)
author_name_entry.grid(row= 1, column= 0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store author initials
author_in_frame = Frame(book_info_frame)
author_in_frame.grid(row= 1, column= 1, padx= (7.5,0), pady= (5,0))
author_in_label = Label(author_in_frame, text= 'Author Initial').grid(row= 0, column= 0)
author_in_entry = Entry(author_in_frame)
author_in_entry.grid(row= 1, column= 0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store number of pages
pages_frame = Frame(book_info_frame)
pages_frame.grid(row= 0, column= 1, padx= (7.5,0))
pages_label = Label(pages_frame, text= 'Pages').grid(row= 0, column= 0)
pages_entry = Entry(pages_frame)
pages_entry.grid(row= 1, column=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
###############################################################################################################################################################################



###############################################################################################################################################################################
#LabelFrame to store publisher info
publisher_info_frame = LabelFrame(frame_1, text='Pubisher Information', padx= 20, pady= 15)
publisher_info_frame.grid(row= 2, column=0, columnspan= 2, padx= 20, pady= (10,0), sticky= 'news')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store publisher name
publisher_name_frame = Frame(publisher_info_frame)
publisher_name_frame.grid(row= 0, column= 0, padx= (0,7.5))
publisher_name_label = Label(publisher_name_frame, text= 'Publisher Name').grid(row= 0, column= 0)
publisher_name_entry = Entry(publisher_name_frame)
publisher_name_entry.grid(row= 1, column=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store publisher year
publisher_year_frame = Frame(publisher_info_frame)
publisher_year_frame.grid(row= 0, column= 1, padx= (7.5,0))
publisher_year_label = Label(publisher_year_frame, text= 'Publisher Year').grid(row= 0, column= 0)
publisher_year_combobox = ttk.Combobox(publisher_year_frame, values=[i for i in range(1750,time.localtime().tm_year+1)])
publisher_year_combobox.current(time.localtime().tm_year-1750)
publisher_year_combobox.grid(row= 1, column= 0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
###############################################################################################################################################################################



###############################################################################################################################################################################
#LabelFrame to store cost & copies info
cost_copies_info_frame = LabelFrame(frame_1, text='Cost & Copies', padx= 20, pady= 15)
cost_copies_info_frame.grid(row= 3, column= 0, columnspan= 2, padx= 20, pady= (10,0), sticky= 'news')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store cost
cost_frame = Frame(cost_copies_info_frame)
cost_frame.grid(row= 0, column= 0, padx= (0,7.5))
cost_label = Label(cost_frame, text= 'Cost').grid(row= 0, column= 0)
cost_entry = Entry(cost_frame)
cost_entry.grid(row= 1, column=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#Frame to store copies
copies_frame = Frame(cost_copies_info_frame)
copies_frame.grid(row= 0, column= 1, padx= (7.5,0))
copies_label = Label(copies_frame, text= 'Copies').grid(row= 0, column= 0)
var = IntVar(copies_frame)
copies_spinbox = ttk.Spinbox(copies_frame, from_=1, to='infinity', textvariable= var)
copies_spinbox.grid(row= 1, column=0)
var.set(1)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
###############################################################################################################################################################################

###############################################################################################################################################################################
#Frame to store 

#add border and sticky
frame_2 = Frame(window)
frame_2.grid(row= 1, column= 0, columnspan= 2 ,padx=10, pady= (5,20))
###############################################################################################################################################################################

###############################################################################################################################################################################
#Button to Cancel
def cancel():
    class_no_entry.delete(0,END)
    title_entry.delete(0,END)
    pages_entry.delete(0,END)
    publisher_name_entry.delete(0,END)
    publisher_year_combobox.current(time.localtime().tm_year-1750)
    cost_entry.delete(0,END)
    var.set(1)
cancel_button = Button(frame_2, text= 'Cancel', command= cancel)
cancel_button.grid(row= 0, column= 0, padx= (0,10))
###############################################################################################################################################################################
#Button to Add
def add():
    pass
    # mycursor.execute(f"insert into library value{(acc_no_entry.get(),class_no_entry.get(),title_entry.get(),author_name_entry.get(),publisher_name_entry.get(),publisher_year_combobox.get(),pages_entry.get(),author_in_entry.get(),cost_entry.get(),copies_spinbox.get())}")
add_button = Button(frame_2, text= 'Add Data', command= add)
add_button.grid(row= 0, column= 1, padx= (10,0))
###############################################################################################################################################################################
window.mainloop()