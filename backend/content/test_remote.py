from remote import app

def test_home():
  "test that the home page loads correctly"
  client = app.test_client()
  response = client.get("/")
  assert b"empty history" in response.data