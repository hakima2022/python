d=input("veuillez entrer la valeur de la densité :")
ViscositéC=input("saisir la valeur de la viscosité cinematique:")
MasseV=input("donner la valeur de la masse volumique de réference:")
try:
    d=float(d)
    ViscositC=float(ViscositéC)
    MasseV=float(MasseV)
    µ=d*ViscositéC*MasseV
    print("la valeur de la viscosité dynamique est:",µ)
except:
    print("la valeur de densité et /ou viscosité ou la masse voulumique que vous avez pas correcte")

