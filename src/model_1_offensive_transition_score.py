import pandas as pd
from sklearn.preprocessing import MinMaxScaler

OFFENSIVE_TRANSITION_METRICS = [
    'BYPASSED_OPPONENTS_AT_PHASE_ATTACKING_TRANSITION',
    'BYPASSED_DEFENDERS_TO_PITCH_POSITION_FIRST_THIRD',
    'BYPASSED_DEFENDERS_TO_PITCH_POSITION_MIDDLE_THIRD',
    'BYPASSED_DEFENDERS_TO_LANE_LEFT_WING',
    'BYPASSED_DEFENDERS_TO_LANE_RIGHT_WING',
    'BYPASSED_DEFENDERS_AT_PHASE_ATTACKING_TRANSITION',
    'BYPASSED_OPPONENTS_RECEIVING_AT_PHASE_ATTACKING_TRANSITION',
    'BYPASSED_DEFENDERS_RECEIVING_AT_PHASE_ATTACKING_TRANSITION',
    'SHOT_XG_AT_PHASE_ATTACKING_TRANSITION'
]


def compute_offensive_transition_score(
    df: pd.DataFrame,
    min_matches: int = 10
) -> pd.DataFrame:
    # 1. Filter coaches by minimum number of matches
    df_filtered = df[df['quantidade_jogos'] >= min_matches].copy()

    # 2. Aggregate by coach and competition
    grouped = (
        df_filtered
        .groupby(['coachId', 'coachName', 'competitionName'], as_index=False)
        [OFFENSIVE_TRANSITION_METRICS + ['quantidade_jogos']]
        .mean()
    )

    # 3. Normalize metrics within each competition
    def normalize_by_competition(df_comp):
        scaler = MinMaxScaler()
        df_comp[OFFENSIVE_TRANSITION_METRICS] = scaler.fit_transform(
            df_comp[OFFENSIVE_TRANSITION_METRICS]
        )
        return df_comp

    normalized = (
        grouped
        .groupby('competitionName', group_keys=False)
        .apply(normalize_by_competition)
        .reset_index(drop=True)
    )

    # 4. Raw score (sum of normalized metrics)
    normalized['raw_score'] = normalized[OFFENSIVE_TRANSITION_METRICS].sum(
        axis=1)

    # 5. Global normalization of the final score
    score_scaler = MinMaxScaler()
    normalized['offensive_transition_score'] = score_scaler.fit_transform(
        normalized[['raw_score']]
    )

    # 6. Select final columns
    final_columns = (
        ['coachId', 'coachName', 'competitionName', 'quantidade_jogos',
         'offensive_transition_score'] +
        OFFENSIVE_TRANSITION_METRICS
    )

    return normalized[final_columns]
