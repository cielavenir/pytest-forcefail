# pytest-forcefail

pytest-forcefail is a plugin providing

- the method `pytest_forcefail.forcefail`
- the exception class `pytest_forcefail.ForceFailed`

these two will make the test failing **regardless of pytest.mark.xfail**.
