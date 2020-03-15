
#!py -3.4

import tkinter as Tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import os
import random

'''Hello anyone reading this! Don't mind the disgusting code in some places. I'm not that good at coding, so don't expect it to work perfectly!
Anyways, hopefully you'll find some enjoyment messing around with this corrupter. Ciao!'''

buildNumber = "13"
versionNumber = "v1.1"
goodIcon = "favi16.ico"

root = Tk()
root.title("Scares Scrambler Build "+buildNumber)
root.geometry("310x600+100+100")
root.iconbitmap(goodIcon)
#root.resizable(width=False, height=False)

'''
Engines:
    0 = Incrementer
    1 = Randomizer
    2 = Scrambler
    3 = Copier
    4 = Tilter
    6 = Sentence Mixer (Text Only)

Unbinding is apparently possible: foo.unbind("<Button-1>")
showerror, showinfo, showwarning, _show? ~These are all message box types.
http://wiki.tcl.tk/37701 ~Hex codes work as well
font="Times"'''

currentEngine = 0
autoEndBool = False
exclusiveBool = False
hexadecimalMode = False
darkMode = False
blockSpaceState = "Linear"

fileName = ""
newFileName = ""
newPresetName = ""

cnameLabel = ""

allWidgets = []
dynamicWidgets = []

listOfEngines = ["Algoritm Incrementer", "Algoritm Randomizer", "Algoritm Scrambler  ",
                 "Algoritm Copier    ", "Algoritm Tilter     ", "Algoritm Mixer "]


class entry_function_class:
    
    def __init__(self, entryBox):
        self.entryBox = entryBox

    def left_click_function(self, event=None):
        '''Increments the entries'''
        try:
            if hexadecimalMode:
                incValue = incValueEntry.get()
                entryBoxValue = self.entryBox.get()
                incValue = hex_convert(incValue)
                entryBoxValue = hex_convert(entryBoxValue)
                entryBoxValue = int(entryBoxValue)
                entryBoxValue += int(incValue)
                self.entryBox.delete(0, "end")
                if entryBoxValue < 0:
                    entryBoxValue = 0
                entryBoxValue = hex_convert(entryBoxValue, hexMode=False)
            else:
                incValue = int(incValueEntry.get()) #Getting values
                entryBoxValue = int(self.entryBox.get())
                entryBoxValue += incValue #Setting values
                self.entryBox.delete(0, "end")
                if entryBoxValue < 0:
                    entryBoxValue = 0
            self.entryBox.insert(0, entryBoxValue)
        except ValueError:
            messagebox.showwarning("Ce faci?", "Foloseste un număr întreg pt."
                                   " valoarea increment!")


    def right_click_function(self, event=None):
        '''Decrements the values'''
        try:
            if hexadecimalMode:
                incValue = incValueEntry.get()
                entryBoxValue = self.entryBox.get()
                incValue = hex_convert(incValue)
                entryBoxValue = hex_convert(entryBoxValue)
                entryBoxValue = int(entryBoxValue)
                entryBoxValue -= int(incValue)
                self.entryBox.delete(0, "end")
                if entryBoxValue < 0:
                    entryBoxValue = 0
                entryBoxValue = hex_convert(entryBoxValue, hexMode=False)
            else:
                incValue = int(incValueEntry.get()) #Getting values
                entryBoxValue = int(self.entryBox.get())
                entryBoxValue -= incValue #Setting values
                self.entryBox.delete(0, "end")
                if entryBoxValue < 0:
                    entryBoxValue = 0
            self.entryBox.insert(0, entryBoxValue)
        except ValueError:
            messagebox.showwarning("Ce faci?", "Foloseste un număr întreg pt."
                                    " valoarea increment!")


    def generate_random_byte(self, event=None):
        '''Generates a number between 1 and 255'''
        self.entryBox.delete(0, "end")
        if hexadecimalMode:
            ran1 = random.randint(0, 15)
            ran2 = random.randint(0, 15)
            ran1 = singular_hex_convert(ran1)
            ran2 = singular_hex_convert(ran2)

            self.entryBox.insert(0, str(ran1)+str(ran2))
        else:
            self.entryBox.insert(0, random.randint(0, 255))


def change_engine_right(event=None):
    global currentEngine
    '''Changes the engine label'''
    currentEngine += 1
    if currentEngine > (len(listOfEngines)-1):
        currentEngine = 0
    engineLabel.config(text=listOfEngines[currentEngine])
    update_layout()


def change_engine_left(event=None):
    global currentEngine
    '''Changes the engine label'''
    currentEngine -= 1
    if currentEngine < 0:
        currentEngine = len(listOfEngines)-1
    engineLabel.config(text=listOfEngines[currentEngine])
    update_layout()


def hide_dynamic_widgets():
    global dynamicWidgets
    '''Hides dynamic widgets, dummy'''
    for x in dynamicWidgets:
        x.grid_forget()


def update_layout():
    '''Updates the layout, dummy'''
    #Do something with the allWidgets list later
    hide_dynamic_widgets()
    if currentEngine == 0: #Incrementer
        blockSizeLabel.grid(row=5, column=0, pady=5, padx=5, sticky=E)
        blockSizeEntry.grid(row=5, column=1, columnspan=2, pady=5)
        blockSizeButton.grid(row=5, column=3, pady=5)

        linearRadio.grid(row=6, column=0, pady=5)
        exponentialRadio.grid(row=6, column=1, pady=5, sticky=E)
        randomRadio.grid(row=6, column=3, pady=5, sticky=E)

        blockSpaceLabel.grid(row=7, column=0, pady=5, padx=5, sticky=E)
        blockSpaceEntry.grid(row=7, column=1, columnspan=2, pady=5)
        blockSpaceButton.grid(row=7, column=3, pady=5)

        addValueLabel.grid(row=8, column=0, pady=5, padx=5, sticky=E)
        addValueEntry.grid(row=8, column=1, columnspan=2, pady=5)
        addValueButton.grid(row=8, column=3, pady=5)
    elif currentEngine == 1: #Randomizer
        blockSizeLabel.grid(row=5, column=0, pady=5, padx=5, sticky=E)
        blockSizeEntry.grid(row=5, column=1, columnspan=2, pady=5)
        blockSizeButton.grid(row=5, column=3, pady=5)

        linearRadio.grid(row=6, column=0, pady=5)
        exponentialRadio.grid(row=6, column=1, pady=5, sticky=E)
        randomRadio.grid(row=6, column=3, pady=5, sticky=E)

        blockSpaceLabel.grid(row=7, column=0, pady=5, padx=5, sticky=E)
        blockSpaceEntry.grid(row=7, column=1, columnspan=2, pady=5)
        blockSpaceButton.grid(row=7, column=3, pady=5)
    elif currentEngine == 2: #Scrambler
        blockSizeLabel.grid(row=5, column=0, pady=5, padx=5, sticky=E)
        blockSizeEntry.grid(row=5, column=1, columnspan=2, pady=5)
        blockSizeButton.grid(row=5, column=3, pady=5)

        linearRadio.grid(row=6, column=0, pady=5)
        exponentialRadio.grid(row=6, column=1, pady=5, sticky=E)
        randomRadio.grid(row=6, column=3, pady=5, sticky=E)

        blockSpaceLabel.grid(row=7, column=0, pady=5, padx=5, sticky=E)
        blockSpaceEntry.grid(row=7, column=1, columnspan=2, pady=5)
        blockSpaceButton.grid(row=7, column=3, pady=5)
        
        blockGapLabel.grid(row=8, column=0, pady=5, padx=5, sticky=E)
        blockGapEntry.grid(row=8, column=1, columnspan=2, pady=5)
        blockGapButton.grid(row=8, column=3, pady=5)
    elif currentEngine == 3: #Copier
        blockSizeLabel.grid(row=5, column=0, pady=5, padx=5, sticky=E)
        blockSizeEntry.grid(row=5, column=1, columnspan=2, pady=5)
        blockSizeButton.grid(row=5, column=3, pady=5)

        linearRadio.grid(row=6, column=0, pady=5)
        exponentialRadio.grid(row=6, column=1, pady=5, sticky=E)
        randomRadio.grid(row=6, column=3, pady=5, sticky=E)

        blockSpaceLabel.grid(row=7, column=0, pady=5, padx=5, sticky=E)
        blockSpaceEntry.grid(row=7, column=1, columnspan=2, pady=5)
        blockSpaceButton.grid(row=7, column=3, pady=5)
        
        blockGapLabel.grid(row=8, column=0, pady=5, padx=5, sticky=E)
        blockGapEntry.grid(row=8, column=1, columnspan=2, pady=5)
        blockGapButton.grid(row=8, column=3, pady=5)

    elif currentEngine == 4: #Tilter
        blockSizeLabel.grid(row=5, column=0, pady=5, padx=5, sticky=E)
        blockSizeEntry.grid(row=5, column=1, columnspan=2, pady=5)
        blockSizeButton.grid(row=5, column=3, pady=5)

        linearRadio.grid(row=6, column=0, pady=5)
        exponentialRadio.grid(row=6, column=1, pady=5, sticky=E)
        randomRadio.grid(row=6, column=3, pady=5, sticky=E)

        blockSpaceLabel.grid(row=7, column=0, pady=5, padx=5, sticky=E)
        blockSpaceEntry.grid(row=7, column=1, columnspan=2, pady=5)
        blockSpaceButton.grid(row=7, column=3, pady=5)

        replaceLabel.grid(row=8, column=0, pady=5, padx=5, sticky=E)
        replaceEntry.grid(row=8, column=1, columnspan=2, pady=5)
        replaceButton.grid(row=8, column=3, pady=5)

        replaceWithLabel.grid(row=9, column=0, pady=5, padx=5, sticky=E)
        replaceWithEntry.grid(row=9, column=1, columnspan=2, pady=5)
        replaceWithButton.grid(row=9, column=3, pady=5)

        replaceXCheck.grid(row=10, column=1, pady=5, padx=30, sticky=W, columnspan=2)
    elif currentEngine == 5: #Mixer
        mixerLabel.grid(row=5, column=0)


def auto_end_switch(event=None):
    global autoEndBool
    '''Yes'''
    if autoEndBool:
        autoEndBool = False
    else:
        autoEndBool = True


def exclusive_switch(event=None):
    global exclusiveBool
    '''Toggles the switch'''
    if exclusiveBool:
        exclusiveBool = False
    else:
        exclusiveBool = True


def hexadecimal_switch(event=None):
    global hexadecimalMode
    '''Toggles the switch'''
    if hexadecimalMode:
        hexadecimalMode = False
    else:
        hexadecimalMode = True


def check_for_period(text):
    '''Checks to see if there's a period in the given text'''
    isDot = False
    for x in text:
        if x == ".":
            isDot = True

    if isDot:
        return True
    else:
        return False


def clear_newFileText(event):
    '''Clears newFileText when it's clicked'''
    global newFileText
    newFileText.delete("1.0", END)


def enter_file(event=None):
    global fileName
    global userFileWindow
    global userFileEntry
    global newFileText
    global fileName
    global newFileName
    global cnameLabel
    '''Chooses the files to use during corrupting'''
    userFileWindow = Tk()
    userFileWindow.title("Introdu fi?iere...")
    userFileWindow.geometry("450x175+250+250")
    userFileWindow.iconbitmap(goodIcon)
    userFileWindow.resizable(width=False, height=False)

    mainFrame = Frame(userFileWindow)
    applyFrame = Frame(userFileWindow)

    instLabel = Label(mainFrame, text="Selectează fisierul pentru corupt, si pune un nume nou:")
    cfileLabel = Label(mainFrame, text="Fisier pt. corupt:")
    
    if fileName == "":
        cnameLabel = Label(mainFrame, text="Niciun fisier selectat")
    else:
        cnameLabel = Label(mainFrame, text="..."+fileName[len(fileName)-25:])

    userFileButton = Button(mainFrame, text="Selectează un fisier")
    nfileLabel = Label(mainFrame, text="Fisier nou:")
    newFileText = Text(mainFrame)
    applyButton = Button(applyFrame, text=" Aplică ")

    if darkMode:
        userFileWindow.config(bg="#1c1c1c")
        mainFrame.config(bg="#1c1c1c")
        applyFrame.config(bg="#1c1c1c")
        instLabel.config(bg="#1c1c1c", fg="#c8c8c8")
        cfileLabel.config(bg="#1c1c1c", fg="#c8c8c8")
        cnameLabel.config(bg="#1c1c1c", fg="#c8c8c8")
        userFileButton.config(bg="#1c1c1c", fg="#c8c8c8", activebackground="#1c1c1c", activeforeground="#c8c8c8")
        nfileLabel.config(bg="#1c1c1c", fg="#c8c8c8")
        newFileText.config(bg="#1c1c1c", fg="#c8c8c8")
        applyButton.config(bg="#1c1c1c", fg="#c8c8c8", activebackground="#1c1c1c", activeforeground="#c8c8c8")

    userFileButton.bind("<Button-1>", select_file)
    applyButton.bind("<Button-1>", get_file_name)

    newFileText.config(width=25, height=1)

    if newFileName == "":
        newFileText.insert(END, "Pune un nume nou...")
    else:
        newFileText.insert(END, newFileName)

    newFileText.bind("<Button-1>", clear_newFileText)

    mainFrame.pack()
    applyFrame.pack()

    instLabel.grid(row=1, column=1, columnspan=10, padx=40, pady=10)
    cfileLabel.grid(row=2, column=1, columnspan=2, padx=0, pady=5)
    cnameLabel.grid(row=2, column=3, columnspan=5, padx=10, pady=5)
    userFileButton.grid(row=2, column=8, padx=20, pady=5)
    nfileLabel.grid(row=3, column=1, columnspan=2, padx=0, pady=5)
    newFileText.grid(row=3, column=3, columnspan=5, padx=28, pady=5)
    applyButton.grid(row=4, column=1, columnspan=1, padx=10, pady=15)

    userFileWindow.mainloop()


def select_file(event=None):
    global fileName
    '''Opens an 'open' window to select the file to corrupt'''
    fileName = askopenfilename()
    cnameLabel.config(text="..."+fileName[len(fileName)-25:])
    

def get_file_name(event=None):
    global userFileWindow
    global userFileLabel
    global newFileText
    global newFileName
    global fileName
    '''Gets the file name that the user entered'''
    newFileName = newFileText.get(1.0, END)
    newFileName = newFileName[:-1]

    if not check_for_period(newFileName):
        for x in range(0, len(fileName)): #Getting the file extension
            if fileName[len(fileName)-x-1] == ".":
                newFileName += fileName[(-x-1):]
                break
           
    if len(fileName) <= 40:
        userFileLabel.config(text=fileName)
    else:
        userFileLabel.config(text="..."+fileName[len(fileName)-40:])
    userFileWindow.destroy()
    

def blockSpaceState_to_linear(event=None): #Now this is good coding
    global blockSpaceState
    global blockStateVar
    '''Changes blockSpaceState to Linear'''
    blockSpaceState = "Linear"
    blockStateVar.set(1)
    blockSpaceLabel.config(text="Spatiu Bloc")


def blockSpaceState_to_exponential(event=None):
    global blockSpaceState
    global blockStateVar
    '''Changes blockSpaceState to Exponential'''
    blockSpaceState = "Exponential"
    blockStateVar.set(2)
    blockSpaceLabel.config(text="Exponent")


def blockSpaceState_to_random(event=None):
    global blockSpaceState
    global blockStateVar
    '''Changes blockSpaceState to Random'''
    blockSpaceState = "Random"
    blockStateVar.set(3)
    blockSpaceLabel.config(text="Upper Bound")


def about_program_window(event=None):
    '''The about window'''
    aboutWindow = Tk()
    
    aboutWindow.title("About Scares Scrambler Build "+buildNumber+" "+"("+versionNumber+")")
    aboutWindow.iconbitmap(goodIcon)

    infoLabel = Label(aboutWindow, text="Program creat de omul tău, Scares. Testat de numai Telic.")
    infoLabel2 = Label(aboutWindow, text="Acesta este un proiect open-source, așa că nu ezitați să vă încurcați în cod și chestii.")
    infoLabel3 = Label(aboutWindow, text="Dacă doriți să lansați propria versiune modificată a acestui proiect, pune-mi numele aici! : 3")
    infoLabel4 = Label(aboutWindow, text="Aș dori, de asemenea, să mulțumesc enorm tuturor celor care s-au alăturat să încerce acest lucru!")
    infoLabel5 = Label(aboutWindow, text="Știu că acesta nu este cel mai bun coruptor, dar am încercat să-l fac cât mai special.")
    infoLabel7 = Label(aboutWindow, text="Tradus de The Techno Guy18 thetechnoguy18@yahoo.com www.youtube.com/TheTechnoGuy18")

    if darkMode:
        infoLabel.config(bg="#1c1c1c", fg="#c8c8c8")
        infoLabel2.config(bg="#1c1c1c", fg="#c8c8c8")
        infoLabel3.config(bg="#1c1c1c", fg="#c8c8c8")
        infoLabel4.config(bg="#1c1c1c", fg="#c8c8c8")
        infoLabel5.config(bg="#1c1c1c", fg="#c8c8c8")
        infoLabel7.config(bg="#1c1c1c", fg="#c8c8c8")
        aboutWindow.config(bg="#1c1c1c")
        goodLogo = PhotoImage(master=aboutWindow, file="darkLogo.png")
        infoLabel6 = Label(aboutWindow, image=goodLogo)
    else:
        goodLogo = PhotoImage(master=aboutWindow, file="logo.png")
        infoLabel6 = Label(aboutWindow, image=goodLogo)

    infoLabel.pack()
    infoLabel2.pack()
    infoLabel3.pack()
    infoLabel4.pack()
    infoLabel5.pack()
    infoLabel6.pack()
    infoLabel7.pack()

    aboutWindow.mainloop()
    

def add_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize, addValue):
    '''Does adding and subtracting'''

    for y in range(0, blockSize): #Corrupting part
        currentByte = baseFile.read(1) #Gets the byte
        if currentByte == b"":
            break
        currentByte = int.from_bytes(currentByte, byteorder="big")
        currentByte += addValue
        if currentByte > 255 or currentByte < 0: #If it's bigger than a byte OR if it's a negative
            currentByte = currentByte % 256
        currentByte = (currentByte).to_bytes(1, byteorder="big")
        corruptedFile.write(currentByte)

    copy_file_contents(baseFile, corruptedFile, blockSpace) #The gap in between - Shoutout to Jason


def random_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize):
    '''Does random byte changes'''

    for y in range(0, blockSize): #Corrupting part
        currentByte = baseFile.read(1) #Gets the byte
        if currentByte == b"":
            break
        currentByte = int.from_bytes(currentByte, byteorder="big")
        currentByte += random.randrange(0, 255)
        if currentByte > 255: #If it's bigger than a byte
            currentByte = currentByte % 256
        currentByte = (currentByte).to_bytes(1, byteorder="big")
        corruptedFile.write(currentByte)

    copy_file_contents(baseFile, corruptedFile, blockSpace) #The gap in between


def scrambler_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize, blockGap):
    '''Does scrambles to bytes'''
    currentByteList1 = []
    bufferList = []
    currentByteList2 = []

    for y in range(0,blockSize): #Corrupting part
        currentByte = baseFile.read(1)
        if currentByte == b"":
            break
        currentByteList1.append(currentByte) #Gets the bytes

    for z in range(0, blockGap): #The gap in between
        currentByte = baseFile.read(1)
        if currentByte == b"":
            break
        bufferList.append(currentByte)

    for y in range(0, blockSize): #Corrupting part
        currentByte = baseFile.read(1)
        if currentByte == b"":
            break
        currentByteList2.append(currentByte) #Gets the bytes
        
    for x in currentByteList2:
        corruptedFile.write(x)

    for x in bufferList:
        corruptedFile.write(x)

    for x in currentByteList1:
        corruptedFile.write(x)

    copy_file_contents(baseFile, corruptedFile, blockSpace) #The gap in between


def copier_corrupt_engine(baseFile, corruptedFile, blockSpace, corruptEndByte, blockSize, blockGap):
    '''Does copying stuff'''
    currentByteList1 = []
    bufferList = []
    currentByteList2 = []
    counter = 0

    for y in range(0, blockSize):
        currentByte = baseFile.read(1)
        if currentByte == b"":
            break
        currentByteList1.append(currentByte)

    for z in range(0, blockGap):
        currentByte = baseFile.read(1)
        if currentByte == b"":
            break
        bufferList.append(currentByte)

    for y in range(0, blockSize):
        currentByte = baseFile.read(1)
        if currentByte == b"":
            break
        currentByteList2.append(currentByte)

    if (blockGap * -1) > blockGap: #Negative
        for x in currentByteList2:
            if corruptedFile.tell() >= corruptEndByte:
                break
            corruptedFile.write(x)
        for x in bufferList:
            if corruptedFile.tell() >= corruptEndByte:
                break
            corruptedFile.write(x)
        for x in currentByteList2:
            if corruptedFile.tell() >= corruptEndByte:
                break
            corruptedFile.write(x)
    else: #Positive
        for x in currentByteList1:
            if corruptedFile.tell() >= corruptEndByte:
                break
            corruptedFile.write(x)
        for x in bufferList:
            if corruptedFile.tell() >= corruptEndByte:
                break
            corruptedFile.write(x)
        for x in currentByteList1:
            if corruptedFile.tell() >= corruptEndByte:
                break
            corruptedFile.write(x)

    copy_file_contents(baseFile, corruptedFile, blockSpace)


def tilter_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize, replace, replaceWith):
    '''You know what it does by now'''

    for y in range(0, blockSize): #Corrupting part
        currentByte = baseFile.read(1) #Gets the byte
        if currentByte == b"":
            break
        currentByte = int.from_bytes(currentByte, byteorder="big")

        if exclusiveBool:
            compareByte = replace
            if currentByte == compareByte:
                currentByte = replaceWith
        else:
            currentByte = replaceWith
            
        currentByte = (currentByte).to_bytes(1, byteorder="big")
        corruptedFile.write(currentByte)

    copy_file_contents(baseFile, corruptedFile, blockSpace)


def copy_file_contents(baseFile, corruptedFile, endValue):
    '''For copying uncorrupted parts of a file'''
    
    for z in range(0, endValue): #The gap in between
        currentByte = baseFile.read(1)
        corruptedFile.write(currentByte) #The gap in between


def hex_convert(number, isFloat=False, hexMode=True):
    '''Converts the input to hexadecimal, or to a number'''
    newNum = ""
        
    if not hexMode: #Convert number to hex
        keepGoing = True
        counter = 0
        while keepGoing: #Checking to see the highest power of 16 that can go into the number
            if number//16**counter == 0:
                keepGoing = False
            else:
                counter += 1

        keepGoing = True
        counter = counter - 1
        tempNum = 0
        number2 = number
        while keepGoing: #Subtract multiples of powers of 16 to get the hex representation
            tempNum = number2//16**counter
            tempNum = singular_hex_convert(tempNum)

            newNum += str(tempNum)
            tempNum2 = hex_convert(str(tempNum))
            number2 -= 16**counter*tempNum2
            counter -= 1 #Fuck you
            if counter == -1:
                keepGoing = False

    else: #Convert hex to number
        if number[0] == "-":
            newNum = "-0x" + number[1:]
        else:
            newNum = "0x" + number

        newNum = float.fromhex(newNum)
        if not isFloat:
            newNum = int(newNum)
        
    return newNum


def singular_hex_convert(n):
    '''Converts the numbers 10 to 16 to hex'''
    newN = n
    if n == 10:
        newN = "a"
    elif n == 11:
        newN = "b"
    elif n == 12:
        newN = "c"
    elif n == 13:
        newN = "d"
    elif n == 14:
        newN = "e"
    elif n == 15:
        newN = "f"

    return newN
        

def corrupt_file(event=None):
    global newFileName
    '''Corrupts the chosen file'''
    nullCounter2 = 0

    try:
        if hexadecimalMode: #Changing hexadecimal values to ints
            startValue = hex_convert(startValueEntry.get())
            if not autoEndBool:
                endValue = hex_convert(endValueEntry.get())
            blockSize = hex_convert(blockSizeEntry.get())
            if blockSpaceState == "Exponential":
                blockSpace = hex_convert(blockSpaceEntry.get(), True)
            else:
                 blockSpace = hex_convert(blockSpaceEntry.get())
            blockSize = hex_convert(blockSizeEntry.get())
            if currentEngine == 0:
                addValue = hex_convert(addValueEntry.get())
            elif currentEngine == 2 or currentEngine == 3:
                blockGap = hex_convert(blockGapEntry.get())
            elif currentEngine == 4:
                replace = hex_convert(replaceEntry.get())
                replaceWith = hex_convert(replaceWithEntry.get())

        else:
            startValue = int(startValueEntry.get())
            if not autoEndBool:
                endValue = int(endValueEntry.get())
            blockSize = int(blockSizeEntry.get())
            if blockSpaceState == "Exponential":
                blockSpace = float(blockSpaceEntry.get())
            else:
                 blockSpace = int(float(blockSpaceEntry.get()))
            blockSize = int(blockSizeEntry.get())
            if currentEngine == 0:
                addValue = int(addValueEntry.get())
            if currentEngine == 2 or currentEngine == 3:
                blockGap = int(blockGapEntry.get())
            if currentEngine == 4:
                replace = int(replaceEntry.get())
                replaceWith = int(replaceWithEntry.get())
            
        if fileName == "":
            messagebox.showinfo("Măi băiete!", "Trebuie să alegi un fisier înainte de a "
                                " corupe! Apasă Alt+F pt. selectare")
        else:
            baseFile = open(fileName, "rb+")
            if newFileName == "":
                corruptedFile = open("CorruptedFile.txt", "wb+")
            else:
                corruptedFile = open(newFileName, "wb+")

            baseFile.seek(startValue) #Goto the start byte
            if not autoEndBool: #If auto end is turned off
                corruptEndByte = endValue

            else: #If auto end is on
                nullCounter = startValue
                while True:
                    nullTester = baseFile.read(1)
                    if nullTester != b"": #If the byte isn't empty
                        nullCounter = baseFile.tell()
                    else:
                        break
                corruptEndByte = nullCounter
                    
            baseFile.seek(0) #Goto the start byte
            if currentEngine <= 5: #All current engines

                copy_file_contents(baseFile, corruptedFile, startValue)
                
                if blockSpaceState == "Linear":
                    corruptStepSize = blockSize + blockSpace
                    for x in range(startValue, corruptEndByte, corruptStepSize): #Through the file

                        if currentEngine == 0:
                            add_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize, addValue)
                        elif currentEngine == 1:
                            random_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize)
                        elif currentEngine == 2:
                            scrambler_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize, blockGap)
                        elif currentEngine == 3:
                            copier_corrupt_engine(baseFile, corruptedFile, blockSpace, corruptEndByte, blockSize, blockGap)
                        elif currentEngine == 4:
                            tilter_corrupt_engine(baseFile, corruptedFile, blockSpace, blockSize, replace, replaceWith)

                elif blockSpaceState == "Exponential":
                    nullCounter = baseFile.tell()
                    exponentPower = blockSpace
                    exponentCounter = 1
                    exponentCap = False
                    exponentCapValue = 1000000

                    while nullCounter < corruptEndByte: #Through the file

                        try: #Fixes the exponent from getting too big
                            if int(exponentCounter**exponentPower) > exponentCapValue: #If exponent is too big
                                exponentCap = True
                        except OverflowError:
                            exponentCap = True

                        if not exponentCap:
                            if currentEngine == 0:
                                add_corrupt_engine(baseFile, corruptedFile, int(exponentCounter**exponentPower), blockSize, addValue)
                            elif currentEngine == 1:
                                random_corrupt_engine(baseFile, corruptedFile, int(exponentCounter**exponentPower), blockSize)
                            elif currentEngine == 2:
                                scrambler_corrupt_engine(baseFile, corruptedFile, int(exponentCounter**exponentPower), blockSize, blockGap)
                            elif currentEngine == 3:
                                copier_corrupt_engine(baseFile, corruptedFile, int(exponentCounter**exponentPower), corruptEndByte, blockSize, blockGap)
                            elif currentEngine == 4:
                                tilter_corrupt_engine(baseFile, corruptedFile, int(exponentCounter**exponentPower), blockSize, replace, replaceWith)
                        else:
                            if currentEngine == 0:
                                add_corrupt_engine(baseFile, corruptedFile, exponentCapValue, blockSize, addValue)
                            elif currentEngine == 1:
                                random_corrupt_engine(baseFile, corruptedFile, exponentCapValue, blockSize)
                            elif currentEngine == 2:
                                scrambler_corrupt_engine(baseFile, corruptedFile, exponentCapValue, blockSize, blockGap)
                            elif currentEngine == 3:
                                copier_corrupt_engine(baseFile, corruptedFile, exponentCapValue, corruptEndByte, blockSize, blockGap)
                            elif currentEngine == 4:
                                tilter_corrupt_engine(baseFile, corruptedFile, exponentCapValue, blockSize, replace, replaceWith)


                        if exponentCap:
                            nullCounter += exponentCapValue
                        else:
                            nullCounter += int(exponentCounter**exponentPower)
                            exponentCounter += 1

                elif blockSpaceState == "Random":
                    nullCounter = startValue
                    if blockSpace == 0: #Prevents random number from being zero
                        blockSpace = 1
                    
                    while nullCounter < corruptEndByte: #Through the file
                        tempRand = random.randrange(0, blockSpace+1)
                        
                        if currentEngine == 0:
                            add_corrupt_engine(baseFile, corruptedFile, tempRand, blockSize, addValue)
                        elif currentEngine == 1:
                            random_corrupt_engine(baseFile, corruptedFile, tempRand, blockSize)
                        elif currentEngine == 2:
                            scrambler_corrupt_engine(baseFile, corruptedFile, tempRand, blockSize, blockGap)
                        elif currentEngine == 3:
                            copier_corrupt_engine(baseFile, corruptedFile, tempRand, corruptEndByte, blockSize, blockGap)
                        elif currentEngine == 4:
                            tilter_corrupt_engine(baseFile, corruptedFile, tempRand, blockSize, replace, replaceWith)

                        nullCounter += tempRand
                        
                while True: #This finishes the uncorrupted part
                    currentByte = baseFile.read(1)
                    if currentByte == b"":
                        break
                    corruptedFile.write(currentByte)

        baseFile.close()
        corruptedFile.close()
        
    except ValueError:
        messagebox.showwarning("Hei!", "Valorile tale nu sunt valide. Asigură-te că sunt corecte! "
                               "Unele valori nu pot fi decimale, deci... uită-te si pe acolo!!")
    except IndexError:
        messagebox.showwarning("Hei!", "Asigură-te că toate valorile sunt prezente!")


def save_presets_window(event=None):
    global newPresetName
    global newPresetEntry
    global newPresetWindow
    '''The UI for saving a preset'''
    
    newPresetWindow = Tk()
    newPresetWindow.title("Pune un nume pentru preset...")
    newPresetWindow.geometry("300x100+250+250")
    newPresetWindow.iconbitmap(goodIcon)
    newPresetWindow.resizable(width=False, height=False)

    newPresetName = ""
    newPresetLabel = Label(newPresetWindow, text="Pune numele noului fisier preset")
    newPresetEntry = Entry(newPresetWindow)
    newPresetButton = Button(newPresetWindow, text=" Ok ")
    newPresetButton.bind("<Button-1>", save_presets)

    if darkMode:
        newPresetWindow.config(bg="#1c1c1c")
        newPresetEntry.config(bg="#1c1c1c", fg="#c8c8c8")
        newPresetLabel.config(bg="#1c1c1c", fg="#c8c8c8")
        newPresetButton.config(bg="#1c1c1c", fg="#c8c8c8", activebackground="#1c1c1c", activeforeground="#c8c8c8")

    newPresetLabel.pack()
    newPresetEntry.pack()
    newPresetButton.pack()

    newPresetWindow.mainloop()


def save_presets(event=None):
    global newPresetEntry
    '''Saves the presets to a text file'''
    
    presetList = []

    presetList.append("~~preset~~")
    presetList.append(fileName)
    presetList.append(newFileName)

    presetList.append(startValueEntry.get())
    presetList.append(endValueEntry.get())
    presetList.append(incValueEntry.get())
    presetList.append(autoEndBool)
    presetList.append(blockSizeEntry.get())
    presetList.append(blockSpaceState)
    presetList.append(blockSpaceEntry.get())
    presetList.append(addValueEntry.get())
    presetList.append(blockGapEntry.get())
    presetList.append(exclusiveBool)
    presetList.append(replaceEntry.get())
    presetList.append(replaceWithEntry.get())

    presetList.append(hexadecimalMode)
    name = newPresetEntry.get()

    if name[-4:] == ".txt": #If there's a file extension
        presetFile = open(name, "w")
        for x in presetList:
            presetFile.write(str(x))
            presetFile.write("\n")
        presetFile.close()
    else:
        presetFile = open(name+".txt", "w")
        for x in presetList:
            presetFile.write(str(x))
            presetFile.write("\n")
        presetFile.close()

    newPresetWindow.destroy()


def load_presets(event=None, coolName=""):
    global fileName
    global newFileName
    global startValueEntry
    global endValueEntry
    global incValueEntry
    global autoEndBool
    global autoEndVar
    global autoEndCheck
    global blockSizeEntry
    global blockSpaceState
    global blockSpaceEntry
    global addValueEntry
    global blockGapEntry
    global exclusiveBool
    global exclusiveVar
    global replaceEntry
    global replaceWithEntry
    global hexadecimalMode
    global hexVar

    global userFileLabel
    '''Loads the presets from the text file'''
    #Fix all the try/excepts later
    
    manualSelect = False

    try:
        if coolName == "": #If no name was entered
            presetFile = askopenfilename()
            presetFile = open(presetFile, "r")
            manualSelect = True
        else: #Use the name given
            presetFile = open(coolName, "r")

        try:
            tempVar = ""
            tag = presetFile.readline()
            if tag == "~~preset~~\n":
                
                fileName = presetFile.readline()[:-1]
                newFileName = presetFile.readline()[:-1]
                startValueEntry.delete(0, END)
                startValueEntry.insert(0, presetFile.readline()[:-1])
                endValueEntry.delete(0, END)
                endValueEntry.insert(0, presetFile.readline()[:-1])
                incValueEntry.delete(0, END)
                incValueEntry.insert(0, presetFile.readline()[:-1])
                
                tempVar = presetFile.readline()
                if tempVar[:len(tempVar)-1] == "True":
                    autoEndBool = True
                    autoEndVar.set(1)
                elif tempVar[:len(tempVar)-1] == "False":
                    autoEndBool = False
                    autoEndVar.set(0)

                blockSizeEntry.delete(0, END)
                blockSizeEntry.insert(0, presetFile.readline()[:-1])
                
                blockSpaceState = presetFile.readline()[:-1]
                if blockSpaceState == "Linear":
                    blockSpaceState_to_linear()
                elif blockSpaceState == "Exponential":
                    blockSpaceState_to_exponential()
                elif blockSpaceState == "Aleatoriu":
                    blockSpaceState_to_random()
                
                blockSpaceEntry.delete(0, END)
                blockSpaceEntry.insert(0, presetFile.readline()[:-1])
                addValueEntry.delete(0, END)
                addValueEntry.insert(0, presetFile.readline()[:-1])
                blockGapEntry.delete(0, END)
                blockGapEntry.insert(0, presetFile.readline()[:-1])

                tempVar = presetFile.readline()
                if tempVar[:len(tempVar)-1] == "True":
                    exclusiveBool = True
                    exclusiveVar.set(1)
                elif tempVar[:len(tempVar)-1] == "False":
                    exclusiveBool = False
                    exclusiveVar.set(0)

                replaceEntry.delete(0, END)
                replaceEntry.insert(0, presetFile.readline()[:-1])
                replaceWithEntry.delete(0, END)
                replaceWithEntry.insert(0, presetFile.readline()[:-1])

                tempVar = presetFile.readline()
                if tempVar[:len(tempVar)-1] == "True":
                    hexadecimalMode = True
                    hexVar.set(1)
                elif tempVar[:len(tempVar)-1] == "False":
                    hexadecimalMode = False
                    hexVar.set(0)

                if len(fileName) <= 40:
                    userFileLabel.config(text=fileName)
                else:
                    userFileLabel.config(text="..."+fileName[len(fileName)-40:])

            else: #If the text file isn't a preset
                if manualSelect:
                    messagebox.showwarning("Hei!", "Fisierul selectat nu este un preset!")

        except: #If the file doesn't have lines to read?
            messagebox.showwarning("Hei!", "Fisierul selectat de preset nu este valid!")

        presetFile.close()
        
    except FileNotFoundError:
        messagebox.showinfo("Hei!", "Fisierul selectat nu a fost găsit!")


def dark_mode(event=None):
    global allWidgets
    global darkMode
    global bannerLabel
    '''Changes the GUI to be dark, or light again'''
    #SystemButtonFace - greyish bg
    #SystemButtonText - text colour
    #SystemWindow - Entry Colour (white) and black select colour for checks and radios

    if not darkMode:
        for x in allWidgets:
            if isinstance(x, Tkinter.Entry) or isinstance(x, Tkinter.Label):
                x.config(bg="#1c1c1c", fg="#c8c8c8")
            elif isinstance(x, Tkinter.Checkbutton) or isinstance(x, Tkinter.Radiobutton):
                x.config(bg="#1c1c1c", fg="#c8c8c8", selectcolor="#000000", activebackground="#1c1c1c", activeforeground="#c8c8c8")
            elif isinstance(x, Tkinter.Button):
                x.config(bg="#1c1c1c", fg="#c8c8c8", activebackground="#1c1c1c", activeforeground="#c8c8c8")
            else:
                x.config(bg="#1c1c1c")
            bannerLabel.config(image=darkBanner)
            darkMode = True

    else:
        for x in allWidgets:
            if isinstance(x, Tkinter.Entry):
                x.config(bg="SystemWindow", fg="SystemButtonText")
            elif isinstance(x, Tkinter.Label):
                x.config(bg="SystemButtonFace", fg="SystemButtonText")
            elif isinstance(x, Tkinter.Checkbutton) or isinstance(x, Tkinter.Radiobutton):
                x.config(bg="SystemButtonFace", fg="SystemButtonText", selectcolor="SystemWindow", activebackground="SystemButtonFace", activeforeground="SystemButtonText")
            elif isinstance(x, Tkinter.Button):
                #x.config(bg="SystemButtonFace", fg="SystemButtonText", activebackground="SystemButtonFace", activeforeground="SystemWindow")
                x.config(bg="SystemButtonFace", fg="SystemButtonText")
            else:
                x.config(bg="SystemButtonFace")
            bannerLabel.config(image=goodBanner)
            darkMode = False


parentMenu = Menu(root)

fileMenu = Menu(parentMenu, tearoff=0)
optionsMenu = Menu(parentMenu, tearoff=0)
aboutMenu = Menu(parentMenu, tearoff=0)
parentMenu.add_cascade(label="Fisier", menu=fileMenu)
parentMenu.add_cascade(label="Optiuni", menu=optionsMenu)
parentMenu.add_cascade(label="Despre", menu=aboutMenu)

#foreground="grey50"

fileMenu.add_command(label="Alege fisier", accelerator="Alt+F", command=enter_file)
fileMenu.add_separator()
fileMenu.add_command(label="Salvează preset", accelerator="Alt+S", command=save_presets_window)
fileMenu.add_command(label="Încarcă presey", accelerator="Alt+L", command=load_presets)

hexVar = IntVar()
darkVar = IntVar()
optionsMenu.add_checkbutton(label="Mod Hexadecimal", command=hexadecimal_switch, var=hexVar)
optionsMenu.add_checkbutton(label="Mod de noapte", command=dark_mode, var=darkVar)

aboutMenu.add_command(label="Info", accelerator="Alt+I", command=about_program_window)

#----------------------------------------------------------------------------------

mainFrame = Frame(root, width=310, height=500)
corruptButtonFrame = Frame(root)

goodBanner = PhotoImage(file="banner.png")
darkBanner = PhotoImage(file="darkBanner.png")
bannerLabel = Label(root, image=goodBanner)

engineLeftButton = Button(mainFrame, text="<")
engineLabel = Label(mainFrame, text="Algoritm Incrementer")
engineRightButton = Button(mainFrame, text=">")

startValueLabel = Label(mainFrame, text="Valoare de start")
startValueEntry = Entry(mainFrame)
startValueClass = entry_function_class(startValueEntry)
startValueEntry.insert(0, 0)
startValueButton = Button(mainFrame, text="+/-")

endValueLabel = Label(mainFrame, text="Valoare de sfârsit")
endValueEntry = Entry(mainFrame)
endValueClass = entry_function_class(endValueEntry)
endValueEntry.insert(0, 0)
endValueButton = Button(mainFrame, text="+/-")

autoEndVar = IntVar()
incValueLabel = Label(mainFrame, text="Valoare Increment")
incValueEntry = Entry(mainFrame)
autoEndCheck = Checkbutton(mainFrame, text="Auto Terminare", var=autoEndVar)

dividerLabel = Label(mainFrame, text="------------------------------------------------------------")

blockSizeLabel = Label(mainFrame, text="Mărime Bloc")
blockSizeEntry = Entry(mainFrame)
blockSizeClass = entry_function_class(blockSizeEntry)
blockSizeButton = Button(mainFrame, text="Aleatoriu")

blockStateVar = IntVar()
blockStateVar.set(1)
linearRadio = Radiobutton(mainFrame, text="Linear", value=1, variable=blockStateVar)
exponentialRadio = Radiobutton(mainFrame, text="Exponential", value=2, variable=blockStateVar)
randomRadio = Radiobutton(mainFrame, text="Aleatoriu", value=3, variable=blockStateVar)

blockSpaceLabel = Label(mainFrame, text="Spatiu Bloc")
blockSpaceEntry = Entry(mainFrame)
blockSpaceClass = entry_function_class(blockSpaceEntry)
blockSpaceButton = Button(mainFrame, text="Aleatoriu")

addValueLabel = Label(mainFrame, text="Adunare/Scădere")
addValueEntry = Entry(mainFrame)
addValueClass = entry_function_class(addValueEntry)
addValueButton = Button(mainFrame, text="Aleatoriu")

blockGapLabel = Label(mainFrame, text="Decalaj Bloc")
blockGapEntry = Entry(mainFrame)
blockGapClass = entry_function_class(blockGapEntry)
blockGapButton = Button(mainFrame, text="Aleatoriu")

exclusiveVar = IntVar()
replaceXCheck = Checkbutton(mainFrame, text="Exclusiv", var=exclusiveVar)

replaceLabel = Label(mainFrame, text="Înlociueste")
replaceEntry = Entry(mainFrame)
replaceClass = entry_function_class(replaceEntry)
replaceButton = Button(mainFrame, text="Aleatoriu")

replaceWithLabel = Label(mainFrame, text="Înlocuieste cu")
replaceWithEntry = Entry(mainFrame)
replaceWithClass = entry_function_class(replaceWithEntry)
replaceWithButton = Button(mainFrame, text="Aleatoriu")

mixerLabel = Label(mainFrame, text="Întodeauna un WIP")

userFileLabel = Label(corruptButtonFrame, text=fileName)
corruptButton = Button(corruptButtonFrame, text="Corupe!", font="Helvetica 25")

#----------------------------------------------------------------------------------

allWidgets.append(root)

allWidgets.append(mainFrame)
allWidgets.append(corruptButtonFrame)

allWidgets.append(engineLeftButton)
allWidgets.append(engineLabel)
allWidgets.append(engineRightButton)

allWidgets.append(startValueLabel)
allWidgets.append(startValueEntry)
allWidgets.append(startValueButton)

allWidgets.append(endValueLabel)
allWidgets.append(endValueEntry)
allWidgets.append(endValueButton)

allWidgets.append(incValueEntry)
allWidgets.append(incValueLabel)
allWidgets.append(autoEndCheck)

allWidgets.append(dividerLabel)

allWidgets.append(blockSizeLabel)
allWidgets.append(blockSizeEntry)
allWidgets.append(blockSizeButton)

allWidgets.append(linearRadio)
allWidgets.append(exponentialRadio)
allWidgets.append(randomRadio)

allWidgets.append(blockSpaceLabel)
allWidgets.append(blockSpaceEntry)
allWidgets.append(blockSpaceButton)

allWidgets.append(addValueLabel)
allWidgets.append(addValueEntry)
allWidgets.append(addValueButton)

allWidgets.append(blockGapLabel)
allWidgets.append(blockGapEntry)
allWidgets.append(blockGapButton)

allWidgets.append(replaceXCheck)

allWidgets.append(replaceLabel)
allWidgets.append(replaceEntry)
allWidgets.append(replaceButton)

allWidgets.append(replaceWithLabel)
allWidgets.append(replaceWithEntry)
allWidgets.append(replaceWithButton)

allWidgets.append(mixerLabel)

allWidgets.append(userFileLabel)
allWidgets.append(corruptButton)

#Dynamic Widgets

dynamicWidgets.append(blockSizeLabel)
dynamicWidgets.append(blockSizeEntry)
dynamicWidgets.append(blockSizeButton)

dynamicWidgets.append(linearRadio)
dynamicWidgets.append(exponentialRadio)
dynamicWidgets.append(randomRadio)

dynamicWidgets.append(blockSpaceLabel)
dynamicWidgets.append(blockSpaceEntry)
dynamicWidgets.append(blockSpaceButton)

dynamicWidgets.append(addValueLabel)
dynamicWidgets.append(addValueEntry)
dynamicWidgets.append(addValueButton)

dynamicWidgets.append(blockGapLabel)
dynamicWidgets.append(blockGapEntry)
dynamicWidgets.append(blockGapButton)

dynamicWidgets.append(replaceXCheck)

dynamicWidgets.append(replaceLabel)
dynamicWidgets.append(replaceEntry)
dynamicWidgets.append(replaceButton)

dynamicWidgets.append(replaceWithLabel)
dynamicWidgets.append(replaceWithEntry)
dynamicWidgets.append(replaceWithButton)

dynamicWidgets.append(mixerLabel)



#----------------------------------------------------------------------------------

engineLeftButton.bind("<Button-1>", change_engine_left)
engineRightButton.bind("<Button-1>", change_engine_right)

startValueButton.bind("<Button-1>", startValueClass.left_click_function)
endValueButton.bind("<Button-1>", endValueClass.left_click_function)
startValueButton.bind("<Button-3>", startValueClass.right_click_function)
endValueButton.bind("<Button-3>", endValueClass.right_click_function)

autoEndCheck.bind("<Button-1>", auto_end_switch)

blockSizeButton.bind("<Button-1>", blockSizeClass.generate_random_byte)
blockSpaceButton.bind("<Button-1>", blockSpaceClass.generate_random_byte)

linearRadio.bind("<Button-1>", blockSpaceState_to_linear)
exponentialRadio.bind("<Button-1>", blockSpaceState_to_exponential)
randomRadio.bind("<Button-1>", blockSpaceState_to_random)

addValueButton.bind("<Button-1>", addValueClass.generate_random_byte)
blockGapButton.bind("<Button-1>", blockGapClass.generate_random_byte)

replaceXCheck.bind("<Button-1>", exclusive_switch)
replaceButton.bind("<Button-1>", replaceClass.generate_random_byte)
replaceWithButton.bind("<Button-1>", replaceWithClass.generate_random_byte)

corruptButton.bind("<Button-1>", corrupt_file)

#------------------------------------------------------------------------------------

bannerLabel.pack()

mainFrame.pack()
corruptButtonFrame.pack(side=BOTTOM)

engineLeftButton.grid(row=0, column=0, pady=5)
engineLabel.grid(row=0, column=0, columnspan=3, pady=5, sticky=E)
engineRightButton.grid(row=0, column=3, pady=5)

startValueLabel.grid(row=1, column=0, padx=5, pady=5, sticky=E)
startValueEntry.grid(row=1, column=1, columnspan=2, pady=5)
startValueButton.grid(row=1, column=3, padx=20, pady=5)

endValueLabel.grid(row=2, column=0, padx=5, pady=5, sticky=E)
endValueEntry.grid(row=2, column=1, columnspan=2, pady=5)
endValueButton.grid(row=2, column=3, padx=20, pady=5)

incValueLabel.grid(row=3, column=0, pady=5, padx=5, sticky=E)
incValueEntry.grid(row=3, column=1, columnspan=2, pady=5)
autoEndCheck.grid(row=3, column=3, pady=5)

dividerLabel.grid(row=4, column=0, pady=5, columnspan=4)
update_layout()

userFileLabel.pack(pady=5)
corruptButton.pack(pady=5)

root.config(menu=parentMenu)

root.bind("<Alt-f>", enter_file)
root.bind("<Alt-i>", about_program_window)
root.bind("<Alt-s>", save_presets_window)
root.bind("<Alt-l>", load_presets)
root.bind("<Left>", change_engine_left)
root.bind("<Right>", change_engine_right)

try: #Looking to see if preset exists
    for f in os.listdir():
        if f.endswith('.txt'):
            load_presets(coolName=f)
except FileNotFoundError:
    pass

root.mainloop()









