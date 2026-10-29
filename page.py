import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException


class BasePage:
    """Classe base contendo todos os métodos utilitários/core do Selenium."""


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def _click(self, locator):
        # Tenta clicar com retentativa automática caso ocorra StaleElementReference
        for tentativa in range(3):
            try:
                element = self.wait.until(
                    EC.element_to_be_clickable(locator)
                )
                element.click()
                return  # Sucesso, sai do método
            except Exception:
                if tentativa == 2:
                    raise  # Se falhar 3 vezes, estoura o erro real

    def _type(self, locator, text):
        element = self._find(locator)
        try:
            element.clear()
            element.send_keys(text)
        except Exception:
            element = self._find(locator)
            element.clear()
            element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    def _press_tab(self):
        self.driver.switch_to.active_element.send_keys(Keys.TAB)


class LoginPage(BasePage):

    #localizadores Login
    NOME_LOCATOR = By.CSS_SELECTOR, '[data-testid="input-nome-exibicao"]'
    NOME_MESA_LOCATOR = By.CSS_SELECTOR,  '[data-testid="input-nome-nova-sala"]'
    NOME_VAZIO_LOCATOR = By.CSS_SELECTOR, '[data-testid="aviso-erro-nome"]'
    BOTAO_CRIAR_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-criar-sala"]'
    BOTAO_ENTRAR_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-entrar-sala"]'
    BOTAO_RECONECTAR_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-reconectar-ultima-sala"]'
    BOTAO_ALERTA_OK_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-alerta-ok"]'

    def __init__(self, driver):
        super().__init__(driver)  # Inicializa o construtor)

    # preencher nome:
    def preencher_nome(self, nome):
        self._type(self.NOME_LOCATOR, nome)

    #preencher nome de mesa:
    def preencher_nome_mesa(self, nome_mesa):
        self._type(self.NOME_MESA_LOCATOR, nome_mesa)

    #criar mesa:
    def criar_mesa(self,nome,nome_mesa):
        self._type(self.NOME_LOCATOR,nome)
        self._type(self.NOME_MESA_LOCATOR,nome_mesa)
        self._click(self.BOTAO_CRIAR_LOCATOR)

    def clicar_criar_sem_nome(self):
        self._click(self.BOTAO_CRIAR_LOCATOR)

    #verificando texto adicionado:
    def _get_nome(self):
        return self._get_value(self.NOME_LOCATOR)
    def _get_nome_mesa(self):
        return self._get_value(self.NOME_MESA_LOCATOR)

    #verificando página de login
    def esta_no_login(self):
        try:
            # Aguarda até 5 segundos para o elemento de login reaparecer
            elemento = self.wait.until(
                EC.visibility_of_element_located(self.NOME_LOCATOR)
            )
            return elemento.is_displayed()
        except TimeoutException:
            return False

    def reconectar_sala(self):
        self._click(self.BOTAO_RECONECTAR_LOCATOR)

    def clicar_alerta_ok(self):
        self._click(self.BOTAO_ALERTA_OK_LOCATOR)

    def alerta_obrigatoriedade_esta_visivel(self):
        try:
            elemento = self.wait.until(
                EC.visibility_of_element_located(self.BOTAO_ALERTA_OK_LOCATOR)
            )
            return elemento.is_displayed()
        except TimeoutException:
            return False

class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)  # Inicializa o construtor)

    #localizadores
    BOTAO_SAIR_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-sair-mesa"]'
    CAMPO_INPUT_LOCATOR = By.CSS_SELECTOR, '[data-testid="input-comando-rolagem"]'
    BOTAO_D4_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-4"]'
    BOTAO_D6_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-6"]'
    BOTAO_D8_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-8"]'
    BOTAO_D10_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-10"]'
    BOTAO_D12_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-12"]'
    BOTAO_D20_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-20"]'
    BOTAO_D100_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-dado-100"]'
    BOTAO_DADOS_MENOS_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-qtd-menos"]'
    BOTAO_DADOS_MAIS_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-qtd-mais"]'
    INDICADOR_DADOS_LOCATOR = By.CSS_SELECTOR, '[data-testid="input-qtd-dados"]'
    BOTAO_BONUS_MENOS_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-bonus-menos"]'
    BOTAO_BONUS_MAIS_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-bonus-mais"]'
    INDICADOR_BONUS_LOCATOR = By.CSS_SELECTOR, '[data-testid="input-bonus-dados"]'
    BOTAO_ROLAR_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-enviar-comando"]'
    BOTAO_ZERAR_MODIFICADORES_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-zerar-modificadores"]'
    CAMPO_HISTORICO_LOCATOR = By.CSS_SELECTOR, '[data-testid="lista-historico-chat"]'
    ULTIMO_CARD_ROLAGEM_LOCATOR = By.CSS_SELECTOR, '[data-testid="card-rolagem"]:last-child'
    ULTIMO_RESULTADO_TOTAL_LOCATOR = By.CSS_SELECTOR, '[data-testid="card-rolagem"]:last-child [data-testid="resultado-total-rolagem"]'
    ULTIMO_CARD_TITULO_LOCATOR = By.CSS_SELECTOR, '[data-testid="card-rolagem"]:last-child [data-testid="rotulo-rolagem"]'
    TITULO_MESA_LOCATOR = By.CSS_SELECTOR, '[data-testid="titulo-mesa-ativa"]'
    BOTAO_SAIR_MESA_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-sair-mesa"]'
    BOTAO_CONFIRMAR_SAIDA = By.CSS_SELECTOR, '[data-testid="btn-confirmacao-confirmar"]'
    CAIXA_CONEXAO_P2P_LOCATOR = (By.CSS_SELECTOR, '.r2r-conexao-status-caixa')
    BOTAO_CONFIG_LOCATOR = By.CSS_SELECTOR, '[data-testid="btn-abrir-modal-configuracoes"]'
    CAIXA_CONFIG_LOCATOR = By.CSS_SELECTOR, '[data-testid="modal-configuracoes"]'


    #sair da sala
    def sair_da_sala(self,):
            self._click(self.BOTAO_SAIR_LOCATOR)
            self._click(self.BOTAO_CONFIRMAR_SAIDA)

    #rolar dados
    def rolar_d4(self):
            self._click(self.BOTAO_D4_LOCATOR)
    def rolar_d6(self):
        self._click(self.BOTAO_D6_LOCATOR)
    def rolar_d8(self):
            self._click(self.BOTAO_D8_LOCATOR)
    def rolar_d10(self):
            self._click(self.BOTAO_D10_LOCATOR)
    def rolar_d12(self):
            self._click(self.BOTAO_D12_LOCATOR)
    def rolar_d20(self):
            self._click(self.BOTAO_D20_LOCATOR)
    def rolar_d100(self):
            self._click(self.BOTAO_D100_LOCATOR)

    #alterar modificadores
    def zerar_mods(self):
        self._click(self.BOTAO_ZERAR_MODIFICADORES_LOCATOR)
    def adicionar_bonus(self):
        self._click(self.BOTAO_BONUS_MAIS_LOCATOR)
    def reduzir_bonus(self):
        self._click(self.BOTAO_BONUS_MENOS_LOCATOR)
    def adicionar_dado(self):
        self._click(self.BOTAO_DADOS_MAIS_LOCATOR)
    def reduzir_dado(self):
        self._click(self.BOTAO_DADOS_MENOS_LOCATOR)

    #campo de comando:
    def inserir_comando(self,comando):
        self._type(self.CAMPO_INPUT_LOCATOR, comando)
    def rolar_comando(self):
        self._click(self.BOTAO_ROLAR_LOCATOR)

    #veriricações
    def verificar_log(self):
        return self._get_text(self.CAMPO_HISTORICO_LOCATOR)
    def obter_ultima_rolagem(self):
        return self._get_text(self.ULTIMO_RESULTADO_TOTAL_LOCATOR)
    def obter_ultimo_titulo(self):
        return self._get_text(self.ULTIMO_CARD_TITULO_LOCATOR)

    def obter_titulo_mesa(self):
        return self._get_text(self.TITULO_MESA_LOCATOR)

    def obter_valor_dados(self):
        return self._get_value(self.INDICADOR_DADOS_LOCATOR)

    def obter_valor_bonus(self):
        return self._get_value(self.INDICADOR_BONUS_LOCATOR)

    def esta_na_main(self):
        try:
            # Aguarda até 5 segundos para o elemento da main page aparecer
            elemento = self.wait.until(
                EC.visibility_of_element_located(self.BOTAO_D4_LOCATOR)
            )
            return elemento.is_displayed()
        except TimeoutException:
            return False

    def aguardar_modal_conexao_sumir(self, timeout=21):
        try:
            # Aguarda até que o backdrop do modal P2P fique invisível (timeout de 5 segundos)
            self.wait.until(
                EC.invisibility_of_element_located(self.CAIXA_CONEXAO_P2P_LOCATOR)
            )
        except TimeoutException:
            #se a caixa ainda estiver ativa, segue.
            pass

    def abrir_configs(self):
        self._click(self.BOTAO_CONFIG_LOCATOR)

    def modal_config_esta_visivel(self):
        try:
            elemento = self.wait.until(
                EC.visibility_of_element_located(self.CAIXA_CONFIG_LOCATOR)
            )
            return elemento.is_displayed()
        except TimeoutException:
            return False