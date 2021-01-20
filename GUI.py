# importing required modules
from ET import *
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook
from tkcalendar.dateentry import DateEntry
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from pandas import DataFrame

#-----------------------------------------------------------------------------------------------------------------------

# central expense tree
expense_tracker = expense_tree()

months = {1: [],  #these are the months that hold a list
          2: [],
          3: [],
          4: [],
          5: [],
          6: [],
          7: [],
          8: [],
          9: [],
          10: [],
          11: [],
          12: []}

# ----------------------------------------------------------------------------------------------------------------------

# (Button call function) creates item nodes and monthly expenses node and inserts them in the central expense tracker tree
def Addexpense():

    Date = EDate.get()
    ItemName = Title.get()
    ItemPrice = float(Expense.get())
    ItemCategory = item(ItemName, ItemPrice).category

    data = [Date, ItemName, ItemPrice, ItemCategory]

    month_num = Date[:2]
    if '/' in month_num:
        month_num = int(Date[0])
    else:
        month_num = int(Date[:2])

    months[month_num].append(item(ItemName, ItemPrice))

    for keys in months:
        m_l = monthly_expenses(months[keys], date_num=keys)
        expense_tracker.add_monthly_expense(m_l)

    TVExpense.insert('', 'end', values=data)

#-----------------------------------------------------------------------------------------------------------------------

# (Button call function) creates a new GUI (Graphical User Interface) window that helps graph necessities and luxuries by the month
def visualize_expenditure():

    graph_GUI = Tk()

    graph_GUI.title('** Visual View of Expenditure **')
    graph_GUI.geometry('700x700')

    # function to graph
    def plot_bar_graphs(month_num):

        categ_n = ["housing", "transportation", "food", "utilities", "clothing", "healthcare", "insurance", "household items", "loans", "education", "savings", "miscellaneous"]
        categ_l = ["entertainment", "personal", "fashion clothing"]

        data1 = {'categories': categ_n,
                 'expenses': get_cumulative_expenses(expense_tracker.get_LON_items()[0][month_num],necessity_list=True),
                 }

        df1 = DataFrame(data1, columns=['categories', 'expenses'])

        figure1 = plt.Figure(figsize=(6, 5), dpi=100)
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, graph_GUI)
        bar1.get_tk_widget().grid(row=1, column=4, columnspan=3, rowspan=20)
        df1 = df1[['categories', 'expenses']].groupby('categories').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Monthly Necessity')
        bar1.draw()
        toolbarFrame = Frame(master=graph_GUI)
        toolbarFrame.grid(row=22, column=4)
        toolbar = NavigationToolbar2Tk(bar1, toolbarFrame)

        data2 = {'categories': categ_l,
                 'expenses': get_cumulative_expenses(expense_tracker.get_LON_items()[1][month_num],necessity_list=False),
                 }

        df2 = DataFrame(data2, columns=['categories', 'expenses'])

        figure2 = plt.Figure(figsize=(6, 5), dpi=100)
        ax2 = figure2.add_subplot(111)
        bar2 = FigureCanvasTkAgg(figure2, graph_GUI)
        bar2.get_tk_widget().grid(row=1, column=8, columnspan=3, rowspan=20)
        df2 = df2[['categories', 'expenses']].groupby('categories').sum()
        df2.plot(kind='bar', legend=True, ax=ax2)
        ax2.set_title('Monthly Luxury')
        bar2.draw()
        toolbarFrame = Frame(master=graph_GUI)
        toolbarFrame.grid(row=22, column=8)
        toolbar = NavigationToolbar2Tk(bar2, toolbarFrame)

    def january():
        plot_bar_graphs(1)

    def february():
        plot_bar_graphs(2)

    def march():
        plot_bar_graphs(3)

    def april():
        plot_bar_graphs(4)

    def may():
        plot_bar_graphs(5)

    def june():
        plot_bar_graphs(5)

    def july():
        plot_bar_graphs(7)

    def august():
        plot_bar_graphs(8)

    def september():
        plot_bar_graphs(9)

    def october():
        plot_bar_graphs(10)

    def november():
        plot_bar_graphs(11)

    def december():
        plot_bar_graphs(12)

    january = ttk.Button(graph_GUI, text="January", command=january)
    january.grid(row=2, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    february = ttk.Button(graph_GUI, text="February", command=february)
    february.grid(row=3, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    march = ttk.Button(graph_GUI, text="March", command=march)
    march.grid(row=4, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    april = ttk.Button(graph_GUI, text="April", command=april)
    april.grid(row=5, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    may = ttk.Button(graph_GUI, text="May", command=may)
    may.grid(row=6, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    june = ttk.Button(graph_GUI, text="June", command=june)
    june.grid(row=7, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    july = ttk.Button(graph_GUI, text="July", command=july)
    july.grid(row=8, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    august = ttk.Button(graph_GUI, text="August", command=august)
    august.grid(row=9, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    september = ttk.Button(graph_GUI, text="September", command=september)
    september.grid(row=10, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    october = ttk.Button(graph_GUI, text="October", command=october)
    october.grid(row=11, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    november = ttk.Button(graph_GUI, text="November", command=november)
    november.grid(row=12, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

    december = ttk.Button(graph_GUI, text="December", command=december)
    december.grid(row=13, column=3, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)



#-----------------------------------------------------------------------------------------------------------------------

# # function to graph
# def plot_bar_graphs():
#
#     categ_n = ["housing", "transportation", "food", "utilities", "clothing", "healthcare", "insurance", "household items", "loans", "education", "savings", "miscellaneous"]
#     categ_l = ["entertainment", "personal", "fashion clothing"]
#
#     data1 = {'categories': categ_n,
#              'expenses': get_cumulative_expenses(expense_tracker.get_LON_items()[0][0],necessity_list=True),
#              }
#
#     df1 = DataFrame(data1, columns=['categories', 'expenses'])
#
#     figure1 = plt.Figure(figsize=(6, 5), dpi=100)
#     ax1 = figure1.add_subplot(111)
#     bar1 = FigureCanvasTkAgg(figure1, GUI)
#     bar1.get_tk_widget().grid(row=1, column=2)
#     df1 = df1[['categories', 'expenses']].groupby('categories').sum()
#     df1.plot(kind='bar', legend=True, ax=ax1)
#     ax1.set_title('Monthly Necessity')
#     bar1.draw()
#     frame = Frame(graph_GUI)
#     frame.grid(row=0, column=1)
#     toobar = NavigationToolbar2Tk(canvas, frame)
#     canvas.get_tk_widget().grid(row=1, column=0)

#-----------------------------------------------------------------------------------------------------------------------

# Setting up the main Graphical User Interface
GUI = Tk()
GUI.title('** Expense Recorder **')
GUI.geometry('1000x600')

Tab = Notebook(GUI)
F1 = Frame(Tab, width=500, height=500, bg="light gray")
Tab.add(F1, text='Expense')

Tab.pack(fill=BOTH, expand=1)

# ==========Row 0 ===========================
LDate = ttk.Label(F1, text='Date', font=(None, 18))
LDate.grid(row=0, column=0, padx=5, pady=5, sticky='w')

EDate = DateEntry(F1, width=19, background='blue', foreground='white', font=(None, 18))
EDate.grid(row=0, column=1, padx=5, pady=5)

# ==========Row 1 ===========================
LTitle = ttk.Label(F1, text='Title', font=(None, 18))
LTitle.grid(row=1, column=0, padx=5, pady=5, sticky='w')
Title = StringVar()
ETitle = ttk.Entry(F1, textvariable=Title, font=(None, 18))
ETitle.grid(row=1, column=1, padx=5, pady=5)

# ========== Row 2 =====================
LExpense = ttk.Label(F1, text='Expense', font=(None, 18))
LExpense.grid(row=2, column=0, padx=5, pady=5, sticky='w')

Expense = StringVar()

EExpense = ttk.Entry(F1, textvariable=Expense, font=(None, 18))
EExpense.grid(row=2, column=1, padx=5, pady=5)

# ========== Row 3 =====================
BFIadd = ttk.Button(F1, text='Add', command=Addexpense)
BFIadd.grid(row=3, column=1, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

# ========= Row 4 =======================

Category = StringVar()  # Matt: allows Category to display a string
CCategory = ttk.Entry(F1, textvariable=Category, font=(None, 18))  # attributes for Category on GUI
CCategory.grid(row=4, column=1, padx=5, pady=5, sticky='w')  # Grid features for Category

# ========= Row 5 ==========================
BFvisualize = ttk.Button(F1, text='Visualize Expenditure', command=visualize_expenditure)
BFvisualize.grid(row=3, column=2, padx=5, pady=5, sticky='w', ipadx=10, ipady=10)

# ===========tree view===========

TVList = ['Date', 'Title', 'Expense', 'Category']
TVExpense = ttk.Treeview(F1, column=TVList, show='headings', height=5)
for i in TVList:
    TVExpense.heading(i, text=i.title())
TVExpense.grid(row=4, column=1, padx=5, pady=5, sticky='w', columnspan=3)

GUI.mainloop()

#-----------------------------------------------------------------------------------------------------------------------