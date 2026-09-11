# Science results — V62.2

## 1. Run12 matched-forcing climate close-out

GitHub Actions workflow **V62 Matched Forcing — FaIR + Hector**, run `34617229257` (run number 12), completed successfully on commit `801982af3d27a2638e8a7fb448f81701f76ae637`. FaIR, Hector, and the cross-model comparison all passed.

The experiment harmonizes future non-CO2 forcing from 2027 onward. This removes different future methane/aerosol/other non-CO2 forcing pathways as a major cross-model confounder while retaining each model's own carbon cycle, historical state, CO2 forcing formulation, and temperature response.

### Atmospheric response to cumulative CDR

| Year | FaIR response p05 | FaIR p50 | FaIR p95 | Hector | Hector inside FaIR p05-p95? |
|---:|---:|---:|---:|---:|:---:|
| 2040 | 0.6543 | 0.7119 | 0.7543 | 0.7064 | yes |
| 2100 | 0.3977 | 0.4722 | 0.5254 | 0.4398 | yes |
| 2156 | 0.3343 | 0.4073 | 0.4559 | 0.3477 | yes |
| 2184 | 0.2979 | 0.3699 | 0.4192 | 0.2948 | no |
| 2200 | 0.2864 | 0.3573 | 0.4084 | 0.2823 | no |
| 2300 | 0.2550 | 0.3076 | 0.3674 | 0.2469 | no |

**Candidate finding:** with future non-CO2 forcing harmonized, FaIR and Hector are close on early-century atmospheric CDR efficacy and increasingly separate on multi-century horizons. In the predeclared milestone table, Hector remains inside the FaIR p05-p95 interval through 2156 and falls below it from 2184 onward.

**Claim boundary:** this is a controlled two-model result for one canonical CDR pathway. It is not yet a universal threshold or law. Generality requires OSCAR under an equivalent forcing protocol and alternative CDR schedules.

## 2. Canonical trajectory does not restore 280 ppm by 2300

The matched experiment uses cumulative canonical CDR of **2,013.8807 GtCO2** from 2026-2183, with a **15.2 GtCO2/yr** peak. Under this pathway:

- FaIR removal-ON CO2 at 2300: **302.101 ppm median** (p05 **298.912**, p95 **305.453**).
- Hector removal-ON CO2 at 2300: **309.513 ppm**.
- FaIR removal-OFF CO2 at 2300: **406.162 ppm median**.
- Hector removal-OFF CO2 at 2300: **393.000 ppm**.

Therefore the older 280-ppm restoration dates cannot be reported as validated outcomes of the canonical pathway. They remain screening or inverse-control target experiments unless a separately defined schedule actually reaches 280 ppm in an externally executed model.

This is a scientific strength: V62.2 records an externally executed result even when it falsifies a favorable earlier screening interpretation.

## 3. Long-run temperature benefit remains large

At 2300:

- FaIR median: **0.963°C** removal-ON versus **1.987°C** removal-OFF, a difference of **1.025°C**.
- Hector: **1.023°C** removal-ON versus **1.957°C** removal-OFF, a difference of **0.934°C**.

Peak removal-ON warming is about **1.670°C in 2051** in the FaIR median and **1.914°C in 2041** in Hector. Peak removal-OFF warming is about **2.047°C in 2202** in the FaIR median and **2.172°C in 2135** in Hector.

Thus failure to reach 280 ppm by 2300 does not imply failure of the programme; both models show a very large long-horizon climatic benefit relative to removal-OFF.

## 4. Hector forcing diagnostic clarification

Hector's raw `FTOT_CONSTRAIN` tracking-offset diagnostic is about **1.0966 W/m2**. It is not the matched-forcing acceptance metric. Hector applies the user forcing constraint within absolute-forcing bookkeeping and then reports forcing relative to its base-year forcing. The scientifically relevant quantity in this experiment is `RF_TOTAL - RF_CO2 - target_nonCO2`, which converged to **9.93e-6 W/m2** removal-ON and **9.12e-6 W/m2** removal-OFF, satisfying the predeclared **1e-5 W/m2** Hector gate.

V62.2 therefore treats the raw 1.0966 W/m2 value as a reporting-offset diagnostic that must be renamed/corrected before publication, not as evidence that the forcing match failed.

## 5. Comprehensive restoration model remains intact

These climate findings do not replace the wider planetary-restoration architecture. V62.2 retains all existing modules for oceans, coral reefs, fisheries, seaweed food and fuels, Grid Harvesting, plastics, eutrophication, blue carbon, land and forests, all CDR routes, energy, transport, materials, water, hunger, meat-inclusive diet pathways, healthcare, vaccines and antibiotics, mRNA cancer-vaccine access if validated/approved, population/carrying-capacity screens, education, housing, justice, robot doctors, robot lawyers, robot tutors, eldercare and other robotics, Carbonite, Proof of Rent, geotagged tree reserves, the restoration charity, finance/governance stress cases, Africa vulnerability, Los Jardines de la Fuente de Cella, and MRV.

Each non-climate module retains its own evidentiary classification. The FaIR/Hector result does not validate those modules by association.

## 6. Nature-flagship candidate and required next tests

The most potentially significant physical finding is not merely that CDR efficacy declines, which is already expected from carbon-cycle adjustment. It is the controlled two-model pattern: **close early-century response under harmonized future non-CO2 forcing, followed by systematic multi-century separation**.

Before presenting that as a general discovery, V62.2 predeclares:

1. matched-forcing OSCAR;
2. explicit land/ocean/permafrost reservoir decomposition;
3. alternative CDR rate/timing schedules;
4. retention of the comprehensive restoration/human-flourishing model with separate evidentiary labels.
