from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'M. Ploner'

doc = """
    MPL risk elicitation à la Holt&Laury
"""

import random

class Constants(BaseConstants):
    name_in_url = 'MPL'
    players_per_group = None
    num_rounds = 1
    # these are the lottery payoffs, f1 and f2 refer to lottery A and f3 and f4 to lottery B
    f1 = 2.00
    f2 = 1.60
    f3 = 3.85
    f4 = 0.10

class Group(BaseGroup):
    pass

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):

    # This is for main choices, each variable is one row in the choice table MPL
    HL_1 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_2 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_3 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_4 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_5 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_6 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_7 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_8 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_9 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)
    HL_10 = models.PositiveIntegerField(choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)

    # This is needed for the instructions
    HL = models.PositiveIntegerField(blank=True,choices=[[1, 'A'],[2, 'B']],widget=widgets.RadioSelectHorizontal)

    # These variables are collected in the final questionnaire
    sex = models.StringField(widget=widgets.RadioSelectHorizontal(),choices=['Male', 'Female'])
    age = models.IntegerField(choices = range(18,60,1))
    comment = models.TextField(label="Your comment here:")
    like = models.IntegerField(choices=[1,2,3,4,5],widget=widgets.RadioSelectHorizontal)

    # Define here the methods associated to Players
    # this method is needed to compute payoffs
    def set_payoff_HL(self):
        #*******************************************
        # select random row and random outcome
        #*******************************************
        self.participant.vars['HL_row'] = random.randint(1,10)
        # select one row randomly for payment (from module random)
        self.participant.vars['HL_random'] = random.randint(1,10)
        # select the number x that defines the outcome of the lottery (if x<=p, outcome is left f1 or f3, otherwise f2 or f4)
        # write it to participant.vars['HL_random']

        #*******************************************
        # select choices in correspondence to random row
        #*******************************************
        choices = [self.HL_1,self.HL_2,self.HL_3,self.HL_4,self.HL_5,self.HL_6,self.HL_7,self.HL_8,self.HL_9,self.HL_10]
        # create a list with all choices of the player (see self)
        self.participant.vars['HL_choice'] = choices[self.participant.vars['HL_row']-1]
        # select from the list the choice in correspondence to the randomly drawn row (notice the offset)
        # write it to participant.vars['HL_choice']

        #*******************************************
        # Compute here the payoffs
        #*******************************************
        if self.participant.vars['HL_random'] <= self.participant.vars['HL_row']:
        # if the random number is smaller equal than the random row
            if self.participant.vars['HL_choice'] == 1: #A
            # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.f1
                # because HL_row is the same as p in the MPL
            else :
            # if the choice was B
                self.participant.vars['payoff_HL'] = Constants.f3
        else:
        # if the random number is slarger than the random row
            if self.participant.vars['HL_choice'] == 1 :#A
                # if the choice was A
                self.participant.vars['payoff_HL'] = Constants.f2
                # because HL_row is the same as p in the MPL
            else :
                self.participant.vars['payoff_HL'] = Constants.f4

        self.payoff = self.participant.vars['payoff_HL']
        # write the payoff to player.payoff
