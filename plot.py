import tkinter
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


hp = Tk()
hp.geometry("600x300")
hp.title("Doctors and Hospitals Information")

def graph():
    house_prices = np.random.normal(200000, 25000, 50000)
    plt.hist(house_prices, 50)
    plt.show()


btn = Button(hp, text="plot", command=graph)
btn.pack()

hp.mainloop()
