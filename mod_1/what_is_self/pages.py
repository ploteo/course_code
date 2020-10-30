from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Results(Page):
    def vars_for_template(self):
        return{
            'round':self.round_number,
            'player_object':self.player,
            'player_session': self.player.session,
            'player_subsession': self.player.subsession,
            'player_group': self.player.group,
            'player_participant': self.player.participant,
            'player_session_config': self.player.session.config,
            'player_object_previous': self.player.in_previous_rounds()
        }

page_sequence = [Results]
