import pytest


from hello.prime import is_prime
from hello.prime import load_numbers_sorted


# def test_is_prime():
#     assert not is_prime(1)
#     assert is_prime(2)
#     assert is_prime(3)
#     assert not is_prime(4)
#     assert is_prime(5)
#     assert not is_prime(6)
#     assert is_prime(7)
#     assert not is_prime(8)
#     assert not is_prime(9)
#     assert not is_prime(10)
#     assert is_prime(11)

@pytest.mark.parametrize(('number', 'expected'), [
    (1, False),
    (2, True),
    (3, True),
    (4, False)
])
def test_is_prime(number, expected):
    assert is_prime(number) == expected


@pytest.fixture
def txt(tmpdir) -> str:
    tmpfile = tmpdir.join('numbers.txt')

    with tmpfile.open('w') as f:
        for n in [2, 5, 4, 3, 1]:
            f.write('{}\n'.format(n))

    yield str(tmpfile)

    tmpfile.remove()


def test_load_numbers_sorted(txt):
    assert load_numbers_sorted(txt) == [1, 2, 3, 4, 5]
