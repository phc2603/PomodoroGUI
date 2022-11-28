import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marcacoes = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset():
    global marcacoes
    tela.after_cancel(timer)
    texto.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_txt, text="00:00")
    marcacoes = ""
    checkbox.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global marcacoes
    reps += 1

    if reps % 8 == 0:
        texto.config(text="Pausa", fg=RED)
        contagem_regress(LONG_BREAK_MIN, 0)
        marcacoes += "✓"
        checkbox.config(text=marcacoes)
    elif reps % 2 == 1:
        texto.config(text="Trabalho", fg=GREEN)
        contagem_regress(WORK_MIN, 0)

    else:
        texto.config(text="Pausa", fg=PINK)
        contagem_regress(SHORT_BREAK_MIN, 0)
        marcacoes += "✓"
        checkbox.config(text=marcacoes)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def contagem_regress(minuto, segundo):
    if segundo < 10:
        comeco_aux = str(minuto) + ":0" + str(segundo)
        canvas.itemconfig(timer_txt, text=comeco_aux)
    else:
        comeco_aux = str(minuto) + ":" + str(segundo)
        canvas.itemconfig(timer_txt, text=comeco_aux)

    if minuto >= 0:
        global timer
        if segundo == 0 and minuto == 0:
            start_timer()
        elif segundo == 0:
            segundo = 60
            minuto -= 1
            timer = tela.after(1000, contagem_regress, minuto, segundo - 1)
        else:
            timer = tela.after(1000, contagem_regress, minuto, segundo-1)


# ---------------------------- UI SETUP ------------------------------- #

tela = tkinter.Tk()
tela.title("Pomodoro")
tela.minsize(width=600, height=450)
tela.config(pady="50", bg=YELLOW, padx="130")
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

#adicionando a imagem
tomate_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomate_img)#colocando a imagem com coordenadas centrais
canvas.grid(row=1, column=1)
timer_txt = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")

#criando o texto
texto = tkinter.Label(text="Timer", font=(FONT_NAME, "24", "bold"), fg=GREEN, bg=YELLOW)
texto.grid(row=0, column=1)

#botao start
botaostart = tkinter.Button(text="Start", width=10, bg="white", command=start_timer)
botaostart.grid(row=2, column=0)

#botao reset
botaoreset = tkinter.Button(text="Reset", width=10, bg="white", command=reset)
botaoreset.grid(row=2, column=2)

#checkbox
checkbox = tkinter.Label(text="", fg=GREEN, bg=YELLOW, font=12)
checkbox.grid(row=3, column=1)


tela.mainloop()