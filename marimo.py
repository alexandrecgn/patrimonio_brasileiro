import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import folium
    import geopandas as gpd
    from utils import pesquisar
    return folium, pesquisar


@app.cell
def _(folium):
    mapa = folium.Map()
    return (mapa,)


@app.cell
def _():
    area = "test/empreendimento_5.gpkg"
    return (area,)


@app.cell
def _(area, pesquisar):
    resultado_pol, resultado_pt = pesquisar(area)
    return resultado_pol, resultado_pt


@app.cell
def _(folium, resultado_pol, resultado_pt):
    res_pol = folium.GeoJson(resultado_pol)
    res_pt = folium.GeoJson(resultado_pt)
    return res_pol, res_pt


@app.cell
def _(mapa, res_pol, res_pt):
    res_pol.add_to(mapa)
    res_pt.add_to(mapa)
    return


@app.cell
def _(mapa):
    mapa
    return


@app.cell
def _(resultado_pol):
    resultado_pol.explore()
    return


@app.cell
def _(resultado_pt):
    resultado_pt.explore()
    return


if __name__ == "__main__":
    app.run()
