import tkinter as tk
from tkinter import ttk
from tkinter import *
import os
import subprocess

global user_name
global user_password
global common_name
global country_name
global state_name
global locality_name
global organization_name
global organization_unit
global Type
global common_name_1
global country_name_1
global state_name_1
global locality_name_1
global organization_name_1
global organization_unit_1

def validate():
    user_name = user_name_input_area.get()
    user_password = user_password_entry_area.get()

    print(user_name)
    print("Validating in Progress")
    print(user_password)
    print("validated")

def certificatedata():
    common_name = common_name_input_area.get()
    country_name = country_name_input_area.get()
    state_name = state_name_input_area.get()
    locality_name = locality_name_input_area.get()
    organization_name =organization_name_input_area.get()
    organization_unit = organization_unit_name_input_area.get()
    '''subprocess.run([
        "openssl", "genrsa", "-out", "rootCA.key", "2048"
    ], check=True)
    csr_filename = 'rootCA.csr'
    csr_cmd = 'openssl req -new -key rootCA.key -out {} -subj "/CN={}/C={}/ST={}/L={}/O={}/OU={}"'
    os.system(csr_cmd.format(csr_filename, common_name, country_name, state_name, locality_name, organization_name, organization_unit))
    # Generate a self-signed root CA certificate
    cert_filename = 'rootCA.crt'
    cert_cmd = 'openssl x509 -req -in {} -signkey rootCA.key -out {} -days 3650'
    os.system(cert_cmd.format(csr_filename, cert_filename))'''

    common_name_1 = common_name_1_input_area.get()
    country_name_1 = country_name_1_input_area.get()
    state_name_1 = state_name_1_input_area.get()
    locality_name_1 = locality_name_1_input_area.get()
    organization_name_1 =organization_name_1_input_area.get()
    organization_unit_1 = organization_unit_name_1_input_area.get()
    Type = Type_input_area.get()
    #domain_name = domain_name_input_area.get()
    '''organisation_unit = organization_unit_name_input_area.get()
    Type = Type_input_area.get()
    comman_name_2 = comman_name_input_area_2.get()
    organization_name_2 = organization_name_input_area_2.get()
    country_name_2 = country_name_input_area_2.get()
    domain_name_2 = domain_name_input_area_2.get()
    print(comman_name)'''

class Firstpage(tk.Frame):
                 def __init__(self, parent, controller):
                     tk.Frame.__init__(self, parent)
                      # Load and resize the image
                     Label= tk.Label(self, text="Renault CA")
                     Label.place(x=230, y=80)
                     Label= tk.Label(self, text="Verify User credentials")
                     Label.place(x=230, y=200)
                     Label= tk.Label(self, text="User Name")
                     Label.place(x=200, y=240)
                     global user_name_input_area
                     global user_password_entry_area
                     user_name_input_area= tk.Entry(self, width=20)
                     user_name_input_area.place(x=280,y=240)
                     Label= tk.Label(self, text="Password")
                     Label.place(x=200, y=280)
                     user_password_entry_area = tk.Entry(self, width=20)
                     user_password_entry_area.place(x=280,y=280)
                     Button= tk.Button(self, text="Click here to validate Smart Card", command=validate)
                     Button.place(x=210,y=310)
                     Label= tk.Label(self, text="Smart Card Authentication Status")
                     Label.place(x=200, y=350)
                     Label= tk.Label(self, text="Authenticated")
                     Label.place(x=400, y=350)
                     Button=tk.Button(self, text="click here to proceed", font=("worksans",10),command=lambda: controller.show_frame(Secondpage))
                     Button.place(x=650, y=450)


class Secondpage(tk.Frame):
                 def __init__(self, parent, controller):
                     tk.Frame.__init__(self, parent)
                     #Label= tk.Label(self, text="Screen 2", font= ("Worksans",15))
                     #Label.place(x=230, y=30)
                     Label= tk.Label(self, text="Certificate Authority", font=("TimesNewRoman",20, "bold"), justify="center",width=40,fg="brown")
                     Label.place(x=230, y=80)
                     Label= tk.Label(self, text="CA", font=("worksans",15))
                     Label.place(x=120, y=140)
                     Label= tk.Label(self, text="SSS", font=("worksans",15))
                     Label.place(x=520, y=140)

                     Label= tk.Label(self, text="Common Name")
                     Label.place(x=80, y=180)
                     global common_name_input_area
                     common_name_input_area= tk.Entry(self, width=20)
                     common_name_input_area.place(x=220,y=180)
                     Label= tk.Label(self, text="Type-Common name")

                     Label= tk.Label(self, text="Country")
                     Label.place(x=80, y=220)
                     global country_name_input_area
                     country_name_input_area= tk.Entry(self, width=20)
                     country_name_input_area.place(x=220,y=220)
                     Label= tk.Label(self, text="Type-Country")

                     Label= tk.Label(self, text="State/Province")
                     Label.place(x=80, y=250)
                     global state_name_input_area
                     state_name_input_area= tk.Entry(self, width=20)
                     state_name_input_area.place(x=220,y=250)
                     Label= tk.Label(self, text="Type-State/Province")
                     
                     Label= tk.Label(self, text="Localilty")
                     Label.place(x=80, y=280)
                     global locality_name_input_area
                     locality_name_input_area= tk.Entry(self, width=20)
                     locality_name_input_area.place(x=220,y=280)
                     Label= tk.Label(self, text="Type-Localilty")

                     Label= tk.Label(self, text="Organization")
                     Label.place(x=80, y=310)
                     global organization_name_input_area
                     organization_name_input_area= tk.Entry(self, width=20)
                     organization_name_input_area.place(x=220,y=310)
                     Label= tk.Label(self, text="Type-Organization")

                     Label= tk.Label(self, text="Organization Unit")
                     Label.place(x=80, y=340)
                     global organization_unit_name_input_area
                     organization_unit_name_input_area= tk.Entry(self, width=20)
                     organization_unit_name_input_area.place(x=220,y=340)
                     Label= tk.Label(self, text="Type-Organization Unit")
                     
                     '''Label= tk.Label(self, text="Domain Component")
                     Label.place(x=80, y=280)
                     global domain_name_input_area
                     domain_name_input_area= tk.Entry(self, width=20)
                     domain_name_input_area.place(x=200,y=280)
                     Label= tk.Label(self, text="Type-DEV/PROD")'''

                     Label.place(x=80, y=370)
                     global Type_input_area
                     Type_input_area= tk.Entry(self, width=20)
                     Type_input_area.place(x=220,y=370)
                     
                     Label= tk.Label(self, text="Common Name")
                     Label.place(x=450, y=180)
                     global common_name_1_input_area
                     common_name_1_input_area= tk.Entry(self, width=20)
                     common_name_1_input_area.place(x=570,y=180)
                     Label= tk.Label(self, text="Type-Common Name")

                     Label= tk.Label(self, text="Country")
                     Label.place(x=450, y=210)
                     global country_name_1_input_area
                     country_name_1_input_area= tk.Entry(self, width=20)
                     country_name_1_input_area.place(x=570,y=210)
                     Label= tk.Label(self, text="Type-Country")

                     Label= tk.Label(self, text="State/Province")
                     Label.place(x=450, y=240)
                     global state_name_1_input_area
                     state_name_1_input_area= tk.Entry(self, width=20)
                     state_name_1_input_area.place(x=570,y=240)
                     Label= tk.Label(self, text="Type-State/Province")
                     
                     Label= tk.Label(self, text="Localilty")
                     Label.place(x=450, y=270)
                     global locality_name_1_input_area
                     locality_name_input_area= tk.Entry(self, width=20)
                     locality_name_input_area.place(x=570,y=270)
                     Label= tk.Label(self, text="Type-Localilty")

                     Label= tk.Label(self, text="Organization")
                     Label.place(x=450, y=310)
                     global organization_name_1_input_area
                     organization_name_1_input_area= tk.Entry(self, width=20)
                     organization_name_1_input_area.place(x=570,y=310)
                     Label= tk.Label(self, text="Type-Organization")

                     Label= tk.Label(self, text="Organization Unit")
                     Label.place(x=450, y=340)
                     global organization_unit_name_1_input_area
                     organization_unit_name_1_input_area= tk.Entry(self, width=20)
                     organization_unit_name_1_input_area.place(x=570,y=340)
                     Label= tk.Label(self, text="Type-Organization Unit")

                     '''global domain_name_input_area_2
                     domain_name_input_area_2= tk.Entry(self, width=20)
                     domain_name_input_area_2.place(x=570,y=280)'''

                     Label= tk.Label(self, text="Platform")
                     Label.place(x=80, y=400)
                     Label= tk.Label(self, text="Crypto Graphic Settings", font=("worksans",15))
                     Label.place(x=80, y=440)
                     Label= tk.Label(self, text="Algorithm -")
                     Label.place(x=80, y=470)
                     Label= tk.Label(self, text="RSA")
                     Label.place(x=150, y=470)
                     Label= tk.Label(self, text="Number of Bits -")
                     Label.place(x=80, y=490)
                     Label= tk.Label(self, text="4096")
                     Label.place(x=170, y=490)
                     Label= tk.Label(self, text="Digest SHA 256")
                     Label.place(x=80, y=510)
                     Button= tk.Button(self, text="Generate CA and SSS certificates", command=certificatedata)
                     Button.place(x=200,y=540)
                     '''Label= tk.Label(self, text="SW", font=("worksans",15))
                     Label.place(x=820,y=140)
                     Label= tk.Label(self, text="Common Name")
                     Label.place(x=770, y=180)
                     common_name_1_input_area= tk.Entry(self, width=20)
                     common_name_1_input_area.place(x=890,y=180)
                     Label= tk.Label(self, text="Country")
                     Label.place(x=770, y=210)
                     country_name_1_input_area= tk.Entry(self, width=20)
                     country_name_1_input_area.place(x=890,y=210)
                     Label= tk.Label(self, text="State/Province")
                     Label.place(x=770, y=240)
                     state_name_1_input_area= tk.Entry(self, width=20)
                     state_name_1_input_area.place(x=890,y=240)
                     Label= tk.Label(self, text="Localilty")
                     Label.place(x=770, y=270)
                     locality_name_1_input_area= tk.Entry(self, width=20)
                     locality_name_1_input_area.place(x=890,y=270)
                     Label= tk.Label(self, text="Organization")
                     Label.place(x=770, y=310)
                     organization_name_1_input_area= tk.Entry(self, width=20)
                     organization_name_1_input_area.place(x=890,y=310)
                     Label= tk.Label(self, text="Organization Unit")
                     Label.place(x=770, y=340)
                     organization_unit_name_1_input_area= tk.Entry(self, width=20)
                     organization_unit_name_1_input_area.place(x=890,y=340)'''
                     v=tk.IntVar()
                     v.set(1)
                     platforms=[("SWEET400" ,101),
                                ("SWEET500", 102)]
                     def ShowChoice():
                         print(v.get())
                     for platform, val in platforms:
                         Radiobutton= tk.Radiobutton(self, text="SWEET400", variable=v,command=ShowChoice,value=val)
                         Radiobutton.place(x=220,y=400)
                         Radiobutton= tk.Radiobutton(self, text="SWEET500", variable=v,command=ShowChoice,value=val)
                         Radiobutton.place(x=220,y=420)
                     
                     Button=tk.Button(self, text="Back", font=("worksans",10), command=lambda: controller.show_frame(Firstpage))
                     Button.place(x=550, y=540)

                    

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args)



        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=1000)
        window.grid_columnconfigure(0, minsize=1000)


        self.frames = {}
        for F in (Firstpage,Secondpage):
            frame = F(window,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(Firstpage)

    def show_frame(self, page):
                frame = self.frames[page]
                frame.tkraise()
       

app = Application()
app.mainloop()
{
}

                
