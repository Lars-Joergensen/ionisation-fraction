(* ::Package:: *)

(* ::Input:: *)
(*\[Alpha] = 0.0072973525693;*)
(*Subscript[m, e]=510998.95;(*eV*)*)
(*Subscript[m, pl]=1.2211*10^28 ;(*eV*)*)
(*Subscript[\[CapitalOmega], m]=0.315;*)
(*Subscript[\[Rho], c] = 3.679272179*10^-11;(*eV^4*)*)
(*z = 1/2.34865477*10^4-1; (*x = 1/T is given as a dimensionless unit *)*)
(**)


(* ::Text:: *)
(* *)


(* ::Input:: *)
(*recrate[x_] := (4*Pi^2*\[Alpha])/Subscript[m, e]^2*6.8*Sqrt[x/(3*Subscript[m, e])]*)
(*nb[x_] := 6.0*10^-10*(Subscript[\[Omega], b]/0.022)*(2*Zeta[3])/(Pi^2*x^3)*)
(*hubble= Sqrt[8/3*Pi/Subscript[m, pl]^2*(Subscript[\[CapitalOmega], m]*Subscript[\[Rho], c]*(1+z)^3+Pi^2/15)]*)


(* ::Input:: *)
(*lambda[x_] := nb[x]*recrate[x]/(x*hubble)*)


(* ::Input:: *)
(*\[Lambda] = lambda[x]/.{x->1}*)


(* ::Input:: *)
(*Xeq[x_] := 5.95*10^7/Sqrt[Subscript[\[Omega], b]]*x^(3/4)*Exp[-6.8*x]*)
(*Delta[x_] := 3.4/\[Lambda]*x^2*)


(* ::Text:: *)
(* *)


(* ::Input:: *)
(*sol = Solve[Xeq[Subscript[x, f]]==Delta[Subscript[x, f]],Subscript[x, f]]*)


(* ::Input:: *)
(*Subscript[x, freeze] = sol/.{Subscript[\[Omega], b]->0.02237}*)


(* ::Input:: *)
(*Subscript[X, e] = Subscript[x, freeze]/\[Lambda]/.{Subscript[\[Omega], b]->0.02237}*)
