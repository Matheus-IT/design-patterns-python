def auto_responder(problem):
    if problem == 'simple':
        return 'solved by auto_responder'
    return live_operator(problem)


def live_operator(problem):
    if problem == 'medium':
        return 'solved by live_operator'
    return tech_engineer(problem)


def tech_engineer(problem):
    if problem == 'geek level':
        return 'solved by tech engineer'
    return 'could not be handled :('


def main():
    my_problem = 'dafasdf'
    result = auto_responder(my_problem)
    print(f'\n{result}\n')


if __name__ == '__main__':
    main()
