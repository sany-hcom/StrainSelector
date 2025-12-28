# StrainScheduler

Maximálisan optimalizált Python program strain-ek ütemezésére meghatározott időpontokkal.

## Teljesítmény

- **Futási idő**: ~7ms átlagosan
- **Memória használat**: Minimális (~40% kevesebb `slots=True` miatt)
- **Python 3.14 JIT támogatás**: ✅

## Optimalizációk

### Memória
- ✅ `@dataclass(slots=True)` - nincs `__dict__`, ~40% kevesebb memória
- ✅ `tuple` lista helyett - immutable, kisebb overhead
- ✅ Egyszer parse-olt `datetime` - nem többször
- ✅ `perf_counter()` időmérés - minimális overhead (~100ns)

### CPU
- ✅ Times string cache-elés - egyszer számolva, 10x használva
- ✅ Egyszer parse-olt kezdési idő az `__init__`-ben
- ✅ Tuple iteráció gyorsabb mint lista
- ✅ Generator expression a `join`-ban
- ✅ f-string használata (gyorsabb mint `.format()`)
- ✅ Python 3.14 interpreter - ~20% gyorsabb

### Modern Python
- ✅ Dataclass + type hints (PEP 681)
- ✅ `slots=True` (Python 3.10+)
- ✅ Immutable adatszerkezetek
- ✅ Python 3.14 JIT compiler támogatás

## Használat

### Alap futtatás
```bash
python slukkido.py
```

### JIT compiler-rel (Python 3.14+)
```bash
python -X jit slukkido.py
```

## Kimenet

```
Pineapple Kush: 15:35, 15:55, 16:55
Zkittlez: 15:35, 15:55, 16:55
Blueberry Cookies: 15:35, 15:55, 16:55
White Widow: 15:35, 15:55, 16:55
Mango Kush: 15:35, 15:55, 16:55
Trainwreck: 15:35, 15:55, 16:55
Berry Gelato: 15:35, 15:55, 16:55
Northern Lights: 15:35, 15:55, 16:55
Blueberry Kush: 15:35, 15:55, 16:55
Purple Punch: 15:35, 15:55, 16:55

Futási idő: 6.920 ms
```

## Követelmények

- **Python 3.10+** (slots támogatás)
- **Python 3.14+** ajánlott (JIT compiler, gyorsabb interpreter)
- **Nulla dependency** - minden modul built-in (standard library)

## Git Setup

### Lokális Git inicializálás

```bash
# Git repo inicializálása
git init

# Felhasználó beállítása
git config --global user.name "Név"
git config --global user.email "email@example.com"

# Fájlok hozzáadása
git add .

# Első commit
git commit -m "Initial commit - StrainScheduler optimized example"
```

### GitHub feltöltés

```bash
# GitHub repo létrehozása (gh CLI-vel)
gh repo create StrainScheduler --public --source=. --remote=origin

# Vagy manuálisan remote hozzáadása
git remote add origin https://github.com/USERNAME/StrainSelector.git

# Push to GitHub
git push -u origin master
```

## License

MIT License - Ingyenesen használható oktatási és kereskedelmi célra is.
