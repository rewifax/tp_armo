
from exponentiation import exponentiation_rapide, exponentiation_modulaire

if __name__ == "__main__":
    # Exemple de test
    a, b, n = 5, 13, 23  # Calcul de 5^13 mod 23
    print("Exponentiation rapide:", exponentiation_rapide(a, b))
    print("Exponentiation modulaire:", exponentiation_modulaire(a, b, n))
