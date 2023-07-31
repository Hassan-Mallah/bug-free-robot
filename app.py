import requests

result = requests.get('<Hello World! Lambda>')
print(result)
print(result.text)

# test output
assert result.text == 'Hello World!'
