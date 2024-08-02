import pandas as pd

from bio.ler_fasta import ler_fasta


def fazer_problema_3(caminho_do_arquivo):
    organismos = ler_fasta(caminho_do_arquivo)

    posicao_mutacao = 999
    base_mutacao = 'G'

    virus = []

    for organismo in organismos:
        tem_mutacao = organismo.sequencia[posicao_mutacao] == base_mutacao
        virus.append({
            "id": organismo.id,
            "nome": organismo.nome,
            "base_esperada": "A",
            "base_achada": organismo.sequencia[posicao_mutacao],
            "tem_mutacao_estudada": "Sim" if tem_mutacao else "Não",
        })

    pd.DataFrame(virus).to_csv('problema_3.csv', index=False)
    print("Foi gerado um csv com essas informações")
