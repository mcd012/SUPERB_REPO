import customtkinter as ctk

ctk.set_appearance_mode(
    'System'
)

app = ctk.CTk()
app.title(
    'Interpolation'
)
app.geometry(
    '1000x800'
)
app.resizable(False, False)

graph_window = ctk.CTkFrame(
    app,
    600,
    600
)
graph_window.place(
    relx=0.35,
    rely=0.5,
    anchor='center'
)

degree_slider = ctk.CTkSlider(
    app,
    from_=0,
    to=10,
    number_of_steps=10,
    command=lambda degree: degree_label.configure(
        text=f'Degree: {int(degree)}'
    )
)
degree_slider.set(
    0
)
degree_slider.place(
    relx=0.8,
    rely=0.6,
    anchor='center'
)


degree_label = ctk.CTkLabel(app, text="Polynomial degree: 0")
degree_label.place(
    relx=0.8,
    rely=0.65,
    anchor='center'
)


app.mainloop()
