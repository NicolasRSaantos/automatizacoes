
# abrir um navegador
from playwright.sync_api import sync_playwright, expect
import time

with sync_playwright() as pw:
    navegador = pw.chromium.launch(headless=False)
    contexto = navegador.new_context()

    # abrir o navegador
    pagina = contexto.new_page()

    # navegar para uma página
    pagina.goto("http://www.type.ddns.com.br:8021/")

    # pegar infos da página
    print(pagina.title())

    # escrevendo nos campos de texto
    pagina.get_by_role("textbox", name="Digite o usuário").fill("admin")
    pagina.get_by_role("textbox", name="Digite a senha").fill("admin")

    # clicando no batao para logar
    botao_logar = pagina.get_by_role("button", name="Entrar")
    botao_logar.click()

    #escolhendo configuração no menu
    pagina.get_by_role("link", name="Configurações").click()
    pagina.locator("#btnReboot").click()
    pagina.get_by_role("button", name="Reiniciar", exact=True).click()
    pagina.get_by_role("button", name="OK").click()
    
    time.sleep(10)
    navegador.close()

