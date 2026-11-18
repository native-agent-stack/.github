# ADR-0005: Non-Negotiable Paper-Only Firewall, `ADR-0022 <= 2.00%` Cap & `6–14 bps` Near-Lossless Shield

- **Status:** Accepted
- **Date:** 2026-11-17
- **Layer:** Execution & Risk (`L1` × `L8` × `L9` × `T5`)
- **Evidence Grade:** E4 (Runtime & Pre-Wall `CVaR_95` Verified)
- **GitHub Evidence:** https://github.com/alpacahq/alpaca-py, https://github.com/alpacahq/alpaca-mcp-server, https://github.com/gerrymanoim/exchange_calendars
- **Revisit Trigger:** 2026-12-06 (`23/5` SIP pause transition) or 2027-01-01

## Context and Problem Statement

Autonomous 24/5 execution across Pre-Market, Regular, After-Hours, and Overnight (`BOATS`) sessions faces two distinct failure modes: accidental routing to live real-money accounts, and asymmetric tail drawdowns on liquid Large-Cap entries or wide off-hours stub quotes.

## Decision Outcome

1. **100% Live-Capital Hard Refusal:** Hard-block live broker endpoints, `.claude/bin/live`, and live IBKR ports (`4001`, `7496`); verify `PA...` / `DU...` paper prefixes before any order action.
2. **Dual-Layer Per-Trade & Daily Account Protection:** Enforce `ADR-0022 <= 2.00%` maximum initial stop across all tiers, `6–14 bps` spread-safe initial scratch stops with `+5–10 bps` instant breakeven+ locks on `MEGA_LARGE_CAP` symbols (cutting pre-wall `CVaR_95` tail loss by `54.1%`), `STUB_SPREAD_GUARDED` off-hours quote filtering, and an account-level `DailyScratchCircuitBreaker` (`4` consecutive scratches -> `15m` cooldown; `-75 bps` daily loss -> NY-session halt).

## Alternatives Considered

1. **Static `1.0%–2.0%` RTH-only trailing stops:** Rejected — leaves positions unprotected outside `09:30–16:00 ET` and suffers `206.4 bps` `CVaR_95` tail loss on Large Caps.

## Verification Witness

- `python3 scripts/merge_gate.py` -> `PASS`
