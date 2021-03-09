import aiohttp
import subprocess
from graphqlclient import GraphQLClient
from .ext import query_format as Q
from .classes import User
import json
from mergedeep import merge


class PronoteAPIError(Exception):
    pass


class Connexion:
    @staticmethod
    async def login(username: str = None, password: str = None, url: str = None, ent: str = None,
                    query: list[Q] = None) -> User:
        """
        Start a connexion with Pronote, and grab the token.
        :type query: object Q
        :param username: : Pronote/ENT username
        :param password: : Pronote/ENT password
        :param url: : Pronote link
        :param ent: : (optional) ENT Name (could be found here: https://github.com/Litarvan/pronote-api#comptes-région-supportés )
        """

        if query is None:
            query = Q.all

        subprocess.Popen(["pronote-api-server"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        body = {
            "url": url,
            "username": username,
            "password": password
        }

        if ent:
            body |= {"cas": ent}

        async with aiohttp.ClientSession() as client:
            async with client.post("http://127.0.0.1:21727/auth/login",
                                   headers={'Content-Type': 'application/json'},
                                   json=body) as resp:
                # noinspection PyTypeChecker
                token = json.loads(await resp.text())
                print(token)
                if "token" not in token.keys():
                    raise PronoteAPIError("Could not log in with given credentials ")

        client = GraphQLClient("http://127.0.0.1:21727/graphql")
        client.inject_token(token["token"], "Token")

        data = json.loads(client.execute(query))
        data = data["data"]

        data = merge(Q.base, data)

        return User(data, token["token"])
