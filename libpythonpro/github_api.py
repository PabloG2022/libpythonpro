import requests


def busca_avatar(usuario):
    '''
    busca um avatar de um usuário no gitHub

    :param usuario:str com nome de usuário no github
    :return:str com o link do avatar
    '''
    url =f'https://api.github.com/users/{}'
    resp = requests.get(url)
    return resp.json()['avatar_url']

if __name__ == '__main__':
    print(busca_avatar('PabloG2022'))

