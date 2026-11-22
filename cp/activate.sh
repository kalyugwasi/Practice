#!/usr/bin/env bash
# Source this once in a terminal opened at the repository root.
if [ -n "${ZSH_VERSION:-}" ]; then
  _cp_activate_source="${(%):-%x}"
else
  _cp_activate_source="${BASH_SOURCE[0]}"
fi
_cp_root="$(cd -- "$(dirname -- "$_cp_activate_source")" && pwd)"
unset _cp_activate_source
cp() { "$_cp_root/bin/cp" "$@"; }
cpjudge() { "$_cp_root/bin/cpjudge" "$@"; }
