#!/usr/bin/python
# -*- coding: utf-8 -*-
from requests import post
import os


# Authentication from access_token
def auth_token(token):
    os.environ['gita_access_token'] = token


# Authentication from client_id and client_secret
def auth(client_id, client_secret):
    request = post('https://bhagavadgita.io/auth/oauth/token',
                   data={
                         'client_id': client_id,
                         'client_secret': client_secret,
                         'grant_type': 'client_credentials',
                         'scope': 'verse chapter',
                          })
    token = request.json()['access_token']
    os.environ['gita_access_token'] = token
    return 'You are authenticated by the generated token ' + token
