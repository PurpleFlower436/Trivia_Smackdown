from sqlalchemy import MetaData, Table, Column, Integer, String, Insert, create_engine, update


engine = create_engine("sqlite:///player_scores.db")
metadata_obj = MetaData()

score_leaderboard = Table(
    "player_and_score_tracker",
    metadata_obj,
    Column("Name", String, primary_key=True),
    Column("Score", Integer, nullable= False)
)

metadata_obj.create_all(engine)


def initialize_leaderboard(player_name, score):
     with engine.begin() as conn:
        initial_score = Insert(score_leaderboard).values(Name = player_name, Score = score)

        conn.execute(initial_score)


def update_leaderboard(player_name, score):

   
    with engine.begin() as conn:

        stmt = (update(score_leaderboard)
        .where(score_leaderboard.c.Name == player_name)
        .values(Score=score))

        conn.execute(stmt)