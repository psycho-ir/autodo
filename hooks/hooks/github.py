def parse(request):
    json_body = request.data
    commits = find_commits(json_body)
    pass


def find_commits(json_body):
    commits = json_body["commits"]
    print("commits are: {}".format(commits))

    return commits
