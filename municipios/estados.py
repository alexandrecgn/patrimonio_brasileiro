import json
import pandas as pd

municipios = pd.read_json("municipios/municipios.json")

ac = []
al = []
am = []
ap = []
ba = []
ce = []
df = []
es = []
go = []
ma = []
mg = []
ms = []
mt = []
pa = []
pb = []
pe = []
pi = []
pr = []
rj = []
rn = []
ro = []
rr = []
rs = []
sc = []
se = []
sp = []
to = []

for index, row in municipios.iterrows():
    match row["sigla_uf"]:
        case "AC":
            ac.append(row["nm_mun"])
        case "AL":
            al.append(row["nm_mun"])
        case "AM":
            am.append(row["nm_mun"])
        case "AP":
            ap.append(row["nm_mun"])
        case "BA":
            ba.append(row["nm_mun"])
        case "CE":
            ce.append(row["nm_mun"])
        case "DF":
            df.append(row["nm_mun"])
        case "ES":
            es.append(row["nm_mun"])
        case "GO":
            go.append(row["nm_mun"])
        case "MA":
            ma.append(row["nm_mun"])
        case "MG":
            mg.append(row["nm_mun"])
        case "MS":
            ms.append(row["nm_mun"])
        case "MT":
            mt.append(row["nm_mun"])
        case "PA":
            pa.append(row["nm_mun"])
        case "PB":
            pb.append(row["nm_mun"])
        case "PE":
            pe.append(row["nm_mun"])
        case "PI":
            pi.append(row["nm_mun"])
        case "PR":
            pr.append(row["nm_mun"])
        case "RJ":
            rj.append(row["nm_mun"])
        case "RN":
            rn.append(row["nm_mun"])
        case "RO":
            ro.append(row["nm_mun"])
        case "RR":
            rr.append(row["nm_mun"])
        case "RS":
            rs.append(row["nm_mun"])
        case "SC":
            sc.append(row["nm_mun"])
        case "SE":
            se.append(row["nm_mun"])
        case "SP":
            sp.append(row["nm_mun"])
        case "TO":
            to.append(row["nm_mun"])

estados = {
"AC": ac,
"AL": al,
"AM": am,
"AP": ap,
"BA": ba,
"CE": ce,
"DF": df,
"ES": es,
"GO": go,
"MA": ma,
"MG": mg,
"MS": ms,
"MT": mt,
"PA": pa,
"PB": pb,
"PE": pe,
"PI": pi,
"PR": pr,
"RJ": rj,
"RN": rn,
"RO": ro,
"RR": rr,
"RS": rs,
"SC": sc,
"SE": se,
"SP": sp,
"TO": to,
}

with open("municipios/est_muni.json", mode="w", encoding="utf8") as file:
    json.dump(obj=estados, fp=file, indent=4, ensure_ascii=False)
