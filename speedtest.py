from tkinter import *
import speedtest 
root=Tk()

root.geometry("800x600")
root.title("Speed test by speed")
root.config(bg="#dee8f1")

internetspeed_check=Label(root,text="Internet speed check",font=("Lucida Sans Unicode",20,"bold","italic"),fg="orange",bg="#dee8f1")     
internetspeed_check.place(relx=0.5,rely=0.2,anchor=CENTER)

download=Label(root,text="Download Speed",font=("Segoe Print",18,"bold"),fg="red",bg="#dee8f1")
download.place(relx=0.3,rely=0.6,anchor=CENTER)

upload=Label(root,text="Upload Speed",font=("Segoe Print",18,"bold"),fg="blue",bg="#dee8f1")
upload.place(relx=0.7,rely=0.6,anchor=CENTER)

D_speed=Label(root)
D_speed.place(relx=0.3,rely=0.7,anchor=CENTER)

U_speed=Label(root)
U_speed.place(relx=0.7,rely=0.7,anchor=CENTER)

def speedcheck():
    speed=speedtest.Speedtest()
    D_S=round(speed.download()/1000000,2)
    U_S=round(speed.upload()/1000000,2)
    print(D_S)
    print(U_S)
    D_speed["text"]=str(D_S)+"mbps"
    U_speed["text"]=str(U_S)+"mbps"
    

btn=Button(root,text="check speed",font=("Segoe Print",15,"bold"),fg="green",bg="#dee8f1",command= speedcheck)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

root.mainloop()
