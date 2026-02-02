import pandas as pd
from src.model_1_offensive_transition_score import (
    compute_offensive_transition_score
)

# Example: dataframe already loaded from a private source
# df_complete = pd.read_parquet("PRIVATE_PATH")

df_offensive_transition_score = compute_offensive_transition_score(
    df_complete,
    min_matches=10
)

# Example save
# df_offensive_transition_score.to_parquet(
#     "outputs/offensive_transition_score.parquet"
# )
