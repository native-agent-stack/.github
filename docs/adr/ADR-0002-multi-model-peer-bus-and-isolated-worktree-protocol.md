# ADR-0002: Multi-Model Peer Bus, Lease Collision Guard & Isolated Git Worktree Protocol

- **Status:** Accepted
- **Date:** 2026-11-17
- **Layer:** Multi-Agent Coordination (`P0–P5` × `L1` × `L5` × `L7`)
- **Evidence Grade:** E4 (Verified Across 5 Concurrent Peer Sessions)
- **GitHub Evidence:** https://github.com/native-agent-stack/sota-multi-model-workflows, https://github.com/aannoo/hcom, https://github.com/stablyai/orca
- **Revisit Trigger:** 2027-01-01 or schema bump on `peer_bus.db`

## Context and Problem Statement

Concurrent sessions across Antigravity (`AGY`), Claude Code, OpenAI Codex, DeepSeek Harness (`DSH`), and Orca workers corrupt shared working trees if two agents edit overlapping files on `main` without transactional leases.

## Decision Outcome

1. **Transactional SQLite WAL Peer Bus:** Require every agent to claim repo/path leases (`sota-bus claim`), broadcast cross-session handshakes (`sota-bus msg` / `hcom`), and record empirical handovers (`HANDOVER.md`, `LESSONS.md`) before releasing leases.
2. **Mandatory Isolated Git Worktrees:** Execute multi-file feature and ADR changes inside isolated `git worktree add` branches (`wt-*`), running full deterministic gates prior to fast-forward merge onto `main`.

## Alternatives Considered

1. **Advisory chat-only coordination:** Rejected — invisible across separate agent processes and terminal sessions.
2. **In-place concurrent edits on `main`:** Rejected — causes index lock contention and dirty-tree merge failures.

## Verification Witness

- `python3 -m unittest discover -s tests -v` -> `PASS`
- `python3 scripts/merge_gate.py` -> `PASS`
