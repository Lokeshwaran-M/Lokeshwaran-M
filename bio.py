#!/usr/bin/python

import json


class Developer:

    def __init__(self):
        self.name = "Lokeshwaran M"
        self.nickname = "Loki"
        self.role = "Developer"
        self.lang_spoken = ["en_US", "tamil", "nihongo"]
        self.gmail = "lokeshwaran.m23072003@gmail.com"
        self.website = "https://lokesh-m.web.app/"
        self.github = "https://github.com/Lokeshwaran-M"
        self.linkedin = "https://www.linkedin.com/in/lokeshwaran-m/"
        self.instagram = "https://www.instagram.com/lokesh_m2003/"
        self.twitter = "https://twitter.com/lokesh_m2003"
        self.medium = "https://medium.com/@lokesh-m"
        self.dev = "https://dev.to/lokeshwaran_m"

    def to_json(self):
        data = {
            "username": self.name,
            "nickname": self.nickname,
            "role": self.role,
            **{key: getattr(self, key) for key in ["lang_spoken", "gmail", "website", "github", "linkedin", "instagram", "twitter", "medium", "dev"]}
        }
        return data

    def save_json(self, filename):
        json_data = self.to_json()
        with open(filename, "w") as json_file:
            json.dump(json_data, json_file, indent=2)

    def print_json(self):
        json_data = self.to_json()
        print(json.dumps(json_data, indent=2))


me = Developer()
me.save_json("developer.json")
me.print_json()
