# Conan Rebase Bug

This is a repository to reproduce a potential renovate bug where it rebases
open PRs, even when it isn't supposed to.

## Setup

The final workaround config can be found in this repository.

The bug appears to be exclusively happening when updating conan packages.

It was not possible to reproduce the issue with the hosted renovate app, as
caching is enabled there.

We're using the regex manager, because we use a custom conandata.yml layout,
which the default conan manager doesn't understand. But in the end this still
uses the conan datasource and everything else related to conan packages.

## Reproduction Steps

1. Have an outdated conan package
1. Run self-hosted renovate with `"repositoryCache": "disabled"` to get a PR.
1. Run renovate again, nothing should happen, as the PR is up to date.
1. Do an unrelated commit to main, e.g. add an empty file.
1. Run renovate again and it force-pushes the PR branch with the changes from
   main.
1. Set `"repositoryCache": "enabled"` and run renovate again to populate the
   cache.
1. Do another unrelated commit to main, e.g. add another empty file.
1. Run renovate again and there should be no more force-pushes.
