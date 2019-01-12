import re

str_nightwatch = "Night gathers, and now my watch begins. It shall not end until my death. I shall take no wife, hold no lands, father no children. I shall wear no crowns and win no glory. I shall live and die at my post. I am the sword in the darkness. I am the watcher on the walls. I am the fire that burns against cold, the light that brings the dawn, the horn that wakes the sleepers, the shield that guards the realms of men. I pledge my life and honor to the Night's Watch, for this night and all the nights to come."
pattern = re.compile(r"\w+")

str_list = pattern.findall(str_nightwatch)
for token in str_list:
    print(token)

pattern1 = re.compile(r"\W+")
str_list1 = pattern1.split(str_nightwatch)
for token in str_list1:
    print(token)