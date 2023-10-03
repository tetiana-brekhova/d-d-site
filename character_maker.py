import random

class Character:
    def __int__(self, name, age, sex):
        race = ""
        # class_ = character_class
        name = name
        age = age
        sex = sex

    def race_selector(self, race:str):
        self.race = race
# Tiny: shorter than 2 feet.
# Small: between 2 & 4 feet.
# Medium: between 4 & 8 feet.
# Large: between 8 & 15 feet.
# Huge: between 15 & 30 feet.
# Gargantuan: taller than 30 feet.


# <div class="collapse navbar-collapse" >
#       <ul class="navbar-nav">
#         {% if user.is_authenticated %}
# <!--          <li class="nav-item p-2 offset-lg-7">-->
# <!--            <a class="nav-link text-light" href="{{ '/auth/profile/' }}">My profile</a>-->
# <!--          </li>-->
#           <li class="nav-item p-2 offset-lg-7">
#             <a class="nav-link text-light" href="{{ '/auth/logout/' }}">Logout</a>
#           </li>
#         {% else %}
#           <li class="nav-item ">
#             <a class="nav-link text-light" href="{{ '/auth/login/' }}">Login</a>
#           </li>
#           <li>
#             <p>|</p>
#           </li>
#           <li>
#             <a class="nav-link text-light" href="{{ '/auth/registration/' }}">LogUp</a>
#           </li>
#         {% endif %}
#       </ul>
#     </div>