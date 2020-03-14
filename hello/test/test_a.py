import hello.a as app


def test_1(check_result):
    inp = '''
    3 4
    '''

    ans = '''
    Even
    '''

    check_result(app, app.main, inp, ans)


def test_2(check_result):
    inp = '''
1 21
    '''

    ans = '''
        Even
    '''

    check_result(app=app, func=app.wrong, inp=inp, ans=ans)
