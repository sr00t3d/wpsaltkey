# WP Salt Key Updater 🔐

Readme: [English](README.md)

![License](https://img.shields.io/github/license/sr00t3d/wpsaltkey)
![Python Script](https://img.shields.io/badge/python-script-green)

<img width="700" src="wpsaltkey-cover.webp" />

O **WP Salt Key Updater** é um utilitário em linha de comando desenhado para fortalecer a segurança de sites WordPress. Ele automatiza a geração e a substituição das chaves secretas e `salts` no ficheiro `wp-config.php`, garantindo que todas as sessões ativas sejam invalidadas e que a criptografia de cookies seja renovada.

## ❓ Por que usar?

As chaves de segurança do WordPress (`AUTH_KEY`, `SECURE_AUTH_KEY`, etc.) tornam o seu site mais difícil de hackear ao adicionar caracteres aleatórios às palavras-passe. É uma boa prática de segurança alterar estas chaves periodicamente ou imediatamente após uma suspeita de invasão.

## ✨ Funcionalidades

- **Automação Completa**: Substitui as chaves antigas pelas novas de forma automática.
- **Integração com API Oficial**: Obtém chaves aleatórias e seguras diretamente do `WordPress.org`.
- **Preservação de Estrutura**: O script identifica o bloco de chaves no seu `wp-config.php` e substitui apenas o necessário, sem corromper outras configurações.
- **Segurança**: Invalida instantaneamente todos os logins ativos, forçando uma nova autenticação (útil para expulsar usuários indesejados).

## 📋 Requerimentos
- **Python** 3 ou superior instalado
- Arquivo **wp-config.php** existente no mesmo diretorio do script.
- Permissões de escrita no arquivo **wp-config.php**.
- Ferramentas `curl` ou `wget` instaladas no servidor.

## 🚀 Instalação e Uso

1. **Clonar o Repositório no mesmo diretorio do WordPress**

```bash
git clone https://github.com/sr00t3d/wpsaltkey/ .
```

2. **Dar Permissão de Execução**:
 
```bash
chmod +x saltkey.py
```

3. **Executar o Script**

```bash
python3 saltkey.py
```

## ⚠️ Aviso de Segurança

> [!WARNING]
> Importante: Este script altera um ficheiro crítico do sistema. Recomendamos fortemente a realização de um backup do seu wp-config.php antes de executar a ferramenta. Ao alterar as chaves, todos os utilizadores (incluindo o administrador) serão desconectados do painel /wp-admin.
> O script cria um backup automatizado antes de executar.

## ⚠️ Aviso Legal

> [!WARNING]
> Este software é fornecido "como está". Certifique-se sempre de testar primeiro em um ambiente de desenvolvimento. O autor não se responsabiliza por qualquer uso indevido, consequências legais ou impacto em dados causado por esta ferramenta.

## 📚 Tutorial Detalhado

Para um guia completo, confira meu artigo completo:

👉 [**Change WordPress Keys for security**](https://perciocastelo.com.br/blog/change-wordPress-keys-for-security.html)

## Licença 📄

Este projeto está licenciado sob a **GNU General Public License v3.0**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
