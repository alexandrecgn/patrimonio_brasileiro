import json

with open("/home/alexandrecgn/DevOps/buscador_do_patrimônio/limpeza_dados/municipios.geojson") as arquivo:
    municipios = json.load(arquivo)
    print("Arquivo de municípios carregado com sucesso!")
    lista_municipios = []
    for item in municipios["features"]:
        nome = item["properties"]["nm_mun"]
        uf = item["properties"]["sigla_uf"]
        cidade = dict(nm_mun=nome, sigla_uf=uf)
        lista_municipios.append(cidade)
    resultado = json.dumps(lista_municipios)
    open("municipios.json", mode="w").write(resultado)

print("Arquivo de municípios salvo com sucesso!")