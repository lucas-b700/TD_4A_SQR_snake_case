from flask import Flask, request
import json
import csv

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
	def __init__(self, name, solde:float):
		self.name = name
		self.solde = solde
		#Transactions
		def debit(self, somme:float)
		self.solde -= somme
		def credit(self, somme:float)
		self.solde += somme

p1 = Person("Maxime",10000)
p2 = Person("Lucas",10000)
p3 = Person("Pierre",6000)
p4 = Person("Paul",4000)
p5 = Person("Jacques",2000)
p6 = Person("Michelle",3000)
p7 = Person("Josette",2500)
p8 = Person("Bernadette",2000)
p9 = Person("Theo",3500)

# Creation de nos listes
people = {0:p1, 1:p2, 2:p3, 3:p4, 4:p5, 5:p6, 6:p7, 7:p8, 8:p9}
transactions = {}
tab = []

#Ouverture du fichier fichierClient.csv
with open('fichierClient.csv', newline='', encoding="utf-8-sig") as csvfile:
	dataRead = csv.reader(csvfile)
	for row in dataRead:
		for rows in row:
			data = (str(rows).split(' | '))
			tab.append(data)

for i in range(1, 8):
	time = tab[i][2]
	sum = tab[i][3]
	for person in people:
		if person.nom == tab[i][0]:
			_P1 = person
			person.debit(sum)
		elif person.nom == tab[i][1]:
			_P2 = person
			person.credit(sum)
		transaction = Transaction(_P1, _P2, time, sum)
		transactions[len(transactions)+1]=transaction


		### Modifications en cours du code suite au changement de la classe Person
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
