import pandas as pd

liste_entreprises = ["NVDA", "INTC", "AMD"]

def transfo_df(liste_entreprises):
    for entreprise in liste_entreprises:
        df = pd.read_csv(f"{entreprise}/{entreprise}.csv")
        df = df.sort_values('Date')
        df = df[::-1].reset_index()
        df = df.reset_index(drop=True)
        print("df ok")
    return df

transfo_df(liste_entreprises)

