from app import calculate_results

def test_calculate_results_with_grade():
    marks = [85, 90, 95]
    result = calculate_results(marks)
    assert result["total"] == 270
    assert result["average"] == 90.0
    assert result["grade"] == "A"

def test_failing_grade():
    marks = [50, 40, 55] 
    result = calculate_results(marks)
    assert result["grade"] == "F"
