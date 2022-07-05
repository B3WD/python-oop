# from player import Player
from project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players = []

    def get_player_names(self):
        return [p.name for p in self.players]

    def get_player_by_name(self, player_name) -> Player:
        for p in self.players:
            if p.name is player_name:
                return p

    def assign_player(self, player : Player):
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in self.get_player_names():
            return f"Player {player_name} is not in the guild."

        p_to_kick = self.get_player_by_name(player_name)
        p_to_kick.guild = "Unaffiliated"
        self.players.remove(p_to_kick)
        return f"Player {player_name} has been removed from the guild."
        
    def guild_info(self):
        name_msg = f"Guild: {self.name}\n"
        player_info_msg = [f"{p.player_info()}" for p in self.players]

        return name_msg + "".join(player_info_msg)