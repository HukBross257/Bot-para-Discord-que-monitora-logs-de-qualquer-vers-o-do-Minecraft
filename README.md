# Script para monitorar logs do Minecraft e enviar para Discord via webhook

Este script lê o arquivo `server.log` do Minecraft (compatível com praticamente todas as versões, incluindo Alpha, Beta e MCPE) e envia atualizações em tempo real para um canal do Discord usando webhook. Ele permite acompanhar o que acontece no servidor diretamente pelo Discord, sem depender de plugins.

## Observações importantes
- Este script **não é um plugin**; funciona como um programa externo.
- **Não funciona** em servidores hospedados remotamente sem acesso direto ao `server.log`.
- É mais útil para servidores **locais**.
- Funciona em versões antigas do Minecraft, incluindo a B1.0, que não possuem suporte nativo para envio de logs ao Discord.

## Como usar
1. Baixe os arquivos `blocklogger.py` e `run_blocklogger.py`.
2. Coloque os arquivos na mesma pasta onde está o `server.log` ou informe o caminho completo do arquivo no script.
3. Copie o webhook do Discord e defina o canal onde os logs serão enviados.
4. Execute `run_blocklogger.py`.

### Verificação em caso de problemas
- Confirme se o caminho do `server.log` está correto.
- Certifique-se de ter instalado a biblioteca `requests` ```(pip install requests)```

### Execução via terminal
```bash
python run_blocklogger.py
