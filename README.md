# 🦸 Hand Power — Sledování rukou a ovládání superschopností

> Proměň pohyby svých rukou v superschopnosti pomocí webkamery.

**Hand Power** je experimentální projekt v Pythonu, který pomocí kamery sleduje pohyby rukou v reálném čase a převádí je na vizuální efekty na obrazovce. Cílem je vytvořit zážitek, ve kterém můžeš pomocí vlastních gest ovládat energetické koule, blesky, štíty a další speciální schopnosti — bez fyzického ovladače.

🚧 **Stav projektu:** Plánování / počáteční vývoj  
🎯 **První cíl:** Zprovoznit sledování rukou a vytvořit první vizuální efekt.

---

## ✨ Hlavní myšlenka

Tvoje ruce se stanou ovladačem superschopností.

Webkamera zachytí pohyby rukou, systém rozpozná jejich polohu a gesta a následně vykreslí odpovídající efekty.

Například:

- 🔵 Pohybem rukou budeš ovládat energetické koule.
- ⚡ Určitým gestem aktivuješ blesky.
- 🛡️ Zvednutím obou rukou vytvoříš energetický štít.
- 💥 Prudkým pohybem ruky vyšleš energetickou střelu.
- 🌌 Kombinací gest budeš aktivovat složitější schopnosti.

Dlouhodobým cílem je vytvořit dojem, jako bys skutečně ovládal superschopnosti.

## 🎬 Jak bude projekt fungovat

1. **Kamera** – zachytí živý obraz z webkamery.
2. **Sledování rukou** – rozpozná ruce, prsty a jejich důležité body.
3. **Rozpoznávání gest** – určí, jaké gesto právě provádíš.
4. **Systém schopností** – přiřadí gestu konkrétní superschopnost.
5. **Vizuální efekty** – vykreslí částice, energii, blesky a animace.
6. **Zobrazení v reálném čase** – spojí obraz z kamery s efekty, které sledují pohyby rukou.

## 🛠️ Použité technologie

| Technologie | Využití |
|---|---|
| Python | Hlavní programovací jazyk |
| OpenCV | Přístup ke kameře a zpracování obrazu |
| MediaPipe | Sledování rukou a rozpoznávání bodů na prstech |
| NumPy | Matematické výpočty a práce se souřadnicemi |
| Pygame nebo vykreslování přes OpenCV | Základní grafika a efekty |
| GPU a shadery | Pokročilé vizuální efekty v dalších verzích |

Konkrétní technologie se mohou během vývoje změnit podle výkonu a výsledků testování.
