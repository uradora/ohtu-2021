from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsecontent = toml.loads(content, _dict=dict)
        name = parsecontent.get('tool').get('poetry').get('name')
        desc = parsecontent.get('tool').get('poetry').get('description')
        deps = parsecontent.get('tool').get('poetry').get('dependencies').keys()
        devdeps = parsecontent.get('tool').get('poetry').get('dev-dependencies').keys()
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, deps, devdeps)
