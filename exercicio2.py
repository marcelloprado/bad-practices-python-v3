# Este arquivo ignora completamente a PEP 8 e outras boas práticas.
# O codigo esta horrivel de proposito.
# Ao todo temos 11 quebras de boas praticas.
# Seu desafio eh identificar todas as quebras de boas praticas e corrigi-las.
#
import pandas
import sys
import os
import random
import glob


def  Processar_Dados_do_arquivo(NOME_DO_ARQUIVO, obter_uma_linha=False):
    """
    Esta funcao processa um arquivo CSV de maneira terrivel.
    """
    try:
        ficheiro = open(NOME_DO_ARQUIVO, 'r')
        global  _dados_globais
        _dados_globais = pandas.read_csv(ficheiro)
        ficheiro.close()
    except Exception as e:
        print("Aconteceu um erro: " + str(e))
        return "Erro"

    if obter_uma_linha == True:
        total_linhas = len(_dados_globais)
        if total_linhas > 0:
            linha_aleatoria_indice = random.randint(0, total_linhas - 1)
            linha_para_obter = _dados_globais.iloc[linha_aleatoria_indice]
            return linha_para_obter.to_dict()
        else:
            return "Nao ha dados"
    else:
        return _dados_globais.to_dict('records')

def main( _):
    nome_do_arquivo = "exemplo.csv" if len(sys.argv) < 2 else sys.argv[1]

    if nome_do_arquivo == "exemplo.csv" and not os.path.exists(nome_do_arquivo):
        print("Criando arquivo de exemplo...")
        pandas.DataFrame({"nome": ["João", "Maria", "Pedro"], "idade": [25, 30, 35], "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]}).to_csv(nome_do_arquivo, index=False)

    dados = Processar_Dados_do_arquivo(nome_do_arquivo)
    print("Dados completos:\n", dados)

    uma_linha = Processar_Dados_do_arquivo(nome_do_arquivo, obter_uma_linha=True)
    print("\nUma linha aleatoria:\n", uma_linha)

if __name__ == '__main__':
    main(None)
