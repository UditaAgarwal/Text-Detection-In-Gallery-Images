label_0 = Label(root, text="Text Detection In Gallery Images",width=40,font=("Helvetica 14 bold", 20))
label_0.place(x=120,y=53)

label_1 = Label(root, text="Enter the text you want to search",width=45,font=("bold", 13))
label_1.place(x=170,y=165)

entry_1 = Entry(root)
entry_1.place(x=500,y=165)

Button(root, text='ENTER',width=22,bg='blue',fg='white').place(x=360,y=270)

label_2 = Label(root, text="NOTE:",width=10,font=("bold", 13))
label_2.place(x=10,y=400)
label_3 = Label(root, text="* All the images that needs to be detected should be in the SOURCE Folder.",width=59,font=("bold", 11))
label_3.place(x=10,y=430)
label_4 = Label(root, text="* The searched images are Stored in the DESTINATION Folder.",width=50,font=("bold", 11))
label_4.place(x=10,y=460)