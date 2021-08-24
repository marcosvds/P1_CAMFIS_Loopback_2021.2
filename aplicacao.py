#####################################################
# Engenharia de Computação Insper
# Camada Física da Computação 2021.1
# Aluno: Marcos Vinícius da Silva
# 24/08/2021
# Projeto LoopBack
####################################################

# esta é a camada superior, de aplicação do seu software de comunicação serial UART.
# para acompanhar a execução e identificar erros, construa prints ao longo do código! 

from enlace import *
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
# para saber a sua porta, execute no terminal:
# python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM3"                  # Windows(variacao de)


def main():
    try:
        # declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        # para declarar esse objeto é o nome da porta.
        com1 = enlace('COM3')
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        # Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        com1.enable()
        print("----------------------------------")
        print("Comunicação aberta com sucesso!")
        print("----------------------------------")

        # aqui você deverá gerar os dados a serem transmitidos. 
        #s eus dados a serem transmitidos são uma lista de bytes a serem transmitidos. Gere esta lista com o 
        # nome de txBuffer. Esla sempre irá armazenar os dados a serem enviados.     
        # txBuffer = imagem em bytes!
    
        # Endereço da imagem a ser transmitida
        imagemTransmitida = "./imgs/image.png"
        #image1 = r"C:\Users\Marqu\OneDrive\Documentos\Insper\4º Semestre\Camada Física da Computação\Projetos\Loopback\P1_CAMFIS_LoopBack_2021.2\imgs\image.png"

        # Endereço da imagem a ser recebida
        imagemRecebida = "./imgs/recebidaCopia.png" 

        # Lista de bytes com a imagem a ser transmitida
        print("\n")
        print("Carregando imagem para transmissão")
        print("Endereço da imagem a ser transmitida: {}".format(imagemTransmitida))
        print("\n")

        txBuffer = open(imagemTransmitida, 'rb').read()
 
        # faça aqui uma conferência do tamanho do seu txBuffer, ou seja, quantos bytes serão enviados.
        tamTxBuffer = len(txBuffer)
        print("Tamanho do txBuffer: {}" .format(tamTxBuffer))
        print("\n")
        print(txBuffer)
        print("\n")
        print(type(txBuffer))
        print("\n")

        # --------------- Aqui --------------   
        # finalmente vamos transmitir os tados. Para isso usamos a funçao sendData que é um método da camada enlace.
        # faça um print para avisar que a transmissão vai começar.
        # tente entender como o método send funciona!
        # Cuidado! Apenas trasmitimos arrays de bytes! Nao listas!

        print("----------------------------------")  
        print("A transmissão está começando!")
        print("----------------------------------")
        print("\n")

        com1.sendData(np.asarray(txBuffer))
       
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # Tente entender como esse método funciona e o que ele retorna

        #txSize = com1.tx.getStatus()
        #print("Status da transmissão: {}".format(txSize))
        #print("\n")
        
        # Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        # Observe o que faz a rotina dentro do thread RX
        # print um aviso de que a recepção vai começar.

        print("----------------------------------")
        print("A recepção vai começar!")
        print("----------------------------------")
        print("\n")
        
        # Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        # Veja o que faz a funcao do enlaceRX  getBufferLen
      
        # acesso aos bytes recebidos
        #txLen = len(txBuffer)
        #rxBuffer, nRx = com1.getData(txLen)
        #print("recebeu {}" .format(rxBuffer))
            
        # Escreve arquivo cópia
        print("Salvando dados no arquivo")
        print("Endereço da imagem recebido: {}" .format(imagemRecebida))
        print("\n")
    
        # Encerra comunicação
        print("----------------------------------")
        print("Comunicação encerrada com sucesso!")
        print("----------------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
