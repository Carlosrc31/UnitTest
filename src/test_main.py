from main import rides, file_html

def test_rides():
    assert rides() != None and len(rides()) > 0

def test_file_html():
    assert file_html() == True 