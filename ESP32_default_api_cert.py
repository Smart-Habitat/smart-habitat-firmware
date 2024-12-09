import json
import datetime
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa, ec
from binascii import b2a_base64
import ipaddress

# os.chdir('/home/meghadeep/GitHub/tower-device/lambda-issue-device-certs')
# Import CA Key
with open('certs/sh_ca.key', 'rb') as root_key_file:
    root_key = serialization.load_pem_private_key(
        root_key_file.read(),
        password=None,
    )
# Import CA Cert
with open('certs/sh_ca.pem', 'rb') as root_cert_file:
    root_cert = x509.load_pem_x509_certificate(
        root_cert_file.read()
    )
# Create new default API cert
try:
    # Create new device cert key
    cert_key = ec.generate_private_key(ec.SECP521R1())
    # Create new device cert subject
    device_subject = x509.Name([
        # x509.NameAttribute(NameOID.COUNTRY_NAME, 'US'),
        # x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, 'WY'),
        # x509.NameAttribute(NameOID.LOCALITY_NAME, 'Sheridan'),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, 'Smart Habitat'),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, 'Local API'),
        x509.NameAttribute(NameOID.COMMON_NAME, 'smart-habitat.local'),
    ])
    cert = x509.CertificateBuilder().subject_name(
        device_subject
    ).add_extension(
        x509.SubjectAlternativeName([x509.IPAddress(ipaddress.ip_address('192.168.4.1'))]),
        critical=False
    ).issuer_name(
        root_cert.issuer
    ).public_key(
        cert_key.public_key()
    ).serial_number(
        x509.random_serial_number()
    ).not_valid_before(
        datetime.datetime.utcnow()
    ).not_valid_after(
    datetime.datetime.utcnow() + datetime.timedelta(days=360)
    ).sign(root_key, hashes.SHA256())
    # return restapi cert
    payload = {'base64_DER_cert': b2a_base64(cert.public_bytes(serialization.Encoding.DER)).decode().strip(),'base64_DER_key': b2a_base64(cert_key.private_bytes(serialization.Encoding.DER, serialization.PrivateFormat.TraditionalOpenSSL, serialization.NoEncryption())).decode().strip()}
    with open('ports/esp32/modules/default_api_cert.py', 'w') as default_cert_file:
        default_cert_file.write('#### COPYRIGHT SMART HABITAT ####\n## LICENSED UNDER AGPL-3.0 ##\n#### COPYRIGHT SMART HABITAT ####\n\nbase64_cert_and_key = '+json.dumps(payload))
    with open('ports/esp32/modules/default_api_cert.py') as default_cert_file:
        print(default_cert_file.read())
except Exception as e:
    print(e)
