# Testing with Pytest

## Introduction

This project demonstrates how to test FastAPI, SQLAlchemy with Pytest.

## Installation

```bash
# create virtual environment
python3 -m venv venv

# activate virtual environment
source venv/bin/activate

# install dependencies with poetry
poetry install

```

## Run FastAPI

```bash
cd project_7

# run FastAPI
uvicorn main:app --reload
# Or
fastapi dev 

# OpenAPI docs
# --> http://localhost:8000/docs

```



## Run tests

```bash
# pytest with verbose output
cd project_7
pytest -v -s
```


## Mock or Monkeypatch
Ref: https://pytest-with-eric.com/mocking/pytest-monkeypatch/#:~:text=The%20two%20are%20very%20similar,as%20part%20of%20your%20test.

```text
Is MonkeyPatch The Same As Mocking or Patching?
Yes and No 

The two are very similar and have subtle differences.

Monkeypatching is the act of replacing a function, method, class or variable at runtime.

Mock actually uses Monkeypatch under the hood to mock or change certain objects being evaluated at run time as part of your test.

The exact differences are not really important, what’s more important is that you understand that it’s possible to override functions, classes, libraries and variables in Unit Tests.
```



## Known Issues


Beware of importing in pytest, it may cause the issue in initialization: https://github.com/tiangolo/fastapi/issues/5090#issuecomment-1170055389

## References

- https://realpython.com/pytest-python-testing/
- https://testdriven.io/blog/pytest-for-beginners/
- https://pytest-with-eric.com/fixtures/pytest-fixture-scope/
- https://pytest-with-eric.com/pytest-best-practices/pytest-conftest/
- https://pytest-with-eric.com/introduction/how-to-run-pytest-in-vscode/
- https://pytest-with-eric.com/introduction/fixture-mocker-not-found/
- https://pytest-with-eric.com/mocking/pytest-monkeypatch/#:~:text=The%20two%20are%20very%20similar,as%20part%20of%20your%20test.
- https://stackoverflow.com/questions/41701226/what-is-the-difference-between-mocking-and-monkey-patching
- https://medium.com/@johnidouglasmarangon/how-to-setup-memory-database-test-with-pytest-and-sqlalchemy-ca2872a92708
- https://github.com/tiangolo/fastapi/issues/5090#issuecomment-1170055389
- https://stackoverflow.com/questions/49028611/pytest-cannot-find-module
- https://fastapi.tiangolo.com/advanced/testing-database/
- https://gist.github.com/kissgyorgy/e2365f25a213de44b9a2?permalink_comment_id=3704123
- https://docs.sqlalchemy.org/en/20/core/metadata.html#sqlalchemy.schema.Table.params.extend_existing