from bio.constantes import CONVERSOR_DE_BASES, DNA_STOP_CODONS, DNA_PARA_AMINOACIDO


class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)

    def complementar(self):
        seq_complementar = ""
        for base in self.sequencia:
            seq_complementar += CONVERSOR_DE_BASES.get(base, base)
        return Sequencia(seq_complementar)

    def complementar_reversa(self):
        seq_complementar_reversa = ""
        for i in range(len(self.sequencia), 0, -1):
            seq_complementar_reversa += CONVERSOR_DE_BASES.get(self.sequencia[i], self.sequencia[i])
        return Sequencia(seq_complementar_reversa)

    def transcrever(self):
        return Sequencia(self.sequencia.replace('T', 'U'))

    def traduzir(self, parar=False):
        n = len(self.sequencia)

        translacao = ""
        for i in range(0, n - n % 3, 3):
            codon = self.sequencia[i:i + 3]
            if codon in DNA_STOP_CODONS and not parar:
                translacao += "*"
            elif codon in DNA_STOP_CODONS:
                return translacao
            else:
                translacao += DNA_PARA_AMINOACIDO.get(codon, "X")
        return translacao

    def calcular_percentual(self, bases):
        bases_count = 0
        for base in self.sequencia:
            if base in bases:
                bases_count += 1
        return bases_count / len(self.sequencia)
