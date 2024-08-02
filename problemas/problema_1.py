import sys
import os

diretorio_principal = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(diretorio_principal)

from bio.ler_fasta import ler_fasta

def fazer_problema_1(caminho_do_arquivo):
    organismos = ler_fasta(caminho_do_arquivo)

    for organismo in organismos:
        porcentagem_a = organismo.sequencia.calcular_percentual(["A"])
        porcentagem_t = organismo.sequencia.calcular_percentual(["T"])
        porcentagem_c = organismo.sequencia.calcular_percentual(["C"])
        porcentagem_G = organismo.sequencia.calcular_percentual(["G"])
        porcentagem_GC = organismo.sequencia.calcular_percentual(["G", "C"])
        print(f"O organismo {organismo.nome} tem:")
        print(f"{porcentagem_a:.2%} de base A,"
              f" {porcentagem_t:.2%} de base T, {porcentagem_c:.2%} de base C, {porcentagem_G:.2%} de base G,"
              f"e counteúdo GC de {porcentagem_GC:.2%}")



if __name__ == "__main__":
    print(fazer_problema_1(f"{diretorio_principal}/arquivos/Flaviviridae-genomes.fasta"))