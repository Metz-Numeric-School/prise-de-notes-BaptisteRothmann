temp_ambiante = float(input("Saisissez la température ambiante : "))
temp_bassin = float(input("Saisissez la température du bassin de refroidissement : "))

diff_temp = temp_ambiante - temp_bassin

if diff_temp < 20:
    print("ALARME !!!!")
elif diff_temp > 40:
    print("ALARME !!!!")
else:
    print("Tout va bien")