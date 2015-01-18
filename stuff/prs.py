import random
import itertools

class Player(object):
    """Player"""
    _bot_counter = 0
    _gestures = ('rock', 'paper', 'scissors', 'spok', 'lizard')

    def __init__(self, human=True):
        self._human = human
        self._score = 0
        self._hand = None

        self._naming()
        
    def _naming(self):
        if self._human:
            self._name = raw_input('Enter name: ')
        else:
            self._name = 'Bot ' + str(Player._bot_counter)
            self._bot_counter += 1

    @staticmethod
    def number_of_gestures():
        return len(Player._gestures)
        
    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    @property
    def hand(self):
        return self._hand
    
    def throw(self):
        if self._human:
            items = list(enumerate(self._gestures))
            gesture = int(raw_input(
                '{}, choose one from {}: '.format(self.name, items)))
        else:
            gesture = random.randrange(0, len(self._gestures))
        self._hand = gesture, self._gestures[gesture]
    
    def update_score(self, value):
        self._score += value
    
    
class Game(object):
    """docstring for Game"""
    
    def __init__(self):
        self._players = []
        self._nmb = Player.number_of_gestures()
        self._run()
        
    def _run(self):
        ''' Entry point'''
        self._create_players()
        self._turn()
        
    def _create_players(self):
        ''' Interactive player creation'''
        counter = 0
        number_of_players = int(raw_input('Number of players: '))
        while counter < number_of_players:
            robot = raw_input('Player#' + str(counter) + ' is a robot? ')
            self._players.append(Player(robot.startswith('n')))
            counter += 1

    def _turn(self, again=True):

        while again:

            for player in self._players:
                player.throw()

            for i, j in itertools.combinations(self._players, 2):
                result = 0 if i.hand == j.hand \
                else (self._nmb + i.hand[0] - j.hand[0]) % self._nmb
                    
                message1 = '{name1}\'s {hand1} vs. {name2}\'s {hand2}\n'\
                            .format(name1=i.name, hand1=i.hand[1],
                                    name2=j.name, hand2=j.hand[1])
                
                if result:
                    if result == 2:
                        i, j = j, i

                    i.update_score(1)
                    j.update_score(-1)
                    message2 = 'winner is {name1}\n'.format(name1=i.name)
                else:
                    message2 = 'tie\n'

                print message1, message2

            again = raw_input('again? ') != 'n'
        for player in sorted(self._players,
                                key=lambda x: x.score,
                                reverse=True):
            print '{name}: {score}'.format(name=player.name,
                                            score=player.score)
game = Game()
