"""
Copyright© 2024 Alexandre Cavalcanti

    This file is part of "Buscador do Patrimônio".

    "Buscador do Patrimônio" is free software: you can redistribute
    it and/or modify it under the terms of the GNU General Public
    License as published by the Free Software Foundation, either version
    3 of the License, or (at your option) any later version.

    "Buscador do Patrimônio" is distributed in the hope that it will
    be useful, but WITHOUT ANY WARRANTY; without even the implied
    warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with "Buscador do Patrimônio". If not, see <https://www.gnu.org/licenses/>. 

"""

from sys import argv
from busca import get_bens, mat_csv, imat_csv

def main():
    print("Buscando bens culturais\n")
    sitios_dict, rg_dict, tb_dict = get_bens(argv[1])
    print("Salvando listas de bens encontrados")
    mat_csv(sitios_dict)
    mat_csv(tb_dict)
    imat_csv(rg_dict)


if __name__ == "__main__":
    main()