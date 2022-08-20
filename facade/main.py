from urllib.request import urlopen
import json


def get_todo_item() -> dict:
    with urlopen('https://jsonplaceholder.typicode.com/todos/1') as res:
        body = res.read()
    return json.loads(body)


def main():
    data = get_todo_item()
    print(data)

    # Output:
    # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}


if __name__ == '__main__':
    main()
