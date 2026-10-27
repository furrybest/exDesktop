import os

def ensure_dir_exists(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path

def get_plugins_dir() -> str:
    import extera_host
    return extera_host.PLUGINS_DIR or os.path.expanduser("~/.local/share/TelegramDesktop/tdata/plugins/plugins")
