#!/usr/bin/env python3
"""Planetary Restoration Model V62.2 — comprehensive restoration + human flourishing.

V62.2 is a conservative overlay on the full V62.0/V62.1 integrated architecture.
It preserves every registered restoration domain and adds the successful Run12
matched-future-non-CO2-forcing FaIR/Hector validation as a new externally executed
climate result. Climate validation does not spill over onto ecological, engineering,
financial, governance, or human-service modules.

The key V62.2 scientific correction is that the canonical 2026–2183 CDR pathway
(~2013.88 GtCO2 cumulative, 15.2 GtCO2/yr peak) materially lowers long-run CO2 and
temperature but does not return atmospheric CO2 to 280 ppm by 2300 in either the
matched-forcing FaIR median or Hector. Earlier 280-ppm dates therefore remain
screening/inverse-control targets rather than validated outcomes of the canonical
trajectory.
"""
from __future__ import annotations

import argparse
import copy
import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

import pandas as pd

HERE = Path(__file__).resolve().parent
RESULTS_DIR = HERE / "results"
MODEL_VERSION = "62.2"
RELEASE_LABEL = "Comprehensive Planetary Restoration and Human Flourishing — matched-forcing validation update"
RELEASE_DATE = "2026-09-11"
MATCHED_RUN_ID = 34617229257
MATCHED_RUN_NUMBER = 12
MATCHED_COMMIT = "801982af3d27a2638e8a7fb448f81701f76ae637"
MATCHED_VALIDATION_FILE = HERE / "v62_2_matched_validation.json"


def _import_v62_base():
    path = HERE / "planetary_restoration_model_v62.py"
    spec = importlib.util.spec_from_file_location("planetary_restoration_model_v62_base", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import V62 base model from {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


base = _import_v62_base()


def _load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def _milestone_lookup(validation: Dict[str, Any], year: int) -> Dict[str, Any]:
    for row in validation["milestones"]:
        if int(row["year"]) == int(year):
            return row
    raise KeyError(f"Matched-forcing milestone {year} not found")


def matched_forcing_climate_update() -> Dict[str, Any]:
    v = _load_json(MATCHED_VALIDATION_FILE)
    if v["source_workflow"]["conclusion"] != "success":
        raise RuntimeError("V62.2 matched-forcing provenance is not green")
    if int(v["source_workflow"]["run_id"]) != MATCHED_RUN_ID:
        raise RuntimeError("V62.2 matched-forcing run ID mismatch")

    return {
        "classification": "EXTERNALLY_EXECUTED",
        "workflow_status": "ALL_GREEN",
        "workflow_run_id": MATCHED_RUN_ID,
        "workflow_run_number": MATCHED_RUN_NUMBER,
        "workflow_commit": MATCHED_COMMIT,
        "experiment": v["experiment"],
        "forcing_target": v["forcing_target"],
        "forcing_match_gates": copy.deepcopy(v["forcing_match_gates"]),
        "common_state_within_model_2026": copy.deepcopy(v["common_state_within_model_2026"]),
        "canonical_cdr_2026_2183_gtco2": v["canonical_cdr_2026_2183_gtco2"],
        "peak_cdr_2026_2183_gtco2_per_year": v["peak_cdr_2026_2183_gtco2_per_year"],
        "milestones": copy.deepcopy(v["milestones"]),
        "endpoints_2300": copy.deepcopy(v["endpoints_2300"]),
        "peak_temperature": copy.deepcopy(v["peak_temperature"]),
        "cross_model_finding": copy.deepcopy(v["cross_model_finding"]),
        "restoration_correction": copy.deepcopy(v["restoration_correction"]),
        "hector_diagnostic_note": copy.deepcopy(v["hector_diagnostic_note"]),
        "next_external_gates": copy.deepcopy(v["next_external_gates"]),
        "claim_boundary": (
            "This matched-forcing experiment validates only the paired climate-carbon response under the documented V62 trajectory. "
            "It does not validate the ecological, engineering, finance, governance, food, health, justice, robotics, or other human-flourishing modules."
        ),
    }


def _append_registry_modules(registry: List[Dict[str, str]]) -> List[Dict[str, str]]:
    out = copy.deepcopy(registry)
    existing = {row["module_id"] for row in out}
    additions = [
        {
            "module_id": "matched_forcing_cross_model",
            "domain": "Climate",
            "module": "FaIR/Hector matched-future-non-CO2 forcing paired attribution",
            "classification": "EXTERNALLY_EXECUTED",
        },
        {
            "module_id": "carbon_reservoir_decomposition",
            "domain": "Climate/Carbon Cycle",
            "module": "Land/ocean/permafrost reservoir decomposition of declining atmospheric CDR response",
            "classification": "OPEN_SCIENCE_GATE",
        },
        {
            "module_id": "oscar_matched_forcing",
            "domain": "Climate",
            "module": "OSCAR matched-future-non-CO2 forcing independent validation",
            "classification": "OPEN_SCIENCE_GATE",
        },
        {
            "module_id": "cdr_schedule_generality",
            "domain": "Climate/CDR",
            "module": "Alternative timing/rate schedules to test generality of long-horizon CDR response divergence",
            "classification": "OPEN_SCIENCE_GATE",
        },
    ]
    for row in additions:
        if row["module_id"] not in existing:
            out.append(row)
    return out


REQUIRED_MODULE_IDS = set(base.REQUIRED_MODULE_IDS) | {
    "matched_forcing_cross_model",
    "carbon_reservoir_decomposition",
    "oscar_matched_forcing",
    "cdr_schedule_generality",
}


def nature_candidate_findings(matched: Dict[str, Any]) -> List[Dict[str, Any]]:
    m2040 = _milestone_lookup(matched, 2040)
    m2100 = _milestone_lookup(matched, 2100)
    m2156 = _milestone_lookup(matched, 2156)
    m2184 = _milestone_lookup(matched, 2184)
    m2300 = _milestone_lookup(matched, 2300)
    return [
        {
            "finding": "Controlled two-model separation of atmospheric CDR efficacy on multi-century horizons",
            "status": "NATURE_CANDIDATE_REQUIRES_GENERALITY_TEST",
            "evidence": {
                "2040_fair_response_p50": m2040["fair_response_fraction_p50"],
                "2040_hector_response": m2040["hector_response_fraction"],
                "2100_fair_response_p50": m2100["fair_response_fraction_p50"],
                "2100_hector_response": m2100["hector_response_fraction"],
                "2156_hector_inside_fair_p05_p95": m2156["hector_inside_fair_p05_p95_fraction"],
                "2184_hector_inside_fair_p05_p95": m2184["hector_inside_fair_p05_p95_fraction"],
                "2300_fair_response_p50": m2300["fair_response_fraction_p50"],
                "2300_hector_response": m2300["hector_response_fraction"],
            },
            "interpretation": (
                "With future non-CO2 forcing harmonized, early-century response is close, while long-horizon response separates. "
                "The first listed milestone where Hector falls below FaIR's p05-p95 response range is 2184."
            ),
            "boundary": "Two models and one canonical CDR trajectory are insufficient to claim a universal threshold or law.",
        },
        {
            "finding": "Canonical CDR pathway strongly cools the long-run climate without restoring 280 ppm by 2300",
            "status": "ROBUST_MATCHED_TWO_MODEL_RESULT",
            "evidence": copy.deepcopy(matched["endpoints_2300"]),
            "interpretation": (
                "The canonical pathway produces roughly 0.93-1.02 degC less warming than removal-OFF at 2300, "
                "while removal-ON CO2 remains about 302 ppm in the FaIR median and about 310 ppm in Hector."
            ),
            "boundary": "This corrects earlier canonical-trajectory restoration timing; inverse 280-ppm target experiments remain separate controlled scenarios.",
        },
        {
            "finding": "Self-correction of prior restoration timing through independent climate-model execution",
            "status": "METHODOLOGICAL_STRENGTH_NOT_STANDALONE_DISCOVERY",
            "interpretation": (
                "V62.2 explicitly distinguishes screening/inverse target dates from independently executed outcomes of the canonical trajectory, "
                "preventing favorable internal screening dates from being presented as externally validated predictions."
            ),
        },
    ]


def run_v62_2() -> Dict[str, Any]:
    result = copy.deepcopy(base.run_v62())
    matched = matched_forcing_climate_update()

    result["model_version"] = MODEL_VERSION
    result["release_label"] = RELEASE_LABEL
    result["release_date"] = RELEASE_DATE
    result["classification"] = "COMPREHENSIVE_COUPLED_RESTORATION_FRAMEWORK_WITH_MATCHED_FORCING_EXTERNALLY_EXECUTED_CLIMATE_CORE"

    # Preserve all legacy/existing climate results, then add the newer matched-forcing experiment.
    result["climate_core"]["matched_forcing_run12"] = matched
    result["climate_core"]["matched_forcing_replaces_cross_model_nonco2_limitation"] = True

    result["headline"].update({
        "matched_forcing_run12_all_green": True,
        "matched_forcing_run_id": MATCHED_RUN_ID,
        "matched_forcing_commit": MATCHED_COMMIT,
        "canonical_cdr_2026_2183_gtco2": matched["canonical_cdr_2026_2183_gtco2"],
        "canonical_peak_cdr_gtco2_per_year": matched["peak_cdr_2026_2183_gtco2_per_year"],
        "canonical_trajectory_returns_to_280ppm_by_2300": False,
        "fair_2300_removal_on_median_co2_ppm": matched["endpoints_2300"]["FaIR"]["co2_on_p50_ppm"],
        "hector_2300_removal_on_co2_ppm": matched["endpoints_2300"]["Hector"]["co2_on_ppm"],
        "fair_2300_temperature_benefit_c": matched["endpoints_2300"]["FaIR"]["tas_difference_off_minus_on_c"],
        "hector_2300_temperature_benefit_c": matched["endpoints_2300"]["Hector"]["tas_difference_off_minus_on_c"],
        "first_listed_cross_model_response_range_exit_year": matched["cross_model_finding"]["first_listed_milestone_outside_fair_p05_p95"],
    })

    result["module_registry"] = _append_registry_modules(result["module_registry"])
    result["nature_candidate_findings"] = nature_candidate_findings(matched)

    # Explicitly preserve the comprehensive scope and stop climate validation from swallowing other domains.
    result["comprehensive_scope_lock"] = {
        "rule": "No revision may silently drop a registered domain. Every module must remain present or be explicitly deprecated with a reason and migration record.",
        "climate": True,
        "cryosphere_sea_level": True,
        "ocean_ph_acidification": True,
        "coral_reefs": True,
        "fisheries": True,
        "seaweed_food_habitat_carbon_fuels_grid_harvesting": True,
        "ocean_plastics": True,
        "eutrophication_nutrients": True,
        "blue_carbon": True,
        "cdr_portfolio": True,
        "forests_soils_wildfire_durable_wood": True,
        "food_hunger_meat_inclusive_diets": True,
        "water_desalination_reuse_wastewater": True,
        "universal_healthcare_vaccines_antibiotics_mrna_pipeline": True,
        "population_and_carrying_capacity": True,
        "education_housing_legal_access": True,
        "robot_doctors_robot_lawyers_robot_tutors_eldercare": True,
        "robot_construction_agriculture_ocean_cleanup_mrv": True,
        "energy_grid_tidal_transport_materials": True,
        "data_center_heat_reuse": True,
        "carbonite_stablecoin_proof_of_rent_tree_reserve_charity": True,
        "finance_governance_us_nonparticipation_bank_transition": True,
        "los_jardines_cella_eight_town_pilot": True,
        "africa_vulnerability_priority": True,
        "mrv_audit_chain": True,
    }

    old_gates = [g for g in result.get("open_science_gates", []) if "matched cross-model future non-CO2 forcing" not in g]
    result["open_science_gates"] = old_gates + [
        "Run OSCAR under the same matched-future-non-CO2 forcing protocol used for FaIR and Hector.",
        "Decompose land, ocean and permafrost carbon reservoirs to explain the declining atmospheric response fraction mechanistically.",
        "Repeat matched-forcing experiments across alternative CDR rates, timing and endpoint schedules to test whether the late-horizon divergence is general.",
        "Correct/rename the Hector raw FTOT tracking diagnostic so absolute-versus-relative forcing bookkeeping cannot be mistaken for a failed forcing match.",
    ]

    result["accounting_and_claim_rules"].extend([
        "The canonical pathway does not receive a 280-ppm restoration date unless an externally executed model actually reaches 280 ppm under that pathway.",
        "Inverse 280-ppm controls are reported as target-solving experiments, not as outcomes of the canonical CDR schedule.",
        "Matched FaIR/Hector climate validation does not upgrade any non-climate module's evidentiary classification.",
    ])

    return result


def completeness_check(result: Dict[str, Any]) -> Dict[str, Any]:
    ids = {r["module_id"] for r in result["module_registry"]}
    missing = sorted(REQUIRED_MODULE_IDS - ids)
    return {
        "required_count": len(REQUIRED_MODULE_IDS),
        "registry_count": len(ids),
        "missing": missing,
        "pass": not missing,
    }


def run_tests(result: Dict[str, Any]) -> None:
    # Run every inherited V62 test first: this is the anti-regression guard for the comprehensive model.
    base.run_tests(result)

    matched = result["climate_core"]["matched_forcing_run12"]
    assert matched["workflow_status"] == "ALL_GREEN"
    assert matched["workflow_run_id"] == MATCHED_RUN_ID
    assert matched["forcing_match_gates"]["fair_on_max_abs_wm2"] < 1e-7
    assert matched["forcing_match_gates"]["fair_off_max_abs_wm2"] < 1e-7
    assert matched["forcing_match_gates"]["hector_on_max_abs_wm2"] <= 1e-5
    assert matched["forcing_match_gates"]["hector_off_max_abs_wm2"] <= 1e-5
    assert result["headline"]["canonical_trajectory_returns_to_280ppm_by_2300"] is False
    assert 298.0 < result["headline"]["fair_2300_removal_on_median_co2_ppm"] < 306.0
    assert 305.0 < result["headline"]["hector_2300_removal_on_co2_ppm"] < 315.0
    assert result["headline"]["first_listed_cross_model_response_range_exit_year"] == 2184
    assert result["headline"]["fair_2300_temperature_benefit_c"] > 0.9
    assert result["headline"]["hector_2300_temperature_benefit_c"] > 0.9
    check = completeness_check(result)
    assert check["pass"], f"Missing V62.2 required modules: {check['missing']}"
    # Keep explicit checks for user-priority domains so a registry editing mistake cannot hide them.
    ids = {row["module_id"] for row in result["module_registry"]}
    for required in [
        "coral_reefs", "fisheries", "ocean_plastic_cleanup", "eutrophication",
        "seaweed_grid_harvesting", "seaweed_aviation_fuel", "seaweed_heavy_equipment_fuel",
        "hunger_elimination", "universal_healthcare", "vaccines_antibiotics",
        "mrna_cancer_vaccine_pipeline", "robot_doctors", "robot_lawyers",
        "population_scenarios", "desalination", "tidal_energy", "data_center_heat_reuse",
        "Carbonite_stablecoin", "Proof_of_Rent", "geotagged_tree_reserve",
        "restoration_charity", "US_nonparticipation_stress", "Los_Jardines_Cella",
    ]:
        assert required in ids, f"Priority comprehensive module missing: {required}"


def write_outputs(result: Dict[str, Any]) -> None:
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    result2 = copy.deepcopy(result)
    result2["legacy_preserved_architecture"] = {
        "location": "repository root (flattened runtime lineage)",
        "status": "FULL_LINEAGE_INCLUDED_IN_PACKAGE",
        "selected_integrations_present_in_main_result": True,
    }
    with (RESULTS_DIR / "planetary_restoration_v62_2_results.json").open("w", encoding="utf-8") as f:
        json.dump(result2, f, indent=2, ensure_ascii=False, allow_nan=False)
    pd.DataFrame(result["module_registry"]).to_csv(RESULTS_DIR / "v62_2_module_registry.csv", index=False)
    pd.DataFrame(result["restoration_milestones"]).to_csv(RESULTS_DIR / "v62_2_restoration_milestones.csv", index=False)
    pd.DataFrame(result["finance_governance"]["financeability_screen"]).to_csv(RESULTS_DIR / "v62_2_finance_stress.csv", index=False)
    pd.DataFrame(result["ai_robotics_services"]["robot_doctors"]["scenarios"]).to_csv(RESULTS_DIR / "v62_2_robot_doctor_scenarios.csv", index=False)
    pd.DataFrame(result["ai_robotics_services"]["robot_lawyers"]["scenarios"]).to_csv(RESULTS_DIR / "v62_2_robot_lawyer_scenarios.csv", index=False)
    pd.DataFrame(result["climate_core"]["matched_forcing_run12"]["milestones"]).to_csv(
        RESULTS_DIR / "v62_2_matched_forcing_cross_model_milestones.csv", index=False
    )
    with (RESULTS_DIR / "v62_2_completeness_gate.json").open("w", encoding="utf-8") as f:
        json.dump(completeness_check(result), f, indent=2)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tests", action="store_true")
    ap.add_argument("--no-write", action="store_true")
    args = ap.parse_args()
    result = run_v62_2()
    run_tests(result)
    if not args.no_write:
        write_outputs(result)
    if args.tests:
        c = completeness_check(result)
        print(f"V62.2 TESTS PASSED — {c['registry_count']} modules, {c['required_count']} mandatory completeness checks")
    print(json.dumps(result["headline"], indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
