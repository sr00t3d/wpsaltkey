# WP Salt Key Updater 🔐

Readme: [Português](README-ptbr.md)

<img src="https://github.com/user-attachments/assets/0d89f024-2b58-4d77-b86f-4cd1becd61bd" width="700">

![License](https://img.shields.io/github/license/sr00t3d/wpsaltkey)
![Python Script](https://img.shields.io/badge/python-script-green)

The **WP Salt Key Updater** is a command-line utility designed to strengthen the security of WordPress sites. It automates the generation and replacement of secret keys and `salts` in the `wp-config.php` file, ensuring that all active sessions are invalidated and cookie encryption is refreshed.

## ❓ Why use it?

WordPress security keys (`AUTH_KEY`, `SECURE_AUTH_KEY`, etc.) make your site harder to hack by adding random characters to passwords. It is a good security practice to change these keys periodically or immediately after a suspected breach.

## ✨ Features

- **Full Automation**: Automatically replaces old keys with new ones.
- **Official API Integration**: Retrieves random and secure keys directly from `WordPress.org`.
- **Structure Preservation**: The script identifies the key block in your `wp-config.php` and replaces only what is necessary, without corrupting other settings.
- **Security**: Instantly invalidates all active logins, forcing re-authentication (useful for expelling unwanted users).

## 📋 Requirements
- **Python** 3 or higher installed  
- Existing **wp-config.php** file in the same directory as the script.  
- Write permissions for the **wp-config.php** file.  
- `curl` or `wget` tools installed on the server.

## 🚀 Installation and Usage

1. **Clone the Repository into the Same Directory as WordPress**

```bash
git clone https://github.com/sr00t3d/wpsaltkey/ .
```

2. **Grant Execution Permission**:
 
```bash
chmod +x saltkey.py
```

3. **Run the Script**

```bash
python3 saltkey.py
```

## ⚠️ Security Warning

> [!WARNING]  
> Important: This script modifies a critical system file. We strongly recommend backing up your wp-config.php before running the tool. When changing the keys, all users (including the administrator) will be logged out of the /wp-admin panel.  
> The script creates an automated backup before executing.

## ⚠️ Legal Notice

> [!WARNING]
> This software is provided "as is". Always make sure to test first in a development environment. The author is not responsible for any misuse, legal consequences, or data impact caused by this tool.

## 📚 Detailed Tutorial

For a complete, step-by-step guide, check out my full article:

👉 [**Change WordPress keys for security**](https://perciocastelo.com.br/blog/change-wordPress-keys-for-security.html)

## License 📄

This project is licensed under the **GNU General Public License v3.0**. See the [LICENSE](LICENSE) file for more details.
