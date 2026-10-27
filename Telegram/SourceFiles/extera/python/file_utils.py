import os
import platform

def ensure_dir_exists(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path

def get_plugins_dir() -> str:
    import extera_host
    if getattr(extera_host, "PLUGINS_DIR", None):
        return extera_host.PLUGINS_DIR
    if platform.system() == "Windows":
        return os.path.abspath("tdata/plugins/plugins")
    return os.path.expanduser("~/.local/share/TelegramDesktop/tdata/plugins/plugins")
