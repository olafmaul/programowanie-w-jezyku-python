#Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest parzysta i zwróci tą informację jako typ logiczny bool (True/False).
#Należy uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" / "Liczba nieparzysta".
def steven_even(x):
	return x % 2 == 0

wybrana_liczba = 10

czy_even = steven_even(wybrana_liczba)

if czy_even :
	print(f"Liczba {wybrana_liczba}: jest parzysta")
else :
	print(f"Liczba {wybrana_liczba}: jest nieparzysta")
