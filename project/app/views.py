from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass
from typing import Dict, List
from django.http import HttpRequest

@dataclass
class Team:
    name: str
    desc: str
    members: List[str]

teamdata: Dict[str, Team] = {
    "Management": Team(
        name="Management",
        desc="Manages chores such as, kitchen cleaning, taking out the trash, and sweeping, and chore schedules. ",
        members=['Chris','Tanner','Kilan','Aidan']
    ),
    "Procurement": Team(
        name='Procurement',
        desc='Procures food and any other items that may be needed for the building. Prepares lunch everyday for students.',
        members=['Markel','Aaron','Jacob','Arthur']
    ),
    'Community': Team(
        name='Community',
        desc='Plan events that bring people together, build lasting relationships, and promote engagement.',
        members=['Arianna','Peyton']
    ),
    'Documentation': Team(
        name='Documentation',
        desc='Documentation team is responsible for taking photos of guest speaker, community events , and unit projects after taking the pictures depending on the event happening in the photos determines which social media we post on we are also responsible for getting all the photos for the year book.',
        members=['Patrick','Jason']
    )
}

def teams(request: HttpRequest, team_name: str=None) -> HttpResponse:
    if team_name:
        team = teamdata.get(team_name)
        return render(request, "index.html", {'team': team})
    return render(request, 'index.html', {'teams': teamdata.keys})
    