import os
from shutil import which

from cx_Freeze import Executable, setup

packages = []
# Read from pyproject.toml [tool.poetry.dependencies]
with open("pyproject.toml", "r") as f:
    lines = f.read().splitlines()
    for i, line in enumerate(lines):
        if line.startswith("[tool.poetry.dependencies]"):
            break
    for line in lines[i + 1 :]:
        if not line:
            break
        package = line.split(" = ")[0].strip()
        if package not in ("python"):
            packages.append(package)


setup(
    executables=[Executable(which("gunicorn"), target_name="app")],
    options={
        "build_exe": {
            "packages": packages,
            "excludes": ['tests', 'alembic'],
            "includes": ["main"],
            "include_files": [
                (os.path.join(".", "start.sh"), "start.sh"),
                (os.path.join(".", "gunicorn_conf.py"), "gunicorn_conf.py"),
            ],
            "optimize": 1,  # 0, 1, 2
        },
    },
    version="1.0.0.20240610",
    description="Repro for cx_freeze and FastAPI",
    author="Cong Vo",
    name="cx_freeze-fastapi-repro",
)
