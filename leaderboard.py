from sqlalchemy import MetaData, Table, Column, Integer, String, Insert, create_engine, update

# Initialize database engine and tracking metadata for SQLite
engine = create_engine("sqlite:///player_scores.db")
metadata_obj = MetaData()

# Define structural relational schema for persistent leaderboard entries
score_leaderboard = Table(
    "player_and_score_tracker",
    metadata_obj,
    Column("Name", String, primary_key=True),
    Column("Score", Integer, nullable= False)
)

# Physically emit schema creation tracking statements to the engine instance
metadata_obj.create_all(engine)


def initialize_leaderboard(player_name, score):
    """
    Inserts a fresh player profile record directly into the persistence layer.

    Spins up an explicit transactional connection pool instance context block to 
    safely execute structural SQL insert mapping queries without leakage.

    :param player_name: str representing the primary key name identifier of the competitor
    :param score: int payload value representing the starting initial score metric
    :return: None
    """
    with engine.begin() as conn:
        initial_score = Insert(score_leaderboard).values(Name = player_name, Score = score)

        conn.execute(initial_score)


def update_leaderboard(player_name, score):
    """
    Modifies an existing player's score entry based on target identity matches.

    Utilizes core SQL expression builders to conditionally execute transaction 
    updates targeting records matching the specific primary key name constraint.

    :param player_name: str representing the primary key identifier query constraint
    :param score: int value representing the modified target score payload state
    :return: None
    """
    with engine.begin() as conn:

        stmt = (update(score_leaderboard)
        .where(score_leaderboard.c.Name == player_name)
        .values(Score=score))

        conn.execute(stmt)