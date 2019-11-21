from tkinter import *
from tkinter import messagebox

win = Tk()
win.title('Subtitle Fixer')
win.geometry('420x180')


def conversion(filename,edit): 
    file = open(filename, 'r')
    sub = file.readlines()
    file.close()
    time_line = []
    c = -1
    abs_time = 0
    for line in sub:
        if '-->' in line:
            time_line.append([line.strip()[:12],line.strip()[17:]])
    del sub
    for i in time_line:
        c += 1
        for j in range(2):
            abs_time = int(i[j][:2])*60*60
            abs_time += int(i[j][3:5])*60
            abs_time += int(i[j][6:8])
            abs_time = abs_time * 1000
            abs_time = abs_time + int(i[j][9:]) + user_change(edit)
            time_line[c][j] = abs_time
    return (time_line)

def user_change(c):
    abs_change = int(c[1:3])*60*60
    abs_change += int(c[4:6])*60
    abs_change += int(c[7:9])
    abs_change = abs_change * 1000
    abs_change = abs_change + int(c[10:])
    if c[0] == '-' : return (-1*abs_change)
    return abs_change

def main(filef, edit):
    converted = conversion(filef, edit)
    output = []
    for x in converted:
        temp = []
        for y in x:
            mili = int(y) % 1000
            secs = (int(y) // 1000) % 60
            mins = ((int(y) // 1000) // 60) % 60
            hours = ((int(y) // 1000) // 60) // 60
            temp.append(str(hours).zfill(2)+':'+str(mins).zfill(2)+':'+str(secs).zfill(2)+','+str(mili).zfill(3))
        output.append(temp)
        del temp
    final = ''
    count = -1
    file = open(filef,'r')
    text = file.readlines()
    file.close()
    for t in text:
        if '-->' in t:
            count += 1
            final += str(output[count][0]).strip()+' --> '+str(output[count][1]).strip()+'\n'
            continue
        final += t
    fin = open('Fixed_subtitles.srt','w')
    fin.write(final)
    fin.close()
    Label(win,text='Done Syncing').grid(row=5,column=5)

## GUI PART
def input_check1(): ##This is checking the import file format
    if (len(hours.get())+len(minutes.get())+len(seconds.get())+len(milisecs.get())) != 9:
        messagebox.showinfo("What've you done",'Follow the given format')
        return False
    if hours.get().isalnum()==True or minutes.get().isalnum()==True or seconds.get().isalnum==True or milisecs.get().isalnum==True:
        messagebox.showinfo("Dumbo",'Numbers are acceptable only')
        return False
    return True

def input_check0(): ## This is checking the time input format
    if filename.get()=='':
        messagebox.showinfo('OH Dear God','Empty Import Field')
        return False
    elif filename.get()[-3:] != 'srt':
        messagebox.showinfo('Invalid Extension','SRT files are acceptable')
        return False
    Label(win, text='Imported!').grid(row=0,column=7,columnspan=4)
    return True
    
def importing():
    if input_check0() == True:
        return filename.get()

def forwarding():
    if input_check1() == True:
        filename = importing()
        edit = '+'+hours.get()+':'+minutes.get()+':'+seconds.get()+':'+milisecs.get()
        main(filename,edit)

def backwarding():
    if input_check1() == True:
        filename = importing()
        edit = '-'+hours.get()+':'+minutes.get()+':'+seconds.get()+':'+milisecs.get()
        main(filename,edit)
        
def about():
    messagebox.showinfo('Version 1.0','Created by Faaz Abidi')

Label(win,text='Import .SRT File').grid(row=0,column=0)
filename = Entry(win)
filename.grid(row=0,column=1,columnspan=3)
filein = Button(win,text='Import',command = importing) # calling import
filein.grid(row=0,column=3,pady=5,columnspan=5)
Label(win, text='Time').grid(row=1,column=0)
Label(win, text=' : ').grid(row=1,column=2)
Label(win, text=' : ').grid(row=1,column=4)
Label(win, text=' , ').grid(row=1,column=6)
hours = Entry(win,width=10)
minutes = Entry(win,width=10)
seconds = Entry(win,width=10)
milisecs = Entry(win,width=10)
hours.grid(row=1,column=1)
minutes.grid(row=1,column=3)
seconds.grid(row=1,column=5)
milisecs.grid(row=1,column=7)
Label(win, text='hours').grid(row=2,column=1)
Label(win, text='minutes').grid(row=2,column=3)
Label(win, text='seconds').grid(row=2,column=5)
Label(win, text='miliseconds').grid(row=2,column=7)
Label(win,text='Follow the same input format: 00:00:00,123').grid(row=3,columnspan=10,pady=2)
Label(win,text='Subtitle Fixer and the SRT file should be in the same directory').grid(row=4,columnspan=10,pady=5)
forward = Button(win,text='Forward',command = forwarding)  ## calling forwarding function
backward = Button(win,text='Backward', command = backwarding) ## calling backwarding function
forward.grid(row=6,column=7,pady=5)
backward.grid(row=6,column=0)
about = Button(win,text='About',command=about).grid(row=6,column=1) ##credits

win.mainloop()
