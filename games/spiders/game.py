# Generated by Creer at 11:41PM on April 07, 2016 UTC, git hash: 'e7ec4e35c89d7556b9e07d4331ac34052ac011bd'
# This is a simple class to represent the Game object in the game. You can extend it by adding utility functions here in this file.

from joueur.base_game import BaseGame

# import game objects
from games.spiders.brood_mother import BroodMother
from games.spiders.cutter import Cutter
from games.spiders.game_object import GameObject
from games.spiders.nest import Nest
from games.spiders.player import Player
from games.spiders.spider import Spider
from games.spiders.spiderling import Spiderling
from games.spiders.spitter import Spitter
from games.spiders.weaver import Weaver
from games.spiders.web import Web

# <<-- Creer-Merge: imports -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
# you can add addtional import(s) here
# <<-- /Creer-Merge: imports -->>

class Game(BaseGame):
    """The class representing the Game in the Spiders game.

    There's an infestation of enemy spiders challenging your queen broodmother spider! Protect her and attack the other broodmother in this turn based, node based, game.
    """

    def __init__(self):
        """Initializes a Game with basic logic as provided by the Creer code generator."""
        BaseGame.__init__(self)

        # private attributes to hold the properties so they appear read only
        self._current_player = None
        self._current_turn = 0
        self._game_objects = {}
        self._max_turns = 100
        self._nests = []
        self._players = []
        self._session = ""
        self._webs = []

        self.name = "Spiders"

        self._game_object_classes = {
            'BroodMother': BroodMother,
            'Cutter': Cutter,
            'GameObject': GameObject,
            'Nest': Nest,
            'Player': Player,
            'Spider': Spider,
            'Spiderling': Spiderling,
            'Spitter': Spitter,
            'Weaver': Weaver,
            'Web': Web
        }


    @property
    def current_player(self):
        """The player whose turn it is currently. That player can send commands. Other players cannot.

        :rtype: Player
        """
        return self._current_player


    @property
    def current_turn(self):
        """The current turn number, starting at 0 for the first player's turn.

        :rtype: int
        """
        return self._current_turn


    @property
    def game_objects(self):
        """A mapping of every game object's ID to the actual game object. Primarily used by the server and client to easily refer to the game objects via ID.

        :rtype: dict[str, GameObject]
        """
        return self._game_objects


    @property
    def max_turns(self):
        """The maximum number of turns before the game will automatically end.

        :rtype: int
        """
        return self._max_turns


    @property
    def nests(self):
        """Every Nest in the game.

        :rtype: list[Nest]
        """
        return self._nests


    @property
    def players(self):
        """List of all the players in the game.

        :rtype: list[Player]
        """
        return self._players


    @property
    def session(self):
        """A unique identifier for the game instance that is being played.

        :rtype: str
        """
        return self._session


    @property
    def webs(self):
        """Every Web in the game.

        :rtype: list[Web]
        """
        return self._webs



    # <<-- Creer-Merge: functions -->> - Code you add between this comment and the end comment will be preserved between Creer re-runs.
    # if you want to add any client side logic (such as state checking functions) this is where you can add them
    # <<-- /Creer-Merge: functions -->>