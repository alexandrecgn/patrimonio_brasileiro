import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(r"""### Converter JSON do imaterial para GeoJson dividido por tipologia""")
    return


@app.cell
def _():
    import geopandas as gpd
    import pandas as pd
    from shapely import wkt
    return gpd, pd, wkt


@app.cell
def _(pd):
    df = pd.read_json("limpeza_dados/imaterial_registrado_sicg.json")
    imat = df.drop(columns=["ativo", "usuario_cadastro"])
    return (imat,)


@app.cell
def _(imat):
    imat_pt = imat.drop(columns="geometria_poligono")
    imat_pol = imat.drop(columns="geometria_ponto")
    return imat_pol, imat_pt


@app.cell
def _(gpd, imat_pol, imat_pt):
    imat_pt_gdf = gpd.GeoDataFrame(imat_pt)
    imat_pol_gdf = gpd.GeoDataFrame(imat_pol)
    return imat_pol_gdf, imat_pt_gdf


@app.cell
def _(imat_pol_gdf, imat_pt_gdf, wkt):
    imat_pt_gdf["geometria_ponto"] = imat_pt_gdf["geometria_ponto"].apply(wkt.loads)
    imat_pol_gdf["geometria_poligono"] = imat_pol_gdf["geometria_poligono"].apply(wkt.loads)
    return


@app.cell
def _(imat_pol_gdf, imat_pt_gdf):
    imat_pt_gdf.set_geometry(col="geometria_ponto", inplace=True, crs="EPSG:4674")
    imat_pol_gdf.set_geometry(col="geometria_poligono", inplace=True, crs="EPSG:4674")
    return


@app.cell
def _(imat_pol_gdf, imat_pt_gdf):
    imat_pt_gdf.set_crs("EPSG:4674", inplace=True)
    imat_pol_gdf.set_crs("EPSG:4674", inplace=True)
    return


@app.cell
def _(imat_pol_gdf, imat_pt_gdf):
    imat_pt_gdf.to_file(filename="bens/imaterial_pontos_sicg.geojson")
    imat_pol_gdf.to_file(filename="bens/imaterial_poligonos_sicg.geojson")
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
