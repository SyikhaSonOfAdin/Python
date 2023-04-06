#OPERASIONAL HITUNG (+,-,/,X)
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

#FUNCTION RANDOM
def stranger(depan,belakang) :
    print('hello',depan,belakang,'and welcome')

depan = input('your first name ;')
belakang = input('your last name ;')
stranger(depan,belakang)