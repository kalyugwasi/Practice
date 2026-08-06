#!/usr/bin/env bash
# Source this once in a terminal opened at the repository root.
_cp_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cp() { "$_cp_root/bin/cp" "$@"; }
cpjudge() { "$_cp_root/bin/cpjudge" "$@"; }
