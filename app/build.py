#!/usr/bin/env python3
"""Build Jade Vault: apply the Jade Vault layers (v2 … v16) to the pi-netrunner base page and
write dist/pandora-dee.html. Every edit is an exact-match replacement that must hit exactly once,
so a drifted base fails loudly instead of building something half-patched.

    python3 app/build.py            (run from anywhere; paths are relative to the repo)
"""
import re, sys, os
D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(D)
NM = os.environ.get('JV_NODE_MODULES', os.path.join(ROOT, 'node_modules')) + '/'
DIST = os.path.join(ROOT, 'dist'); os.makedirs(DIST, exist_ok=True)
src = open(os.path.join(D, 'base', 'pi-netrunner-mobile.html'), encoding='utf-8').read()
s = src
def rep(old, new, count=1):
    global s
    n = s.count(old)
    if n < 1: sys.exit(f'MISSING: {old[:90]!r}')
    if count == 1 and n != 1: sys.exit(f'AMBIGUOUS ({n}): {old[:90]!r}')
    s = s.replace(old, new)
def rep_between(start, end, new, keep_end=True):
    global s
    i = s.find(start); j = s.find(end, i + 1)
    if i < 0 or j < 0: sys.exit(f'RANGE MISSING: {start[:60]!r} .. {end[:60]!r}')
    s = s[:i] + new + (s[j:] if keep_end else s[j + len(end):])
def rd(n): return open(os.path.join(D, 'modules', n), encoding='utf-8').read()
