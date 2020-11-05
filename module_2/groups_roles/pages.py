from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    def vars_for_template(self):
        return{
            'round': self.round_number,
            'player_current_id': self.player.id_in_subsession,
            'player_current_type': self.player.type,
            'player_current_value': self.player.value,
            'player_current_id_oth': self.player.id_oth,
            'player_current_type_oth': self.player.type_oth,
            'player_current_value_oth': self.player.value_oth,
            }

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [MyPage]
