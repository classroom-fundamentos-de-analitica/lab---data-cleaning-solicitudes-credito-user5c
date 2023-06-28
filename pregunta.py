"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")
    dftmp = df.copy()

    # Campo Sexo
    dftmp.sexo = dftmp.sexo.apply(lambda c: c.lower())
    dftmp.sexo = dftmp.sexo.astype('category')

    # Campo Tipo de emprendimiento
    dftmp.tipo_de_emprendimiento = dftmp.tipo_de_emprendimiento.astype('category')
    dftmp.tipo_de_emprendimiento = dftmp.tipo_de_emprendimiento.apply(lambda c: c.lower())
    dftmp.tipo_de_emprendimiento = dftmp.tipo_de_emprendimiento.astype('category')


    return dftmp
