"""This a sports team management program using FastAPI"""

from fastapi import FastAPI
from pydantic import BaseModel


class Player(BaseModel):
    """This class is player details class"""
    player_name: str
    role: str
    age: int


app = FastAPI()

cricket_team = {}


@app.get("/players_list")
async def get_list():
    """This function gives product list added"""
    return {"Team": cricket_team}


@app.post("/add_player/{player_id}")
def add_player(player_id: str, player: Player):
    """This function adds players in cricket team."""
    if player_id in cricket_team:
        return "Player already exists"
    if player.age <= 0:
        return "Enter valid age"
    cricket_team[player_id] = player.dict()
    return {"Team": cricket_team}


@app.put("/update_player/{player_id}")
def update_player(player_id: str, player: Player):
    """This is for updating the available product list"""
    if player_id not in cricket_team:
        return "Player not found"
    if player.age <= 0:
        return "Enter valid amount/quantity"
    cricket_team.update({
        player_id: player.dict()
    })
    return "Updated Successfully"


@app.get("/no_of_players")
def get_count():
    """This gives the total amount of items in product list"""
    return {"Number of players in Team ": len(cricket_team.items())}


@app.delete("/delete_player/{player_id}")
def delete_player(player_id: str):
    """This function deletes the product from product list"""
    if player_id not in cricket_team:
        return "Player not found"
    del cricket_team[player_id]
    return "Deleted Successfully"
