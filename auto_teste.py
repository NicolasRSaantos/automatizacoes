from selenium import webdriver
import time

#abre navegador
navegador = webdriver.Chrome()

#acessar um site
navegador.get("link do seu site http")

#coloca em tela cheia
navegador.maximize_window()

#escrever em um campo
campo_user = navegador.find_element("id","input_user")
campo_user.send_keys("admin")

campo_user = navegador.find_element("id","input_password")
campo_user.send_keys("admin")

#selecionar um elemento na tela
botao_logar = navegador.find_element("class name", "pull-right")

#clicar em um elemento
botao_logar.click()

#indo para uma pagina pois nao tem elemento no link
navegador.get("link do seu site http config")

#clicando no menu de reiniciar
botao_reiniciar = navegador.find_element("id", "btnReboot")
botao_reiniciar.click()

time.sleep(2)

#encontrar varios elementos
lista_botoes = navegador.find_elements("css selector", "button[type='button']")
for botao in lista_botoes:
    if "Reiniciar" in botao.text:
        botao.click()
        break

time.sleep(2)

lista_botoes = navegador.find_elements("css selector", "button[type='button']")
for botao in lista_botoes:
    if "OK" in botao.text:
        botao.click()
        break


#navegar para um site diferente
#navegador.get()

#selecionar abas
#abas = navegador.window_handles
#navegador.switch_to.window(abas[1])

time.sleep(30)