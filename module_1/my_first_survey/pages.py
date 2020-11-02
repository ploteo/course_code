from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class CollectAge(Page):
    form_model = 'player'
    form_fields = ['age']

class Results(Page):
    def vars_for_template(self):
        return{
            'your_age':self.player.age
        }


page_sequence = [CollectAge, Results]
