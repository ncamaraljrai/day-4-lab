# Run Evidence

## Shared baseline

- Same five feature definitions for both runs
- Same `tests/test_features.py`
- Same per-feature verification commands

## Control run

The unconstrained control activated all five features together and was stopped with F01/F02 verified while F03/F04/F05 remained active and unverified.

## Treatment run

The WIP=1 treatment activated one feature at a time and marked it `passing` only after the exact verification command succeeded.

## Reproduce final treatment verification

```bash
python -m pytest -q
```

Expected final result:

```text
.....                                                                    [100%]
5 passed
```

## Integrity note

This is a controlled assistant replay using the same backlog and executable tests for both conditions. The VCR values and git line/file counts were measured from the local experiment; they are not copied from the course case study and are not represented as telemetry from an external Claude/Codex/Cursor session.
