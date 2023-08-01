import requests

URL = '<Hello World! Lambda>'


def hello_world():
    result = requests.get(URL)
    print(result)
    print(result.text)

    # test output
    assert result.text == 'Hello World!'


def hello_name(name):
    link = f'{URL}?name={name}'
    result = requests.get(link)

    print(result)
    print(result.text)

    # test output
    assert result.text == f'Hello, {name}!'


hello_name('John')
