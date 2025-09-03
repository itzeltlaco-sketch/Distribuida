from sympy import isprime
import alice
import bob

def establecerParametros():

    while True:
        try:
            p = int(input("Ingrese el valor de p: "))
            if isprime(p):
                break
            else:
                print("Ingrese un numero primo.")
        except ValueError:
            print("Error. Ingrese un numero entero primo.")

    print(" ")

    while True:
        try:
            g = int(input("Ingrese el valor de g: "))
            if 1 < g < p :
                break
            else:
                print("Ingrese un numero entero mayor a 1 y menor a p.")
        except ValueError:
            print("Error. Ingrese un numero entero.")

    print(" ")
    print(f"Parámetros públicos establecidos: p = {p}, g = {g}")
    print(" ")
    return p,g


def clavesCorrectas() -> bool:
    p,g = establecerParametros()

    a = alice.pedirSecretoAlice()
    b = bob.pedirSecretoBob()
    print(" ")

    A = alice.clavePublicaAlice(p,g,a)
    B = bob.clavePublicaBob(p,g,b)
    print(" ")

    claveCompartidaAlice = alice.claveCompartidaAlice(B,a,p)
    claveCompartidaBob = bob.claveCompartidaBob(A,b,p)
    
    if claveCompartidaAlice == claveCompartidaBob:
        print("Éxito, las claves son iguales")
        return True
    else: 
        print("Fracaso, las claves son diferentes")
        return False
        
if __name__ == "__main__":
    exito = clavesCorrectas()
    if exito:
        print("El intercambio de claves Diffie-Hellman fue exitoso ")
    else:
        print("El intercambio de claves Diffie-Hellman falló ")




