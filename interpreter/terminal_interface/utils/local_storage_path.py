import os

try:
    import appdirs
except Exception:  # pragma: no cover - optional dependency
    appdirs = None

# Using appdirs if available, otherwise fall back to a standard location
if appdirs:
    config_dir = appdirs.user_config_dir("Open Interpreter")
else:
    config_dir = os.path.join(os.path.expanduser("~"), ".config", "Open Interpreter")


def get_storage_path(subdirectory=None):
    if subdirectory is None:
        return config_dir
    else:
        return os.path.join(config_dir, subdirectory)
