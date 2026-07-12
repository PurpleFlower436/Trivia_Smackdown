from sqlalchemy import MetaData, Table, Column, Integer, String



metadata_obj = MetaData()

score_leaderboard = Table(
    "player_and_score_tracker",
    metadata_obj,
    Column("Name", String, primary_key=True),
    Column("Score", Integer, nullable= False)
)
