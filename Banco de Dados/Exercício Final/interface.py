import PySimpleGUI as sg #pip install pysimplegui

sg.theme("DarkAmber")

layout = [[sg.Push(),sg.MLine(key="textarea", size=(50,10)),sg.Push()],
[sg.Text("Chat: "), sg.Input(key="input")],
[sg.Push(),sg.Button("Enviar"),sg.Button("Fechar"),sg.Push()]
]

window = sg.Window("Nova janela", layout)
chatLog = ''
usuario = "Abel: "
while True:
    event, values = window.read()

    if event in ('Fechar', sg.WIN_CLOSED):
        break
    if event == "Enviar":
        texto = values["input"]
        chatLog += usuario + texto + "\n"
        window["input"].update('')
        window["textarea"].update(chatLog)

window.close()