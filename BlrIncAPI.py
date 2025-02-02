import requests
from tabulate import tabulate


def displayTable(data):
    headers = ["Username", "Email", "Solde", "Description", "Date"]
    table = [[user["username"], user["email"], user["solde"], user["description"], user["date"]] for user in data]
    print(tabulate(table, headers=headers, tablefmt="grid"))


def RequestBLR(type="users"):
    UserURL = "https://9d330c61-5751-4a4b-996b-cdb372d3dfe2-00-181ng4cjfs9fd.spock.replit.dev/api/v1/users.json"
    MarketURL = "https://9d330c61-5751-4a4b-996b-cdb372d3dfe2-00-181ng4cjfs9fd.spock.replit.dev/api/v1/market.json"
    url = ""

    if type == "users":
        url = UserURL
    elif type == "market":
        url = MarkerURL
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data, response.status_code
        else:
            return response.status_code
    except requests.RequestException as e:
        return e


def printPretty(data):
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
        self.data, self.status = RequestBLR("users")

    def all(self):
        if self.CheckStatus():
            return self.data["data"]
        else:
            raise ConnectionError

    def name(self, username):
        for user in self.data["data"]:
            if user["username"] == username:
                return user

    def sortBy(self, types, order="asc"):
        if self.CheckStatus():
            if types in ["username", "solde", "date"]:
                reverse = order == "desc"
                return sorted(self.data["data"], key=lambda x: x[types], reverse=reverse)
            else:
                raise ValueError("Type de tri non supporté")
        else:
            raise ConnectionError("Échec de connexion à l'API")

    def CheckStatus(self):
        if self.status == 200:
            return True
        else:
            return False


class getMarketCap:
    def __init__(self):
        super().__init__()
        self.data, self.status = RequestBLR("market)


class getTransaction:
    def __init__(self):
        super().__init__()
        
