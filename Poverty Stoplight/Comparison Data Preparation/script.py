import pandas as pd
import json

newComp = pd.read_excel("MPI_PSL_comparison4.8.25.xlsx")
desc = pd.read_excel("family_similarity_results.xlsx", sheet_name="Family Descriptions")
indic = pd.read_excel("Unbound - Rwanda.xlsx", sheet_name="Indicators")

jason = {}

num2word = {
    1: "Poor",
    2: "Normal",
    3: "Good"
}

for index, row in newComp.iterrows():
    MPInum = row["MPI_family_id"]
    simFamID = row["PSL_family_id"]
    simscore = row["Similarity_score"]
    PSLrow = indic.loc[indic["Family code"] == simFamID]
    description = desc.loc[desc["family_id"] == simFamID]
    if PSLrow.empty:
        print(f"Family code {simFamID} not found in the indicators sheet.")
        break
    education = num2word[PSLrow["Schooling"].values[0]]
    electricity = num2word[PSLrow["Power connection"].values[0]]
    sanitation = num2word[round((PSLrow["Garbage"].values[0] + PSLrow["Unpolluted environment"].values[0]) / 2)]
    water = num2word[PSLrow["Water"].values[0]]
    housing = num2word[round((PSLrow["Safe home"].values[0] + PSLrow["Latrine/Toilet"].values[0] + PSLrow["Household appliances"].values[0] + PSLrow["Separate bedrooms"].values[0] + PSLrow["Ventilated kitchen"].values[0]) / 5)]
    assets = num2word[PSLrow["Security"].values[0]]

    
    jason[MPInum] = {
        "sim_family_id": simFamID,
        "similarity_score": simscore,
        "education": education,
        "electricity": electricity,
        "sanitation": sanitation,
        "water": water,
        "housing": housing,
        "assets": assets,
        "description": description["description"].values[0]
    }

with open("newList.json", "w") as f:
    json.dump(jason, f, indent=4)

    