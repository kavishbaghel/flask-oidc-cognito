from flask_oidc_ex.validation import validate_token

from python_jwt import generate_jwt, verify_jwt
from jwcrypto.jwk import JWK, JWKSet
import datetime

def test_validate_token():
  key = JWK.generate(kty='RSA', size=1024, kid='1234')
  
  payload = {'foo': 'bar', 'baz': 42}
  other_headers = { 'kid': key.key_id}
  
  token = generate_jwt(payload, key, 'RS256', datetime.timedelta(minutes=5), other_headers=other_headers)
  header, claims = verify_jwt(token, key, ['RS256'])
  
  assert header is not None
  assert claims is not None
  
  keyset = JWKSet()
  keyset.add(key)
  
  assert validate_token(keyset, token)
  