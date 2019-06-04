from flask_oidc_ex.jwks import retrieve_jwks

op_url = 'https://accounts.google.com/'

def test_can_retrieve_jwks_from_google():
  jwkset = retrieve_jwks(op_url)
  assert jwkset is not None
  