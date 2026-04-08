from __future__ import annotations

# --- 1. Różnica między metodą statyczną a dynamiczą -----
class Axes:
    def __init__(self):
        pass

    @staticmethod
    def orthogonal_static() -> Axes:
        pass

    def orthogonal_dynamic(self) -> Axes:
        pass


ax  = Axes.orthogonal_static()
ax2 = Axes().orthogonal_dynamic()

# --- 2. Wykorzystanie metod statycznych do konstrukcji obiektów -----

class BadDesignMSA:
    def __init__(self, filename: str=None):
        """tworzy pusty obiekt lub wczytuje plik"""
        if not filename:
            # stwórz pusty MSA
            pass
        if filename.endswith(".aln"):
            # wczytaj format aln
            pass
        elif filename.endswith(".clw"):
            # wczytaj format clw
            pass
        else:
            # wczytaj format fasta
            pass

class BetterDesignMSA:
    def __init__(self, filename: str=None):
        """tworzy pusty obiekt"""
        pass

    @staticmethod
    def from_aln(fname: str) -> BetterDesignMSA:
        # wczytaj format aln
        pass

    @staticmethod
    def from_fasta(fname: str) -> BetterDesignMSA:
        # wczytaj format fasta
        pass

    @staticmethod
    def from_clw(fname: str) -> BetterDesignMSA:
        # wczytaj format clw
        pass


msa = BadDesignMSA("plik.fasta") # działa
msa = BadDesignMSA("plik.xyz") # nie działa!!

msa = BetterDesignMSA.from_fasta("plik.xyz")
