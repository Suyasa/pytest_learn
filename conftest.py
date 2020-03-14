import re
import pytest

reg_ss = re.compile(r'^\s+', re.MULTILINE)
reg_nl = re.compile(r'\n')
reg_ex_nl = re.compile(r'^\n')


@pytest.fixture
def check_result(capsys):
    def _check_result(app, func, inp, ans):
        def preprocess(text):
            regs = (reg_ex_nl, reg_ss)
            for r in regs:
                text = r.sub('', text)
            return text

        inp_list = reg_nl.split(preprocess(inp))
        ans = preprocess(ans)
        app.input = lambda: inp_list.pop(0)
        func()

        out, err = capsys.readouterr()
        assert out == ans
        assert err == ''

    return _check_result
