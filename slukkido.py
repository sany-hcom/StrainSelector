"""
StrainScheduler - Optimalizált időzítés generátor

Ez a program bemutatja a modern Python best practice-eket:
- Dataclass használata (PEP 681)
- Type hints
- slots=True memória optimalizálás (Python 3.10+)
- Immutable adatszerkezetek (tuple)
- Performance mérés
"""

from datetime import datetime, timedelta
from dataclasses import dataclass, field
from time import perf_counter

@dataclass(slots=True)
class StrainScheduler:
    """
    Időzítés generáló osztály.

    Optimalizációk:
    - slots=True: ~40% kevesebb memória (nincs __dict__)
    - tuple: immutable, gyorsabb iteráció
    - datetime cache: egyszer parse-olva az __init__-ben
    """
    # Tuple használata lista helyett - immutable és memóriahatékony
    strains: tuple[str, ...] = field(default_factory=lambda: ("Pineapple Kush", "Zkittlez", "Blueberry Cookies",
                                                               "White Widow", "Mango Kush", "Trainwreck",
                                                               "Berry Gelato", "Northern Lights",
                                                               "Blueberry Kush", "Purple Punch"))
    # Datetime objektum előre parse-olva - ne minden iterációban számoljon
    start: datetime = field(default_factory=lambda: datetime.strptime("15:35", "%H:%M"))
    # Offsetek percben
    offsets: tuple[int, ...] = field(default_factory=lambda: (0, 20, 80))

    def generate_schedule(self) -> None:
        """
        Időzítés kiírása minden strainhez.

        Optimalizáció: az időpontok stringje egyszer kerül kiszámításra,
        majd minden strain ugyanazt használja.
        """
        # Times csak egyszer számolódik, nem minden iterációban
        times = ", ".join((self.start + timedelta(minutes=o)).strftime("%H:%M") for o in self.offsets)
        for strain in self.strains:
            print(f"{strain}: {times}")

if __name__ == '__main__':
    start = perf_counter()
    StrainScheduler().generate_schedule()
    print(f"\nFutási idő: {(perf_counter() - start) * 1000:.3f} ms")
