Coach Offensive Transition Models
Objective

This project aims to build interpretable models to explain and compare football coaches’ offensive transition behaviour across multiple leagues and seasons.

The focus is on modelling behaviour, not on generative AI or narrative storytelling.

Central Question

How do football coaches differ in their offensive transition behaviour across leagues?

Analytical Scope

Unit of analysis: Coach

Game phase: Offensive transition

Context: Multi-league, multi-season

Approach: Behavioural and comparative modelling

Offensive transition is analysed as a complete game phase, not restricted to the first action after ball recovery.

Modelling Approach

Data Ingestion

Event and match-level data (non-public)

Accessed locally via configurable paths

Feature Engineering

Transition speed

Verticality

Risk profile

Spatial progression

Efficiency in creating advantage

Models

Interpretable statistical models

Behavioural scores per coach

Clustering to identify transition styles

Explanation Layer

Models are designed to be self-explanatory

Outputs directly describe coach behaviour

No generative AI or LLMs involved

Outputs

The project produces model-based explanations, not raw tables:

Coach rankings by offensive transition behaviour (per league)

Offensive transition archetypes

Structured comparisons between coaches

All outputs are stored as readable and interpretable artifacts.

Repository Structure
coach-offensive-transition-profile/
│
├─ src/            # Feature engineering and models
├─ data/
│  └─ sample/      # Fictitious data (format only)
├─ outputs/        # Rankings and archetypes
├─ main.py         # End-to-end pipeline
└─ README.md

Data Disclaimer

Real datasets are non-public and proprietary

No real data is versioned in this repository

data/sample/ contains synthetic data only

Code is fully data-agnostic

Motivation

This project was developed as part of an application to the
Context Engineering for Football course by Twelve Football.

It reflects an interest in:
Behavioural modelling in football
Interpretable data science
Explaining football decisions through models

Author

Otavio Santos
Football Data Scientist
