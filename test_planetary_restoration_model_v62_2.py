import planetary_restoration_model_v62_2 as model


def test_v62_2_comprehensive_model():
    result = model.run_v62_2()
    model.run_tests(result)
    gate = model.completeness_check(result)
    assert gate["pass"]
    assert result["model_version"] == "62.2"
