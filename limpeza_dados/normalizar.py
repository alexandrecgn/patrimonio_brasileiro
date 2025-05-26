import geopandas as gpd


# Adicionar e renomear colunas dos bens registrados

impt = gpd.read_file("/home/alexandrecgn/DevOps/buscador_do_patrimônio/bens/imaterial_pt.geojson")
impol = gpd.read_file("/home/alexandrecgn/DevOps/buscador_do_patrimônio/bens/imaterial_pol.geojson")

impt["ds_natureza"] = "Bem Registrado"

impt.rename(columns={"fid": "FID", "titulo": "identificacao_bem", "bcr": "ficha"}, inplace=True)
impol.rename(columns={"fid": "FID", "titulo": "identificacao_bem", "bcr": "ficha"}, inplace=True)


# Acrescentar coluna com a ficha dos bens tombados e valorados
    

tom = gpd.read_file("/home/alexandrecgn/DevOps/buscador_do_patrimônio/bens/tombados.geojson")
val = gpd.read_file("/home/alexandrecgn/DevOps/buscador_do_patrimônio/bens/valorados.geojson")


tom["ficha"] =  "https://sicg.iphan.gov.br/sicg/bem/visualizar/" + tom["id_bem"].astype(str)
val["ficha"] =  "https://sicg.iphan.gov.br/sicg/bem/visualizar/" + val["id_bem"].astype(str)

# Salvar os novos arquivos

impt.to_file("bens/imaterial_pt.geojson")
impol.to_file("bens/imaterial_pol.geojson")
tom.to_file("bens/tombados.geojson")
val.to_file("bens/valorados.geojson")