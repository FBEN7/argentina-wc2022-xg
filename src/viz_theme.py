"""Reusable professional football-viz theme for matplotlib.
Import in every project: from football_viz_theme import apply_theme, clean_axis, COLORS
"""
import matplotlib as mpl

COLORS = {
    "bg":        "#0E1117",
    "text":      "#E6EDF3",
    "muted":     "#8B949E",
    "grid":      "#2A313C",
    "highlight": "#6CB4EE",   # the team/subject you want the eye to land on
    "neutral":   "#3D444D",   # everything you're comparing against -> greyed out
    "accent":    "#F4A259",
    "good":      "#3FB950",
    "bad":       "#F85149",
}

def apply_theme():
    mpl.rcParams.update({
        "figure.facecolor":  COLORS["bg"],
        "axes.facecolor":    COLORS["bg"],
        "savefig.facecolor": COLORS["bg"],
        "text.color":        COLORS["text"],
        "axes.labelcolor":   COLORS["muted"],
        "xtick.color":       COLORS["muted"],
        "ytick.color":       COLORS["text"],
        "font.family":       "sans-serif",
        "font.sans-serif":   ["DejaVu Sans"],  # swap "Oswald"/"Roboto Condensed" locally for the broadcast look
        "font.size":         11,
        "axes.titlesize":    15, "axes.titleweight": "bold",
        "axes.edgecolor":    COLORS["grid"], "axes.linewidth": 0.8,
        "axes.grid":         True, "grid.color": COLORS["grid"],
        "grid.linewidth":    0.6, "grid.alpha": 0.5,
        "figure.dpi":        150,
    })

def clean_axis(ax, keep=("left", "bottom")):
    """Remove chartjunk: hide unused spines, kill tick marks."""
    for side in ("top", "right", "left", "bottom"):
        ax.spines[side].set_visible(side in keep)
    ax.tick_params(length=0)
    return ax
