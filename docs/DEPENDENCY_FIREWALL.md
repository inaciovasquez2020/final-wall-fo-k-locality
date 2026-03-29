# Dependency Firewall

Allowed dependency chain

urf-axioms
    ↓
urf-core
    ↓
urf-spine
    ↓
applications

Forbidden dependencies

applications → urf-core
experiments → urf-core
numerical tests → urf-core
