"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import datetime as dt
import pandas as pd
import re


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col=0)
    dftmp = df.copy()
    dftmp.dropna(inplace=True)

    # Campo Sexo
    dftmp.sexo = dftmp.sexo.apply(lambda c: c.lower())
    dftmp.sexo = dftmp.sexo.astype('category')

    # Campo Tipo de emprendimiento
    dftmp.tipo_de_emprendimiento = dftmp.tipo_de_emprendimiento.astype('category')
    dftmp.tipo_de_emprendimiento = dftmp.tipo_de_emprendimiento.apply(lambda c: c.lower())
    dftmp.tipo_de_emprendimiento = dftmp.tipo_de_emprendimiento.astype('category')

    # Limpieza de Idea de negocio
    dftmp.idea_negocio = dftmp.idea_negocio.apply(lambda idea: str.lower(idea.replace("_", " ").replace("-", " ")))

    # Limpieza de Barrio
    dftmp.barrio = dftmp.barrio.apply(lambda barrio: str.lower(barrio).replace("_", " ").replace("-", " "))

    # Limpieza de Comuna
    dftmp.comuna_ciudadano = dftmp.comuna_ciudadano.astype(int)

    # Tipado de estado
    dftmp.estrato = dftmp.estrato.astype(int)

    # Limpieza de Linea de Credito
    dftmp["línea_credito"] = dftmp["línea_credito"].apply(lambda linea: str.lower(linea.strip().replace("-", " ").replace("_", " ").replace(". ", ".")))

    fecha_de_beneficio_tmp = []
    for date in dftmp.fecha_de_beneficio:
        if bool(re.search(r"\d{1,2}/\d{2}/\d{4}", date)):
           fecha_de_beneficio_tmp.append(dt.datetime.strptime(date, "%d/%m/%Y"))
        else:
           fecha_de_beneficio_tmp.append(dt.datetime.strptime(date, "%Y/%m/%d"))

    dftmp.fecha_de_beneficio = fecha_de_beneficio_tmp

    dftmp.monto_del_credito = dftmp.monto_del_credito.apply(lambda monto: int(monto.replace("$ ", "").replace(".00", "").replace(",", "")))
    
    dftmp.drop_duplicates(inplace=True)


    return dftmp
