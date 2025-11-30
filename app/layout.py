import sys
import os

# --- pour pouvoir importer layout.py depuis app/ ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

import base64
from pathlib import Path

import streamlit as st
from app.layout import apply_global_style, render_header, set_page_config


# -------- Page config + styles globaux --------
set_page_config("Vedoinvest – Home")
apply_global_style()
render_header(active_page="Home")


# -------- HERO IMAGE (bannière) --------
hero_path = Path(__file__).parents[1] / "assets" / "home.png"

with open(hero_path, "rb") as f:
    hero_base64 = base64.b64encode(f.read()).decode("utf-8")

st.markdown(
    """
    <style>
    .hero-wrapper {
        margin-top: 1.0rem;
    }

    .hero-card {
        padding: 0 !important;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12);
        background-color: transparent;
    }

    .hero-card img {
        width: 100%;
        height: 260px;
        object-fit: cover;
        display: block;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div class="hero-wrapper">
        <div class="vedoinvest-card hero-card">
            <img src="data:image/png;base64,{hero_base64}" alt="Vedoinvest hero">
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# -------- TITLE BLOCK --------
st.markdown(
    """
    <div class="vedoinvest-card" style="margin-top:1.5rem;">
        <div class="vedoinvest-title">Welcome to Vedoinvest</div>
        <div class="vedoinvest-subtitle">
            A quantitative ETF portfolio platform designed to help investors compare
            three systematic strategies: Global Minimum Variance (GMV),
            Tangency (max Sharpe), and Equal Risk Contribution (ERC).
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)
