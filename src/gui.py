import tkinter
import customtkinter
from tkinter.messagebox import showinfo

from packages.fa.dfa import DFA
from packages.fa.nfa import NFA
import utils.gui_setup as setup

# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_appearance_mode("System")
# Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    WIDTH = 780
    HEIGHT = 820

    def __init__(self):
        super().__init__()

        self.dfa = DFA()
        self.nfa = DFA()

        self.title("TRABALHO PRÁTICO - FTC")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # call .on_closing() when app gets closed
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(0, minsize=10)
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)
        # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(
            master=self.frame_left, text="Tipos", text_font=("Roboto Medium", -16))
        self.label_radio_group.grid(row=0, column=0, pady=30, padx=10)

        self.radio_var = tkinter.IntVar(value=0)

        self.radio_button_1 = customtkinter.CTkRadioButton(
            master=self.frame_left, variable=self.radio_var, value=0, text="AFD")
        self.radio_button_1.grid(row=1, column=0, pady=10, padx=10)
        

        self.radio_button_2 = customtkinter.CTkRadioButton(
            master=self.frame_left, value=1, variable=self.radio_var ,text="AFN")
        self.radio_button_2.grid(row=2, column=0, pady=10, padx=10)
        
        self.radio_button_3 = customtkinter.CTkRadioButton(
            master=self.frame_left, variable=self.radio_var, value=2, text="APD/APN")
        self.radio_button_3.grid(row=3, column=0, pady=10, padx=10)
        self.radio_button_3.configure(state=tkinter.DISABLED)

        self.label_mode = customtkinter.CTkLabel(
            master=self.frame_left, text="Tema da Aplicação:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left, values=[
                                                        "Light", "Dark", "System"], command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        #self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        #self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2,
                             rowspan=4, pady=20, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        self.label_info_1 = customtkinter.CTkLabel(master=self.frame_info,
                                                   text="Preencha todos os inputs\n" +
                                                        "Antes de computar uma palavra\n",
                                                   height=100,
                                                   corner_radius=6,  # <- custom corner radius
                                                   # <- custom tuple-color
                                                   fg_color=(
                                                       "white", "gray38"),
                                                   justify=tkinter.LEFT)
        self.label_info_1.grid(column=0, row=0, sticky="nwe", padx=15, pady=15)


        # ============ frame_right ============

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Estados")
        self.entry.grid(row=4, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="definir",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_5.grid(row=4, column=2, columnspan=1,
                           pady=20, padx=20, sticky="we")

        self.entry_1 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Alfabeto")
        self.entry_1.grid(row=5, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_6 = customtkinter.CTkButton(master=self.frame_right,
                                                text="definir",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event_option_2)
        self.button_6.grid(row=5, column=2, columnspan=1,
                           pady=20, padx=20, sticky="we")

        self.entry_2 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Estado Inicial")
        self.entry_2.grid(row=6, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_7 = customtkinter.CTkButton(master=self.frame_right,
                                                text="definir",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_7.grid(row=6, column=2, columnspan=1,
                           pady=20, padx=20, sticky="we")

        self.entry_3 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Estado Final")
        self.entry_3.grid(row=7, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_8 = customtkinter.CTkButton(master=self.frame_right,
                                                text="definir",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_8.grid(row=7, column=2, columnspan=1,
                           pady=20, padx=20, sticky="we")

        self.entry_4 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Transição")
        self.entry_4.grid(row=8, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_9 = customtkinter.CTkButton(master=self.frame_right,
                                                text="adicionar",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_9.grid(row=8, column=2, columnspan=1,
                           pady=20, padx=20, sticky="we")

        self.entry_5 = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            placeholder_text="Palavra")
        self.entry_5.grid(row=10, column=0, columnspan=2,
                        pady=20, padx=20, sticky="we")

        self.button_10 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Computar!",
                                                border_width=2,  # <- custom border_width
                                                fg_color=None,  # <- no fg_color
                                                command=self.button_event)
        self.button_10.grid(row=10, column=2, columnspan=1,
                           pady=20, padx=20, sticky="we")

        # set default values
        self.optionmenu_1.set("Dark")    

    def button_event_option_2(self):
        if self.radio_var.get() == 0:
            sigma = setup.set_S_dfa(self.entry_1.get())
            if sigma != None:
                self.dfa.set_sigma()
            self.dfa.display()
        else:
            sigma = setup.set_S_nfa(self.entry_1.get())
            if sigma != None:
                self.nfa.set_sigma()
            self.nfa.display()


    def button_event(self):
        showinfo("Window", "Hello World!", icon="error")
        print(self.entry.get())

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()