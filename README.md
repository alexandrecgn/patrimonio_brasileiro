
# Buscador do Patrimônio

O Buscador do Patrimônio é um programa escrito em Python para buscar Bens Culturais acautelados em nível federal na área de um polígono definido pelo usuário.

Os Bens Culturais acautelados em nível federal são aqueles sob a gestão do Iphan - Instituto do Patrimônio Histórico e Artístico Nacional, protegidos pelo Decreto-Lei nº 25/1937; Lei nº 3.924/1961; Decreto nº 3.551/2000; e Lei nº 11.482/2007.

O programa ainda está em desenvolvimento. No momento a busca retorna apenas os sítios arqueológicos cadastrados em um arquivo do formato CSV, contendo o nome do sítio e o link para sua ficha no SICG - Sistema Integrado de Conhecimento e Gestão.

Ao longo do tempo serão adicionadas as respostas referentes aos demais bens culturais.


## Como utilizar

>**Pré-requisito:** Python e as bibliotecas *geopandas*, *sys* e *requests* instalados no computador utilizado para rodar o programa.

1. Baixe o arquivo *busca.py*;
2. Cole 'busca.py' na mesma pasta onde está o arquivo geoespacial com a área de pesquisa;
3. Abra o terminal no diretório (pasta) onde ambos os arquivos estão;
4. Digite no terminal:

- (**Windows**) py busca.py "nome do arquivo da pesquisa".
    Exemplos:

    `py busca.py empreendimento.shp`
    
    `py busca.py parque_nacional.gpkg`

    `py busca.py municipio.geojson`

- (**Linux**) python3 busca.py "nome do arquivo da pesquisa".
    Exemplos:

    `python3 busca.py empreendimento.shp`

    `python3 busca.py parque_nacional.gpkg`

    `python3 busca.py municipio.geojson`
    
5. Na pasta onde está colado *busca.py* irá aparecer um outro arquivo, nomeado *"sitios_csv.csv"*. Nele você verá uma lista dos sítios arqueológicos encontrados na área de pesquisa. Em cada linha constará o nome do sítio, seguido de sua ficha no SICG.

Exemplo:

>Nome,Ficha<br>
>Boqueirão do Neisinho 3, https://sicg.iphan.gov.br/sicg/bem/visualizar/45318<br>
>Boqueirão do Neisinho 4, https://sicg.iphan.gov.br/sicg/bem/visualizar/45319<br>
>Boqueirão do Neisinho 5, https://sicg.iphan.gov.br/sicg/bem/visualizar/45320<br>


## Desenvolvimento

* [x] ~~Criar busca de Sítios Arqueológicos Cadastrados com retorno em CSV~~;
* [ ] Adicionar retorno de Bens Culturais Registrados (Imaterial);
* [ ] Adicionar retorno de Bens Culturais Tombados;
* [ ] Adicionar retorno de Bens Culturais Valorados (Ferroviário);
* [ ] Adicionar busca de todos os bens a partir da seleção da Unidade Federativa e município;
* [ ] Disponibilizar o programa em uma interface web com as listas de bens sendo exibidas na página;
* [ ] Adicionar exibição dos resultados em mapa renderizado na página;
* [ ] Adicionar basemap de imagem de satélite ao mapa;
* [ ] Tornar os itens mapa clicáveis para exibir um pop-up com as informações do bem.

