import Lean

open Lean

/-
Deterministic, functional minimal cache tool:
- `cache get` creates a marker file under `.lake/cache/` and exits 0
- never depends on network, timestamps, randomness
- stable stdout
-/

def ensureDir (p : System.FilePath) : IO Unit := do
  if !(← p.pathExists) then
    IO.FS.createDirAll p
  else
    pure ()

def writeIfMissing (p : System.FilePath) (s : String) : IO Unit := do
  if !(← p.pathExists) then
    IO.FS.writeFile p s
  else
    pure ()

def main (args : List String) : IO UInt32 := do
  match args with
  | ["get"] =>
      let dir : System.FilePath := ".lake" / "cache"
      let marker : System.FilePath := dir / "cache.get.ok"
      ensureDir dir
      writeIfMissing marker "ok\n"
      IO.println "OK: cache get"
      return 0
  | _ =>
      IO.println "usage: cache get"
      return 0
