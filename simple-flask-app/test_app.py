from simple-python-flask-app import home

# Sample test case
def test_home_page():
    response = home()
    assert response == "Welcome to the home page!"
