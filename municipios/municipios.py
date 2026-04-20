import pandas as pd
import geopandas as gpd


muni_gpd = gpd.read_file("municipios/pbqg22_04_Municipios_cd_mun.geojson")

municipios = pd.DataFrame(muni_gpd)
municipios.drop(columns=["id", "cd_recorte", "quadro", "cd_uf", "cd_mun", "geometry"], inplace=True)

municipios.to_json("municipios/municipios.json")