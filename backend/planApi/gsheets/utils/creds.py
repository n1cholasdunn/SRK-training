from decouple import config  # type:ignore


PROJECT_ID = config("GOOGLE_PROJECT_ID")
PRIVATE_KEY_ID = config("SERVICE_PRIVATE_KEY_ID")
PRIVATE_KEY = config("SERVICE_PRIVATE_KEY").replace(r"\n", "\n")
CLIENT_EMAIL = config("SERVICE_CLIENT_EMAIL")
CLIENT_ID = config("SERVICE_CLIENT_ID")
CLIENT_X509_CERT_URL = config("GOOGLE_CLIENT_X509_CERT_URL")


credentials = {
    "type": "service_account",
    "project_id": PROJECT_ID,
    "private_key_id": PRIVATE_KEY_ID,
    "private_key": PRIVATE_KEY,
    "client_email": CLIENT_EMAIL,
    "client_id": CLIENT_ID,
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": CLIENT_X509_CERT_URL,
    "universe_domain": "googleapis.com",
}
