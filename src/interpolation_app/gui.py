import customtkinter as ctk
import pandas as pd

from tkinter import filedialog


ctk.set_appearance_mode(
    'System'
)


class InterpolationApp(
    ctk.CTk
):
    def __init__(
        self
    ):
        super().__init__()

        self.title(
            'Interpolation'
        )
        self.geometry(
            '1000x800'
        )
        self.resizable(False, False)

        graph_window = ctk.CTkFrame(
            self,
            600,
            600
        )
        graph_window.place(
            relx=0.35,
            rely=0.5,
            anchor='center'
        )

        self._data = None
        def select_file():
            file_path = filedialog.askopenfilename(
                title='Select a file',
                filetypes=[
                    ('CSV files', '*.csv'),
                    ('All files', '*.*')
                ]
            )
            self._data = pd.read_csv(
                file_path
            )

        load_data_button = ctk.CTkButton(
            self,
            text='Load data',
            font=('Arial', 14, 'bold'),
            command=select_file
        )
        load_data_button.place(
            relx=0.8,
            rely=0.3,
            anchor='center'
        )

        degree_slider = ctk.CTkSlider(
            self,
            from_=0,
            to=10,
            number_of_steps=10,
            command=lambda degree: degree_label.configure(
                text=f'Polynomial degree: {int(degree)}'
            )
        )
        degree_slider.set(
            0
        )
        degree_slider.place(
            relx=0.8,
            rely=0.4,
            anchor='center'
        )

        degree_label = ctk.CTkLabel(
            self,
            text='Polynomial degree: 0'
        )
        degree_label.place(
            relx=0.8,
            rely=0.45,
            anchor='center'
        )

        method_label = ctk.CTkLabel(
            self,
            text='Interpolation method',
            font=('Arial', 14, 'bold')
        )
        method_label.place(
            anchor='center',
            relx=0.8,
            rely=0.55
        )
        method = ctk.StringVar(value='Polynomial')
        poly_button = ctk.CTkRadioButton(
            self,
            text='Linear',
            variable=method,
            value='Linear'
        )
        poly_button.place(
            anchor='w',
            relx=0.75,
            rely=0.6)
        nn_button = ctk.CTkRadioButton(
            self,
            text='Neural network',
            variable=method,
            value='Neural network'
        )
        nn_button.place(
            anchor='w',
            relx=0.75,
            rely=0.65)

if __name__ == '__main__':
    app = InterpolationApp()
    app.mainloop()
