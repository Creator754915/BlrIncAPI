# API BLR - Documentation

## Description
Cette API permet de récupérer des informations sur les utilisateurs via une requête HTTP GET. Elle inclut des fonctionnalités pour afficher et manipuler les données des utilisateurs.

## Installation
Assurez-vous d'avoir Python installé ainsi que la bibliothèque `requests`.

```sh
pip install requests
```

## Utilisation

### 1. Récupérer les données de l'API
La fonction `RequestBLR()` envoie une requête à l'API et récupère les données sous forme de dictionnaire.

```python
from BlrIncAPI import RequestBLR

data, status = RequestBLR()
if status == 200:
    print(data)
```

### 2. Affichage des données de manière lisible
La fonction `PrintPretty(data)` permet d'afficher les informations utilisateur de manière formatée.

```python
from BlrIncAPI import PrintPretty

PrintPretty(data)
```

### 3. Classe `getUser`
Une classe `getUser` est disponible pour manipuler plus facilement les données des utilisateurs.

#### a. Récupérer tous les utilisateurs
```python
from BlrIncAPI import getUser

gu = getUser()
all_users = gu.all()
print(all_users)
```

#### b. Rechercher un utilisateur par nom
```python
user_info = gu.name("nom_utilisateur")
```

#### c. Vérifier le statut de la requête
```python
if gu.CheckStatus():
    print("Connexion réussie !")
else:
    print("Échec de connexion !")
```

## Remarque
- Les mots de passe des utilisateurs sont masqués pour des raisons de sécurité.
- La méthode `sortBy(self, type)` est actuellement non implémentée.

## Auteur
Développé par [Votre Nom].

## Licence
Ce projet est sous licence MIT.

