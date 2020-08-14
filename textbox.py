
from tkinter import *
from tkinter import ttk
from re import split
import numpy as np
import re


def address():
    def bit():
        my_label = Label(root, text='')
        my_list = []
        address = []
        for add in my_add:
            address1 = (add.get())
            address.append(address1)

        for entries in my_add1:
            ent = int(entries.get())
            my_list.append(ent)
        def bits():
            my_label = Label(root, text='')
            my_label.place(x=600, y=500)
            bitrange = []
            bitvalue = []
            for entries in bitranges:
                entry_list = str(entries.get())
                bitrange.append(entry_list)
            for entries in bitvalues:
                ent = entries.get()
                bitvalue.append(ent)
            liist = []
            for i in range(len(bitrange)):
                Mystring = str(bitrange[i])
                ans = str(bitvalue[i])
                an_integer = int(ans, 16)
                hex_value = hex(an_integer)
                print(hex_value)
                regexp = re.compile(':')
                if regexp.search(Mystring):
                    splitted_string = Mystring.split(':')
                    string1 = splitted_string[0]
                    string2 = splitted_string[1]
                    int1 = int(string1)
                    int2 = int(string2)
                    int3 = int1 - int2 + 1
                    dec = int(hex_value,16)
                    final_binary =np.binary_repr (dec, width =int3)
                else:
                    dec = int(hex_value, 16)
                    final_binary = np.binary_repr(dec, width=1)
                bi = len(liist)
                liist.insert(i,final_binary)
            print(liist)

            final_list = []
            p = []
            for x in my_list:
                y = liist[0:x]
                z = y[::-1]
                q = (''.join(z))
                p = hex(int(q, 2))
                print(p)
                del liist[0:x]
                final_list.append(p)
            x = []
            for t in range(0, len(final_list)):
                x.append(final_list[t])
                print(final_list[t])
            Lb1 = Listbox(root, height=10,
                          width=70, )
            i = 1
            for fi in range(len(address)):
                Lb1.insert(i,address[fi] +"      "+ x[fi])
                Lb1.place(x=20, y=500)
                i = i + 1

            def mentry():

                #import Bit_Det
                ent2.delete(0, END)
                my_add.delete(0, END)
                my_add1.delete(0, END)
                bitrange.delete(0, END)
                bitvalue.delete(0, END)

            Button(root, text="New Entries", command=mentry).place(x=1260, y=90)
        j = 3
        i = 2
        bitranges = []
        bitvalues = []
        for ta in my_list:
            label2 = Label(root, text="bit range")
            label2.grid(row=i, column=4)
            label2 = Label(root, text="bit value")
            label2.grid(row=i, column=5)
            for a in range(ta):
                n = StringVar()
                my_list_of_entries = Entry(root, textvariable=n)
                my_list_of_entries.grid(row=j + a, column=4, pady=1, padx=1)
                bitranges.append(my_list_of_entries)
            for l in range(ta):
                k = StringVar()
                my_list_of_entries = Entry(root, textvariable=k)
                my_list_of_entries.grid(row=j + l, column=5, pady=1, padx=1)
                bitvalues.append(my_list_of_entries)
            i = i + ta + 1
            j = i + 1
        Button(root, text="Submit", command=bits).place(x=1260, y=70)

    i = ent.get()
    global root, my_list_of_entries
    label2 = Label(root, text="Address")
    label2.grid(row=2, column=1)
    label3 = Label(root, text="No.of data field")
    label3.grid(row=2, column=2)
    label3 = Label(root, text="                               ")
    label3.grid(row=2, column=3)
    my_add = []
    my_add1 = []
    for a in range(i):
        n = StringVar()
        my_list_of_entries = Entry(root, textvariable=n)
        my_list_of_entries.grid(row=a + 3, column=1, pady=1, padx=1)
        my_add.append(my_list_of_entries)
    for l in range(i):
        k = StringVar()
        my_list_of_entries = Entry(root, textvariable=k)
        my_list_of_entries.grid(row=l + 3, column=2, pady=1, padx=1)
        my_add1.append(my_list_of_entries)
    Button(root, text="Submit", command=bit).grid(row=2,column=3)


root = Tk()
label2 = Label(root, text="Number of Entry field")
label2.grid(row=0, column=0)
ent = IntVar()
ent2 = ttk.Entry(root, textvariable=ent)
ent2.grid(row=0, column=1)
ent2.focus()
ent2.delete(0, END)
Button(root, text="Submit", command=address).grid(row=0,column=2)
root.geometry("1366x768")
root.mainloop()

