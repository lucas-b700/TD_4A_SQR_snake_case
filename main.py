from flask import Flask, request
import json

app = Flask(__name__)


# Definition de la classe Transaction
class Transaction:
    def __init__(self, P1, P2, t, s):
        self.P1 = P1
        self.P2 = P2
        self.t = t
        self.s = s

	
# Definition de la classe Person
class Person:
    def __init__(self, solde, transactions):
        self.solde = solde
        self.transactions = transactions

# Creation de nos listes de Transaction et de personnes, vide à cet instant
transactions = []
people = []

# fonction pour afficher une personne
@app.route('/')
def get_people():
    return json.dumps([p.__dict__ for p in people])

# fonction pour afficher une transaction
@app.route('/transactions')
def get_transactions():
    return json.dumps([t.__dict__ for t in transactions])

# fonction pour ajouter une personne dans la liste
@app.route('/add_person', methods=["POST"])
def add_person():
    if request.method == 'POST':
        solde = request.form.get('solde')
        people.append(Person(solde, []))
        return get_people()

# fonction pour ajouter une transaction dans la liste
@app.route('/add_transaction', methods=["POST"])
def add_transaction():
    if request.method == 'POST':
        P1_index = int(request.form.get('P1'))
        P2_index = int(request.form.get('P2'))
	if 0 <= P1_index < len(people) and 0 <= P2_index < len(people):
   		P1 = people[P1_index]
  	  	P2 = people[P2_index]
	else:
  	        return "Error : Aucune personne n'a été trouvée avec cet indice."
        t = int(request.form.get('t'))
        s = int(request.form.get('s'))
        P1.solde -= s
        P2.solde += s
        transaction = Transaction(P1, P2, t, s)
        transactions.append(transaction)
        P1.transactions.append(transaction)
        P2.transactions.append(transaction)
        return get_transactions()
