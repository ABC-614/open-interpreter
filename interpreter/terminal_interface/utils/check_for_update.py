import pkg_resources
from packaging import version

try:
    import requests
except Exception:  # pragma: no cover - optional dependency
    requests = None


def check_for_update():
    if requests is None:
        return False

    # Fetch the latest version from the PyPI API
    response = requests.get("https://pypi.org/pypi/open-interpreter/json")
    latest_version = response.json()["info"]["version"]

    # Get the current version using pkg_resources
    current_version = pkg_resources.get_distribution("open-interpreter").version

    return version.parse(latest_version) > version.parse(current_version)
