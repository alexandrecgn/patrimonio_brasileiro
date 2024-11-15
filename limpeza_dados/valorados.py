import csv

sicg = []

with open("lista_ferroviario.csv", "r") as codigos:
    reader = csv.DictReader(codigos)
    for item in reader:
        sicg.append(item["COD-IPHAN"])


with open("tg_bem_classificacao.csv", "r") as geoserver, open("valorados.csv", "a") as valorados:
    reader = csv.DictReader(geoserver)
    writer = csv.DictWriter(valorados, fieldnames=["FID","ponto","id_bem","identificacao_bem","co_iphan","no_logradouro","nu_logradouro","id_natureza","ds_natureza","codigo_iphan","id_classificacao","ds_classificacao","id_tipo_bem","ds_tipo_bem","sg_tipo_bem","sintese_bem","dt_cadastro"])
    writer.writeheader()
    for bem in reader:
        if bem["co_iphan"] in sicg:
            writer.writerow(bem)