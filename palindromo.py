word = input("Palabra/Frase: ")

print("Si" if word.replace(" ", "") == word[::-1].replace(" ", "") else "No")