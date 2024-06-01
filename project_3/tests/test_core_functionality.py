def test_area_of_triangle(area_fixture) -> None:
    """
    Unit Test for Area of Triangle
    :return: None
    """
    expected_response = "The Area of the Triangle is `4.0` units"
    actual_response = area_fixture.area_of_triangle()
    assert actual_response == expected_response
