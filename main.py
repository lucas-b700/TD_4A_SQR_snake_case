from flask import Flask, request
import json
import csv

app = Flask(__name__)


# Definition de la classe Transaction 
class Transaction:
	def __init__(self, P1, P2, t, s:float):
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
	def debit(self, somme:float):
		self.solde -= somme
	def credit(self, somme:float):
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

for i in range(0, 5):
	i++
	time = tab[i][2]
	sum = float(tab[i][3])
	for j in range(len(people)):
		if(people[j].name == str(tab[i][0])):
			_P1 = people[j]
			people[j].debit(sum)
		if(people[j].name == str(tab[i][1])):
			_P2 = people[j]
			people[j].credit(sum)
	transaction = Transaction(_P1, _P2, time, sum)
	transactions[len(transactions) + 1] = transaction
	
# fonction pour afficher l'historique d'une personne
@app.route('/name/<_person>', methods = ['GET'])
def get_transactions_people(_person = None):
	if request.method == 'GET':
		returnTransaction=""
		for i in range(len(transactions) - 1):
			if(transactions[i].t > transactions[i + 1].t):
				temp = transaction[i]
				transaction[i] = transaction[i + 1]
				transaction[i + 1] = temp
		for i in range(len(transactions) + 1):
			if(i>0 and ((transactions[i].P1.name == str(_person)) or (transactions[i].P2.name == str(_person)))):
				returnTransaction += "Transaction de "+str(transactions[i].P1.name)+" vers le compte de "+str(transactions[i].P2.name)+" a "+str(transactions[i].t)+" pour une somme de "+str(transactions[i].s)+"€"+"<br><br>"
		return returnTransaction

# fonction pour afficher des transactions
@app.route('/', methods = ['GET'])
def get_transactions():
	if request.method == 'GET':
		returnTransaction=""
		for i in range(len(transactions) + 1):
			if(i>0):
				returnTransaction += "Transaction de "+str(transactions[i].P1.get_name())+" vers le compte de "+str(transactions[i].P2.name)+" a "+str(transactions[i].t)+" pour une somme de "+str(transactions[i].s)+"€"+"<br><br>"
		return returnTransaction
	
# fonction pour afficher le solde d'une personne
@app.route("/solde/<_person>", methods = ['GET']) 
def getSolde(_person = None): 
	if request.method == 'GET':
		returnSolde=""
		for i in range(len(people)):
			if(people[i].name == str(_person)):
				returnSolde += "Solde du compte de "+str(people[i].name)+" : "+str(people[i].solde)+"€"+"<br><br>"
		return returnSolde
	
# fonction pour ajouter une transaction
@app.route("/<_person1>/<_person2>/<_t>/<_s>", methods = ['PUT']) 
def addTransaction(_person1 = None, _person2 = None, _t = None, _s = None): 
	if request.method == 'PUT':
		for i in range(len(people)):
			if(people[i].name == str(_person1)):
				_person1 = people[i]
				people[i].debit(float(_s))
			if(people[i].name == str(_person2)):
				_person2 = people[i]
				people[i].credit(float(_s))
		transaction = Transaction(_person1, _person2, str(_t), float(_s))
		transactions[len(transactions)+1] = transaction
		return str(transactions)

if __name__ == '__main__':
	app.run()
