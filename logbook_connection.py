import requests
import json


class CommentBot:
    """Bot for working with student comments in logbook"""
    base_url = "https://logbook.itstep.org/"
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/79.0.3945.130 Safari/537.36 OPR/66.0.3515.115'
    }
    cookies = {}
    students = []

    def request(self, part_url, payload=None, method='POST'):
        """Unified method for sending requests to server"""
        s = requests.Session()
        resp = s.request(method, self.base_url + part_url, headers=self.headers, data=json.dumps(payload),
                         cookies=self.cookies)

        self.cookies = resp.cookies
        return resp.json(), resp.content

    def login(self, username: str, password: str):
        """Login to logbook"""
        payload = {
            "LoginForm": {
                "id_city": None,
                "username": username,
                "password": password
            }
        }
        error, data = self.request('auth/login', payload)
        if 'error' in error:
            print(error)
            return False
        else:
            return True

    def get_groups(self):
        """All available groups for account"""
        groups = []
        code, data = self.request('students/get-groups-list')
        data = json.loads(data, parse_int=int)
        for row in data:
            groups.append({'id': row['id_tgroups'], 'name': row['name_tgroups']})

        return groups

    def get_students_of_group(self, group_id: str):
        """Students for chosen group"""
        students = []
        payload = {"group": group_id}
        code, data = self.request('students/get-students-short', payload)
        data = json.loads(data)
        for row in data:
            students.append({'id': row['id_stud'], 'name': row['fio_stud']})
        return students

    def get_subjects_for_group(self, stud_id: str):
        """Subjects for student of chosen group"""
        subjects = []
        payload = {"stud": stud_id}
        code, data = self.request('students/get-specs', payload)
        data = json.loads(data)
        for row in data:
            subjects.append({'id': row['id_spec'], 'name': row['name_spec']})
        return subjects

    def get_student_comments(self, stud_id: str):
        """Comments for chosen student"""
        comments = []
        payload = {
            "stud": stud_id
        }
        code, data = self.request('students/get-comments', payload)
        data = json.loads(data)
        for row in data:
            comments.append({'teacher': row['fio_teach'], 'subject': row['name_spec'], 'comment': row['message']})

        return comments

    def get_students(self):
        """Help method. All available students for account"""
        code, data = self.request('students/get-students')
        data = json.loads(data)
        self.students.extend(data)

    def get_profile(self, stud_id: str):
        """Profile of chosen student"""
        profile = next((item for item in self.students if item["id_stud"] == stud_id), False)

        return profile

    def send_comment(self, group_id: str, stud_id: str, subj_id: int, comment: str):
        """Sending comment to server"""
        payload = {
            "group": group_id,
            "stud": stud_id,
            "spec": subj_id,
            "comment": comment
        }
        error, data = self.request('students/set-comment', payload)

        if 'success' in error:
            return True
        else:
            return False
