from random import *
import random

from data import subjects, objects, environments, famous_artists, locations, stylings, prepositions, adjectives, verbs, adverbs


def generatePrompt():
        x = randint(1, 100)

        if x < 33:
            class generation_v1:
                def __init__(self, subject, prepositions, environments, stylings):
                    self.subject = subject.lower()
                    self.prepositions = prepositions.lower()
                    self.environments = environments.lower()
                    self.stylings = stylings.lower()


                def prompt(self):
                    return f' {self.subject} in a {self.environments} {self.prepositions} {self.stylings}'

            a = random.choice(subjects)
            b = random.choice(prepositions)
            c = random.choice(environments)
            d = random.choice(stylings)

            myObject = generation_v1(a, b, c, d)
            print(myObject.prompt())
            return myObject.prompt()
            

        if x < 66:
            class generation_v2:
                def __init__(self, subjects, adverbs, verbs, preposition, locations, famous_artists):
                    self.subjects = subjects.lower()
                    self.adverbs = adverbs.lower()
                    self.verbs = verbs.lower()
                    self.prepositions = verbs.lower()
                    self.locations = locations.lower()
                    self.famous_artists = famous_artists.lower()

                def prompt(self):
                    return f' {self.subjects} {self.adverbs} {self.verbs} in a {self.locations} in {self.famous_artists} styling'
                
            a = random.choice(subjects)
            b = random.choice(adverbs)
            c = random.choice(verbs)
            d = random.choice(prepositions)
            e = random.choice(locations)
            f = random.choice(famous_artists)

            myObject = generation_v2(a, b, c, d, e, f)
            print(myObject.prompt())
            return myObject.prompt()

        if x < 99:
            class generation_v3:
                def __init__(self, stylings, prepositions, environments, adjectives, objects):
                    self.stylings = stylings.lower()
                    self.prepositions = prepositions.lower()
                    self.environments = environments.lower()
                    self.adjectives = adjectives.lower()
                    self.objects = objects.lower()

                def prompt(self):
                    return f' {self.stylings} {self.prepositions} {self.environments} with a {self.adjectives} {self.objects}'
            
            a = random.choice(stylings)
            b = random.choice(prepositions)
            c = random.choice(environments)
            d = random.choice(adjectives)
            e = random.choice(objects)

            myObject = generation_v3(a, b, c, d, e)
            print(myObject.prompt())
            return myObject.prompt()

        else:
            class generation_v4:
                def __init__(self, subjects, prepositions, adjectives, locations, famous_artists):
                    self.subjects = subjects.lower()
                    self.prepositions = prepositions.lower()
                    self.adjectives = adjectives.lower()
                    self.locations = locations.lower()
                    self.famous_artists = famous_artists.lower()

                def prompt(self):
                    return f' {self.subjects} {self.prepositions} a {self.subjects} in a {self.adjectives} {self.locations} in {self.famous_artists} styling'

            a = random.choice(subjects)
            b = random.choice(prepositions)
            c = random.choice(adjectives)
            d = random.choice(locations)
            e = random.choice(famous_artists)

            myObject = generation_v4(a, b, c, d, e)
            print(myObject.prompt())
            return myObject.prompt()
