
# Argentina at the 2022 World Cup — Shot Quality & xG Analysis

<img width="587" height="443" alt="image" src="https://github.com/user-attachments/assets/2120aa95-3dcb-4ecf-b512-e8e320e59e9f" />

How sustainable was Argentina's attacking output at the 2022 World Cup?
Non-penalty xG analysis using StatsBomb open data, benchmarked against
all 32 teams.

## The question
Argentina won the tournament — but did the underlying shot quality
support the result, or were they riding variance? This project measures
their non-penalty xG (npxG) profile and ranks it against the full field.

## Data & scope
- **Source:** StatsBomb Open Data, FIFA World Cup 2022
- **Metric:** non-penalty xG (npxG) — penalties and shootouts excluded
- **Benchmark:** all 32 teams, z-scores vs tournament mean
- **Note:** goals-against reconciled for one own goal (excluded from
  shot-based metrics)

## Key findings

- **Argentina's chance creation was genuinely strong, not variance-driven.**
  Their 1.23 npxG/90 ranked 6th of 32 teams, above the tournament median
  (0.92) and the top of the interquartile range (1.01).

- **The title run was not built on unsustainable finishing.**
  Non-penalty goals came in +0.98 above npxG, but the z-score of just 0.31
  places this within normal finishing noise — not a significant
  overperformance.

- **Result = a top-quartile attacking base plus match-level variance.**
  Germany and Brazil posted higher npxG/90 and went out earlier; Argentina
  paired strong underlying numbers with high-variance games (e.g. Mexico:
  0.33 xGF, won 2-0) rather than systematic overperformance.

## How to run
\```bash
pip install -r requirements.txt
python src/[ton_script].py
\```
Figures are written to `figures/`.

## Repo structure
\```
src/                 Analysis scripts (incl. football_viz_theme.py)
figures/             Exported visualisations
requirements.txt
\```

## Limitations & next steps
- npxG treats all chances by location/context, not finishing skill
- Single-tournament sample — small n per team
- Next: [ex : custom xG model / per-90 normalisation]

## Data & credit
StatsBomb Open Data — https://github.com/statsbomb/open-data
Licensed under StatsBomb's open-data terms.
