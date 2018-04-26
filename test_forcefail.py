pytest_plugins = "pytester"
import pytest

@pytest.mark.parametrize(('func','fail'),[
    ('fail',False),
    ('forcefail',True)
])
def test_forcefail(testdir, func, fail):
    p = testdir.makepyfile(test="""
        import pytest
        from _pytest.outcomes import fail
        from pytest_forcefail import forcefail

        @pytest.mark.xfail
        def test_foo():
            %s()
    """ % func)
    result = testdir.runpytest(p, '-rxf')
    result.stdout.fnmatch_lines('*1 failed*' if fail else '*1 xfailed*')
    
    assert result.ret == (1 if fail else 0)

@pytest.mark.parametrize(('exc','fail'),[
    ('Failed',False),
    ('ForceFailed',True)
])
def test_ForceFailed(testdir, exc, fail):
    p = testdir.makepyfile(test="""
        import pytest
        from _pytest.outcomes import Failed
        from pytest_forcefail import ForceFailed

        @pytest.mark.xfail
        def test_foo():
            raise %s()
    """ % exc)
    result = testdir.runpytest(p, '-rxf')
    result.stdout.fnmatch_lines('*1 failed*' if fail else '*1 xfailed*')
    assert result.ret == (1 if fail else 0)
