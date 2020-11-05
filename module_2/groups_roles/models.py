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


author = 'Matteo P.'

doc = """
Matching and roles:

Constant type and constant matching (CT/CM)
Varying type and constant matching (VT/CM)
Constant type and varying matching (CT/VM)
Varying type and varying matching (VT/VM)

Uncomment the desired mathing protocol
"""



############################################################
# 1) Constant Type and Constant Matching (CT/CM)
############################################################

# class Constants(BaseConstants):
#     name_in_url = 'groups_roles'
#     players_per_group = 2
#     num_rounds = 10
#     matching = "Constant Type and Constant Matching (CT/CM)"

# class Subsession(BaseSubsession):
#     def creating_session(self):
#         if self.round_number == 1: # this way we get a fixed role across repetitions
#             self.group_randomly()
#             print(self.get_group_matrix())
#             for g in self.get_groups():
#                 for p in g.get_players():
#                     if p.id_in_group % 2 == 0:
#                         p.type = 'BLUE'
#                         p.value = c(10) # assign the corresponding value
#                     else:
#                         p.type = 'GREEN'
#                         p.value = c(0)# assign the corresponding value
#         else:
#             self.group_like_round(1)
#             for g in self.get_groups():
#                 for p in g.get_players():
#                     p.type = p.in_round(self.round_number-1).type
#                     p.value= p.in_round(self.round_number-1).value
# #---------------------------------------------------------------------

# # print some information
#             print(self.round_number)
#             print(self.get_group_matrix())
#             for p in self.get_players():
#                 for i in p.in_previous_rounds():
#                     print(i.id_in_subsession,i.type)

# # To get values of the other in the group
#         for p in self.get_players():
#             for i in p.get_others_in_group():
#                 p.id_oth=i.id_in_subsession
#                 p.type_oth=i.type
#                 p.value_oth=i.value


############################################################
# END OF Constant type and constant matching (partner)
############################################################

############################################################
# 2) Varying Type and Constant Matching (VT/CM)
############################################################

# class Constants(BaseConstants):
#     name_in_url = 'groups_roles'
#     players_per_group = 2
#     num_rounds = 10
#     matching = " Varying Type and Constant Matching (VT/CM)"

# import random
# class Subsession(BaseSubsession):
#     def creating_session(self):
#         if self.round_number == 1: # this way we get a fixed role across repetitions
#             self.group_randomly()# built-in function
#             print(self.get_group_matrix())
#             rdm=random.randint(0, 1)
#             print(rdm)
#             for g in self.get_groups():
#                 for p in g.get_players():
#                     if rdm==1: #this way we randomize role accordin to id in group
#                         if p.id_in_group % 2 == 0:
#                             p.type = 'BLUE'
#                             p.value = c(10)# assign the corresponding value
#                         else:
#                             p.type = 'GREEN'
#                             p.value = c(0)   # assign the corresponding value
#                     else:
#                         if p.id_in_group % 2 == 0:
#                             p.type = 'GREEN'
#                             p.value = c(0)
#                         else:
#                             p.type = 'BLUE'
#                             p.value = c(10)
#         else:
#             self.group_like_round(1)
#             rdm=random.randint(0, 1)
#             print(rdm)
#             for g in self.get_groups():
#                 for p in g.get_players():
#                     if rdm==1: #this way we randomize role accordin to id in group
#                         if p.id_in_group % 2 == 0:
#                             p.type = 'BLUE'
#                             p.value = c(10)
#                         else:
#                             p.type = 'GREEN'
#                             p.value = c(0)
#                     else:
#                         if p.id_in_group % 2 == 0:
#                             p.type = 'GREEN'
#                             p.value = c(0)
#                         else:
#                             p.type = 'BLUE'
#                             p.value = c(10)
#             print(self.get_group_matrix())
# #---------------------------------------------------------------------

# # print some information (just a check)
#             print(self.round_number)
#             print(self.get_group_matrix())
#             for p in self.get_players():
#                 for i in p.in_previous_rounds():
#                     print(i.id_in_subsession, i.type)

# # To get values of the other in the group
#         for p in self.get_players():
#             for i in p.get_others_in_group():
#                 p.id_oth = i.id_in_subsession
#                 p.type_oth = i.type
#                 p.value_oth = i.value

############################################################
# END OF  Varying type and constant matching (partner)
############################################################

############################################################
# 3) Constant Type and Varying Matching (CT/VM)
############################################################

# class Constants(BaseConstants):
#     name_in_url = 'groups_roles'
#     players_per_group = 2
#     num_rounds = 10
#     matching = "Constant Type and Varying Matching (CT/VM)"

# class Subsession(BaseSubsession):
#     def creating_session(self):
#         self.group_randomly(fixed_id_in_group=True)# built-in function
#         print(self.get_group_matrix())
#         for g in self.get_groups():
#             for p in g.get_players():
#                 if p.id_in_group % 2 == 0:
#                     p.type = 'BLUE'
#                     p.value = c(10)
#                 else:
#                     p.type = 'GREEN'
#                     p.value = c(0)

# #To assign values in each round, the blue get 10 and the green get 0
#         for p in self.get_players():
#             if p.type == 'BLUE':
#                 p.value = c(10)
#             else:
#                 p.value = c(0)
# #---------------------------------------------------------------------

# # print some information (just a check)
#             print(self.round_number)
#             print(self.get_group_matrix())
#             for p in self.get_players():
#                 for i in p.in_previous_rounds():
#                     if self.round_number==Constants.num_rounds:
#                         print(i.id_in_subsession, i.type)

# # To get values of the other in the group
#         for p in self.get_players():
#             for i in p.get_others_in_group():
#                 p.id_oth = i.id_in_subsession
#                 p.type_oth = i.type
#                 p.value_oth = i.value


############################################################
# END Constant type and varying matching
############################################################

############################################################
# 4) Varying Type and Varying Matching (VT/VM)
############################################################

class Constants(BaseConstants):
    name_in_url = 'groups_roles'
    players_per_group = 2
    num_rounds = 10
    matching = "Varying Type and Varying Matching (VT/VM)"

import random
class Subsession(BaseSubsession):
    def creating_session(self):
        self.group_randomly()# built-in function
        rdm=random.randint(0, 1)
        print(rdm)
        for g in self.get_groups():
            for p in g.get_players():
                if rdm==1: #this way we randomize role according to id in group
                    if p.id_in_group % 2 == 0:
                        p.type = 'BLUE'
                        p.value = c(10)
                    else:
                        p.type = 'GREEN'
                        p.value = c(0)
                else:
                    if p.id_in_group % 2 == 0:
                        p.type = 'GREEN'
                        p.value = c(0)
                    else:
                        p.type = 'BLUE'
                        p.value = c(10)
        print(self.get_group_matrix())

#---------------------------------------------------------------------

# print some information (just a check)

        print(self.round_number)
        print(self.get_group_matrix())
        for p in self.get_players():
            for i in p.in_previous_rounds():
                print(i.id_in_subsession, i.type)

# To get values of the other in the group
        for p in self.get_players():
            for i in p.get_others_in_group():
                p.id_oth = i.id_in_subsession
                p.type_oth = i.type
                p.value_oth = i.value


############################################################
# END Varying type and varying matching
############################################################


class Group(BaseGroup):
    pass

# needed to store values 

class Player(BasePlayer):
    type = models.StringField()
    value = models.CurrencyField()
    id_oth = models.IntegerField()
    type_oth = models.StringField()
    value_oth = models.CurrencyField()

