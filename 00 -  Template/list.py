l1 = ['aku','kamu','dia']
print(l1)
l2 = ('aku','kamu','dia')
print(l2)
chc1 = input("Apakah anda akan mengakses list atau data tuple? :")
if chc1 == 'list' :
    print(l1)
    a=input('Tambah atau Kurang? :')
    if a== 'tambah' :
        b=input('Masukkan apa yang akan anda tambah :')
        l1.append(b)
        print(l1)
    if a== 'kurang' :
        c=input('Masukkan objek yang akan anda hilangkan :')
        l1.remove(c)
        print(l1)
if chc1 == 'tuple' :
    print(l2)
        