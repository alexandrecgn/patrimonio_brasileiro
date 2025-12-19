import geopandas as gpd
import pandas as pd

from utils import (
    adicionar_municipio,
    normalizar_imaterial_bcr,
    normalizar_imaterial_sicg,
    normalizar_material,
    separar_tombados,
)

print("\nCarregando bens culturais\n")

# Carregar GeoDataFrame dos bens culturais em pontos e polígonos.
tombados = separar_tombados(
    "limpeza_dados/2024-10-02-CONTROLE BENS TOMBADOS.xlsx",
    "BENS TOMBADOS E PROCESSO ABERTO",
)
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

print("\nNormalizando tabelas dos bens culturais\n")

# Normalizar os dados dos bens culturais no SICG.
tomb_norm = normalizar_material(tombados, "tombado", "ponto")
val_norm = normalizar_material(valorados, "valorado", "ponto")
sit_pt_norm = normalizar_material(sitios_pt, "arqueológico", "ponto")
sit_pol_norm = normalizar_material(sitios_pol, "arqueológico", "polígono")
ima_pt_sicg_norm = normalizar_imaterial_sicg(imaterial_pt_sicg, "imaterial", "ponto")
ima_pol_sicg_norm = normalizar_imaterial_sicg(
    imaterial_pol_sicg, "imaterial", "polígono"
)
# Normalizar os dados dos bens culturais no BCR.
ima_pt_bcr_norm = normalizar_imaterial_bcr(imaterial_pt_bcr, "imaterial", "ponto")
ima_pol_bcr_norm = normalizar_imaterial_bcr(imaterial_pol_bcr, "imaterial", "polígono")

print("\nConcatenando bens culturais por geometria\n")

# Concatenar GeoDataFrames de bens culturais por geometria.
bens_pt = pd.concat(
    [tomb_norm, val_norm, ima_pt_sicg_norm, ima_pt_bcr_norm, sit_pt_norm]
)
bens_pol = pd.concat([ima_pol_sicg_norm, ima_pol_bcr_norm, sit_pol_norm])

# Definir crs de cada GDF de bens.
bens_pt.set_crs("EPSG:4674", inplace=True)
bens_pol.set_crs("EPSG:4674", inplace=True)

print("\nIdentificando estado e munícipio de cada bem\n")

bens_muni_uf_pt = adicionar_municipio(bens_pt)
bens_muni_uf_pol = adicionar_municipio(bens_pol)

# Dissolver GDF dos bens na geometria ponto.
bens_x_pt = bens_muni_uf_pt.explode()

print(bens_x_pt, bens_muni_uf_pol)

# Salvar os bens em GeoJSON.
print("\nSalvando arquivos GeoJSON dos bens culturais\n")

bens_x_pt.to_file(
    filename="bens/bens_pt.gpkg",
    driver="GPKG",
    layer="bens_pt",
    engine="fiona",
    crs="EPSG:4674",
)

bens_muni_uf_pol.to_file(
    filename="bens/bens_pol.gpkg",
    driver="GPKG",
    layer="bens_pol",
    engine="fiona",
    crs="EPSG:4674",
)
