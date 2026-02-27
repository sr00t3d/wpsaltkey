#!/usr/bin/env python3
# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║                                                                           ║
# ║   WordPress Salt Key Updater v1.1.0                                       ║
# ║                                                                           ║
# ╠═══════════════════════════════════════════════════════════════════════════╣
# ║   Autor:   Percio Castelo                                                 ║
# ║   Contato: percio@evolya.com.br | contato@perciocastelo.com.br            ║
# ║   Web:     https://perciocastelo.com.br                                   ║
# ║                                                                           ║
# ║   Função:  Automatically fetch and update                                 ║
# ║            WP security keys in wp-config.php                              ║
# ╚═══════════════════════════════════════════════════════════════════════════╝

import os
import re
import sys
import shutil
import urllib.request

# --- CONFIGURATION ---
API_URL = "https://api.wordpress.org/secret-key/1.1/salt/"
WP_CONFIG = "wp-config.php"
WP_BACKUP = "wp-config.php.bak"
# ---------------------

# Detect System Language
# Gets the first 2 characters from environment variable (e.g., 'pt' from 'pt_BR.UTF-8')
system_lang = os.getenv('LANG', 'en')[:2]

if system_lang == 'pt':
    # Portuguese Messages
    MSG_ERR_NOT_FOUND = "ERRO: O arquivo '{}' não foi encontrado neste diretório."
    MSG_FETCHING = "Obtendo novas chaves de segurança da API do WordPress..."
    MSG_BACKUP = "Criando backup do arquivo original para '{}'..."
    MSG_UPDATING = "Atualizando chaves no arquivo de configuração..."
    MSG_SUCCESS = "SUCESSO: As chaves de segurança foram atualizadas!"
    MSG_ERR_NET = "ERRO: Falha ao conectar na API do WordPress."
    MSG_ERR_PERM = "ERRO: Permissão negada ao tentar gravar o arquivo."
else:
    # English Messages (Default)
    MSG_ERR_NOT_FOUND = "ERROR: The file '{}' was not found in this directory."
    MSG_FETCHING = "Fetching fresh security keys from WordPress API..."
    MSG_BACKUP = "Creating backup of original file to '{}'..."
    MSG_UPDATING = "Updating keys in configuration file..."
    MSG_SUCCESS = "SUCCESS: Security keys have been updated!"
    MSG_ERR_NET = "ERROR: Failed to connect to WordPress API."
    MSG_ERR_PERM = "ERROR: Permission denied when trying to write file."

# Get the absolute path of the script file
script_directory = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(script_directory, WP_CONFIG)
backup_path = os.path.join(script_directory, WP_BACKUP)

# 1. Check if wp-config.php exists
if not os.path.exists(config_path):
    print(MSG_ERR_NOT_FOUND.format(WP_CONFIG))
    sys.exit(1)

# 2. Fetch values from API
print(MSG_FETCHING)
try:
    with urllib.request.urlopen(API_URL) as response:
        new_keys_content = response.read().decode("utf-8")
except Exception as e:
    print(f"{MSG_ERR_NET} ({e})")
    sys.exit(1)

# 3. Create Backup
print(MSG_BACKUP.format(WP_BACKUP))
try:
    shutil.copy2(config_path, backup_path)
except IOError as e:
    print(f"{MSG_ERR_PERM} ({e})")
    sys.exit(1)

# 4. Parse the NEW keys into a dictionary
key_dict = {}
for line in new_keys_content.splitlines():
    # Regex to capture the Key Name (group 1) and the New Value (group 2)
    match = re.search(r"define\('([^']*)',\s*'([^']*)'\);", line)
    if match:
        key_name, key_value = match.groups()
        # Store the complete replacement string
        key_dict[key_name] = f"define('{key_name}', '{key_value}');"

# 5. Read the current configuration
with open(config_path, "r", encoding="utf-8", errors="ignore") as file:
    config_content = file.read()

# 6. Replace keys in memory
print(MSG_UPDATING)
for key_name, replacement_line in key_dict.items():
    # Regex to find the existing line in wp-config (handles different spacing)
    # Looks for: define('KEY_NAME', 'anything');
    pattern = r"define\('" + re.escape(key_name) + r"',\s*'.*'\);"
    
    # If the key exists in the file, replace it. 
    # If it doesn't exist, we don't add it (safety measure to not break custom configs)
    if re.search(pattern, config_content):
        config_content = re.sub(pattern, replacement_line, config_content)

# 7. Write the updated file
try:
    with open(config_path, "w", encoding="utf-8") as file:
        file.write(config_content)
    print(f"\n{MSG_SUCCESS}")
except IOError as e:
    print(f"{MSG_ERR_PERM} ({e})")
    # Try to restore backup if write fails
    shutil.copy2(backup_path, config_path)
    sys.exit(1)