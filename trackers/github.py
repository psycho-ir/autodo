from trackers.tracker import Tracker


class GithubIssueTracker(Tracker):
    def __init__(self, url):
        pass

    def create_issue(self, issue):
        super().create_issue(issue)

    def find_todo_issues(self):
        super().find_todo_issues()
