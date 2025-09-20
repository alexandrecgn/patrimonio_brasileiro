import marimo

__generated_with = "0.15.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd

    return (gpd,)


@app.cell
def _(gpd):
    bens = gpd.read_file("bens.geojson")
    return (bens,)


@app.cell
def _(bens):
    bens.set_crs(crs="EPSG:4674", allow_override=True)
    return


@app.cell
def _(bens):
    bens.dissolve()
    return


@app.cell
def _(bens):
    len(bens)
    return


@app.cell
def _(bens):
    bens.to_file(
        filename="bens/bens.geojson", driver="GeoJSON", engine="fiona", crs="EPSG:4674"
    )
    return


if __name__ == "__main__":
    app.run()
