import requests
import json

class User:
    def __init__(self, username):
        self.username = username

class Task:
    def __init__(self, user, firmid, filemd5):
        self.user = user
        self.firmid = firmid
        self.filemd5 = filemd5

    def create_scan(self, payload):
        url = "https://api.shambles.cloud:10081/submit"
        data = {
            "filemd5": self.filemd5,
            "firmware": self.firmid,
            "text": payload,
            "username": self.user.username,
        }
        req = requests.post(url, data=data)
        return req.content

    def get_status(self):
        url = "https://api.shambles.cloud:10081/getbinql"
        data = {
            "filemd5": self.filemd5,
            "firmware": self.firmid,
            "username": self.user.username,
        }
        req = requests.post(url, data=data)
        while "finished" not in req.content:
            req = requests.post(url, data=data)
        return req.content

if __name__ == "__main__":
    pass