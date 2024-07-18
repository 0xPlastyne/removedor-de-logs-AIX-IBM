# Removedor de Logs - AIX (IBM)

Este script Python remove diversos arquivos de log em sistemas Unix/Linux, incluindo AIX da IBM. Ele verifica a existência de arquivos de log em diretórios comuns e os exclui, garantindo que o sistema fique livre de rastros de atividades anteriores.

## Como Usar

### Pré-requisitos

- Python 3.x instalado no sistema.
- Permissões adequadas para excluir arquivos de log (pode ser necessário executar como root).

### Execução do Script

1. Clone o repositório para seu ambiente local:
    ```sh
    git clone https://github.com/0xPlastyne/removedor-de-logs-AIX-IBM.git
    cd removedor-de-logs-AIX-IBM
    ```

2. Execute o script:
    ```sh
    sudo python3 dell-logs.py
    ```

### Funcionamento

- Configura o encoding para UTF-8.
- Verifica e remove diversos arquivos de log em diretórios comuns.
- Remove todos os arquivos com extensão `.log` e arquivos que começam com `log` na pasta `/var/`.
- Imprime mensagens indicando o status de cada operação.

### Nota

Este script é para fins educacionais e de pesquisa. Use com responsabilidade.
