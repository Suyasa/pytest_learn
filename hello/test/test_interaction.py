from hello.interaction import send
from hello.interaction import send2
from hello.interaction import receive


def test_send(mocker):
    receive = mocker.patch('hello.interaction.receive')

    send('Hello World!!!')

    receive.assert_called_once_with('Hello World!!!')

    assert receive.call_args_list == [
        mocker.call('Hello World!!!'),
    ]


def test_send2_failure(mocker, capsys):
    receive2 = mocker.patch('hello.interaction.receive2', return_value=False)

    send2('Hello World!')

    receive2.assert_called_once_with('Hello World!')

    out, _ = capsys.readouterr()

    assert out == 'send2: failure\n'


def test_send2_success(mocker, capsys):
    receive2 = mocker.patch('hello.interaction.receive2')

    send2('Hello World!')

    receive2.assert_called_once_with('Hello World!')

    out, _ = capsys.readouterr()

    assert out == 'send2: success\n'


def test_receive(capsys):

    receive('hello')
    out, _ = capsys.readouterr()

    assert out == 'received: hello\n'
