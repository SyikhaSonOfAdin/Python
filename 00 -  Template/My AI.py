import pyttsx3
engine = pyttsx3.init()

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

engine.setProperty('rate',150)
engine.setProperty('volume',1)
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[0].id)

engine.say('hello my name is echo')
engine.say("PLEASE INPUT PASSWORD")
engine.runAndWait()

pw = input(".")
if pw == "MUCHAMAD SYIKHA AKMAL" :
    engine.say("WELCOME BACK SIR")
    print("WELCOME BACK SIR")
    engine.say("Calculator or else sir?")
    print("Calculator or else sir?")
    engine.runAndWait()
    answer = input(".")
    if answer == "CALCULATOR" :
        engine.say("Do you want a quiz?(YES/NO)")
        yn = input(".")
        if yn == "YES" :
            print("Congratulation!! your first program was finish at 8/14/2022")
            hasil = int(input("Berapakah hasil dari 2x2?..."))
            if hasil == 4 :
                print("BENAR!")
            if hasil > 4 :
                print("HITUNGLAH DENGAN BENAR!")
            if hasil < 4 :
                print("BISA NGITUNG NGGA?!")
        if yn == "NO" : 
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

    if answer == "ELSE" :
        print("What's on your mind sir?")
else :
        print("WHO THE FUCK ARE YOU?"),
engine.stop()
