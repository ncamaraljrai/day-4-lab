# Control vs Treatment Comparison

Both runs started from the same local git tag, `baseline`, and used the same five feature definitions and exact verification commands.

The control run activated all five features at once. At the hard stop, F01 and F02 passed while F03, F04, and F05 remained active/unverified. The treatment run enforced WIP=1: one feature was activated, implemented, verified, marked `passing` with evidence, and only then was the next feature activated.

| Metric | Control (unconstrained) | Treatment (WIP=1 + VCR) |
|---|---:|---:|
| Lines added | 86 | 49 |
| Lines deleted | 6 | 19 |
| Total changed lines | **92** | **68** |
| Files touched | **8** | **3** |
| Features activated | 5 | 5 |
| Features `passing` | 2 | 5 |
| VCR | **2/5 = 0.40** | **5/5 = 1.00** |
| Duplicate/abandoned work | 3 unfinished feature scaffolds | None |

## VCR calculation

`VCR = verified_tasks / activated_tasks`

- Control: `2 / 5 = 0.40`
- Treatment: `5 / 5 = 1.00`

## Verification summary

Control final states: F01/F02 `passing`; F03/F04/F05 `active`.

Treatment final suite:

```text
.....                                                                    [100%]
5 passed
```

The unconstrained run changed more code and touched more files, but verified fewer features. The WIP=1 treatment produced less churn and a clean VCR of 1.00.
