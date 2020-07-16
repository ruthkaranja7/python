#PROJECT 2 : RUTH KARANJA

'''This program builds a GUI calculator that perfoms simple arithmetic
calculations'''

from tkinter import * #contains functions that will build the GUI
class calculator(Frame): # Parent container inherits from Frame

    def __init__(self):
        
        Frame.__init__(self) # Base-class constructor initializes top component
        self.master.title("Calculator-Ruth") #title of the GUI      
        self.grid(sticky = W+E+N+S) #Grid divides into rows and columns. With
                                   #W+E+N+S, the available space in the cell is
                                   #filled
                                   
        #constructing the calculator display
        self.display = StringVar() #stores what is entered on the screen.
        self.screen = Entry(self, justify=RIGHT, relief = SUNKEN, 
            textvariable = self.display)
        self.screen.grid(column= 0, columnspan = 4, stick = W+E+N+S)
        self.memory = 0 # sets the calculator memory to zero. Important for 
                            # the memory buttons
        #constructing the buttons of the calcutor and linking them to commands 
        #that will control what happens when clicked.
        self.button7 = Button(self, text = '7', width = 5, command = self.seven)
        self.button7.grid(row = 2, column = 0, sticky = W+E+N+S)       
        self.button8 = Button(self, text = '8', width = 5, command = self.eight)
        self.button8.grid(row = 2, column = 1, sticky = W+E+N+S)      
        self.button9 = Button(self, text = '9', width = 5, command = self.nine)
        self.button9.grid(row = 2, column = 2, sticky = W+E+N+S)
        self.button4 = Button(self, text = '4', width = 5, command = self.four)
        self.button4.grid(row = 3, column = 0, sticky = W+E+N+S)
        self.button5 = Button(self, text = '5', width = 5, command = self.five)
        self.button5.grid(row = 3, column = 1, sticky = W+E+N+S)
        self.button6 = Button(self, text = '6', width = 5, command = self.six)
        self.button6.grid(row = 3, column = 2, sticky = W+E+N+S)
        self.button1 = Button(self, text = '1', width = 5, command = self.one)
        self.button1.grid(row = 4, column = 0, sticky = W+E+N+S)                                                                                                                                                                                        
        self.button2 = Button(self, text = '2', width = 5, command = self.two)
        self.button2.grid(row = 4, column = 1, sticky = W+E+N+S)
        self.button3 = Button(self, text = '3', width = 5, command = self.three)
        self.button3.grid(row = 4, column = 2, sticky = W+E+N+S)                                                                                                                                                
        self.button0 = Button(self, text = '0', width = 5, command = self.zero)
        self.button0.grid(row = 5, column = 0, sticky = W+E+N+S)
        self.buttonDot = Button(self, text = '.', width = 5, command = 
            self.decimal)
        self.buttonDot.grid(row = 5, column = 1, sticky = W+E+N+S)
        self.buttonReciprocal = Button(self, text = '1/x', width = 5, command = 
         self.reciprocal)
        self.buttonReciprocal.grid(row = 5, column = 2, sticky = W+E+N+S)
        self.buttonMul = Button(self, text = chr(215), width = 5, command = 
            self.mult)
        self.buttonMul.grid(row = 2, column = 3, sticky = W+E+N+S)
        self.buttonDiv = Button(self, text = chr(247), width = 5, command = 
            self.division)
        self.buttonDiv.grid(row = 2, column = 4, sticky = W+E+N+S)
        self.buttonBrackOpen = Button(self, text = '(', width = 5, command = 
            self.brackOpen) #especially important in order of operations(BODMAS)
        self.buttonBrackOpen.grid(row = 3, column = 3, sticky = W+E+N+S)
        self.buttonBrackClose = Button(self, text = ')', width = 5, command = 
            self.brackClose)
        self.buttonBrackClose.grid(row = 3, column = 4, sticky = W+E+N+S)
        self.buttonPlus = Button(self, text = '+', width = 5, command = 
            self.plus)
        self.buttonPlus.grid(row = 4, column = 3, sticky = W+E+N+S)
        
        self.buttonPow = Button(self, text = 'POW', width = 5, command = 
            self.pow)
        self.buttonPow.grid(row = 5, column = 3, sticky = W+E+N+S)
         
        self.buttonMinus = Button(self, text = '-', width = 5, command = 
            self.minus)
        self.buttonMinus.grid(row = 4, column = 4, sticky = W+E+N+S)
        self.buttonEquals = Button(self, text = '=', width = 5, command = 
            self.operations)
        self.buttonEquals.grid(row = 5, column = 4,sticky = W+E+N+S)
        self.buttonClear = Button(self, text = 'Clr', width = 5, command = 
            self.clear)
        self.buttonClear.grid(row = 0, column = 4, sticky = W+E+N+S)
        self.buttonCE = Button(self, text = 'CE', width = 5, command = 
            self.CE)
        self.buttonCE.grid(row = 6, column = 4, sticky = W+E+N+S)
        
        self.buttonMplus = Button(self, text = 'M+', width = 5, command = 
            self.Mplus)
        self.buttonMplus.grid(row = 6, column = 0, sticky = W+E+N+S)
        
        self.buttonMminus = Button(self, text = 'M-', width = 5, command = 
            self.Mminus)
        self.buttonMminus.grid(row = 6, column = 1, sticky = W+E+N+S)
        self.buttonMC= Button(self, text = 'MC', width = 5, command = 
            self.MC)
        self.buttonMC.grid(row = 6, column = 2, sticky = W+E+N+S)
        self.buttonMR= Button(self, text = 'MR', width = 5, command = 
            self.MR)
        self.buttonMR.grid(row = 6, column = 3, sticky = W+E+N+S)
        
    #defining functions that control the buttons
    def seven(self):
        self.screen.insert(INSERT,'7')# simply inserts the clicked character    
    def eight(self): 
        self.screen.insert(INSERT,'8')     
    def nine(self):  
        self.screen.insert(END,'9')        
    def four(self):  
        self.screen.insert(END,'4')        
    def five(self):  
        self.screen.insert(END,'5')        
    def six(self):  
        self.screen.insert(END,'6')        
    def one(self):  
        self.screen.insert(END,'1')        
    def two(self):  
        self.screen.insert(END,'2')        
    def three(self):  
        self.screen.insert(END,'3')        
    def zero(self): 
        self.screen.insert(END,'0')        
    def decimal(self):
        self.screen.insert(END,'.')        
    def reciprocal(self):
        self.screen.delete(0,END) #removes any former digits
        self.screen.insert(END,'1.0/')
    def division(self):
        try:
            self.display.set(float(self.display.get()))#stores the information                            
            self.screen.insert(END,'/') #entered as a float to ensure correct                                 
                                        #floating point results
        except:                        
            self.screen.delete(0,END)  #catches an error incase there is any 
            self.screen.insert(END,'MATHERROR')# wrong usage of the sign.               
    def plus(self):  
        self.screen.insert(END,'+')        
    def mult(self):  
        self.screen.insert(END,'*')        
    def minus(self):  
        self.screen.insert(END,'-')        
    def brackOpen(self):
        self.screen.insert(END,'(')        
    def brackClose(self):
        self.screen.insert(END,')') 
    def pow(self):
        self.screen.insert(END,'**')       
    def CE(self): #removes the last digit on the screen
        self.display.set(self.display.get()[:-1])
    def clear(self):
        self.screen.delete(0,END) # deletes everything on the screen    
    def Mplus(self):
        self.memory += int(self.display.get())
    def Mminus(self):
        self.memory -= int(self.display.get())
    def MC(self):
        self.memory = 0
    def MR(self):
        self.display.set(self.memory)
    def operations(self):     
        try:
            v = eval(self.screen.get())
            self.screen.delete(0,END)
            self.screen.insert(END, v)         
        except: #catches errors in the formula being evaluated
            self.screen.delete(0,END)
            self.screen.insert(END,"MATH ERROR")
                       
#runs the program        
def main():
    calculator().mainloop()  
        
if __name__ == "__main__":
    main()

        
