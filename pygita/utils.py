def generate_token(client_id, client_secret, grant_type='client_credentials', scope='verse chapter'):
    request = post('https://bhagavadgita.io/auth/oauth/token',
                   data={
                         'client_id': client_id,
                         'client_secret': client_secret,
                         'grant_type': grant_type,
                         'scope': scope,
                          })
    token = request.json()['access_token']
    os.environ['gita_access_token'] = token
    return token
