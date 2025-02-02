import requests


def RequestBLR():
    url = "https://9d330c61-5751-4a4b-996b-cdb372d3dfe2-00-181ng4cjfs9fd.spock.replit.dev/api/v1/test.json"
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print("Données reçues :", data)
            return data, response.status_code
        else:
            return response.status_code
    except requests.RequestException as e:
        return e


def PrintPretty(data):
    print("Informations utilisateur :")
    print("-" * 30)
    for key, value in data.items():
        if key == 'password':
            value = '********'
        print(f"{key.capitalize()}: {value}")
    print("-" * 30)


class getUser:
    def __init__(self):
        super().__init__()
        self.data, self.status = RequestBLR()

    def all(self):
        if self.CheckStatus():
            for user in self.data:
                return user
        else:
            raise ConnectionError

    def name(self, username):
        for user in self.data["data"]:
            if user["username"] == username:
                PrintPretty(user)

    def sortBy(self, type):
        pass

    def CheckStatus(self):
        if self.status == 200:
            return True
        else:
            return False
