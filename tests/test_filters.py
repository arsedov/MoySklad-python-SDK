from moysklad.utils.filters import Filter

def test_filter_builder():
    f = Filter().eq("name", "Test").gt("sum", 100).contains("code", "abc")
    assert str(f) == "name=Test;sum>100;code~abc"

def test_filter_bool():
    f = Filter().eq("archived", False)
    assert str(f) == "archived=false"
