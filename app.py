import requests

URL = '<Hello World! Lambda>'


def hello_world():
    result = requests.get(URL)
    print(result)
    print(result.text)

    # test output
    assert result.text == 'Hello World!'


def hello_name(name, method):
    """ accepts GET or POST and send request to amazon function """

    link = f'{URL}?name={name}'

    # from aws lambda, you can check method with httpMethod
    if method == 'GET':
        result = requests.get(link)
    elif method == 'POST':
        result = requests.get(link)

    print(result)
    print(result.text)

    # test output
    assert result.json() == {'httpMethod': f'{method}', 'text': f'Hello, {name}!'}


hello_name('John', 'GET')
