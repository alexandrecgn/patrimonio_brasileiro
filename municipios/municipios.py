import pandas as pd
import geopandas as gpd


muni_gpd = gpd.read_file("municipios/pbqg22_04_Municipios_cd_mun.geojson")
# geojson de municípios disponível em https://geoservicos.ibge.gov.br/geoserverIBGE/CGMAT/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=CGMAT%3Apbqg22_04_Municipios_cd_mun&outputFormat=application%2Fjson&maxFeatures=600000

municipios = pd.DataFrame(muni_gpd)
municipios.drop(columns=["id", "cd_recorte", "quadro", "cd_uf", "cd_mun", "geometry"], inplace=True)

municipios.to_json("municipios/municipios.json")