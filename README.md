# StackStorm ChatOps Release

An attempt to rub some ChatOps on st2 release machinery. Currently WIP, but it already works as a request-confirmation mechanics PoC.

## Request-confirmation

Two-step verification works in the following way:

1. You request a release with `!release a patch`.
2. Bot gathers pre-release information (current version, pull requests since the last release, etc.).
3. Bot gives a summary along with a confirmation ID: "@emedvedev wants to release, new version will be X.Y.Z, the following PRs were merged, type `!confirm 1234567890abcdef` to confirm."
4. A team member issues a confirmation command.
5. Bot executes pre-flight checks: you can't confirm your own release, ID is valid, request is not too old, etc.
6. The release procedure is started.

## Release procedure

WIP.
