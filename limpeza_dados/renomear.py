import os

os.chdir("/home/alexandrecgn/DevOps/buscador_do_patrimônio/municipios")

print(os.getcwd())

for arquivo in os.listdir():
    nm, ext = os.path.splitext(arquivo)
    nm = nm.replace(" ", "_")
    nm = nm.encode("ascii", "ignore").decode("ascii")
    nv_nm = "{}{}".format(nm, ext)
    os.rename(arquivo, nv_nm)

print("Arquivos renomeados com sucesso!")