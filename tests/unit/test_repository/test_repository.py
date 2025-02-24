import pytest
from unittest.mock import patch, Mock
from punkapi.repository.repository import random_beer, beer, beers, beers_size

# Create a larger mock dataset
MOCK_BEERS = [
    {"id": i, "name": f"Beer {i}", "abv": 4.0 + (i * 0.5)} 
    for i in range(1, 31)  # 30 beers with increasing ABV
]

@pytest.fixture
def mock_db():
    with patch('punkapi.repository.repository.full_db', MOCK_BEERS):
        with patch('punkapi.repository.repository.sorted_db', MOCK_BEERS):
            yield MOCK_BEERS

def test_random_beer():
    # Test that random_beer returns a dictionary
    result = random_beer()
    assert isinstance(result, dict)
    assert "id" in result
    assert "name" in result

def test_beer_by_id():
    # Test getting existing beer
    result = beer(1)
    assert isinstance(result, dict)
    assert result["id"] == 1
    assert "name" in result

    # Test getting non-existent beer
    result = beer(9999)
    assert result is None

def test_beers_with_no_options():
    # Test getting all beers without options
    result = beers()
    assert isinstance(result, list)
    assert len(result) > 0
    assert all(isinstance(beer, dict) for beer in result)

def test_beers_with_pagination(mock_db):
    # Update the mock path to match the actual import
    with patch('punkapi.repository.repository.get_beers_with_options') as mock_get:
        options = {"page": 1, "per_page": 10}
        mock_get.return_value = MOCK_BEERS[:10]
        result = beers(options)
        assert len(result) == 10
        mock_get.assert_called_once_with(MOCK_BEERS, options)

def test_beers_with_filters(mock_db):
    with patch('punkapi.repository.repository.get_beers_with_options') as mock_get:
        options = {
            "page": 1, 
            "per_page": 10,
            "abv_gt": 5
        }
        filtered_beers = [b for b in MOCK_BEERS if b["abv"] > 5][:10]
        mock_get.return_value = filtered_beers
        result = beers(options)
        assert len(result) == len(filtered_beers)
        assert all(beer["abv"] > 5 for beer in result)
        mock_get.assert_called_once_with(MOCK_BEERS, options)

def test_beers_multiple_pages(mock_db):
    with patch('punkapi.repository.repository.get_beers_with_options') as mock_get:
        mock_get.return_value = MOCK_BEERS[10:20]
        page2 = beers({"page": 2, "per_page": 10})
        assert len(page2) == 10
        assert page2[0]["id"] != MOCK_BEERS[0]["id"]
        mock_get.assert_called_once_with(MOCK_BEERS, {"page": 2, "per_page": 10})

def test_beers_with_filters_no_pagination(mock_db):
    with patch('punkapi.repository.repository.get_beers_with_options') as mock_get:
        options = {"abv_gt": 5}
        filtered_beers = [b for b in MOCK_BEERS if b["abv"] > 5]
        mock_get.return_value = filtered_beers
        result = beers(options)
        assert all(beer["abv"] > 5 for beer in result)
        mock_get.assert_called_once_with(MOCK_BEERS, options)

def test_beers_size(mock_db):
    result = beers_size()
    assert result == 30  # Now we know exactly how many mock beers we have