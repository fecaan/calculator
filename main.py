
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


hesap = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def hesap_makinası():
    print(logo)
    num1 = float(input("ilk sayıyı girin: "))

    for sayı in hesap:
        print(sayı)
    devam = True
    while devam:

        hesap_sembolu = input("Yapmak istediğiniz işlemi seçiniz: ")
        num2 = float(input("sonraki sayıyı girin: "))

        hesaplama = hesap[hesap_sembolu]
        sonuc = hesaplama(num1, num2)
        print(f"{num1} {hesap_sembolu} {num2} = {sonuc}")

        if input(f"{sonuc} sayısı ile devam edecek misiniz? yes or no ") == "yes":
            num1 = sonuc
        else:
            devam = False

            hesap_makinası()


hesap_makinası()
