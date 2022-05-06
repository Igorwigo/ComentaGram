from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,random 
import getpass
import tkinter as tk
from tkinter import filedialog as dlg
from tkinter import messagebox


# Fiz algumas modificações

class InstagramBot:
    def __init__(self, username, password,qtdPessoasComemtario,url,arq):
        self.username = username
        self.password = password
        self.qtdPessoasComemtario=qtdPessoasComemtario
        self.url=url
        self.arq = arq
        
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"./geckodriver"
        )
        #instale a biblioteca selenium pelo comando pip install selenium
        """ # Coloque o caminho para o seu geckodriver aqui, lembrando que você precisa instalar o firefox e geckodriver na versão mais atual """
        # Link download do geckodriver: https://github.com/mozilla/geckodriver/releases
        # Link download Firefox https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")

        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.post_sorteio()
        time.sleep(5)

    def post_sorteio(self):
        time.sleep(5)
        link=self.url#coloque aqui o link da publicação
        driver = self.driver
        driver.get(link)
        time.sleep(5)
        self.comenta_no_sorteio()

    @staticmethod
    def escreve_como_pessoa(sentence, single_input_field):
        """ Este código irá basicamente permitir que você simule a digitação como uma pessoa """
        print("Comentando perfil: ", sentence)
        #single_input_field.send_keys("@")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 60)
        single_input_field.send_keys(" ")

    def lista_de_seguidores(self):

        #caminho=self.arq
        #f=open(caminho, 'r')
        return self.arq

    def comenta_no_sorteio(self):
        log_Ultimo=open("Log_ultimo_comentado.txt","w")#cria arquivo com o ultimo comentado
        
        driver = self.driver
        driver.find_element_by_class_name("Ypffh").click()
        comment_input_box = driver.find_element_by_class_name("Ypffh")
        comment_input_box.click()
        
        time.sleep(5)
        lista_perfis=self.lista_de_seguidores()
        
        total=len(lista_perfis)
        qtdPessoas=int(self.qtdPessoasComemtario) #quantidade de pessoas por comentario

        repeticao=50000#pega o total de seus seguidores e divide pela quantidade de pessoas por comentario
        
        comentarios_ate_agora=0
        for i in range(0,repeticao,1):#repete de acordo com os dados da variavel repeticao
            time.sleep(5)
            aleatorio=random.randint(0,2)
            comenta_aleatorio=lista_perfis[aleatorio]
            for z in range(0,qtdPessoas,1):
                self.escreve_como_pessoa(comenta_aleatorio,comment_input_box)
                time.sleep(2)
                print("Ultima pessoa comentada: "+comenta_aleatorio)
                time.sleep(2)
                comentarios_ate_agora+=1
            print("Comentarios até agora: "+str(comentarios_ate_agora)+"/"+str(repeticao))
            time.sleep(random.randint(180, 240))#altere aqui o valor para o de sua preferencia, no caso a cada quantos segundos o bot comente para vc
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()

            
# Entre com o usuário e senha aqui
userman=input("Qual o seu usuario: ")
senha=getpass.getpass("qual a sua senha: ")
qtdPessoas=input("quantidade de pessoas por comentario?: ")
url=input("Qual a url do post do sorteio: ")



root=tk.Tk()
root.withdraw()

#messagebox.showinfo('Comenta Gram', \
 #     'Escolha o arquivo em TEXTO(.txt) onde tem a lista de seus seguidores')

arq = dlg.askopenfilename(filetypes=[("Arquivo de texto", "*.txt")])

#arq=["EU QUERO","VOU GANHAR","JÁ GANHEI"]

comenta_gram = InstagramBot(userman,senha,qtdPessoas,url,arq)
comenta_gram.login()
