from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Radio(Page):
    form_model = 'player'
    form_fields = ['input_radio']

class Button(Page):
    form_model = 'player'
    form_fields = ['input_button']

class Checker(Page):
    form_model = 'player'
    form_fields = ['input_checker']

class Dropdown(Page):
    form_model = 'player'
    form_fields = ['input_dropdown']

class RadioSequence(Page):
    form_model = 'player'
    form_fields = ['input_radiosequence']

class Text(Page):
    form_model = 'player'
    form_fields = ['input_text']

class Value(Page):
    form_model = 'player'
    form_fields = ['input_value']

class Tabular(Page):
    form_model = 'player'
    form_fields = ['tab_1','tab_2','tab_3','tab_4','tab_5','tab_6','tab_7','tab_8','tab_9']

class Slider(Page):
    form_model = 'player'
    form_fields = ['input_slider']

class Slider_2(Page):
    form_model = 'player'
    form_fields = ['input_slider']

class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [Radio, Button, Checker, Dropdown, RadioSequence, Text, Value, Tabular, Slider, Slider_2,]
