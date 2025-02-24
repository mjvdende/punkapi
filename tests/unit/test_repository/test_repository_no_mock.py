import pytest
from punkapi.repository.repository import random_beer, beer, beers, beers_size

def test_beers_with_pagination():
    # Test pagination
    options = {"page": 1, "per_page": 10}
    result = beers(options)
    assert len(result) == 10, f"Expected 10 beers, got {len(result)}"

    # Test second page returns different beers
    page2 = beers({"page": 2, "per_page": 10})
    assert len(page2) == 10
    assert page2[0]["id"] != result[0]["id"], "Second page should return different beers"

def test_beers_with_filters():
    # Test ABV filter
    options = {"abv_gt": 5}
    result = beers(options)
    assert all(beer["abv"] > 5 for beer in result), "All beers should have ABV > 5"
    
    # Test ABV filter with pagination
    options = {"abv_gt": 5, "page": 1, "per_page": 10}
    result = beers(options)
    assert len(result) <= 10, f"Expected max 10 beers, got {len(result)}"
    assert all(beer["abv"] > 5 for beer in result), "All beers should have ABV > 5"

def test_total_beers_count():
    # Get total number of beers
    total = beers_size()
    print(f"Total beers in database: {total}")
    
    # Get all pages
    per_page = 10
    page1 = beers({"page": 1, "per_page": per_page})
    page2 = beers({"page": 2, "per_page": per_page})
    
    print(f"Page 1 size: {len(page1)}")
    print(f"Page 2 size: {len(page2)}")
    
    assert len(page1) == per_page, f"First page should have {per_page} beers"
    assert len(page2) == per_page, f"Second page should have {per_page} beers"