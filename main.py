import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import data
import page
from page import LoginPage, BasePage
from page import MainPage

class TestLoginECriacaodeMesa:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get(data.URL)
        time.sleep(1.5)
        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)

    def test_validar_nome_obrigatorio(self):
        self.login_page.clicar_criar_sem_nome()
        assert self.login_page.alerta_obrigatoriedade_esta_visivel()
        self.login_page.clicar_alerta_ok()

    def test_create_room(self):
        # 1. Open the live app
        self.login_page.criar_mesa(data.NOME_USUARIO, data.NOME_MESA)
        assert self.main_page.obter_titulo_mesa() == data.NOME_MESA


    @classmethod
    def teardown_class(cls):
        try:
            cls.driver.quit()
        except Exception:
            pass


class TestFuncionalidadesDaMesa:

    def setup_method(self):
        # O driver nasce limpo para CADA teste (ou iteração de parâmetro)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(data.URL)
        time.sleep(1.5)

        self.login_page = LoginPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.login_page.criar_mesa(data.NOME_USUARIO, data.NOME_MESA)
        self.main_page.aguardar_modal_conexao_sumir()

    def teardown_method(self):
        # O driver morre e fecha a janela após CADA teste ou iteração
        try:
            self.driver.quit()
        except Exception:
            pass

    def test_d4_btn(self):
        self.main_page.rolar_d4()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 4

    def test_d6_btn(self):
        self.main_page.rolar_d6()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 6

    def test_d8_btn(self):
        self.main_page.rolar_d8()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 8

    def test_d10_btn(self):
        self.main_page.rolar_d10()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 10

    def test_d12_btn(self):
        self.main_page.rolar_d12()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 12

    def test_d20_btn(self):
        self.main_page.rolar_d20()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 20

    def test_d100_btn(self):
        self.main_page.rolar_d100()
        time.sleep(4)
        valor = int(self.main_page.obter_ultima_rolagem())
        assert 1 <= valor <= 100

    def test_input_field(self):
        self.main_page.inserir_comando(data.COMANDO)
        self.main_page.rolar_comando()
        time.sleep(4)
        titulo_resultado = self.main_page.obter_ultimo_titulo()
        valor = int(self.main_page.obter_ultima_rolagem())
        assert titulo_resultado in data.COMANDO
        assert 4 <= valor <= 11

    @pytest.mark.parametrize("comando, min_val, max_val, rotulo", [
        ("1d6+2 | Espada Curta", 3, 8, "Espada Curta"),
        ("2d4-1 | Adaga", 1, 7, "Adaga"),
        ("1d20 | Teste de Pericia", 1, 20, "Teste de Pericia"),
        ("3d6+5 | Bola de Fogo", 8, 23, "Bola de Fogo"),
    ])
    def test_modificadores_e_comandos(self, comando, min_val, max_val, rotulo):
        self.main_page.inserir_comando(comando)
        self.main_page.rolar_comando()
        time.sleep(4)

        texto_resultado = self.main_page.obter_ultima_rolagem()
        valor_total = int(texto_resultado)
        titulo_card = self.main_page.obter_ultimo_titulo()

        assert min_val <= valor_total <= max_val, f"Erro no comando '{comando}': O valor gerado foi {valor_total}, mas esperava entre {min_val} e {max_val}!"
        assert titulo_card == rotulo, f"Erro no comando '{comando}': Esperado rótulo '{rotulo}', mas veio '{titulo_card}'!"

    def test_botoes_mais_menos_bonus(self):
        #estado inicial
        valor_inicial = int(self.main_page.obter_valor_bonus())
        #clica no botão somar
        self.main_page.adicionar_bonus()
        valor_apos_incremento = int(self.main_page.obter_valor_bonus())
        #verificação
        assert valor_apos_incremento == valor_inicial + 1, f"Esperava {valor_inicial + 1}, mas o bônus foi para {valor_apos_incremento}"
        #clica no botão subtrair do bônus 2x
        self.main_page.reduzir_bonus()
        self.main_page.reduzir_bonus()
        valor_apos_reducao = int(self.main_page.obter_valor_bonus())
        #verificação
        assert valor_apos_reducao == valor_apos_incremento -2, f"Esperava {valor_apos_incremento - 2}, mas o bônus ficou em {valor_apos_reducao}"

    def test_botoes_mais_menos_dados(self):
        #estado inicial
        qtd_dados_inicial = int(self.main_page.obter_valor_dados())
        #clica no botão somar
        self.main_page.adicionar_dado()
        qtd_apos_soma = int(self.main_page.obter_valor_dados())
        #verificação
        assert qtd_apos_soma == qtd_dados_inicial + 1, f"Esperava {qtd_dados_inicial + 1}, mas a quantidade foi para {qtd_apos_soma}"
        #clicar no botao reduzir
        self.main_page.reduzir_dado()
        self.main_page.reduzir_dado()
        qtd_apos_reducao = int(self.main_page.obter_valor_dados())
        #verificação
        assert qtd_apos_reducao == 1, f"O contador de dados permitiu furar o piso mínimo! Esperava 1, mas ficou em {qtd_apos_reducao}"

    def test_botao_zerar(self):
        #estado inicial
        #clica no botão somar dado e reduzir bonus 2x
        self.main_page.adicionar_dado()
        self.main_page.reduzir_bonus()
        self.main_page.reduzir_bonus()
        self.main_page.zerar_mods()
        dados_final = int(self.main_page.obter_valor_dados())
        bonus_final = int(self.main_page.obter_valor_bonus())
        assert bonus_final == 0
        assert dados_final == 1

    def test_sair_mesa(self):
        #clica no botao sair e confirma
        self.main_page.sair_da_sala()
        #verifica se saiu
        assert self.login_page.esta_no_login(), "O usuário não saiu da sala, a tela de login não apareceu!"

    def test_reconectar(self):
        #clica em sair e confirma
        self.main_page.sair_da_sala()
        self.login_page.preencher_nome(data.NOME_USUARIO)
        self.login_page.reconectar_sala()
        assert self.main_page.esta_na_main(),  "O usuário não retornou a sala, a tela de dados não apareceu!"

    def test_config(self):
        #abre as configs:
        self.main_page.abrir_configs()
        #valida se a caixa está aberta:
        assert self.main_page.modal_config_esta_visivel(), "O modal de configurações não abriu"

