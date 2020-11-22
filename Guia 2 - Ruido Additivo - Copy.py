
import ast
import pandas as pd
import numpy as np

df_census = pd.read_csv('data/adult.data',
names=[
'age', 'workclass', 'fnlwgt', 'education',
'education-num', 'marital-status', 'occupation',
'relationship', 'race', 'sex', 'capital-gain',
'capital-loss', 'hours-per-week', 'native-country',
'target'])

df_census.drop(['workclass', 'education', 'education-num', 'marital-status',
'occupation', 'relationship', 'race', 'sex', 'native-country',
'target'],
axis=1, inplace=True)

print('*' * 50 )
print('DF_CENSUS.INFO INICIAL')
print('*' * 50 )
print()
df_census.info()


print('*' * 50 )
print('DF_CENSUS INICIAL')
print('*' * 50 )
print()
print(df_census)

print('*' * 50 )
print('DESARROLLO EJERCICIO 7')
print('*' * 50 )
print()
# Ejericcio 7

#AGE
print('|' * 50)
print('AGE . INFO')
print('|' * 50 )
print()
df_census_age = df_census.drop(columns=['fnlwgt','capital-gain','capital-loss','hours-per-week'])
df_census_age.info()
x = df_census_age.to_numpy()

print('|' * 50)
print('DESVIACION ESTANDARD AGE')
print('|' * 50 )
print()

standard_desviation_age = np.std(x)
media = 0

print('La desviacion estandard de age es:')
print(standard_desviation_age)
print()

print('|' * 50)
print('VALORES DE RUIDO PARA AGE')
print('|' * 50 )
print()
p_age = np.random.normal(media,standard_desviation_age, df_census_age.shape)

print(p_age)

print('|' * 50)
print('VALORES DE AGE + RUIDO')
print('|' * 50 )
print()
df_age = p_age + df_census_age
print(df_age)


#FNLWGT
print('|' * 50)
print('FNLWGT . INFO')
print('|' * 50 )
print()
df_census_fnlwgt = df_census.drop(columns=['age','capital-gain','capital-loss','hours-per-week'])
df_census_fnlwgt.info()
y = df_census_fnlwgt.to_numpy()

print('|' * 50 )
print('DESVIACION ESTANDARD FNLWGT')
print('|' * 50 )
print()

standard_desviation_fnlwgt = np.std(y)
media = 0

print('La desviacion estandard de fnlwgt es:')
print(standard_desviation_fnlwgt)
print()

print('|' * 50)
print('VALORES DE RUIDO PARA FNLWGT')
print('|' * 50 )
print()
p_fnlwgt = np.random.normal(media,standard_desviation_fnlwgt, df_census_fnlwgt.shape)
print(p_fnlwgt)


print('|' * 50)
print('VALORES DE FNLWGT + RUIDO')
print('|' * 50 )
print()
df_fnlwgt = p_fnlwgt + df_census_fnlwgt
print(df_fnlwgt)


#CAPITAL GAIN
print('|' * 50)
print('CAPITAL GAIN . INFO')
print('|' * 50 )
print()
df_census_capital_gain = df_census.drop(columns=['age','fnlwgt','capital-loss','hours-per-week'])
df_census_capital_gain.info()
Z = df_census_capital_gain.to_numpy()


print('|' * 50 )
print('DESVIACION ESTANDARD CAPITAL GAIN')
print('|' * 50 )
print('La desviacion estandard de Capital gain es:')
standard_desviation_capital_gain = np.std(Z)
media = 0
print(standard_desviation_capital_gain)
print()

print('|' * 50)
print('VALORES DE RUIDO PARA CAPITAL GAIN')
print('|' * 50 )
p_capital_gain = np.random.normal(media,standard_desviation_capital_gain, df_census_capital_gain.shape)
print(p_capital_gain)

print('|' * 50)
print('VALORES DE CAPITAL GAIN + RUIDO')
print('|' * 50 )
print()
df_capital_gain = p_capital_gain + df_census_capital_gain
print(df_capital_gain)


#CAPITAL LOSS
print('|' * 50)
print('CAPITAL LOSS . INFO')
print('|' * 50 )
print()
df_census_capital_loss = df_census.drop(columns=['age','fnlwgt','capital-gain','hours-per-week'])
df_census_capital_loss.info()
a = df_census_capital_loss.to_numpy()

print('|' * 50 )
print('DESVIACION ESTANDARD CAPITAL LOSS')
print('|' * 50 )
standard_desviation_capital_loss = np.std(a)
media = 0
print('La desviacion estandard de Capital Loss es:')
print(standard_desviation_capital_loss)
print()


print('|' * 50)
print('VALORES DE RUIDO PARA CAPITAL LOSS')
print('|' * 50 )
p_capital_loss = np.random.normal(media,standard_desviation_capital_loss, df_census_capital_loss.shape)
print(p_capital_loss)

print('|' * 50)
print('VALORES DE CAPITAL LOSS + RUIDO')
print('|' * 50 )
print()
df_capital_loss = p_capital_loss + df_census_capital_loss
print(df_capital_loss)


#HOURS PER WEEK

print('|' * 50)
print('HOURS PER WEEK . INFO')
print('|' * 50 )
print()
df_census_hours_per_week = df_census.drop(columns=['age','fnlwgt','capital-gain','capital-loss'])
df_census_hours_per_week.info()
b = df_census_hours_per_week.to_numpy()

print('|' * 50 )
print('DESVIACION ESTANDARD HOURS PER WEEK')
print('|' * 50 )
print()
standard_desviation_hours_per_week = np.std(b)
media = 0
print('La desviacion estandard de Hours per Week es:')
print(standard_desviation_hours_per_week)
print()


print('|' * 50)
print('VALORES DE RUIDO PARA HOURS PER WEEK')
print('|' * 50 )
p_hours_per_week = np.random.normal(media,standard_desviation_hours_per_week, df_census_hours_per_week.shape)
print(p_hours_per_week)
p_hours_per_week_2 = np.random.normal(media,standard_desviation_hours_per_week, df_census_hours_per_week.shape)
print(p_hours_per_week_2)

print('|' * 50)
print('VALORES DE HOURS PER WEEK + RUIDO')
print('|' * 50 )
df_hours_per_week = p_hours_per_week + df_census_hours_per_week
print(df_hours_per_week)

print('|' * 50)
print('DF_CENSUS2 - VALORES MAS RUIDO')
print('|' * 50 )
df_census2 = pd.concat([df_age, df_fnlwgt,df_capital_gain, df_capital_loss, df_hours_per_week], axis=1)
print(df_census2)

print('|' * 50)
print('DF_CENSUS2 - VALORES MAS RUIDO EN ENTEROS')
print('|' * 50 )
print(df_census2.round(0))

#EJERCICIO 8

def mse(df_census: pd.DataFrame, df_census2: pd.DataFrame) -> float:
    return ((df_census - df_census2)**2).mean().mean()

print(mse(df_census, df_census2))

















#def additive_noise(df_census_column, p):
    #x = df_census_column.to_numpy()
    #new_variance = p * np.var(x)
    #media = 0
    #distribucion_normal =
    #print(addnoise)
    #return addnoise.round()





#df_census_fnlwgt = df_census.drop(columns=['age','capital-gain','capital-loss','hours-per-week'])
#df_census_capital_gain = df_census.drop(columns=['age','fnlwgt','capital-loss','hours-per-week'])
#df_census_capital_loss = df_census.drop(columns=['age','fnlwgt','capital-gain','hours-per-week'])
#df_census_hours_per_week = df_census.drop(columns=['age','fnlwgt','capital-gain','capital-loss','hours-per-week'])














#print('TO NUMPY')
#x = df_census.to_numpy()
#print(x)
#print(type(x))
#print(np.var(x))





#p = np.random.normal(1, 1, df_census.shape)

#def additive_noise(df_census, p):
    #addnoise = df_census + p
    #print(addnoise)
    #return addnoise.round()

#print(p)
#print(additive_noise(df_census,p))



#Ejercicio 8

#def mse(df_census: pd.DataFrame, df_census2: pd.DataFrame) -> float:
    #return ((df_census - df_census2)**2).mean().mean()
