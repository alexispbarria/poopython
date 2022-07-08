A = {"gato": "cat", "perro" : "dog", "caballo" : "horse"}
words = ['gato', 'leon', 'caballo']
for word in words:

    if word in A:

        print(word, "->", A[word])

    else:
        print(word, "no está en el diccionario")