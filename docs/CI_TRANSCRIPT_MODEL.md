State space:
  S := (p, t, h)
  p ∈ Σ*   = PATH string
  t ∈ Σ*   = lean-toolchain file content
  h ∈ Σ*   = env hash = sha256(env.txt)

Observation alphabet:
  O := lines written to env.txt

Transition:
  (p,t,_) --install--> (p',t,h')
  (p,t,h) --build--> (p,t,h)

Determinism claim (conditional):
  Fix t and installer script content; then h is a function of (runner image, t).
