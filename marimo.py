import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import geopandas as gpd
    return (gpd,)


@app.cell
def _(gpd):
    bens_pol = gpd.read_file("/home/alexandrecgn/Developer/patrimonio_brasileiro/test/empreendimento_6.gpkg")
    return (bens_pol,)


@app.cell
def _(bens_pol):
    bens_pol.explore()
    return


if __name__ == "__main__":
    app.run()
