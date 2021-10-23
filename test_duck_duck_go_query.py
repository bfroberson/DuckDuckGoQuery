import pytest
import requests


# Querying the duckduckgo api and gathering the results
url = 'https://api.duckduckgo.com/?q=DuckDuckGo&format=json'
response = requests.get(url, params={'q': 'presidents of the united states'})
my_json = response.json()
related_topics = my_json['RelatedTopics']


@pytest.fixture
def presidents_list():
    presidents_list = [
        'Washington', 'Adams', 'Jefferson', 'Madison',
        'Monroe', 'Adams', 'Jackson', 'Buren',
        'Harrison', 'Tyler', 'Polk', 'Taylor',
        'Fillmore', 'Pierce', 'Buchanan', 'Lincoln',
        'Johnson', 'Grant', 'Hayes', 'Garfield',
        'Arthur', 'Cleveland', 'Harrison',
        'McKinley', 'Roosevelt', 'Taft', 'Wilson',
        'Harding', 'Coolidge', 'Hoover', 'Roosevelt',
        'Truman', 'Eisenhower', 'Kennedy', 'Johnson',
        'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush',
        'Clinton', 'Bush', 'Obama', 'Trump',
        'Biden'
    ]
    return presidents_list


@pytest.fixture
def presidents_results(presidents_list):
    presidents_results = []
    # Iterates through the results and places name into list
    # if it is in a predetermined list of presidents
    # then returns the list
    for data in related_topics:
        if data['Text'].split()[1] in presidents_list:
            presidents_results.append(data['Text'].split()[1])
        elif data['Text'].split()[2] in presidents_list:
            presidents_results.append(data['Text'].split()[2])
        elif data['Text'].split()[3] in presidents_list:
            presidents_results.append(data['Text'].split()[3])
    return presidents_results


# Should equal 45 since Grover Cleveland had 2 non-contiguous terms
def test_ddg_instant_results_presidents_length(presidents_results):
    assert len(presidents_results) == 45, "Not all presidents listed"


def test_ddg_instant_results_presidents_contents(presidents_list, presidents_results):
    assert sorted(presidents_results) == sorted(presidents_list), "Not all presidents listed"
