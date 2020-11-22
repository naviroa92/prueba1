# Ejercicio 1
import ast
import pandas as pd
import re
df_books = pd.read_csv("data/books.csv", dtype={'postal_code': str},
                        converters={'books': ast.literal_eval})
df_ratings = pd.read_csv("data/books_rating.csv")

print('')
print('')
print('|' * 50)
print(  'DF_BOOKS.INFO - ORIGINAL')
print('|' * 50)
print('')
print('')

df_books.info()
df_books_original = df_books.copy()
df_ratings_original = df_ratings.copy()

print('')
print('*' * 50)
print('EJERCICIO 1 ')
print('Se establece que la columna (name) es un identificador, por lo cual'
      'se procede a eliminar la columna con df_books = df_books.drop ')
print('*' * 50)


#Se elimina la columna 'name', ya que se considera un diferenciador.
df_books = df_books.drop(columns=['name'])
print('|' * 50)
print('DATA FREAME SIN COLUMNA NAME - INFO')
print('|' * 50)
print('')
print(df_books.info())

#Ejercicio 2
print('')
print('*' * 50)
print('EJERCICIO 2 ')
print('*' * 50)
print('')
print('Para este ejercicio convertimos el df_books y el df_ratings en un diccionario para '
      'iterar entre diccionarios y hacer la respectiva comparacion')
print('')
print('Creamos el diccionario d_users, la cual recibe los valores (user_ide / name) de '
      'la comparacion del valor de la llave (books - d_books) y el valor de (d_ratinds), cuando estos sean iguales'
      'se almacenaran en la valriable (d_users)  ')


#Codido para convertir df_books en un diccionario
d_books=df_books_original.to_dict('index')
#Codido para convertir df_rating en un diccionario
d_ratings = df_ratings.groupby(['user_id'])['book'].apply(lambda grp: list(grp.value_counts().index)).to_dict()
d_ratings_2=df_ratings_original.to_dict('index')

print()
print()
print('|' * 50)
print(  'D_BOOKS DICCIOANRIO')
print('|' * 50)
print()
print(d_books)
print()

print('|' * 50)
print('D_RATINGS DICCIONARIO')
print('|' * 50)
print()
print(d_ratings)



d_users = []
for d_books_key, d_books_value in d_books.items():

    for d_ratings_key, d_ratings_value in d_ratings.items():

        if  set(d_books_value['books']) == set(d_ratings_value):

            one_user= {}
            one_user['user_id'] = d_ratings_key
            one_user['name'] = d_books_value['name']
            d_users.append(one_user)
print()
print('|' * 50)
print('D_USERS DICCIONARIO')
print('|' * 50)
print(d_users)

#Ejericio 3
print('')
print('*' * 50)
print('EJERCICIO 3 ')
print('*' * 50)
print('')
print('Generamos un diccioanio donde se publica los valores (name - sex - age - postal_code - book - rating) con el'
      'objetivo de dentificar el rating de cada libro por cada usuario')
print('')
print('')

d_users_name = []

for d_ratings_key, d_ratings_value in d_ratings.items():

    for d_books_key, d_books_value in d_books.items():

            for d_ratings_2_key, d_ratings_2_value in d_ratings_2.items():

                if  set(d_books_value['books']) == set(d_ratings_value): # Comparacion de listado de libros

                    if (d_ratings_key) == (d_ratings_2_value['user_id']): # comparacion id entre (id - libros ) / ( id - rating )


                        books_user= {}
                        books_user['name'] = d_books_value['name']
                        books_user['sex'] = d_books_value['sex']
                        books_user['age'] = d_books_value['age']
                        books_user['postal_code'] = d_books_value['postal_code']
                        books_user['book'] = d_ratings_2_value['book']
                        books_user['rating'] = d_ratings_2_value['rating']

                        d_users_name.append(books_user)

print('|' * 50)
print('d_users_name')
print('|' * 50)
print('')
print(d_users_name)



#Ejericio 4
print('')
print('*' * 50)
print('EJERCICIO 4 ')
print('*' * 50)
print('')
#https://stackoverflow.com/questions/56999525/how-to-mask-specific-values-in-particular-column-in-python
df_books['postal_code'] = df_books['postal_code'].apply(lambda s: re.sub(r"(\d{3})\d{2}",r"\1**",s))
print(df_books)

#Ejericio 5
print('')
print('*' * 50)
print('EJERCICIO 5 - RANK SWAPPING')
print('*' * 50)
print('')
df_books['age'] = df_books['age'].rank(ascending=False)

print('|' * 50)
print('df_books')
print('|' * 50)
print(df_books[['sex','age','postal_code']])

print('|' * 50)
print('df_books_original')
print('|' * 50)
print(df_books_original[['sex','age','postal_code']])



