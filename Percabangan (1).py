#!/usr/bin/env python
# coding: utf-8

# <h3>Percabangan<h3>

# In[2]:


#menentukan ganjil genap
nilai = int(input('isikan nilai:'))
sisa_bagi = nilai % 2

if sisa_bagi==0:
    print(f'{nilai} adalah bilangan genap')
else:
    print(f'{nilai}adalah bilangan  ganjil')
print('program selesai')


# In[13]:


# 0 - 49 => E
# 50 - 59 => D
# 60 - 69 => C
# 70 - 84 => B
# 85 - 100 => A

nilai_program = int(input('Isikan Nilai Pemograman:'))
if nilai_program < 0 or nilai_program > 100:
    print("nilai ada salah")

if nilai_program <50:
    print("E")
elif nilai_program <60:
    print("D")
elif nilai_program <70:
    print ("C")
elif nilai_program <85:
    print ("B")
elif nilai_program <=100:
    print ("A")
else:
    print("input anda salah")
    
            


# In[24]:


username = input('isikan username')
password = input('isikan password')

# jika username salah => Username anda salah
# jika password salah => Password anda salah
# jika keduanya salah => Username dan password anda salah
# jika keduanya benar => Selamat datang {username}
# username: admin
# password: admin

if username == 'admin':
    if password=='admin':
        print(f'selamat datang {username}')
    else:
        print(f'password anda salah')
else:
    if password == 'admin':
        print("Username anda salah")
    else:
        print("Username dan password anda salah")
        

        


# In[59]:


nama = input("isikan nama:")
umur = int(input("isikan umur:"))
tempat_tinggal = input("isikan alamat:")
tabungan = int(input("isikan nominal:"))

pangkat =''
if umur > 40:
    if tempat_tinggal == 'New York' or tempat_tinggal =='Nevada' or tempat_tinggal=='Havana' :
        if tabungan > 10:
            pangkat = 'Don'
elif umur >= 25 and umur <= 40:
    if tempat_tinggal == 'New Jersey' or tempat_tinggal == 'Manhattan' or tempat_tinggal == 'Nevada':
        if tabungan > 0 and tabungan <= 2:
            pangkat = "Underboss"
elif umur >= 18 and umur <= 24:
    if tempat_tinggal =='California' or tempat_tinggal =='Detroit' or tempat_tinggal =='Boston':
        if tabungan < 1:
            pangkat ='Capo'
            
if pangkat != '':
    print(f'{nama} kemungkinan seorang anggota mafia dengan pangkat {pangkat}')
else:
    print(f'{nama} tidak mencurigakan')


# In[ ]:




