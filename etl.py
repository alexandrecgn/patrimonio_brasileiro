import geopandas as gpd
import pandas as pd
from utils import (
    normalizar_material,
    normalizar_imaterial_sicg,
    normalizar_imaterial_bcr,
)

print("Carregando bens culturais")

# Carregar GeoDataFrame dos bens culturais em pontos e polígonos.
tombados = gpd.read_file("bens/tombados.geojson")
valorados = gpd.read_file("bens/valorados.geojson")
imaterial_pt_bcr = gpd.read_file("bens/imaterial_pt.geojson")
imaterial_pt_sicg = gpd.read_file("bens/imaterial_pontos_sicg.geojson")
imaterial_pol_bcr = gpd.read_file("bens/imaterial_pol.geojson")
imaterial_pol_sicg = gpd.read_file("bens/imaterial_poligonos_sicg.geojson")
sitios_pt = gpd.read_file(
    "http://portal.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios&maxFeatures=2147483647&outputFormat=application%2Fjson"
)
sitios_pol = gpd.read_file(
    "https://geoserver.iphan.gov.br/geoserver/SICG/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=SICG%3Asitios_pol&maxFeatures=2147483647&outputFormat=application%2Fjson"
)

print("Normalizando tabelas dos bens culturais")

# Normalizar os dados dos bens culturais no SICG.
tomb_norm = normalizar_material(tombados, "tombado", "ponto")
val_norm = normalizar_material(valorados, "valorado", "ponto")
sit_pt_norm = normalizar_material(sitios_pt, "arqueológico", "ponto")
sit_pol_norm = normalizar_material(sitios_pol, "arqueológico", "polígono")
ima_pt_sicg_norm = normalizar_imaterial_sicg(
    imaterial_pt_sicg, "imaterial", "ponto")
ima_pol_sicg_norm = normalizar_imaterial_sicg(
    imaterial_pol_sicg, "imaterial", "polígono"
)
# Normalizar os dados dos bens culturais no BCR.
ima_pt_bcr_norm = normalizar_imaterial_bcr(
    imaterial_pt_bcr, "imaterial", "ponto")
ima_pol_bcr_norm = normalizar_imaterial_bcr(
    imaterial_pol_bcr, "imaterial", "polígono")

print("Concatenando bens culturais por geometria")

# Concatenar GeoDataFrames de bens culturais por geometria.
bens_pt = pd.concat(
    [tomb_norm, val_norm, ima_pt_sicg_norm, ima_pt_bcr_norm, sit_pt_norm]
)
bens_pol = pd.concat([ima_pol_sicg_norm, ima_pol_bcr_norm, sit_pol_norm])

# Definir crs de cada GDF de bens.
bens_pt.set_crs("EPSG:4674", inplace=True)
bens_pol.set_crs("EPSG:4674", inplace=True)

print("Identificando estado e munícipio de cada bem")

# Carregar GDF dos municípios brasileiros (fonte: IBGE).
municipios = gpd.read_file("limpeza_dados/municipios.geojson")
# Definir crs do GDF de municípios.
municipios.set_crs("EPSG:4674", inplace=True)

# Inserir dados de Estado e município nos GDF dos bens na geometria ponto.
bens_muni_uf_pt = bens_pt.sjoin(
    df=municipios, how="inner", predicate="intersects")
# Definir crs do novo GDF.
bens_muni_uf_pt.set_crs("EPSG:4674", inplace=True)
# Renomear colunas de Estado e município.
bens_muni_uf_pt.rename(
    columns={
        "nm_mun": "municipio",
        "sigla_uf": "uf",
    },
    inplace=True,
)

# Excluir colunas desnecessárias vindas do GDF de municípios.
bens_muni_uf_pt.drop(
    columns=[
        "cd_recorte",
        "quadro",
        "cd_uf",
        "cd_mun",
        "area_km2",
        "index_right",
    ],
    inplace=True,
)


# Inserir dados de Estado e município nos GDF dos bens na geometria polígono.
bens_muni_uf_pol = bens_pol.sjoin(
    df=municipios, how="inner", predicate="intersects")
# Definir crs do novo GDF.
bens_muni_uf_pol.set_crs("EPSG:4674", inplace=True)
# Renomear colunas de Estado e município.
bens_muni_uf_pol.rename(
    columns={
        "nm_mun": "municipio",
        "sigla_uf": "uf",
    },
    inplace=True,
)

# Excluir colunas desnecessárias vindas do GDF de municípios.
bens_muni_uf_pol.drop(
    columns=[
        "cd_recorte",
        "quadro",
        "cd_uf",
        "cd_mun",
        "area_km2",
        "index_right",
    ],
    inplace=True,
)


# Dissolver GDF dos bens na geometria ponto.
bens_x_pt = bens_muni_uf_pt.explode()

print(bens_x_pt, bens_muni_uf_pol)


# Salvar os bens em GeoJSON.
print("Salvando arquivos GeoJSON dos bens culturais")
bens_x_pt.to_file(
    filename="bens/bens_pt.gpkg",
    driver="GPKG",
    layer="bens_pt",
    engine="fiona",
    crs="EPSG:4674",
)

bens_pol.to_file(
    filename="bens/bens_pol.gpkg",
    driver="GPKG",
    layer="bens_pol",
    engine="fiona",
    crs="EPSG:4674",
)
