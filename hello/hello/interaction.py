def send(message: str):
    receive(message)


def receive(message: str):
    print('received: {}'.format(message))


def send2(message: str):
    ok = receive2(message)

    if ok:
        print('send2: success')
    else:
        print('send2: failure')


def receive2(message: str) -> bool:
    print('received: {}'.format(message))

    return True
