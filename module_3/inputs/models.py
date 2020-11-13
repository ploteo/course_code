from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

import random

author = 'Matteo P.'

doc = """
A review of input formats
"""


class Constants(BaseConstants):
    name_in_url = 'inputs'
    players_per_group = None
    num_rounds = 1



class Subsession(BaseSubsession):
    def creating_session(self):
        display_value=random.randint(1, 9)# this value will be diplayed
        print(display_value)
        for p in Subsession.get_players(self):
            p.display_value=display_value

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    display_value=models.IntegerField()

    # a simple radio button with two options (ordinal)
    input_radio = models.CharField(
        choices=['Odd', 'Even'],
        widget=widgets.RadioSelect)

    input_button = models.CharField()

    input_checker = models.CharField(
    choices=[
    ["Even", 'Yes'],
    ["Odd", 'No']
    ],
    widget=widgets.RadioSelectHorizontal, label="Is the number even?")

    input_dropdown = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8, 9]
    )

    input_radiosequence = models.IntegerField(
    choices=[1, 2, 3, 4, 5, 6, 7, 8, 9],
    widget=widgets.RadioSelectHorizontal
    )

    input_value = models.IntegerField(min=1, max=9)

    input_text = models.CharField()

    tab_1 = models.BooleanField(blank=True)
    tab_2 = models.BooleanField(blank=True)
    tab_3 = models.BooleanField(blank=True)
    tab_4 = models.BooleanField(blank=True)
    tab_5 = models.BooleanField(blank=True)
    tab_6 = models.BooleanField(blank=True)
    tab_7 = models.BooleanField(blank=True)
    tab_8 = models.BooleanField(blank=True)
    tab_9 = models.BooleanField(blank=True)

    input_slider = models.IntegerField(min=1, max=9)