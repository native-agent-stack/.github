# ADR-0004: Five-Stage Compounding Strategy Promotion Manifest (`Sim -> Backtest -> Paper -> Fine-Tune -> Broker`)

- **Status:** Accepted
- **Date:** 2026-11-17
- **Layer:** Strategy Lifecycle (`T3–T8`)
- **Evidence Grade:** E4 (Live Alpaca Paper `:8787`/`:8799` & IBKR `:4002` Parity)
- **GitHub Evidence:** https://github.com/nautechsystems/nautilus_trader, https://github.com/nkaz001/hftbacktest, https://github.com/alpacahq/alpaca-py, https://github.com/ib-api-reloaded/ib_async
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP cutover) or 2027-01-01

## Context and Problem Statement

Promoting factor ideas directly to broker execution without event-driven queue simulation, paper fill reconciliation, and shrinkage-regularized parameter updates leads to live slippage decay.

## Decision Outcome

1. **5-Stage Typed Promotion Pipeline:** Every strategy entry in `ECOSYSTEM_ORG_MANIFEST.json` and `STRATEGY_PROMOTION_MANIFEST.json` progresses deterministically through `STAGE_1_PREWALL_RESEARCH` -> `STAGE_2_EVENT_SIM` (`NautilusTrader` / `hftbacktest`) -> `STAGE_3_FALSIFIED_BACKTEST` (`CPCV` + `DSR`) -> `STAGE_4_LIVE_PAPER` (`200 req/min` Alpaca `PA...` & `3,000 msg/min` IBKR `:4002` `DU...`) -> `STAGE_5_EMPIRICAL_BAYES_COMPOUNDING`.
2. **Closed-Loop Fine-Tuning:** Reconcile realized paper slippage and excursion quantiles back into shrinkage-regularized per-symbol priors (`prewall_symbol_params.json`) without violating pre-wall causal boundaries.

## Alternatives Considered

1. **Direct bar-backtest to execution deployment:** Rejected — misses sub-second L1 spread bounce, `extended_hours` venue order-type constraints, and multi-lot partial-fill races.

## Verification Witness

- `python3 -m unittest discover -s tests -v` -> `PASS`
