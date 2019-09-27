from vending_machine import create_app

def test_config():
    """Test create_app with and without passing test config."""
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
