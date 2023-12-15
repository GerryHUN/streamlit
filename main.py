import streamlit as st

st.title("Programozás feladat")

szov = st.text_input("Adj meg egy szöveget!")

#1 Csupa nagybetű

st.write(f"1. Nagybetű: {szov.upper()}")

#2 Szavak száma


szavak = szov.split(" ")
darab = 0
for i in szavak:
    if i == "":
        continue
    else:
        darab += 1

st.write(f"2. Szavak száma: {darab}")

#3 Leggyakoribb szó

szavak_szama = {}

for i in szavak:
    if i in szavak_szama:
          szavak_szama[i] += 1
    else:
          szavak_szama[i] = 1

st.write(f"3. Leggyakoribb szó: {max(szavak_szama, key=szavak_szama.get)}")

#4 Leggyakoribb betű

betuk_szama = {}

for i in szov:
    if i in betuk_szama:
          betuk_szama[i] += 1
    else:
          betuk_szama[i] = 1
try: st.write(f"4. Leggyakoribb betű: {max(betuk_szama, key=betuk_szama.get)}")
except: st.write("")



#5 Betűk száma

betuk_szama = 0

betuk = szov.strip()

for i in betuk:
        betuk_szama += 1

st.write(f"5. Betűk száma: {betuk_szama}")