"""
● BROJ INDEKSA (izračunati broj potrebnih karaktera) - 
● IME (jedna reč, do 20 karaktera) - limitiraj name input do20 karaktera
● PREZIME (jedna reč, do 20 karaktera) limitiraj surname input do 20 karaktera
● BROJ POENA (neoznačen ceo broj) brojac za espb poena
Nakon toga:
a) Sortirati niz prema broju indeksa i ispisati ga u datoteku sortirani_studenti.txt.
b) Na standardni izlaz ispisati studenta sa najdužim i studenta sa najkraćim prezimenom.
c) Ispisati sve studente koji imaju više poena od broja koji je zadat kao argument poziva
programa u fajl čiji se naziv sastoji iz prefiksa “preko_”, unete cifre i postfiksa “_poena.txt”
(primer: preko_35_poena.txt)
d) U fajl izlaz.txt ispisati prosečnu dužinu imena studenata.


"""


 #cuva niz

data_base = open('studenti.txt', 'r')
while data_base:
    line = data_base.readline()
    print(line)
    if line == "":
        break



studenti = data_base.read()
print(studenti)

# Reads one line from file and writes it in the variable student
data_base = open('studenti.txt', 'r')
student = data_base.readline()


print(data_base.readline())

print(len(data_base.readline()))




student_podaci = student.split(" ")
index = student_podaci[0]
print(index)
index_length = len(index)
print("ovo", index_length)
name = student_podaci[1]
surname = student_podaci[2]
number_of_points = student_podaci[3]
print(index)
print(student_podaci)
print(index)
print(name)
print(surname)
print(number_of_points)
student_var = [index, name, surname, number_of_points]

