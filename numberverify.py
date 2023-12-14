import re

def verifie_format_telephone_regex(numero):
    pattern = re.compile(r'^\d{2}-\d{7}$')
    return bool(pattern.match(numero))

# Exemple d'utilisation
numero_test = "12-3456789"
resultat = verifie_format_telephone_regex(numero_test)
print(resultat)  # Cela devrait afficher True
