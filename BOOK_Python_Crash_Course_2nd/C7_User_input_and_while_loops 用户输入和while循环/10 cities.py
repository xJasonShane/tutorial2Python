promet = "\nPlease enter the name of a city you have visited:"
promet += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(promet)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
