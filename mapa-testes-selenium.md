# 🗺️ Guia e Mapa de Testes Automatizados (QA) — Ready2Roll VTT
### *Referência Completa de Seletores e Automação com Selenium WebDriver (Python)*

Este guia foi elaborado para servir como base sólida para a elaboração de planos de teste, suítes de teste funcionais e automações de ponta a ponta (E2E) com **Selenium WebDriver** no **Ready2Roll VTT**.

---

## 📌 1. Convenção de Seletores (`data-testid`)

Todas as telas e componentes essenciais da interface possuem o atributo semântico padronizado `data-testid`.

### Por que utilizar `data-testid` em vez de XPath ou Classes CSS?
- **Imunidade a mudanças de estilo:** Se o layout ou as classes do Tailwind CSS forem alterados, seu teste não quebra.
- **Padrão do Mercado de QA:** Facilita a manutenção do código de automação e permite seguir o padrão *Page Object Model (POM)*.

### Como localizar elementos no Selenium (Python):
```python
from selenium.webdriver.common.by import By

# Forma padrão e recomendada:
elemento = driver.find_element(By.CSS_SELECTOR, '[data-testid="nome-do-seletor"]')
```

---

## 📋 2. Dicionário Completo de Elementos e Seletores

### 2.1. Tela Inicial / Lobby (`Lobby.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Campo Nome de Exibição** | `input-nome-exibicao` | `[data-testid="input-nome-exibicao"]` | Input (Texto) | `send_keys("Seu Nome")` — Nome obrigatório |
| **Aviso de Erro de Nome** | `aviso-erro-nome` | `[data-testid="aviso-erro-nome"]` | Texto/Alerta | Aparece quando tenta avançar com nome vazio |
| **Código da Última Mesa** | `input-codigo-ultima-sala` | `[data-testid="input-codigo-ultima-sala"]` | Input (Readonly) | Exibe código da última sessão conectada |
| **Botão Reconectar** | `btn-reconectar-ultima-sala` | `[data-testid="btn-reconectar-ultima-sala"]` | Botão | Clica para entrar na última mesa |
| **Botão Esquecer Mesa** | `btn-esquecer-ultima-sala` | `[data-testid="btn-esquecer-ultima-sala"]` | Botão | Limpa o registro da última mesa |
| **Campo Código da Mesa** | `input-codigo-sala` | `[data-testid="input-codigo-sala"]` | Input (Texto) | `send_keys("r2r-...")` para entrar em mesa existente |
| **Botão Entrar na Mesa** | `btn-entrar-sala` | `[data-testid="btn-entrar-sala"]` | Botão | Desabilitado se campo estiver vazio; Clica para entrar |
| **Campo Nome da Nova Mesa** | `input-nome-nova-sala` | `[data-testid="input-nome-nova-sala"]` | Input (Texto) | `send_keys("Mesa do Dragão")` |
| **Botão Criar Nova Mesa** | `btn-criar-sala` | `[data-testid="btn-criar-sala"]` | Botão | Cria uma nova sala e transiciona para a Mesa |

---

### 2.2. Cabeçalho Geral da Aplicação (`App.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Contêiner do Cabeçalho** | `cabecalho-app` | `[data-testid="cabecalho-app"]` | Header | Topbar do Ready2Roll |
| **Botão Doações / Café** | `btn-cabecalho-doacoes` | `[data-testid="btn-cabecalho-doacoes"]` | Botão | Abre página de apoio/doação |
| **Botão Manual de Instruções** | `btn-cabecalho-manual` | `[data-testid="btn-cabecalho-manual"]` | Botão | Abre o manual completo do usuário |
| **Botão Copiar Chave** | `btn-copiar-chave-sala` | `[data-testid="btn-copiar-chave-sala"]` | Botão | Visível apenas dentro da mesa; copia código da sala |
| **Botão Conectar Celular/QR**| `btn-abrir-modal-compartilhar`| `[data-testid="btn-abrir-modal-compartilhar"]`| Botão | Abre modal com QR Code e link |
| **Botão Configurações** | `btn-abrir-modal-configuracoes` | `[data-testid="btn-abrir-modal-configuracoes"]`| Botão | Abre modal de preferências |

---

### 2.3. Topo da Mesa e Conexão (`Mesa.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Barra Superior da Mesa** | `barra-topo-mesa` | `[data-testid="barra-topo-mesa"]` | Barra/Container | Contém ações de saída e participantes |
| **Botão Sair da Mesa** | `btn-sair-mesa` | `[data-testid="btn-sair-mesa"]` | Botão | Abre modal para confirmar saída |
| **Título da Mesa Ativa** | `titulo-mesa-ativa` | `[data-testid="titulo-mesa-ativa"]` | Texto/Span | Nome da sala conectada atualmente |
| **Botão Participantes** | `btn-participantes-topo` | `[data-testid="btn-participantes-topo"]` | Botão | Alterna a lista de jogadores online |
| **Contador Participantes** | `contador-participantes-online`| `[data-testid="contador-participantes-online"]`| Badge | Exibe o número de jogadores online |
| **Lista de Participantes** | `popover-participantes` | `[data-testid="popover-participantes"]` | Painel/Menu | Painel com a lista de avatares e status |

---

### 2.4. Barra de Comandos e Fórmulas (`CommandBar.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Formulário de Comandos** | `form-barra-comando` | `[data-testid="form-barra-comando"]` | Formulário | Submete a fórmula ao pressionar Enter |
| **Input de Rolagem** | `input-comando-rolagem` | `[data-testid="input-comando-rolagem"]` | Input (Texto) | Aceita `1d20+5`, `4d6kh3`, `1d8 | Espada`, etc. |
| **Botão Rolar** | `btn-enviar-comando` | `[data-testid="btn-enviar-comando"]` | Botão | Dispara a rolagem da fórmula digitada |

---

### 2.5. Grade de Dados e Modificadores Rápidos (`DiceGrid.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Visibilidade Pública** | `btn-visibilidade-publica` | `[data-testid="btn-visibilidade-publica"]` | Botão | Define visibilidade para todos na sala |
| **Visibilidade Direcionada** | `btn-visibilidade-direcionada` | `[data-testid="btn-visibilidade-direcionada"]` | Botão | Permite escolher destinatários específicos |
| **Visibilidade Privada** | `btn-visibilidade-privada` | `[data-testid="btn-visibilidade-privada"]` | Botão | Define rolagem visível apenas para o autor |
| **Alternar Teclado Dados** | `btn-toggle-painel-dados` | `[data-testid="btn-toggle-painel-dados"]` | Botão | Recolhe ou expande botões de dados |
| **Diminuir Quantidade (-)** | `btn-qtd-menos` | `[data-testid="btn-qtd-menos"]` | Botão | Diminui a quantidade de dados a rolar |
| **Campo Quantidade** | `input-qtd-dados` | `[data-testid="input-qtd-dados"]` | Input (Número) | Valor numérico da quantidade (mín 1, máx 50) |
| **Aumentar Quantidade (+)** | `btn-qtd-mais` | `[data-testid="btn-qtd-mais"]` | Botão | Aumenta a quantidade de dados a rolar |
| **Diminuir Bônus (-)** | `btn-bonus-menos` | `[data-testid="btn-bonus-menos"]` | Botão | Diminui o modificador numérico |
| **Campo Bônus** | `input-bonus-dados` | `[data-testid="input-bonus-dados"]` | Input (Número) | Valor do modificador/bônus |
| **Aumentar Bônus (+)** | `btn-bonus-mais` | `[data-testid="btn-bonus-mais"]` | Botão | Aumenta o modificador numérico |
| **Botão Zerar** | `btn-zerar-modificadores` | `[data-testid="btn-zerar-modificadores"]` | Botão | Reseta quantidade para 1 e bônus para 0 |
| **Botão Rolar d4** | `btn-dado-4` | `[data-testid="btn-dado-4"]` | Botão | Rola dado de 4 faces com modificadores |
| **Botão Rolar d6** | `btn-dado-6` | `[data-testid="btn-dado-6"]` | Botão | Rola dado de 6 faces com modificadores |
| **Botão Rolar d8** | `btn-dado-8` | `[data-testid="btn-dado-8"]` | Botão | Rola dado de 8 faces com modificadores |
| **Botão Rolar d10** | `btn-dado-10` | `[data-testid="btn-dado-10"]` | Botão | Rola dado de 10 faces com modificadores |
| **Botão Rolar d12** | `btn-dado-12` | `[data-testid="btn-dado-12"]` | Botão | Rola dado de 12 faces com modificadores |
| **Botão Rolar d20** | `btn-dado-20` | `[data-testid="btn-dado-20"]` | Botão | Rola dado de 20 faces com modificadores |
| **Botão Rolar d100** | `btn-dado-100` | `[data-testid="btn-dado-100"]` | Botão | Rola dado percentual (d100) |

---

### 2.6. Histórico de Mensagens e Rolagens (`ChatLog.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Lista de Histórico** | `lista-historico-chat` | `[data-testid="lista-historico-chat"]` | Contêiner | Contém a rolagem elegante e todos os cards |
| **Mensagem de Sessão Vazia**| `mensagem-chat-vazio` | `[data-testid="mensagem-chat-vazio"]` | Aviso | Exibido quando não há rolagens na mesa |
| **Log do Sistema** | `log-sistema` | `[data-testid="log-sistema"]` | Mensagem | Entradas, saídas ou avisos automáticos |
| **Card de Rolagem** | `card-rolagem` | `[data-testid="card-rolagem"]` | Card | Card com o resultado completo da rolagem |
| **Autor da Rolagem** | `autor-rolagem` | `[data-testid="autor-rolagem"]` | Texto | Nome de quem realizou a rolagem |
| **Rótulo/Descrição** | `rotulo-rolagem` | `[data-testid="rotulo-rolagem"]` | Texto | Rótulo da rolagem (ex: "Ataque Espada Longa") |
| **Detalhes da Rolagem** | `detalhes-dados-rolagem` | `[data-testid="detalhes-dados-rolagem"]`| Texto/Fórmula | Faces tiradas nos dados (ex: `[18] + 2`) |
| **Resultado Total** | `resultado-total-rolagem` | `[data-testid="resultado-total-rolagem"]`| Número | **Principal campo para asserções de teste** |

---

### 2.7. Modal de Compartilhamento / QR Code (`ModalCompartilhar.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Modal Compartilhar** | `modal-compartilhar` | `[data-testid="modal-compartilhar"]` | Dialog/Modal | Contêiner modal |
| **Botão Fechar** | `btn-fechar-modal-compartilhar`| `[data-testid="btn-fechar-modal-compartilhar"]`| Botão | Fecha o modal |
| **Campo Link da Mesa** | `input-link-mesa` | `[data-testid="input-link-mesa"]` | Input (Readonly) | URL completa para convidar jogadores |
| **Botão Copiar Link** | `btn-copiar-link-mesa` | `[data-testid="btn-copiar-link-mesa"]` | Botão | Copia o link da mesa para o clipboard |
| **Botão Compartilhar Nativo**| `btn-compartilhar-nativo` | `[data-testid="btn-compartilhar-nativo"]`| Botão | Presente caso o navegador suporte `navigator.share` |

---

### 2.8. Modal de Configurações (`ModalConfiguracoes.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Modal Configurações** | `modal-configuracoes` | `[data-testid="modal-configuracoes"]` | Dialog/Modal | Contêiner modal de preferências |
| **Botão Fechar (Topo)** | `btn-fechar-modal-configuracoes`| `[data-testid="btn-fechar-modal-configuracoes"]`| Botão | Fecha o painel |
| **Toggle Som Rolagem** | `toggle-som-rolagem` | `[data-testid="toggle-som-rolagem"]` | Switch | Alterna áudio dos dados colidindo |
| **Toggle Som Boas-vindas** | `toggle-som-boas-vindas` | `[data-testid="toggle-som-boas-vindas"]` | Switch | Alterna áudio "Ready to roll!" |
| **Toggle Som Entrada Part.**| `toggle-som-participante-entrou`| `[data-testid="toggle-som-participante-entrou"]`| Switch | Alterna áudio de entrada de usuário |
| **Toggle Som Saída Part.** | `toggle-som-participante-saiu` | `[data-testid="toggle-som-participante-saiu"]`| Switch | Alterna áudio de saída de usuário |
| **Toggle Dados 3D** | `toggle-dados-3d` | `[data-testid="toggle-dados-3d"]` | Switch | Liga/desliga animação 3D dos dados |
| **Toggle Sombras 3D** | `toggle-sombras-dados-3d` | `[data-testid="toggle-sombras-dados-3d"]` | Switch | Liga/desliga sombras nos dados 3D |
| **Toggle Inverter d20** | `toggle-regras-inverter-critico-d20`| `[data-testid="toggle-regras-inverter-critico-d20"]`| Switch | Regra 1 Crítico / 20 Falha (CoC) |
| **Toggle Inverter Chance** | `toggle-regras-inverter-chance`| `[data-testid="toggle-regras-inverter-chance"]`| Switch | Regra de faces altas em chances |
| **Botão Restaurar Padrões** | `btn-restaurar-padroes-configuracoes`| `[data-testid="btn-restaurar-padroes-configuracoes"]`| Botão | Redefine todas as opções aos valores iniciais |
| **Botão Concluir** | `btn-concluir-configuracoes` | `[data-testid="btn-concluir-configuracoes"]`| Botão | Salva e fecha o modal |

---

### 2.9. Modais de Alerta e Confirmação (`ModalAlerta.svelte` e `ModalConfirmacao.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Modal Alerta** | `modal-alerta` | `[data-testid="modal-alerta"]` | Dialog/Alerta | Notificação com botão único de OK |
| **Título do Alerta** | `titulo-modal-alerta` | `[data-testid="titulo-modal-alerta"]` | Título | Cabeçalho do alerta |
| **Mensagem do Alerta** | `mensagem-modal-alerta` | `[data-testid="mensagem-modal-alerta"]` | Texto | Conteúdo explicativo |
| **Botão OK do Alerta** | `btn-alerta-ok` | `[data-testid="btn-alerta-ok"]` | Botão | Fecha o modal de alerta |
| **Modal Confirmação** | `modal-confirmacao` | `[data-testid="modal-confirmacao"]` | Dialog/Confirmação| Diálogo com duas opções (Sim/Não) |
| **Título da Confirmação** | `titulo-modal-confirmacao` | `[data-testid="titulo-modal-confirmacao"]` | Título | Ex: "Confirmar Saída" |
| **Mensagem da Confirmação**| `mensagem-modal-confirmacao`| `[data-testid="mensagem-modal-confirmacao"]`| Texto | Texto descritivo da ação |
| **Botão Cancelar** | `btn-confirmacao-cancelar` | `[data-testid="btn-confirmacao-cancelar"]` | Botão | Cancela a ação e fecha o diálogo |
| **Botão Confirmar** | `btn-confirmacao-confirmar`| `[data-testid="btn-confirmacao-confirmar"]`| Botão | Executa a ação perigosa/confirmada |

---

### 2.10. Tela de Convite Direto via Link (`TelaConvite.svelte`)

| Elemento / Função | `data-testid` | Seletor CSS | Tipo | Ação / Retorno Esperado |
| :--- | :--- | :--- | :--- | :--- |
| **Card do Convite** | `card-tela-convite` | `[data-testid="card-tela-convite"]` | Contêiner | Card central de recepção do jogador |
| **Nome da Mesa** | `titulo-nome-mesa-convite` | `[data-testid="titulo-nome-mesa-convite"]` | Título | Nome da sala recebida pelo link |
| **Código da Sala** | `codigo-sala-convite` | `[data-testid="codigo-sala-convite"]` | Texto | Código da sala recebida pelo link |
| **Botão Assumir Origem** | `btn-assumir-origem` | `[data-testid="btn-assumir-origem"]` | Botão | Conecta usando o mesmo nome do criador |
| **Campo Nome Personalizado**| `input-nome-convite` | `[data-testid="input-nome-convite"]` | Input (Texto) | Digitar novo nome antes de ingressar |
| **Botão Entrar no Convite** | `btn-entrar-convite` | `[data-testid="btn-entrar-convite"]` | Botão | Entra na mesa com o nome digitado |
| **Botão Recusar Convite** | `btn-recusar-convite` | `[data-testid="btn-recusar-convite"]` | Botão | Descarta o convite e volta ao Lobby |

---

## 🎯 3. Casos de Teste (Test Cases) Sugeridos para o TCC

### **CT01 — Validação de Campo Obrigatório (Nome de Exibição)**
1. Acessar a aplicação (`http://localhost:5173/`).
2. Deixar o campo `[data-testid="input-nome-exibicao"]` vazio.
3. Clicar no botão `[data-testid="btn-criar-sala"]`.
4. **Resultado Esperado:** O modal de alerta `[data-testid="modal-alerta"]` deve se tornar visível com a mensagem de que o nome é obrigatório, ou o aviso `[data-testid="aviso-erro-nome"]` deve ser exibido.

### **CT02 — Criação de Nova Mesa com Sucesso**
1. Preencher `[data-testid="input-nome-exibicao"]` com "Mestre QA".
2. Preencher `[data-testid="input-nome-nova-sala"]` com "Mesa de Testes".
3. Clicar em `[data-testid="btn-criar-sala"]`.
4. **Resultado Esperado:** Transição para a tela da Mesa. O elemento `[data-testid="titulo-mesa-ativa"]` deve conter o texto "Mesa de Testes".

### **CT03 — Rolagem Rápida via Grade de Dados (d20)**
1. Na Mesa, localizar a grade de dados.
2. Clicar no botão `[data-testid="btn-dado-20"]`.
3. **Resultado Esperado:** Um card `[data-testid="card-rolagem"]` deve aparecer no `[data-testid="lista-historico-chat"]`. O autor `[data-testid="autor-rolagem"]` deve ser "Mestre QA" e o total `[data-testid="resultado-total-rolagem"]` deve ser um número inteiro entre 1 e 20.

### **CT04 — Rolagem com Fórmula e Rótulo via Barra de Comandos**
1. Localizar o campo `[data-testid="input-comando-rolagem"]`.
2. Digitar `2d6+4 | Dano Espada`.
3. Clicar no botão `[data-testid="btn-enviar-comando"]` (ou submeter com Enter).
4. **Resultado Esperado:** No card de rolagem mais recente, o rótulo `[data-testid="rotulo-rolagem"]` deve exibir "Dano Espada" e o total `[data-testid="resultado-total-rolagem"]` deve ser um valor entre 6 e 16.

### **CT05 — Abertura e Fechamento de Modal de Configurações**
1. Clicar no botão `[data-testid="btn-abrir-modal-configuracoes"]` no cabeçalho.
2. Aguardar o modal `[data-testid="modal-configuracoes"]` ficar visível.
3. Alternar o switch `[data-testid="toggle-dados-3d"]`.
4. Clicar no botão `[data-testid="btn-concluir-configuracoes"]`.
5. **Resultado Esperado:** O modal `[data-testid="modal-configuracoes"]` deve desaparecer da tela.

---

## 💡 4. Dicas de Ouro para Automação com Selenium

1. **Evite `time.sleep()` fixo:**
   Aplicações modernas em Svelte renderizam e atualizam o DOM de forma assíncrona. Use sempre esperas explícitas (`WebDriverWait`):
   ```python
   from selenium.webdriver.support.ui import WebDriverWait
   from selenium.webdriver.support import expected_conditions as EC

   espera = WebDriverWait(driver, 10)
   botao = espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="btn-criar-sala"]')))
   botao.click()
   ```

2. **Rolagem Física dos Dados 3D:**
   A animação 3D dos dados leva cerca de 1 a 2 segundos para concluir a física e registrar o número definitivo. O `WebDriverWait` no elemento `[data-testid="card-rolagem"]` garante que seu teste aguarde o dado cair antes de verificar o resultado.

