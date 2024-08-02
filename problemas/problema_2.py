from bio.ler_fasta import ler_fasta


def fazer_problema_2(caminho_do_arquivo):
    organismos = ler_fasta(caminho_do_arquivo)
    for organismo in organismos:
        print(f"Traduzindo sequencia do {organismo.nome}:")
        print(organismo.sequencia.traduzir())
