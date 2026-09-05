# WIP=1 and VCR Gate Audit

The treatment history follows this invariant for every feature:

1. Before activation, there is no active feature and VCR is 1.00.
2. Exactly one `not_started` feature changes to `active`.
3. Only that feature is implemented.
4. Its exact `verification` command is executed.
5. Only after exit code 0 does the feature change to `passing` and receive evidence.
6. The next feature is activated only after the queue is clean again.

A `passing` feature is never reverted. In the controlled treatment history, each `wip(Fxx)` activation was followed by one implementation step and one verification/passing transition before the next activation.
