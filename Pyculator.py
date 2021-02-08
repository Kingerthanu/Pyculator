import tkinter as tk
import math
from tkinter.font import Font


class pyculator:
    Currentval = ""
    nextIfClear = 0

    def putIn(self, addPart):
        if self.var.get() == "0":
            self.var.set(addPart)
        else:
            newvar = self.var.get() + str(addPart)
            self.var.set(str(newvar))

    def putOut(self):
        self.var.set("0")
        self.gui.update()

    def swapSign(self):
        if self.var.get()[0] == "-":
            self.var.set(self.var.get()[1:])
        else:
            self.var.set("-" + self.var.get())

    def ifNegative(self, varToTest):
        pass

    def posequalBut(self):
        Currentval = ""
        countr = 0
        varr = self.var.get()
        print("Out: ")
        crnt = ""
        runTime = 0
        for ind, crnt in enumerate(varr):
            if crnt in self.listOfSymbols:
                self.SetofSigns.append(crnt)
                if len(Currentval) != 0:
                    self.SetofVariables.append(Currentval)
                    Currentval = ""
            elif crnt == "." or crnt == "0" or int(crnt):
                Currentval += crnt
        if len(Currentval) != 0:
            self.SetofVariables.append(Currentval)
        for each in self.SetofSigns:
            print(each)
        self.doMath()

    def doMath(self):
        approve = False
        finalValue = 0.0
        itrable = 0
        for idx, num in enumerate(self.SetofVariables):
            if itrable < len(self.SetofSigns):
                sign = self.SetofSigns[itrable]
            else:
                break
            print(num)
            if idx == 0 and sign != "-":
                finalValue = num
            elif finalValue == 0.0 and sign == "-":
                approve = True
                finalValue = float(num)*-1.0
            else:
                if sign == "x":
                    approve = True
                    finalValue = (float(finalValue) *
                                  float(num))
                elif sign == "+":
                    approve = True
                    finalValue = (float(finalValue) +
                                  float(num))
                elif sign == "-":
                    approve = True
                    finalValue = (float(finalValue) -
                                  float(num))
                elif sign == "/":
                    approve = True
                    finalValue = (float(finalValue) /
                                  float(num))
            if approve is True:
                itrable += 1
                approve = False
        self.var.set(finalValue)
        self.nextIfClear += 1

    def ifToClear(self):
        if self.nextIfClear == 1:
            self.var.set("")
            self.SetofVariables.clear()
            self.SetofSigns.clear()
            self.nextIfClear = 0

    def __init__(self):
        self.gui = tk.Tk()
        self.var = tk.StringVar()
        self.gui.iconbitmap("pyIcon.ico")
        self.var.set(0)
        self.gui.resizable(False, False)
        self.gui.title("Pyculator")
        self.gui.geometry("800x900")
        self.SetofVariables = []
        self.SetofSigns = []
        self.listOfSymbols = ['+', '-', 'x', '/']
        # Creating Buttons
        self.B1 = tk.Button(self.gui, text="1", command=lambda: {
                            self.putIn(1), self.ifToClear()}, width=24, height=10)
        self.B2 = tk.Button(self.gui, text="2", command=lambda: {
                            self.putIn(2), self.ifToClear()}, width=24, height=10)
        self.B3 = tk.Button(self.gui, text="3", command=lambda: {
                            self.putIn(3), self.ifToClear()}, width=24, height=10)
        self.Bplus = tk.Button(
            self.gui, text="+", command=lambda: {self.putIn("+"), self.ifToClear()}, width=24, height=10)
        self.Bc = tk.Button(self.gui, text="C", command=lambda: {
                            self.putOut(), self.ifToClear()}, width=24, height=10)
        self.B4 = tk.Button(self.gui, text="4", command=lambda: {
                            self.putIn(4), self.ifToClear()}, width=24, height=10)
        self.B5 = tk.Button(self.gui, text="5", command=lambda: {
                            self.putIn(5), self.ifToClear()}, width=24, height=10)
        self.B6 = tk.Button(self.gui, text="6", command=lambda: {
                            self.putIn(6), self.ifToClear()}, width=24, height=10)
        self.Bminus = tk.Button(self.gui, text="-", command=lambda: {
                                self.putIn(str("-")), self.ifToClear()}, width=24, height=10)
        self.B7 = tk.Button(self.gui, text="7", command=lambda: {
                            self.putIn(7), self.ifToClear()}, width=24, height=10)
        self.B8 = tk.Button(self.gui, text="8", command=lambda: {
                            self.putIn(8), self.ifToClear()}, width=24, height=10)
        self.B9 = tk.Button(self.gui, text="9", command=lambda: {
                            self.putIn(9), self.ifToClear()}, width=24, height=10)
        self.Bx = tk.Button(self.gui, text="X", command=lambda: {
                            self.putIn("x"), self.ifToClear()}, width=24, height=10)
        self.Bequals = tk.Button(self.gui, text="=", command=lambda: {
                                 self.posequalBut()}, width=24, height=20)
        self.Bposneg = tk.Button(self.gui, text="+/-", command=lambda: {
                                 self.swapSign(), self.ifToClear()}, width=24, height=10)
        self.B0 = tk.Button(self.gui, text="0", command=lambda: {
                            self.putIn(0), self.ifToClear()}, width=24, height=10)
        self.Bd = tk.Button(self.gui, text=".", command=lambda: {
                            self.putIn("."), self.ifToClear()}, width=24, height=10)
        self.Bdivision = tk.Button(
            self.gui, text="/", command=lambda: {self.putIn("/"), self.ifToClear()}, width=24, height=10)
        self.Breturn = tk.Button(self.gui, text="R", command=lambda: {
                                 self.var.set(self.var.get()[:-1])}, width=24, height=10)
        # Creating Output Window
        self.font = Font(font=("C:\Windows\Fonts\Verdana", 25))
        self.formula = tk.Label(
            self.gui, textvariable=self.var, font=self.font)
        # Placing Buttons
        self.formula.place(x=0, y=10)
        self.B1.place(x=0, y=300)
        self.B2.place(x=160, y=300)
        self.B3.place(x=320, y=300)
        self.Bplus.place(x=480, y=300)
        self.Bc.place(x=640, y=300)
        self.B4.place(x=0, y=450)
        self.B5.place(x=160, y=450)
        self.B6.place(x=320, y=450)
        self.Bminus.place(x=480, y=450)
        self.Bminus.place(x=480, y=450)
        self.B7.place(x=0, y=600)
        self.B8.place(x=160, y=600)
        self.B9.place(x=320, y=600)
        self.Bx.place(x=480, y=600)
        self.Bequals.place(x=640, y=450)
        self.Bposneg.place(x=0, y=750)
        self.B0.place(x=160, y=750)
        self.Bd.place(x=320, y=750)
        self.Bdivision.place(x=480, y=750)
        self.Breturn.place(x=640, y=750)
        self.gui.mainloop()


calc = pyculator()
