"""Constrói o CSV do dicionário de produtos usado pela publicação."""

from __future__ import annotations

import csv
from pathlib import Path


DICIONARIO_PRODUTOS = {
    "31021010": "Ureia",
    "31022100": "SAM",
    "31055900": "NP",
    "31042090": "MOP",
    "31054000": "MAP",
    "31031100": "Superfosfatos>35 %",
    "31031900": "O.Superfosfatos",
    "31052000": "NPK",
    "31023000": "NAM",
    "31059090": "NK",
    "31026000": "Nit. de Cálcio",
    "31043010": "SOP",
    "12019000": "Soja",
    "38089329": "Herbicidas",
    "38089199": "Inseticidas",
    "38089299": "O.fungicidas",
    "09011110": "Café .n.t",
    "17011400": "O.açúcares cana",
}


def atualizar_csv(caminho: str | Path | None = None) -> Path:
    """Grava o dicionário em CSV e retorna o caminho produzido."""
    destino = Path(caminho) if caminho else Path(__file__).with_name("dicionario-produtos.csv")
    destino.parent.mkdir(parents=True, exist_ok=True)

    with destino.open("w", encoding="utf-8", newline="") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=("ncm", "nick"))
        escritor.writeheader()
        escritor.writerows(
            {"ncm": ncm, "nick": nick}
            for ncm, nick in DICIONARIO_PRODUTOS.items()
        )

    return destino


if __name__ == "__main__":
    print(atualizar_csv())
