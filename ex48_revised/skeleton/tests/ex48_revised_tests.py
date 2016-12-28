from nose.tools import *
from ex48_revised import lexicon

def test_directions():

	assert_equal(lexicon.scan('north'), [('direction', 'north')])

def test_multiple_directions():
	result = lexicon.scan('north west south east')
	assert_equal(result, [('direction', 'north'),
							('direction', 'west'),
							('direction', 'south'),
							('direction', 'east')])

def test_verbs():
	assert_equal(lexicon.scan("go"), [('verb', 'go')])
	result = lexicon.scan("go kill leave eat")
	assert_equal(result, [('verb', 'go'),
							('verb', 'kill'),
							('verb', 'leave'),
							('verb', 'eat')])

def test_stops():
	assert_equal(lexicon.scan('the'), [('stop', 'the')])
	result = lexicon.scan("the in out of")
	assert_equal(result, [('stop', 'the'),
							('stop', 'in'),
							('stop', 'out'),
							('stop', 'of')])

def test_noun():
	assert_equal(lexicon.scan("bear"), [('noun', 'bear')])
	result = lexicon.scan("bear princess")
	assert_equal(result, [("noun", "bear"),
							("noun", "princess")])

def test_numbers():
	assert_equal(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("3 91234")
	assert_equal(result, [('number', 3),
							('number', 91234)])


def test_errors():
	assert_equal(lexicon.scan("ASDFADFASDF"), [('error', 'ASDFADFASDF')])
	result = lexicon.scan("bear IAS princess")
	assert_equal(result, [('noun', 'bear'),
							('error', 'IAS'),
							('noun', 'princess')])