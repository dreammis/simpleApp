from locust import Locust, TaskSet, task, HttpLocust
import json


def login(l):
    l.client.post("api/student/mobile/login/",
                  {"username": 'ycg', "password": "888888", "ostype": 3, "devicetoken": "student"
                   })
    # content = data.content
    # sessionid = json.loads(content)['sessionid']


def logout(l):
    l.client.post("api/student/mobile/logout/")


def index(l):
    l.client.get("api/student/mobile/tasks/?action=get_child_rank_by_grade&subjectid=1")


def uncorrect(l):
    l.client.get("api/student/stats/?correctstatus=1&create_before=1540483200&create_after=1543247999&action=m_getonesubjectfailedquestion&subjectid=1&page=0")

def correct(l):
    l.client.get("api/student/stats/?correctstatus=0&create_before=1540483200&create_after=1543247999&action=m_getonesubjectfailedquestion&subjectid=1&page=0")





class UserBehavior(TaskSet):
    tasks = {index: 2, uncorrect: 1, correct: 3}
    # tasks = {index: 1}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
