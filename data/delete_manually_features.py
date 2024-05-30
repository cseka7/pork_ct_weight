import pandas as pd
import glob
import os

mdir = "manually_labels"

# find ids of manually_labels
ids = [i for i in os.listdir(mdir) if i.endswith(".nii.gz")]

ids = [i.split(".")[0].split("-")[0] for i in ids]

ids = list(set(ids))

print(ids)
parts = ["belly", "body", "groin", "shoulder", "leg", "loin"]
csvs = [i for i in glob.glob("*.csv") if any(part in i for part in parts)]

for csv in csvs:
    df = pd.read_csv(csv)
    for i in ids:
        df = df[df["filename"].str.contains(i) == False]
    df.to_csv(csv, index= False)
