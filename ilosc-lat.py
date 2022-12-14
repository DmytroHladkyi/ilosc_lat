from datetime import date
today = date.today()
birth_date = int(input('Kiedy się urodziłes (podaj rok): '))
age = today.year - birth_date
if age < 18:
    print(" Masz ", age, ". Jesteś jeszcze młody")
elif age >= 18 and age <= 25:
    print("Jesteś w złotym wieku, masz", age, "lat.")
else:
    print( "Ale stary jesteś, masz aż", age, "lat.")