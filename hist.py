#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.ttk as ttk


class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        self.master.title('Histogram Maker')
        self.master.resizable(False, False)

        top = ttk.LabelFrame(self.master, text='Input numbers')
        bot = ttk.Frame(self.master)

        top.pack(ipadx=10, ipady=10, expand=True)
        bot.pack(ipadx=10, ipady=10)

        self.entry = ttk.Entry(top, text='In')
        self.label = ttk.Label(bot, text='Enter all of the numbers seperated with spaces, then click "Done"')
        self.but = ttk.Button(bot, text='Done', command=self.get_numbers)

        self.entry.pack()
        self.label.pack(pady=5)
        self.but.pack()

    def get_numbers(self):
        numbers = self.entry.get()
        self.master.destroy()

        numbers = np.array([float(i) for i in numbers.split()])

        mu = np.mean(numbers)
        sigma = np.std(numbers)

        x = np.linspace(mu - (4*sigma), mu+(4*sigma), 1000)
        plt.plot(x, 1/sigma * np.sqrt(2 * np.pi) * np.exp(-(x - mu)**2 / (2 * sigma**2)))
        plt.title(f'Histogram, Mean: {mu}, Std Dev: {sigma}')
        plt.xlabel('x')
        plt.ylabel('y')

        plt.show()


def main():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    main()

