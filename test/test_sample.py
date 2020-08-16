def inc(x):
    return x + 1


def test_answer1():
    assert inc(3) == 5


def upper_case(x):
	return x.upper()


def test_answer2():
	assert upper_case('software') == 'SOFTWARE'


def check_length(x):
	return len(x)


def test_answer3():
	return check_length('abc') == 3

	
