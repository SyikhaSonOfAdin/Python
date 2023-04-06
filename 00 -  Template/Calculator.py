def perkalian(a,b) :
    hasil = a*b
    print(a,"x",b,"=",hasil)
    return hasil
def penjumlahan(a,b) :
    hasil = a + b
    print(a,"+",b,"=",hasil)
    return hasil
def pengurangan(a,b) :
    hasil = a-b
    print(a,"-",b,"=",hasil)
    return hasil
def pembagian(a,b) :
    hasil = a/b
    print(a,":",b ,"=", hasil)
    return hasil
print("Calculator.beta")
bilangan = int(input("Masukkan bilangan pertama :"))
bilangan1 = int(input("Masukkan bilangan kedua :"))
print("Tentukan operasi yang diinginkan (Jawab dalam +, -, x, / )")
calc1 = input(".")

if calc1 == "+" :
    penjumlahan(bilangan,bilangan1)
if calc1 == "x" :
    perkalian(bilangan,bilangan1)
if calc1 == "-" :
    pengurangan(bilangan,bilangan1)
if calc1 == "/" :
    pembagian(bilangan,bilangan1)