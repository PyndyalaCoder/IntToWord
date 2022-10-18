def wordForUnit(single):
    match single:
        case 0:
            return "Zero"
        case 1:
            return "One"
        case 2:
            return "Two"
        case 3:
            return "Three"
        case 4:
            return "Four"
        case 5:
            return "Five"
        case 6:
            return "Six"
        case 7:
            return "Seven"
        case 8:
            return "Eight"
        case 9:
            return "Nine"

def wordForTens(double):
    match double:
        case 2:
            return "Twenty"
        case 3:
            return "Thirty"
        case 4:
            return "Forty"
        case 5:
            return "Fifty"
        case 6:
            return "Sixty"
        case 7:
            return "Seventy"
        case 8:
            return "Eighty"
        case 9:
            return "Ninety"

def wordForTeens(double):
    match double:
        case 10:
            return "Ten"
        case 11:
            return "Eleven"
        case 12:
            return "Twelve"
        case 13:
            return "Thirteen"
        case 14:
            return "Fourteen"
        case 15:
            return "Fifteen"
        case 16:
            return "Sixteen"
        case 17:
            return "Seventeen"
        case 18:
            return "Eighteen"
        case 19:
            return "Nineteen"

def wordForHundreds(number):
    niw = ""
    hundreds = number//100
    if hundreds != 0:
        temporary = wordForUnit(hundreds) + " Hundred "
        niw += temporary
    number = number % 100
    tens = number//10
    if tens != 0:
        if tens == 1:
            temp = wordForTeens(number)
            niw += temp + " "
            number = None
        else:
            temp = wordForTens(tens)
            niw += temp + " "
    if number:
        number = number % 10
        if number != 0:
            temp = wordForUnit(number)
            niw += temp
    return niw

big_numbers = {
    "Trillion": 1000000000000,
    "Billion": 1000000000,
    "Million":1000000,
    "Thousand":1000
}
while True:
    number = int(input("Enter the Number: "))
    if len(str(number)) > 15:
        exit("This program currently does not support numbers with lengths greater than 15 digits")
    print(f"{number}:")
    if number <0:
        exit()
    if number == 0:
        print("Zero")
    else:
        newWord = ""
        trillions = number//big_numbers["Trillion"]
        if trillions != 0:
            newWord += wordForHundreds(trillions) + " " +"Trillion "
        number = number % big_numbers["Trillion"]
        billions = number//big_numbers["Billion"]
        if billions != 0:
            newWord += wordForHundreds(billions) + " " + "Billion "
        number = number% big_numbers["Billion"]
        millions = number//big_numbers["Million"]
        if millions != 0:
            newWord += wordForHundreds(millions) + " " + "Million "
        number = number%big_numbers["Million"]
        thousands = number//big_numbers["Thousand"]
        if thousands != 0:
            newWord += wordForHundreds(thousands) + " " + "Thousand "
        number = number%big_numbers["Thousand"]
        newWord += wordForHundreds(number)

        print(newWord)
