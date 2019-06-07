from flask_oidc_ex.jwks import retrieve_jwks
import certifi
from httplib2 import Http

op_url = 'https://accounts.google.com/'

def http_factory_ssl_cert_validation_disabled():
  return Http(ca_certs="/etc/pki/tls/certs/ca-bundle.crt")

def test_can_retrieve_jwks_from_google():
  jwkset = retrieve_jwks(op_url, http_factory_ssl_cert_validation_disabled)
  assert jwkset is not None
