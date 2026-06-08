# rest
import requests
import json



def simple_rest_demo():
    """
    See https://realpython.com/python-download-file-from-url/
    """
    # r = requests.get("https://pubmed.ncbi.nlm.nih.gov/27333362/")
    #
    # print(r.status_code)
    # print(r.text)

    pmids = ["40638047", "40598827"]
    params = {
        "db": "pubmed",
        "id": ",".join(pmids),
        "retmode": "json"
    }
    response = requests.get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi",
                            params=params)
    data = response.json()
    print(data)


def simple_subprocess_demo():
    import subprocess

    # on Linux
    reslt = subprocess.run(["ls", "-l", "-s"])
    print(reslt.stdout)
    # on Win
    # subprocess.run(["dir"], shell=True)

    result = subprocess.run(["python", "--version"], capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)
    print(result.returncode)

    # output to a file
    with open("output.txt", "w") as f:
        subprocess.run(["python", "--version"],stdout=f, text=True, check=True)

def simple_pandas_demo():
    import pandas as pd

    COLUMN_NAMES = ["sequence ID", "tax ID", "species name", "PFam domain", "Pfam evalue",
                    "# CYPs", "# CYPs long", "CYP ID 1", "sequence identity 1",
                    "e-value 1", "alignment length 1", "db length 1", "CYP ID 2", "sequence identity 2", "e-value 2",
                    "alignment length 2", "db length 2", "sequence description", "the query sequence"]

    fname = "/Users/dgront/work.runs/P450/TheBisSearch_baskets/RESULTS/results_v3/Archa.Methan.Methan.Methan.tsv"

    df = pd.read_csv(fname, sep="\t")
    df.columns = COLUMN_NAMES
    # df = pd.read_excel("data.xlsx", sheet_name="Sheet1")

    print(df.head())
    print(df.tail())
    print(df.shape)
    print(df.columns)
    print(df.dtypes)
    print(df.info())
    print(df.describe())

    col_sp_name =  df["species name"]
    print(col_sp_name)
    sp_seq = df[["species name", "sequence ID"]]
    print(sp_seq)
    #
    w1 = df.iloc[0]  # first row by position
    df.iloc[0:5]  # first five rows
    # df.loc[0]  # row by label/index
    df.loc[:, "sequence ID"]  # all rows, selected column
    #
    good_enough = df[df["sequence identity 1"] > 50]
    #
    df_part = df[(df["sequence identity 1"] > 30) & ("Methanolobus" in df["species name"])]

if __name__ == "__main__":
    # simple_rest_demo()
    # simple_subprocess_demo()
    simple_pandas_demo()
    # jakis_dzejson_z_internetu = '{"klucz": "wartosc", "kl2": [2, 3]}'
    # d = eval(jakis_dzejson_z_internetu)
    # print(d["klucz"])