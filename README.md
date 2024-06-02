# Testing with Pytest

## Introduction

- project_2:
- project_3:
- project_4:
- project_5:



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

## Run 
```bash
# pytest with verbose output
pytest -v -s
```

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