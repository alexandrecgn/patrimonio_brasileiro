import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd
    return (gpd,)


@app.cell
def _(gpd):
    bens_pol = gpd.read_file("bens/bens_pol.geojson")
    return (bens_pol,)


@app.cell
def _(bens_pol):
    bens_pol.to_file(filename="bens/bens_pol.gpkg", driver="GPKG", layer="bens_pol", engine="fiona", crs="EPSG:4674")
    return


if __name__ == "__main__":
    app.run()
