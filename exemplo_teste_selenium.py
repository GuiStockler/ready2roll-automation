"""
Exemplo de Automação de Testes com Selenium WebDriver (Python)
Projeto: Ready2Roll VTT
Objetivo: Demonstrar a automação de testes funcionais ponta a ponta (E2E)
          utilizando atributos padronizados `data-testid`.

Pré-requisitos:
  1. Servidor web do Ready2Roll rodando localmente (ex: `npm run dev` na porta 5173).
  2. Python 3.8+ instalado.
  3. Dependências instaladas: `pip install -r requirements.txt`

Como executar:
  python exemplo_teste_selenium.py
"""

import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

# URL padrão do ambiente de desenvolvimento web
URL_BASE = "https://r2rvtt.vercel.app/"

def obter_driver():
    """Inicializa o navegador Google Chrome com opções otimizadas para testes."""
    opcoes = webdriver.ChromeOptions()
    opcoes.add_argument("--start-maximized")
    opcoes.add_argument("--disable-notifications")
    opcoes.add_argument("--disable-infobars")
    
    # Se desejar rodar em modo silencioso (sem abrir janela física), descomente:
    # opcoes.add_argument("--headless=new")
    
    try:
        driver = webdriver.Chrome(options=opcoes)
        return driver
    except WebDriverException:
        # Fallback usando webdriver-manager caso necessário
        from webdriver_manager.chrome import ChromeDriverManager
        servico = Service(ChromeDriverManager().install())
        return webdriver.Chrome(service=servico, options=opcoes)


def executar_testes():
    print("=" * 70)
    print("🚀 INICIANDO SUÍTE DE TESTES AUTOMATIZADOS: READY2ROLL VTT")
    print("=" * 70)
    
    driver = obter_driver()
    espera = WebDriverWait(driver, 10)
    
    try:
        # 1. Navegar até a aplicação
        print(f"\n[PASSO 1] Acessando aplicação em: {URL_BASE}")
        try:
            driver.get(URL_BASE)
        except WebDriverException as erro_conexao:
            print("\n❌ ERRO: Não foi possível conectar ao servidor local.")
            print("👉 Certifique-se de que o Ready2Roll está rodando no terminal:")
            print("   npm run dev")
            return

        # Aguarda o Lobby carregar
        input_nome = espera.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="input-nome-exibicao"]'))
        )
        print("✔ Aplicação carregada com sucesso!")

        # -------------------------------------------------------------
        # TESTE 1: Validação de campo obrigatório (Nome de exibição)
        # -------------------------------------------------------------
        print("\n[TESTE 1] Validando obrigatoriedade do Nome de Exibição...")
        input_nome.clear()
        btn_criar = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-criar-sala"]')
        btn_criar.click()

        # Verifica se o modal de alerta ou aviso de erro foi exibido
        alerta_aberto = espera.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="modal-alerta"]'))
        )
        assert alerta_aberto.is_displayed(), "O modal de alerta deveria estar visível."
        print("✔ Alerta de validação exibido corretamente!")

        # Fecha o alerta clicando em 'Entendido!'
        btn_ok_alerta = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-alerta-ok"]')
        btn_ok_alerta.click()
        espera.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-testid="modal-alerta"]'))
        )
        print("✔ Alerta fechado com sucesso.")

        # -------------------------------------------------------------
        # TESTE 2: Criação de Nova Mesa
        # -------------------------------------------------------------
        print("\n[TESTE 2] Criando uma nova mesa virtual...")
        nome_jogador = "Auditor QA"
        nome_mesa = "Mesa de Qualidade e Testes"

        input_nome.send_keys(nome_jogador)
        
        input_mesa = driver.find_element(By.CSS_SELECTOR, '[data-testid="input-nome-nova-sala"]')
        input_mesa.send_keys(nome_mesa)
        
        btn_criar.click()

        # Aguarda a transição para a tela da Mesa
        titulo_mesa = espera.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="titulo-mesa-ativa"]'))
        )
        assert nome_mesa in titulo_mesa.text, f"Título esperado '{nome_mesa}', obtido: '{titulo_mesa.text}'"
        print(f"✔ Mesa criada e acessada! Título verificado: '{titulo_mesa.text}'")

        # -------------------------------------------------------------
        # TESTE 3: Rolagem via Grade de Dados (Botão d20)
        # -------------------------------------------------------------
        print("\n[TESTE 3] Realizando rolagem rápida de 1d20 pela grade...")
        btn_d20 = espera.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="btn-dado-20"]'))
        )
        btn_d20.click()

        # Aguarda o registro aparecer no histórico de chat
        card_rolagem = espera.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="card-rolagem"]'))
        )
        autor = card_rolagem.find_element(By.CSS_SELECTOR, '[data-testid="autor-rolagem"]').text
        total_d20 = card_rolagem.find_element(By.CSS_SELECTOR, '[data-testid="resultado-total-rolagem"]').text

        assert autor == nome_jogador, f"Autor incorreto: {autor}"
        assert total_d20.isdigit() and 1 <= int(total_d20) <= 20, f"Valor de d20 inválido: {total_d20}"
        print(f"✔ Rolagem de 1d20 validada! Autor: {autor} | Total obtido: {total_d20}")

        # -------------------------------------------------------------
        # TESTE 4: Rolagem de fórmula avançada com rótulo
        # -------------------------------------------------------------
        print("\n[TESTE 4] Enviando fórmula '2d6+5 | Golpe Devastador' via barra de comando...")
        input_comando = driver.find_element(By.CSS_SELECTOR, '[data-testid="input-comando-rolagem"]')
        input_comando.send_keys("2d6+5 | Golpe Devastador")
        
        btn_enviar = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-enviar-comando"]')
        btn_enviar.click()

        # Aguarda a nova rolagem ser computada (espera pequena para física ou renderização)
        time.sleep(1.5)
        
        # Obtém o último card adicionado ao histórico
        todos_cards = driver.find_elements(By.CSS_SELECTOR, '[data-testid="card-rolagem"]')
        ultimo_card = todos_cards[-1]
        
        rotulo = ultimo_card.find_element(By.CSS_SELECTOR, '[data-testid="rotulo-rolagem"]').text
        total_formula = ultimo_card.find_element(By.CSS_SELECTOR, '[data-testid="resultado-total-rolagem"]').text
        
        assert "Golpe Devastador" in rotulo, f"Rótulo não confere: {rotulo}"
        assert total_formula.isdigit() and 7 <= int(total_formula) <= 17, f"Total fora do intervalo esperado (7-17): {total_formula}"
        print(f"✔ Fórmula validada com sucesso! Rótulo: '{rotulo}' | Total: {total_formula}")

        # -------------------------------------------------------------
        # TESTE 5: Abertura e fechamento do painel de Configurações
        # -------------------------------------------------------------
        print("\n[TESTE 5] Verificando modal de configurações...")
        btn_config = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-abrir-modal-configuracoes"]')
        btn_config.click()

        modal_config = espera.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-testid="modal-configuracoes"]'))
        )
        assert modal_config.is_displayed(), "Modal de configurações deveria estar visível."
        print("✔ Modal de configurações aberto.")

        # Alterna o switch dos dados 3D
        toggle_3d = driver.find_element(By.CSS_SELECTOR, '[data-testid="toggle-dados-3d"]')
        toggle_3d.click()
        print("✔ Switch de dados 3D alternado.")

        # Conclui e fecha
        btn_concluir = driver.find_element(By.CSS_SELECTOR, '[data-testid="btn-concluir-configuracoes"]')
        btn_concluir.click()

        espera.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '[data-testid="modal-configuracoes"]'))
        )
        print("✔ Modal de configurações fechado com sucesso.")

        print("\n" + "=" * 70)
        print("🎉 TODOS OS TESTES PASSARAM COM SUCESSO (100% OK)!")
        print("=" * 70)

    except AssertionError as erro_assercao:
        print(f"\n❌ FALHA DE ASSERÇÃO NO TESTE: {erro_assercao}")
    except TimeoutException as erro_timeout:
        print(f"\n❌ TEMPO LIMITE EXCEDIDO (TIMEOUT): Um elemento esperado não apareceu no prazo.")
        print(f"Detalhes: {erro_timeout}")
    except Exception as erro_inesperado:
        print(f"\n❌ ERRO INESPERADO: {erro_inesperado}")
    finally:
        print("\nEncerrando sessão do WebDriver em 3 segundos...")
        time.sleep(3)
        driver.quit()


if __name__ == "__main__":
    executar_testes()

