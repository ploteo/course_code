from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class Instructions(Page):
    form_model = 'player'
    form_fields = ['HL'] # the demo MPL

class PageHL(Page):
# which forms are needed from class player
    form_model = 'player'
    form_fields = ['HL_1','HL_2','HL_3','HL_4','HL_5','HL_6','HL_7','HL_8','HL_9','HL_10'] # all 10 options

    # values that are to be displayed (dictionary)
    def vars_for_template(self):
        # retrieve values from constants and store them in a dictionary
        return{
        'f1':Constants.f1,
        'f2':Constants.f2,
        'f3':Constants.f3,
        'f4':Constants.f4
        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method 
        self.player.set_payoff_HL()# see in models in Player class

class PageHL_2(Page):
    form_model = 'player'
    form_fields = ['HL_1','HL_2','HL_3','HL_4','HL_5','HL_6','HL_7','HL_8','HL_9','HL_10'] # all 10 options

    def vars_for_template(self):
        Lotteries = []
        for i in range(1,11):
            Lotteries.append([i,str(i)+"/10 of €"+str(Constants.f1), str(10-i)+"/10 of €"+str(Constants.f2),"", str(i)+"/10 of €"+str(Constants.f3), str(10-i)+"/10 of €"+str(Constants.f4)])
        return{
        'Lott': Lotteries
        }

    # before moving to next page, compute payoffs (avoids that with refreshing payoffs are recomputed again)
    def before_next_page(self):
        # built-in method 
        self.player.set_payoff_HL()# see in models in Player class

class OutcomeHL(Page):
# values needed to inform subjects about the actual outcome
    def vars_for_template(self):
        # retrieve values from participant.vars and store them in a dictionary
        return{
        'payoff_HL': self.participant.vars['payoff_HL'],#payoff
        'row': self.player.participant.vars['HL_row'], # randomly chosen row
        'value': self.participant.vars['HL_random'],# randomly chosen value to define outcome
        'choice': self.participant.vars['HL_choice'],# actual choice
        # outcomes of the selected row
        'p_A_1': self.participant.vars['HL_row'],
        'p_A_2': 10-self.participant.vars['HL_row'],
        'p_B_1': self.participant.vars['HL_row'],
        'p_B_2': 10-self.participant.vars['HL_row']
        }

class Anag(Page):
# forms to retrieve individual information
    form_model = 'player'
    form_fields = ['comment','like','sex','age']# plyaer.comment, player.like, ...


# the coreography of pages
page_sequence = [
                    Instructions,
                    PageHL,
                    OutcomeHL,
                    Anag
]
