import pandas as pd

def generate_df(entreprise):
    df = pd.read_csv(f"/home/cedric/Microsoft Lovelace/emmanuel/trading/{entreprise.upper()}/{entreprise.upper()}.csv")
    df = df.sort_values('Date')
    #df = df[::-1].reset_index()
    df = df.reset_index(drop=True)
    return df