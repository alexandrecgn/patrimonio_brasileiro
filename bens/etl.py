import geopandas as gpd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///./bens.db", echo=True)

bens = gpd.GeoDataFrame(
    columns=[
        "nome",
        "descricao",
        "ficha",
        "tipo",
        "classificacao",
        "data_protecao",
        "processo_iphan",
        "geometry",
    ],
    geometry="geometry",
    crs="EPSG:4674",
)

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


for index, row in tombados.iterrows():
    bem = {}
    bem["nome"] = row["identificacao_bem"]
    bem["descricao"] = row["sintese_bem"]
    bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{
        row['id_bem']}"
    bem["tipo"] = "tombado"
    bem["classificacao"] = row["ds_classificacao"]
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in valorados.iterrows():
    bem = {}
    bem["nome"] = row["identificacao_bem"]
    bem["descricao"] = row["sintese_bem"]
    bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{
        row['id_bem']}"
    bem["tipo"] = "valorado"
    bem["classificacao"] = row["ds_classificacao"]
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in imaterial_pt_sicg.iterrows():
    bem = {}
    bem["nome"] = row["no_bem_imaterial"]
    bem["descricao"] = row["ds_bem_imaterial"]
    bem["ficha"] = (
        f"https://sicg.iphan.gov.br/sicg/bemImaterial/acao/{
            row['id_bem_imaterial']}"
    )

    bem["tipo"] = "imaterial"
    bem["classificacao"] = None
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in imaterial_pol_sicg.iterrows():
    bem = {}
    bem["nome"] = row["no_bem_imaterial"]
    bem["descricao"] = row["ds_bem_imaterial"]
    bem["ficha"] = (
        f"https://sicg.iphan.gov.br/sicg/bemImaterial/acao/{
            row['id_bem_imaterial']}"
    )
    bem["tipo"] = "imaterial"
    bem["classificacao"] = None
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in imaterial_pt_bcr.iterrows():
    bem = {}
    bem["nome"] = row["identificacao_bem"]
    bem["descricao"] = None
    bem["ficha"] = row["ficha"]
    bem["tipo"] = "imaterial"
    bem["classificacao"] = None
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in imaterial_pol_bcr.iterrows():
    bem = {}
    bem["nome"] = row["identificacao_bem"]
    bem["descricao"] = None
    bem["ficha"] = row["ficha"]
    bem["tipo"] = "imaterial"
    bem["classificacao"] = None
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in sitios_pt.iterrows():
    bem = {}
    bem["nome"] = row["identificacao_bem"]
    bem["descricao"] = row["sintese_bem"]
    bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{
        row['id_bem']}"
    bem["tipo"] = "arqueologico"
    bem["classificacao"] = row["ds_classificacao"]
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

for index, row in sitios_pol.iterrows():
    bem = {}
    bem["nome"] = row["identificacao_bem"]
    bem["descricao"] = row["sintese_bem"]
    bem["ficha"] = f"https://sicg.iphan.gov.br/sicg/bem/visualizar/{
        row['id_bem']}"
    bem["tipo"] = "arqueologico"
    bem["classificacao"] = row["ds_classificacao"]
    bem["data_protecao"] = None
    bem["processo_iphan"] = None
    bem["municipio"] = None
    bem["uf"] = None
    bem["geometry"] = row["geometry"]
    bens.loc[len(bens)] = bem

print(bens)

bens.set_crs("EPSG:4674")

municipios = gpd.read_file("limpeza_dados/municipios.geojson")
municipios.set_crs("EPSG:4674")

bens_muni_uf = bens.sjoin(df=municipios, how="inner", predicate="intersects")
bens_muni_uf.set_crs("EPSG:4674")
bens_muni_uf.rename(columns={"nm_mun": "municipio",
                    "sigla_uf": "uf"}, inplace=True)

bens_muni_uf.drop(
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


bens_str = bens_muni_uf.map(str)
bens_sql = bens_str.to_sql(name="bens.db", con=engine)
