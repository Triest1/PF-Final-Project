# Core Packages
# used to construct basic (GUI) applications. 
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import *
import tkinter.filedialog

# NLP Pkgs
from spacy_summarization import text_summarizer
from nltk_summarization import nltk_summarizer

# Web Scraping Pkg
from bs4 import BeautifulSoup
from urllib.request import urlopen

 # Structure and Layout
window = Tk()
window.title("Summarizer GUI")
window.geometry("1000x600")
window.config(background='black')

style = ttk.Style(window)
style.configure('lefttab.TNotebook', tabposition='wn',)


# TAB LAYOUT
tab_control = ttk.Notebook(window,style='lefttab.TNotebook')
 
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

# ADD TABS TO NOTEBOOK
tab_control.add(tab1, text=f'{"Home":^20s}')
tab_control.add(tab2, text=f'{"File":^20s}')
tab_control.add(tab4, text=f'{"Comparer ":^20s}')


label1 = Label(tab1, text= 'Summarizer',padx=5, pady=5)
label1.grid(column=0, row=0)
 
label2 = Label(tab2, text= 'File Processing',padx=5, pady=5)
label2.grid(column=0, row=0)

label3 = Label(tab4, text= 'Compare Summarizers',padx=5, pady=5)
label3.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both')

# Functions 
def get_summary():
	raw_text = str(entry.get('1.0',tk.END))
	final_text = text_summarizer(raw_text) #using spacy
	print(final_text)
	result = '\nSummary:{}'.format(final_text)
	tab1_display.insert(tk.END,result)


# Clear entry widget
def clear_text():
	entry.delete('1.0',END)

def clear_display_result():
	tab1_display.delete('1.0',END)


# Clear Text  with position 1.0
def clear_text_file():
	displayed_file.delete('1.0',END)

# Clear Result of Functions
def clear_text_result():
	tab2_display_text.delete('1.0',END)


# Clear entry widget
def clear_compare_text():
	entry1.delete('1.0',END)

def clear_compare_display_result():
	tab4_display.delete('1.0',END)


# Functions for TAB 2 FILE PROCESSER
# Open File to Read and Process
def openfiles():
	file1 = tkinter.filedialog.askopenfilename(filetypes=(("Text Files",".txt"),("All files","*")))
	read_text = open(file1).read()
	displayed_file.insert(tk.END,read_text)


def get_file_summary():
	raw_text = displayed_file.get('1.0',tk.END)
	final_text = text_summarizer(raw_text)
	result = '\nSummary:{}'.format(final_text)
	tab2_display_text.insert(tk.END,result)


# COMPARER FUNCTIONS

def use_spacy():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = text_summarizer(raw_text)
	print(final_text)
	result = '\nSpacy Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

def use_nltk():
	raw_text = str(entry1.get('1.0',tk.END))
	final_text = nltk_summarizer(raw_text)
	print(final_text)
	result = '\nNLTK Summary:{}\n'.format(final_text)
	tab4_display.insert(tk.END,result)

# MAIN NLP TAB
l1=Label(tab1,text="Enter Text To Summarize")
l1.grid(row=1,column=0)

entry=Text(tab1,height=10)
entry.grid(row=2,column=0,columnspan=2,padx=5,pady=5)

# BUTTONS
button1=Button(tab1,text="Reset",command=clear_text, width=12,bg='#8a5551',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab1,text="Summarize",command=get_summary, width=12,bg='#8a5551',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab1,text="Clear Result", command=clear_display_result,width=12,bg='#8a5551',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

# Display Screen For Result
tab1_display = ScrolledText(tab1,height=10)
tab1_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


#FILE PROCESSING TAB
l1=Label(tab2,text="Open File To Summarize")
l1.grid(row=1,column=1)

displayed_file = ScrolledText(tab2,height=7)# Initial was Text(tab2)
displayed_file.grid(row=2,column=0, columnspan=3,padx=5,pady=3)

# BUTTONS FOR SECOND TAB/FILE READING TAB
b0=Button(tab2,text="Open File", width=12,command=openfiles,bg='#8a5551',fg='#fff')
b0.grid(row=3,column=0,padx=10,pady=10)

b1=Button(tab2,text="Reset ", width=12,command=clear_text_file,bg="#8a5551",fg='#fff')
b1.grid(row=3,column=1,padx=10,pady=10)

b2=Button(tab2,text="Summarize", width=12,command=get_file_summary,bg='#8a5551',fg='#fff')
b2.grid(row=3,column=2,padx=10,pady=10)

b3=Button(tab2,text="Clear Result", width=12,command=clear_text_result,bg='#8a5551',fg='#fff')
b3.grid(row=5,column=1,padx=10,pady=10)

b4=Button(tab2,text="Close", width=12,command=window.destroy,bg='#8a5551',fg='#fff')
b4.grid(row=5,column=2,padx=10,pady=10)

# Display Screen
# tab2_display_text = Text(tab2)
tab2_display_text = ScrolledText(tab2,height=10)
tab2_display_text.grid(row=7,column=0, columnspan=3,padx=5,pady=5)

# Allows you to edit
tab2_display_text.config(state=NORMAL)

# Display Screen For Result
url_display = ScrolledText(tab3,height=10)
url_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


tab3_display_text = ScrolledText(tab3,height=10)
tab3_display_text.grid(row=10,column=0, columnspan=3,padx=5,pady=5)


# COMPARER TAB
l1=Label(tab4,text="Enter Text To Summarize")
l1.grid(row=1,column=0)

entry1=ScrolledText(tab4,height=10)
entry1.grid(row=2,column=0,columnspan=3,padx=5,pady=3)

# BUTTONS
button1=Button(tab4,text="Reset",command=clear_compare_text, width=12,bg='#8a5551',fg='#fff')
button1.grid(row=4,column=0,padx=10,pady=10)

button2=Button(tab4,text="SpaCy",command=use_spacy, width=12,bg='#8a5551',fg='#fff')
button2.grid(row=4,column=1,padx=10,pady=10)

button3=Button(tab4,text="Clear Result", command=clear_compare_display_result,width=12,bg='#8a5551',fg='#fff')
button3.grid(row=5,column=0,padx=10,pady=10)

button4=Button(tab4,text="NLTK",command=use_nltk, width=12,bg='#8a5551',fg='#fff')
button4.grid(row=5,column=1,padx=10,pady=10)

# Display Screen For Result
tab4_display = ScrolledText(tab4,height=15)
tab4_display.grid(row=7,column=0, columnspan=3,padx=5,pady=5)


window.mainloop() # tells Python to run the Tkinter event loop.
