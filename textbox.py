
from tkinter import *
from tkinter import ttk
from re import split
import numpy as np
import re

def address():
    def bit():
        my_label=Label(root,text='')
        #my_label.place(x=600,y=500)
        entry_list=''
        my_list=[]
        we=[]
        for entries in my_add:
            entry_list=entry_list+str(entries.get())+'\n'
            we=my_label.config(text=entry_list)
        for entries in my_add1:
            ent=int(entries.get())
            my_list.append(ent)
        #print(my_list)
        def bits():
            my_label=Label(root,text='')
            my_label.place(x=600,y=500)
            entry_list=''
            bitrange=[]
            bitvalue=[]
            for entries in bitranges:
                entry_list=str(entries.get())
                bitrange.append(entry_list)
            for entries in bitvalues:
                ent=int(entries.get())
                bitvalue.append(ent)
            #print(bitrange)
            #print(bitvalue)
            liist=[]
            for i in range(len(bitrange)):
                Mystring=str(bitrange[i])
                ans=str(bitvalue[i])
                A=10
                B=11
                C=12
                D=13
                E=14
                F=15
                if ans=="A":
                    ans=A
                elif ans=="B":
                    ans=B
                elif ans=="C":
                    ans=C
                elif ans=="D":
                    ans=D
                elif ans=="E":
                    ans=E
                elif ans=="F":
                    ans=F
                else:
                    pass
                regexp=re.compile(':')
                if regexp.search(Mystring):
                    splitted_string = Mystring.split(':')
                    string1 = splitted_string[0]
                    string2 = splitted_string[1]
                    int1 = int(string1)
                    int2 = int(string2)
                    int3 = int1 - int2 + 1
                    int4=int(ans)
                    #print(int3)
                    binary1 = np.binary_repr(int4, width=int3)
                    #print(binary1)
                    hexi1 = hex(int(binary1, 2))
                    #print(hexi1)
                else:
                    int1 = int(Mystring)
                    #print(int1)
                    int4=int(ans)
                    binary1 = np.binary_repr(int4, width=1)
                    #print(binary1)
                    hexi1 = hex(int(binary1, 2))
                    #print(hexi1)
                bi=len(liist)
                liist.insert(i,binary1)
            print(liist)


            '''my_labels = Label(root, text='')
            my_labels.place(x=900, y=800)
            final_list1='''''
            final_list=[]
            #listx=str(final_list[1,-1])
            #print(listx)
            p=[]
            for x in my_list:
                y = liist[0:x]
                #print(y)
                q=int(''.join(y))
                #print(q)
                p=hex(q)
                #print(p)
                del liist[0:x]
                #for final in :
                final_list.append(p)
                #print(final_list) back
            x=[]
            for t in range(0,len(final_list)):
                x.append(final_list[t])
                print(final_list[t])
                '''entn = Label(root, textvariable='')
                entn.place(x=1000,y=700)'''

            ''' my_label11 = Label(root, text='')
            my_label11.place(x=1000, y=500)
            final_list = ''
            x=[]
            for entries1 in p:
                final_list = final_list + str(entries1)
                x.append(final_list)
            my_label.config(text=x)'''



            '''my_label=Label(root,text='')     # intha line thana address print panrathu?
            my_label.place(x=800,y=500)
            entry_list=''
            for list in liist:
                entry_list=entry_list+(list)
                my_label.config(text=entry_list)'''
            Lb1 = Listbox(root,height = 10,
                  width = 100,)

            for fi in x:
                Lb1.insert(1,my_add +x)
                Lb1.place(x=500,y=400)


            Button(root, text="Submit", command=bits).place(x=1260,y=90)
        j=3
        i=2
        bitranges=[]
        bitvalues=[]

        for ta in my_list:
            #k=ta*2
            #print(k)
            label2=Label(root,text="bit range")
            label2.grid(row=i, column=4)
            label2=Label(root,text="bit value")
            label2.grid(row=i, column=5)
            for a in range(ta):
                n=StringVar()
                my_list_of_entries=Entry(root,textvariable=n)
                my_list_of_entries.grid(row=j+a,column=4,pady=1,padx=1)
                bitranges.append(my_list_of_entries)
            for l in range(ta):
                k=StringVar()
                my_list_of_entries=Entry(root,textvariable=k)
                my_list_of_entries.grid(row=j+l,column=5,pady=1,padx=1)
                bitvalues.append(my_list_of_entries)
            i=i+ta+1
            j=i+1
        Button(root, text="Submit", command=bits).place(x=1260,y=70)
    i=ent.get()
    global root, my_list_of_entries
    label2=Label(root,text="Address")
    label2.grid(row=2, column=1)
    label2=Label(root,text="No.of data field")
    label2.grid(row=2, column=2)
    label2=Label(root,text="                               ")
    label2.grid(row=2, column=3)
    my_add=[]
    my_add1=[]
    for a in range(i):
        n=StringVar()
        my_list_of_entries=Entry(root,textvariable=n)
        my_list_of_entries.grid(row=a+3,column=1,pady=1,padx=1)
        my_add.append(my_list_of_entries)
    for l in range(i):
        k=StringVar()
        my_list_of_entries=Entry(root,textvariable=k)
        my_list_of_entries.grid(row=l+3,column=2,pady=1,padx=1)
        my_add1.append(my_list_of_entries)
    Button(root, text="Submit", command=bit).place(x=1260,y=30)
root = Tk()
label2=Label(root,text="Number of Entry field")
label2.grid(row=0,column=0)
ent=IntVar()
ent2=ttk.Entry(root,textvariable=ent)
ent2.grid(row=0,column=1)
ent2.focus()
ent2.delete(0,END)
Button(root, text="Submit", command=address).place(x=1260,y=10)
root.geometry("1366x768")
root.mainloop()
