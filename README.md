
# Buscador do Patrimônio

O Buscador do Patrimônio é um programa escrito em Python para buscar Bens Culturais acautelados em nível federal na área de um polígono definido pelo usuário.

Os Bens Culturais acautelados em nível federal são aqueles sob a gestão do Iphan - Instituto do Patrimônio Histórico e Artístico Nacional, protegidos pelo Decreto-Lei nº 25/1937; Lei nº 3.924/1961; Decreto nº 3.551/2000; e Lei nº 11.483/2007.

O programa ainda está em desenvolvimento. No momento a busca retorna os bens culturais em arquivos separados pelo tipo de bem acautelado, no formato CSV, contendo o nome de cada bem e o link para sua ficha no SICG - Sistema Integrado de Conhecimento e Gestão ou no BCR - Banco de Bens Culturais Registrados.

## Pesquisar direto do navegador

Para pesquisar a existência de Bens Culturais em uma determinada área:
1. [Clique aqui](https://buscadorpatrimonio.streamlit.app/) ou acesse https://buscadorpatrimonio.streamlit.app/;
2. Insira a poligonal de pesquisa; e
3. Clique em "Pesquisar".

Ao fim da pesquisa serão exibidas as tabelas de cada tipologia de Bem Cultural existentes na área. 



## Pesquisar pela linha de comando do seu computador

>**Pré-requisito:** Python e as bibliotecas *geopandas*, *sys* e *requests* instalados no computador utilizado para rodar o programa.

1. Baixe os arquivos deste repositório;
2. Cole o arquivo geoespacial com a área de pesquisa na mesma pasta onde está o arquivo baixado com o nome 'main.py';
3. Abra o terminal no diretório (pasta) onde ambos os arquivos estão;
4. Digite no terminal:

- (**Windows**) py main.py "nome do arquivo da pesquisa".
    Exemplos:

    `py main.py empreendimento.shp`
    
    `py main.py parque_nacional.gpkg`

    `py main.py municipio.geojson`

- (**Linux**) python3 main.py "nome do arquivo da pesquisa".
    Exemplos:

    `python3 main.py empreendimento.shp`

    `python3 main.py parque_nacional.gpkg`

    `python3 main.py municipio.geojson`
    
5. Na pasta onde está colado *main.py* irão aparecer quatro outros arquivos: *Patrimônio Arqueológico.csv*; *Patrimônio Imaterial.csv*; *Patrimônio Tombado.csv*; e *Patrimônio Valorado.csv*. Neles você verá uma lista dos bens encontrados na área de pesquisa. Em cada linha constará o nome do bem, seguido de sua ficha de cadastro.

Exemplo:

>,Nome do bem,Ficha do bem<br>
>0,Edifício da Bolsa de Valores de Pernambuco e Paraíba, https://sicg.iphan.gov.br/sicg/bem/visualizar/48980<br>
>1,Sítio Empresarial Armazem do Porto, https://sicg.iphan.gov.br/sicg/bem/visualizar/22648<br>
>2,Pátio Ferroviário das Cinco Pontas, https://sicg.iphan.gov.br/sicg/bem/visualizar/27299<br>


## Desenvolvimento

* [x] ~~Criar busca de Sítios Arqueológicos Cadastrados com retorno em CSV~~;
* [x] ~~Adicionar retorno de Bens Culturais Registrados (Imaterial)~~;
* [x] ~~Adicionar retorno de Bens Culturais Tombados~~;
* [x] ~~Adicionar retorno de Bens Culturais Valorados (Ferroviário)~~;
* [x] ~~Disponibilizar o programa em uma interface web com as listas de bens sendo exibidas na página~~;
* [x] ~~Adicionar exibição dos resultados em mapa renderizado na página~~;
* [x] ~~Adicionar redenrização do polígono de busca no mapa~~;
* [x] ~~Adicionar controle de camadas~~;
* [x] ~~Adicionar basemap de imagem de satélite ao mapa~~;
* [x] ~~Adicionar escala ao mapa~~;
* [x] ~~Tornar os itens mapa clicáveis para exibir um pop-up com as informações do bem~~;
* [ ] Refatorar main.py;
* [ ] Possibilitar a seleção das tipologias de bens a serem pesquisados;
* [ ] Adicionar busca de todos os bens a partir da seleção da Unidade Federativa e município.

