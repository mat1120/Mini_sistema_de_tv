# #Crie a classe ControleRemoto, onde vamos simular o funcionmento de um controle simples (canal, volume e ligar e desligar)
# # Crie a classe ControleRemoto
from rich import print
from rich.panel import Panel
class ControleRemoto:
    def __init__(self, canal=1, volume=10):
        self.canal = canal
        self.volume = volume
        self.ligado = False


    def ligar(self):
        self.ligado = True


    def desligar(self):
        self.ligado = False


    def aumentar_canal(self):
        if self.ligado:
            if self.canal < 5:
                self.canal += 1
            else:
                self.canal = 1

    def diminuir_canal(self):
        if self.ligado:
            if self.canal > 1:
                self.canal -= 1
            else:
                self.canal = 5

    def aumentar_volume(self):
        if self.ligado:
            if self.volume < 15:
                self.volume += 1

    def diminur_volume(self):
        if self.ligado:
            if self.volume > 0:
                self.volume -= 1


    def mostrar(self,aviso=""):
        if self.ligado:
            estado = "[green]TV LIGADA[/]"
            mensagem = ""

            if self.volume == 15:
                mensagem = "[red]VOLUME MÁXIMO ALCANÇADO[/]"
            elif self.volume == 0:
                mensagem = "[red]VOLUME MÍNIMO ALCANÇADO[/]"

            texto = "Estado: {}\n" \
            "{}\n" \
            "Canal: [red]{}[/]\n" \
            "Volume: [yellow]{}[/]\n{}".format(estado, aviso, self.canal, self.volume, mensagem)

        else:
            estado = "[red]TV DESLIGADA[/]"
            texto = "Estado: {}\n{}".format(estado, aviso)

        print(Panel(texto, title="[bold cyan]TV[/]",expand=False))



c1 = ControleRemoto()
aviso = ""
while True:
    c1.mostrar(aviso)
    aviso = ""
    comando = input("[L] Ligar Tv | [D] desligar TV\n" \
    "[C] Aumentar canal | [E] Diminuir Canal\n" \
    "[+] Aumentar volume | [-] Diminuir Volume: ").upper().strip()

    if not c1.ligado and comando in ["+", "-", "C", "E", "D"]:
        aviso = "[red]LIGUE A TV[/]"
        continue

    if comando == "L":
        c1.ligar()

    elif comando == "D":
        c1.desligar()

    elif comando == "C":
        c1.aumentar_canal()

    elif comando == "E":
        c1.diminuir_canal()

    elif comando == "+":
        c1.aumentar_volume()

    elif comando == "-":
        c1.diminur_volume()

    else:
        aviso = "[red]COMANDO INVALIDO[/]"

            
