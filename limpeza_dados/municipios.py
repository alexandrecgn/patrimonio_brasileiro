import json

with open("geo/municipios.geojson") as arquivo:
    municipios = json.load(arquivo)
    print("Arquivo de municípios carregado com sucesso!")
    i = 0
    for item in municipios["features"]:
        with open(f"municipios/{item["properties"]["nm_mun"]}.geojson", "a") as cidade:
            json.dump(item, cidade, indent=4)
        print(f"Município {i} salvo com sucesso!")
        i += 1