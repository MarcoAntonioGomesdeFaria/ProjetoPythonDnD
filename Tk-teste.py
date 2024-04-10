from tkinter import *
from PIL import ImageTk,Image
import matplotlib.pyplot as plt
import numpy as np

root = Tk()
root.title('Teste')
root.geometry("400x300")

def graph():
    house_prices = np.random.normal(20000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()

btn_1 = Button(root, text='Graph_it', command=graph)
btn_1.grid(row=0,column=3)

root.mainloop()