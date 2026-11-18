# ADR-0003: Pre-Wall (`<= 2026-10-15`) Causal Isolation & HLZ / DSR / CPCV Statistical Gates

- **Status:** Accepted
- **Date:** 2026-11-17
- **Layer:** Quant Research (`L8` × `T1–T4`)
- **Evidence Grade:** E4 (82 Pre-Registered Trials Logged)
- **GitHub Evidence:** https://github.com/skfolio/skfolio, https://github.com/ml4t/diagnostic, https://github.com/pola-rs/polars, https://github.com/duckdb/duckdb
- **Revisit Trigger:** 2027-01-01 or formal post-wall regime epoch cutover

## Context and Problem Statement

Iterative LLM-driven factor search rapidly inflates false-discovery rates through multiple testing, intrabar lookahead, and survivorship/dilution leakage unless constrained by a hard temporal study wall and multiplicity-adjusted hurdles.

## Decision Outcome

1. **Immutable Pre-Registration & Temporal Wall:** Lock SHA-256 hypothesis specs before evaluation, keep factor discovery strictly `<= 2026-10-15`, and increment global trial count `N` on every run (pass or fail).
2. **Multiplicity & Cost Stress Hurdle:** Require Rogers date-clustered `t`-stats clearing Harvey-Liu-Zhu `t*(N)`, `ml4t-diagnostic` `DSR >= 0.95`, `skfolio` `CombinatorialPurgedCV` positive fold stability, point-in-time SEC `S-3`/`424B5` dilution filtering, and positive expectancy under `2x` spread plus Almgren-Chriss square-root market impact.

## Alternatives Considered

1. **IID trade-level `t >= 2.0` without trial tracking:** Rejected — severely understates correlated same-day equity cross-sectional variance and selection bias.

## Verification Witness

- `python3 -m unittest discover -s tests -v` -> `PASS`
