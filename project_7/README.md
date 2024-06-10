# FastAPI + SQLAlchemy + Pytest


# TODO
- [x] Add `FastAPI`
- [x] Add `SQLAlchemy` Models
- [x] Add `Pytest`
- [x] Add `Alemic` for migrations
- [x] Add `Poetry` to manage dependencies
- [x] Add `cx_Freeze` to create an executable
- [x] Add `docker` to containerize the application
- [ ] Add `GitHub Actions` for CI/CD

## Installation

```bash

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the requirements with poetry
poetry install

# Run the FastAPI server
uvicorn main:app --reload

# Run the migrations
alembic upgrade head

# Run the tests
pytest . -v -s

# Export the requirements
poetry export -f requirements.txt --output requirements.txt
```



## Known Issues

```bash
sqlalchemy.exc.MissingGreenlet: greenlet_spawn has not been called; can't call await_only() here. Was IO attempted in an unexpected place? (Background on this error at: https://sqlalche.me/e/20/xd2s)
```