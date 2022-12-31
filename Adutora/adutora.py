from elementos import *

def paginaAtiva(pagina):
    global cabecalho, inferiorBT, tela

    pagina["bg"] = rgb_to_hex(127, 174, 0)
    cabecalho["text"] = pagina["text"]

    for element in menuEsquerdoBT:
        if element["text"] != pagina["text"]:
            element["bg"] = rgb_to_hex(100, 150, 0)
    
    ## Botões
    if inferiorBT == None:
        inferiorBT = [button(styleBT, inferiorFM, "+", 0, 0).display(),
                      button(styleBT, inferiorFM, "EDITAR", 0, 1).display(),
                      button(styleBT, inferiorFM, "-", 0, 2).display()]  
    else:
        for element in inferiorBT:
            element.destroy()
        
        tela.destroy()

        if pagina["text"] == "PESSOAS":
            tela = listbox(styleLI, paginaFM, 1, 0).display()
            inferiorBT = [button(styleBT, inferiorFM, "+", 0, 0).display(),
                          button(styleBT, inferiorFM, "EDITAR", 0, 1).display(),
                          button(styleBT, inferiorFM, "-", 0, 2).display()]

        elif pagina["text"] == "DADOS GERAIS":
            tela = text(styleTX, paginaFM, 1, 0).display()
            inferiorBT = [button(styleBT, inferiorFM, "EDITAR", 0, 1).display()]

        elif pagina["text"] == "METRAGEM":
            tela = text(styleTX, paginaFM, 1, 0).display()
            inferiorBT = [button(styleBT, inferiorFM, "+", 0, 0).display(),
                          button(styleBT, inferiorFM, "EDITAR", 0, 1).display(),
                          button(styleBT, inferiorFM, "RESETAR", 0, 2).display()]

        elif pagina["text"] == "PAPÉIS":
            tela = listbox(styleLI, paginaFM, 1, 0).display()
            inferiorBT = [button(styleBT, inferiorFM, "PAGAR", 0, 0).display(),
                          button(styleBT, inferiorFM, "GERAR", 0, 1).display(),
                          button(styleBT, inferiorFM, "TAXAR", 0, 2).display()]

        elif pagina["text"] == "ATUAL":
            tela = text(styleTX, paginaFM, 1, 0).display()
            inferiorBT = [button(styleBT, inferiorFM, "IMPORTAR", 0, 0).display(),
                          button(styleBT, inferiorFM, "EDITAR", 0, 1).display()]

        elif pagina["text"] == "ANTERIOR":
            tela = text(styleTX, paginaFM, 1, 0).display()
            inferiorBT = [button(styleBT, inferiorFM, "IMPORTAR", 0, 0).display(),
                          button(styleBT, inferiorFM, "EDITAR", 0, 1).display()]
        

"""LABEL"""

# BT = Button
# FM = Frame
# LB = Label
# TX = Text
# LI = Listbox

janela = Tk()
janela.title("Adutora")
janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

# Estilo dos Frames
styleFM = {"bg": rgb_to_hex(127, 174, 0),
           "bd": 0,
           "relief": "flat",
           "padx": 0,
           "pady": 0,
           "ipadx": 0,
           "ipady": 0,
           "sticky": "NSEW"}

# Estilo dos Labels
styleLB = {"font": "Times 20 bold",
           "justify": "center",
           "fg": "white",
           "bg": rgb_to_hex(100, 150, 0),
           "bd": 0,
           "relief": "solid",
           "padx": 0,
           "pady": 0,
           "ipadx": 20,
           "ipady": 40,
           "sticky": "NSEW"}

# Estilo dos Texts
styleTX = {"font": "Times 15 bold",
           "fg": "black",
           "bg": "white",
           "bd": 5,
           "relief": "raised",
           "padx": 0,
           "pady": 0,
           "ipadx": 100,
           "ipady": 50,
           "sticky": "NSEW",
           "ht": 0}

# Estilo dos Buttons 
styleBT = {"font": "Times 14 bold",
           "justify": "center",
           "fg": "white",
           "bg": rgb_to_hex(100, 150, 0),
           "bd": 0,
           "relief": "flat",
           "padx": 0,
           "pady": 0,
           "ipadx": 50,
           "ipady": 20,
           "sticky": "NSEW",
           "af": rgb_to_hex(25, 75, 0),
           "ab": rgb_to_hex(127, 174, 0),
           "ht": 0,
           "cursor": "hand1"}

# Estilo dos Listboxes
styleLI = {"font": "Times 14 bold",
           "justify": "center",
           "fg": "black",
           "bg": "white",
           "bd": 5,
           "relief": "raised",
           "padx": 0,
           "pady": 0,
           "ipadx": 100,
           "ipady": 50,
           "sticky": "NSEW",
           "sf": rgb_to_hex(25, 75, 0),
           "sb": rgb_to_hex(127, 174, 0),
           "ht": 0,
           "cursor": "hand1"}


# Construíndo o frame principal
mainFM = frame(styleFM, janela, 0, 0).display()
mainFM.rowconfigure(0, weight=1)
mainFM.columnconfigure(1, weight=1)

# Construíndo menu esquerdo

## Frames
styleFM["bg"] = rgb_to_hex(100, 150, 0)
menuEsquerdoFM = frame(styleFM, mainFM, 0, 0).display()
menuEsquerdoFM.rowconfigure(0, weight=1)

styleFM["sticky"] = ""
botoesEsquerdoFM = frame(styleFM, menuEsquerdoFM, 0, 0).display()


## Botões esquerdos
menuEsquerdoBT = [button(styleBT, botoesEsquerdoFM, "PESSOAS", 0, 0).display(),
                  button(styleBT, botoesEsquerdoFM, "DADOS GERAIS", 1, 0).display(),
                  button(styleBT, botoesEsquerdoFM, "METRAGEM", 2, 0).display(),
                  button(styleBT, botoesEsquerdoFM, "PAPÉIS", 3, 0).display(),
                  button(styleBT, botoesEsquerdoFM, "ATUAL", 4, 0).display(),
                  button(styleBT, botoesEsquerdoFM, "ANTERIOR", 5, 0).display()]


### Vinculando os botões a um evento
menuEsquerdoBT[0]["command"] = lambda: paginaAtiva(menuEsquerdoBT[0])
menuEsquerdoBT[1]["command"] = lambda: paginaAtiva(menuEsquerdoBT[1])
menuEsquerdoBT[2]["command"] = lambda: paginaAtiva(menuEsquerdoBT[2])
menuEsquerdoBT[3]["command"] = lambda: paginaAtiva(menuEsquerdoBT[3])
menuEsquerdoBT[4]["command"] = lambda: paginaAtiva(menuEsquerdoBT[4])
menuEsquerdoBT[5]["command"] = lambda: paginaAtiva(menuEsquerdoBT[5])

# Frame para acomodar página
styleFM["sticky"] = "NSEW"
styleFM["bg"] = rgb_to_hex(127, 174, 0)
paginaFM = frame(styleFM, mainFM, 0, 1).display()
paginaFM.columnconfigure(0, weight=1)
paginaFM.rowconfigure(1, weight=1)

# Construíndo cabeçalho da página
cabecalho = label(styleLB, paginaFM, "PESSOAS (0)", 0, 0).display()

## Tela
tela = text(styleTX, janela, 2, 0).display()

# Construíndo barra inferior
## Frame para botões inferiores
styleFM["sticky"] = "NSWE"
styleFM["bg"] = rgb_to_hex(100, 150, 0)
inferiorFM = frame(styleFM, paginaFM, 2, 0).display()

## Botões
inferiorBT = []

# Abrindo página inicial
paginaAtiva(menuEsquerdoBT[0])

janela.mainloop()