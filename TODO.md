# TODO

> General project roadmap. A few nice-to-haves are deliberately omitted for now, because I'll just get distracted by them.


— contextual data
---

> Annotate entire item corpus with pickup reason context.

1. `(current) → → →` prelim annotations & common misc items 
2. tier list tagging
    - runeword bases
    - sets & uniques
    - niche set/unique/build items
    - leveling items
3. crafting bases
4. refactor pass


— style processor
---

> Create style rendering defaults.

1. default styling & annotation variants for common items
2. default styling for sets, uniques, and bases
3. item-text tag composer
4. refactor pass


— mod pkg generation
---

> Ingest static configs, annotative data, and D2R data &rarr; output a plug-and-play loot filter 'mod'.

1. compose filter inputs
2. load & modify D2R dataset
3. write mod zipfile
4. refactor & optimisations pass


— webapp
---

1. env/infra (likely `pyodide` + ?)
2. functional GUI
3. pretty GUI
4. optimisation/compatibility pass
