
import ast
import pandas as pd
import numpy as np
import math

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

def additive_noise_to_column(dataframe_column, media, p):

    dataframe_column.info()
    dataframe_array = dataframe_column.to_numpy()
    standard_deviation = np.std(dataframe_array)
    variance = pow(float(standard_deviation), 2)
    new_variance = p * variance
    new_standard_deviation = math.sqrt(new_variance)
    noise = np.random.normal(media, new_standard_deviation, dataframe_column.shape)
    dataframe_with_noise = noise + dataframe_column
    return dataframe_with_noise


def additive_noise(dataframe,p):
    media = 0
    # age
    df_census_age = dataframe.drop(columns=['fnlwgt','capital-gain','capital-loss','hours-per-week'])
    df_census_age_with_noise = additive_noise_to_column(df_census_age, media,p)

    # fnlwgt
    df_census_fnlwgt = dataframe.drop(columns=['age','capital-gain','capital-loss','hours-per-week'])
    df_census_fnlwgt_with_noise = additive_noise_to_column(df_census_fnlwgt, media,p)

    # Capital-gain
    df_census_capital_gain = dataframe.drop(columns=['age','fnlwgt','capital-loss','hours-per-week'])
    df_census_capital_gain_with_noise = additive_noise_to_column(df_census_capital_gain, media,p)

    # Capital - Loss
    df_census_capital_loss = dataframe.drop(columns=['age','fnlwgt','capital-gain','hours-per-week'])
    df_census_capital_loss_with_noise = additive_noise_to_column(df_census_capital_loss, media,p)


    # hours-per-week
    df_census_hours_per_week = dataframe.drop(columns=['age', 'fnlwgt','capital-gain','capital-loss'])
    df_census_hours_per_week_with_noise = additive_noise_to_column(df_census_hours_per_week, media,p)

    dataframe_with_noise = pd.concat([df_census_age_with_noise, df_census_fnlwgt_with_noise,
                                      df_census_capital_gain_with_noise, df_census_capital_loss_with_noise,
                                      df_census_hours_per_week_with_noise], axis=1)

    dataframe_with_noise = dataframe_with_noise.round(0)


    return dataframe_with_noise

p = 0.5
df_census_with_noise = additive_noise(df_census, p)
print(df_census_with_noise)


b
#EJERCICIO 8

def mse(original_dataframe: pd.DataFrame, dataframe_with_noise: pd.DataFrame) -> float:
    return ((original_dataframe - dataframe_with_noise)**2).mean().mean()



mse_result = mse(df_census, df_census_with_noise)
mse_result_round = round(mse_result,1)
print(mse_result_round)




















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
