from views.customwidgets import Frame, Label, Button
from ttkbootstrap import Style
from tkinter.font import Font
from PIL import Image, ImageTk
import tkinter as tk


images = {}

def get_image(path: str):
    image = Image.open(path)
    imagetk = ImageTk.PhotoImage(image)
    
    image_name = path.split("/")[-1].split(".")[0]
    images[image_name] = imagetk

    return imagetk


class MainHeader(Frame):
    def __init__(self, parent=None, name="", _class="", *args, **kwargs):
        super().__init__(parent=parent, 
                         name=name, 
                         _class=_class, 
                         *args,
                         **kwargs)
        self.old_btn = None
        self.font_btn = Font(family="Roboto", size=12, weight="bold")
        self.__first_color = "#4582EC"
        self.__bg_color = "#D1DEF4"

        self.show_main_container()

    def show_top_header(self, parent=None) -> None:
        container = Label(parent=parent)
        container.grid(row=0, column=1, sticky="nsew")
        container.configure(style="TFrame", background=self.__first_color)

        logo = get_image("resources/images/logo.png")
        logo_container = Label(parent=container, image=logo)
        logo_container.pack(side="left", padx=8, pady=0, ipadx=0, ipady=0)
        logo_container.configure(background=self.__first_color, border=0)

    def configure_btn(self, event) -> None:
        widget = event.widget
        self.span_width = widget.winfo_width()        

        if self.old_btn == None:
            self.old_btn = self.__appointment_btn

            span = Frame(self.old_btn, name="span",
                    height=5,
                    width = self.span_width)

            self.span_y = widget.winfo_height() - 5
            span.place(x=0, y=self.span_y)

            self.old_btn.add_child(span)

    def button_click(self, event) -> None:
        widget = event.widget
        widget.configure(style="CustomActive.TButton")

        old_span = self.old_btn.remove_child("span")
        old_span.destroy()

        self.old_btn.configure(style="CustomDisable.TButton")

        self.old_btn = widget
        span = Frame(self.old_btn, name="span",
                height=5,
                width = self.span_width)

        self.span_y = widget.winfo_height() - 5
        span.place(x=0, y=self.span_y)
        self.old_btn.add_child(span)

    def set_button_style(self) -> None:
        style = self.get_parent().get_style()
        style.configure(style="CustomActive.TButton", 
                font=self.font_btn,
                foreground="#FFFFFF",
                relief="solid")

        style.configure(style="CustomDisable.TButton",
                font=self.font_btn,
                foreground="#B9D1FB",
                relief="solid")

    def show_button_appointment(self, parent=None) -> None:
        self.__appointment_btn = Button(parent=parent,
                name="appointment-btn",
                text="Consultas")
        self.__appointment_btn.grid(row=0, column=0, sticky="nsew")

        self.__appointment_btn.configure(style="CustomActive.TButton")

        self.__appointment_btn.bind("<Configure>", self.configure_btn)
        self.__appointment_btn.bind("<1>", self.button_click)

        parent.columnconfigure(0, weight=1)

    def show_button_doctor(self, parent=None) -> None:
        self.__doctor_btn = Button(parent=parent,
                name="doctor-btn",
                text="Médico")
        self.__doctor_btn.grid(row=0, column=1, sticky="nsew")

        self.__doctor_btn.configure(style="CustomDisable.TButton")

        self.__doctor_btn.bind("<Configure>", self.configure_btn)
        self.__doctor_btn.bind("<1>", self.button_click)

        parent.columnconfigure(1, weight=1)

    def show_button_patient(self, parent=None) -> None:
        self.__patient_btn = Button(parent=parent,
                name="patient-btn",
                text="Paciente")
        self.__patient_btn.grid(row=0, column=2, sticky="nsew")

        self.__patient_btn.configure(style="CustomDisable.TButton")

        self.__patient_btn.bind("<Configure>", self.configure_btn)
        self.__patient_btn.bind("<1>", self.button_click)

        parent.columnconfigure(2, weight=1)

    def show_bottom_header(self, parent=None) -> None:
        container = Label(parent=parent)
        container.grid(row=1, column=1, sticky="nsew")
        container.configure(style="TFrame", background=self.__first_color)

        self.set_button_style()

        self.show_button_appointment(parent=container)
        self.show_button_doctor(parent=container)
        self.show_button_patient(parent=container)

        container.rowconfigure(0, weight=1)


    def show_main_container(self) -> None:
        main_container = Label(parent=self, name="main_container")
        main_container.grid(row=0, column=0, sticky="nsew")
        main_container.configure(style="TFrame", background=self.__first_color)

        main_header_span_height = Label(parent=main_container)
        main_header_span_height.grid(row=0, 
                column=0, 
                rowspan=2, 
                ipady=55,
                ipadx=0)
        main_header_span_height.configure(style="TFrame", 
                background=self.__first_color,
                border=0)

        self.show_top_header(parent=main_container)
        self.show_bottom_header(parent=main_container)
        main_container.columnconfigure(0, weight=0)
        main_container.columnconfigure(1, weight=1)
        
        span_width = Frame(parent=self)
        header_width = self.get_parent().get_screenwidth() // 2
        span_width.grid(row=1, column=0, sticky="nsew", ipadx=header_width)

