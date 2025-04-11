import json

with open('RW_MPI.jsonl', 'r') as file:
    # Read each non-empty line and parse it as JSON, storing all records in a list
    jsons = [json.loads(line) for line in file if line.strip()]

bigGuy = {}

for jason in jsons:

    newJson = {}
    strings = jason["input"].split(".")
            
    number = strings[0].split(" ")[4]

    veryOld = not len(strings) == 16

    oldNum = int(veryOld)

    
    if  (not strings[5].split(" ")[3] == "lacks") and strings[6].split(" ")[1] == "All":
        education = "Good"
    elif (not strings[5].split(" ")[3] == "lacks") ^ (strings[6].split(" ")[1] == "All"):
        education = "Normal"
    else:
        education = "Poor"
    if strings[9 - oldNum].split(" ")[3] == "has":
        electricity = "Normal"
    else: 
        electricity = "Poor"
    
    if strings[10 - oldNum].split(" ")[5] == "not":
        sanitation = "Poor"
    else:
        sanitation = "Normal"
    
    if strings[11 - oldNum].split(" ")[3] == "lacks":
        water = "Poor"
    else:
        water = "Normal"

    # if strings[12 - oldNum].split(" ")[1] == "At":
    #     housing = "Poor"
    # else:
    #     housing = "Normal"

    if  (not strings[12 - oldNum].split(" ")[1] == "At") and (not strings[13 - oldNum].split(" ")[4] == "deprived"):
        housing = "Good"
    elif (not strings[12 - oldNum].split(" ")[1] == "At") ^ (not strings[13 - oldNum].split(" ")[4] == "deprived"):
        housing = "Normal"
    else:
        housing = "Poor"
    
    if strings[14 - oldNum].split(" ")[4] == "one":
        assets = "Poor"
    else:
        assets = "Normal"

    if jason["output"] == "poor":
        label = "Poor"
    elif jason["output"] == "normal":
        label = "Normal"
    elif jason["output"] == "extremely poor":
        label = "Extemely Poor"
    else:
        label = "Vulnerable"
    
    bigGuy[number] = {
        "education": education,
        "electricity": electricity,
        "sanitation": sanitation,
        "water": water,
        "housing": housing,
        "assets": assets,
        "description": jason["input"],
        "label": label
    }
    

with open("temp.json", "w") as f:
    json.dump(bigGuy, f, indent=4)
