import spine.lean.Certificates.CertificateSoundness

namespace URF

universe u

structure CertCat where
  Obj : Type u
  Accepts : Obj → Prop

structure ThmCat where
  Obj : Type u
  Holds : Obj → Prop

structure FunctorCT (C : CertCat) (T : ThmCat) where
  onObj : C.Obj → T.Obj
  preserves : ∀ c, C.Accepts c → T.Holds (onObj c)

structure FunctorTC (C : CertCat) (T : ThmCat) where
  onObj : T.Obj → C.Obj
  reflects : ∀ t, T.Holds t → C.Accepts (onObj t)

structure EquivalenceCT (C : CertCat) (T : ThmCat) where
  F : FunctorCT C T
  G : FunctorTC C T
  left_inv : ∀ c, G.onObj (F.onObj c) = c
  right_inv : ∀ t, F.onObj (G.onObj t) = t

end URF
