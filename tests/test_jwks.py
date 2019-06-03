from flask_oidc_ex.jwks import retrieve_jwks
from jose import jwk

op_url = 'https://accounts.google.com/'

def test_can_retrieve_jwks_from_google():
  jwks = retrieve_jwks(op_url)
  print(jwks)
  rsa_jwk = jwk.construct(jwks['2c3fac16b73fc848d426d5a225ac82bc1c02aefd'])
  print(rsa_jwk)
  assert jwks is not None 
