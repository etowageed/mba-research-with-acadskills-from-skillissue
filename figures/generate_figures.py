#!/usr/bin/env python3
"""
Publication-Ready Figures (300 DPI, Colorblind-Safe Okabe-Ito Palette)
UEL-SG-7002 Applied Business Project: UK Hybrid Working, Retention & Productivity (2021-2024)
All data points strictly sourced from verified ONS (BICS, OPN, LFS, PRDY) and CIPD (2023) releases.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Okabe-Ito colorblind-safe palette
OKABE_BLUE = "#0072B2"
OKABE_ORANGE = "#D55E00"
OKABE_GREEN = "#009E73"
OKABE_SKY = "#56B4E9"
OKABE_GREY = "#7F7F7F"
OKABE_PURPLE = "#CC79A7"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 10,
    "axes.titlesize": 11,
    "axes.titleweight": "bold",
    "axes.labelsize": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "figure.dpi": 300,
    "savefig.dpi": 300,
    "savefig.bbox": "tight",
})


def make_fig1_conceptual():
    """Figure 1: Multi-Theoretical Conceptual Framework (Chapter 2)."""
    fig, ax = plt.subplots(figsize=(11.5, 6.2))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")

    def draw_box(x, y, w, h, title, body, edge_col, face_col="#FFFFFF", title_col="#111111"):
        box = mpatches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle="round,pad=0.6,rounding_size=1.8",
            linewidth=1.8, edgecolor=edge_col, facecolor=face_col, zorder=2
        )
        ax.add_patch(box)
        ax.text(
            x + w / 2, y + h - 3.6, title,
            ha="center", va="top", fontsize=9.8, fontweight="bold", color=title_col, zorder=3
        )
        ax.text(
            x + w / 2, y + h / 2 - 2.2, body,
            ha="center", va="center", fontsize=8.4, color="#222222", linespacing=1.35, zorder=3
        )

    def draw_arrow(x1, y1, x2, y2, style="->", col="#333333", lw=1.4, ls="-"):
        ax.annotate(
            "", xy=(x2, y2), xytext=(x1, y1),
            arrowprops=dict(arrowstyle=style, color=col, lw=lw, linestyle=ls, shrinkA=2, shrinkB=2),
            zorder=4
        )

    # Title
    ax.text(
        50, 97.5,
        "Conceptual Framework: Hybrid Working, Mediating Mechanisms, Governance & UK Performance",
        ha="center", va="top", fontsize=11.5, fontweight="bold", color="#111111"
    )

    # Top: Organisational-Level Enabler (Dynamic Capabilities)
    draw_box(
        18, 75, 64, 15.5,
        "Organisational-Level Enabler: Dynamic Capabilities (Teece, Pisano & Shuen, 1997)",
        "Sensing labour-market shifts • Seizing digital-asset & scheduling flexibility\n"
        "Transforming routines across Knowledge (SIC J, K, M) vs. Location-Bound (SIC C, G, I) firms",
        OKABE_SKY, face_col="#F2F9FD", title_col=OKABE_BLUE
    )

    # Left: Independent Variable
    draw_box(
        2.0, 34, 23.5, 32,
        "Independent Variable\nHybrid Working Arrangements",
        "• Knowledge Sectors (J, K, M):\n  42%–49% hybrid adoption\n  (ONS BICS, 2024a)\n\n"
        "• Location-Bound (C, G, I):\n  4% hybrid (Sec. I); temporal\n  & shift flexibility focus",
        OKABE_BLUE, face_col="#F0F6FA", title_col=OKABE_BLUE
    )

    # Centre: Mediating Mechanisms (Individual & Team Level)
    draw_box(
        30.5, 53.5, 39, 13.5,
        "JD-R Theory (Bakker & Demerouti, 2017)",
        "Job Resource: 56 min/day commute saving (ONS, 2024a)\n"
        "vs. Job Demand: meeting overload & boundary blur",
        OKABE_GREEN, face_col="#F1FAF6", title_col="#006B4E"
    )
    draw_box(
        30.5, 37.0, 39, 13.5,
        "Social Exchange Theory (Cropanzano & Mitchell, 2005)",
        "Perceived organisational trust & autonomy support\n"
        "-> Reciprocal commitment vs. RTO psychological breach",
        OKABE_GREEN, face_col="#F1FAF6", title_col="#006B4E"
    )
    draw_box(
        30.5, 20.5, 39, 13.5,
        "Self-Determination Theory (Ryan & Deci, 2000)",
        "Autonomy (remote focus) + Competence & Relatedness\n"
        "(in-office mentoring & tacit knowledge transfer)",
        OKABE_GREEN, face_col="#F1FAF6", title_col="#006B4E"
    )

    # Right: Dependent Outcomes
    draw_box(
        74.5, 34, 23.5, 32,
        "Dependent Outcomes\nOrganisational Performance",
        "• Employee Retention:\n  -33% to -35% quit rates (RCT);\n  lower job-to-job attrition\n\n"
        "• Labour Productivity:\n  Sectoral GVA/hour resilience\n  (Sec. J vs. macro -0.8% drag)",
        OKABE_PURPLE, face_col="#FCF4F8", title_col="#8C3B69"
    )

    # Bottom: Governance & Institutional Moderators
    draw_box(
        18, 2.5, 64, 13.5,
        "Governance & Institutional Moderators (UK Context, 2021–2024)",
        "Formal 3:2 Hybrid Policy (vs. 24% ad-hoc) • Line-Manager Output Appraisal (Anti-Proximity Bias)\n"
        "Statutory Compliance: Employment Relations (Flexible Working) Act 2023 (49% unawareness gap)",
        OKABE_ORANGE, face_col="#FFF6F0", title_col="#A84300"
    )

    # Arrows: Top -> Left & Centre
    draw_arrow(34, 75, 15, 66.8, col=OKABE_BLUE, lw=1.3, ls="--")
    draw_arrow(50, 75, 50, 67.8, col=OKABE_BLUE, lw=1.3, ls="--")

    # Arrows: Left -> Centre (3 mediators)
    draw_arrow(26.2, 54, 29.8, 60.2, col="#333333", lw=1.4)
    draw_arrow(26.2, 50, 29.8, 43.8, col="#333333", lw=1.4)
    draw_arrow(26.2, 46, 29.8, 27.2, col="#333333", lw=1.4)

    # Arrows: Centre (3 mediators) -> Right
    draw_arrow(70.2, 60.2, 73.8, 54, col="#333333", lw=1.4)
    draw_arrow(70.2, 43.8, 73.8, 50, col="#333333", lw=1.4)
    draw_arrow(70.2, 27.2, 73.8, 46, col="#333333", lw=1.4)

    # Arrows: Bottom Moderator -> Centre & Right
    draw_arrow(50, 16.8, 50, 19.8, col=OKABE_ORANGE, lw=1.4)
    draw_arrow(72, 16.8, 83, 33.2, col=OKABE_ORANGE, lw=1.3, ls="--")

    plt.tight_layout()
    plt.savefig("figures/fig1_conceptual_framework.png")
    plt.close()


def make_fig2_adoption():
    """Figure 2: UK Sectoral Hybrid Adoption (ONS BICS) & GB Workforce Trajectory (ONS OPN)."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.5))

    # Panel A: Sectoral Hybrid/Homeworking Adoption (ONS BICS)
    sectors = [
        "Information &\nCommunication (Sec. J)",
        "Professional, Scientific\n& Technical (Sec. M)",
        "Accommodation &\nFood Service (Sec. I)",
    ]
    apr_2022_perm = [54, np.nan, 3]
    dec_2023_hybrid = [49, 42, 4]

    y = np.arange(len(sectors))
    height = 0.35

    bars2 = ax1.barh(y - height / 2, dec_2023_hybrid, height, label="Dec 2023: Operating Hybrid Model", color=OKABE_BLUE)
    valid_idx = [0, 2]
    bars1 = ax1.barh(
        [y[i] + height / 2 for i in valid_idx],
        [apr_2022_perm[i] for i in valid_idx],
        height,
        label="Apr 2022: Permanent WFH Intention",
        color=OKABE_SKY,
    )

    ax1.set_yticks(y)
    ax1.set_yticklabels(sectors)
    ax1.invert_yaxis()
    ax1.set_xlabel("Proportion of Businesses (%)")
    ax1.set_xlim(0, 65)
    ax1.set_title("A. Sectoral Hybrid Polarisation (ONS BICS)")
    ax1.legend(loc="lower right", frameon=False, fontsize=8.5)

    for bar in bars2:
        w = bar.get_width()
        ax1.text(w + 1.2, bar.get_y() + bar.get_height() / 2, f"{int(w)}%", va="center", fontsize=9)
    for bar in bars1:
        w = bar.get_width()
        ax1.text(w + 1.2, bar.get_y() + bar.get_height() / 2, f"{int(w)}%", va="center", fontsize=9)

    # Panel B: GB Working Adults Hybrid Working Trajectory (ONS OPN 2022-2024)
    periods = ["Feb–May\n2022*", "Sep 2022–\nJan 2023", "Apr–Jun\n2024", "Oct\n2024"]
    opn_rates = [18.5, 28.0, 26.0, 28.0]
    ax2.plot(periods, opn_rates, marker="o", linewidth=2.2, markersize=7, color=OKABE_GREEN)
    ax2.fill_between(range(len(periods)), [13, 28, 26, 28], [24, 28, 26, 28], color=OKABE_GREEN, alpha=0.15)
    ax2.set_ylim(0, 40)
    ax2.set_ylabel("Working Adults Hybrid Working (%)")
    ax2.set_title("B. GB Hybrid Workforce Stabilisation (ONS OPN)")
    ax2.grid(axis="y", linestyle="--", alpha=0.35)

    labels = ["13%–24%", "28%", "26%", "28%"]
    for i, (x_val, y_val) in enumerate(zip(range(len(periods)), opn_rates)):
        ax2.text(x_val, y_val + (6.6 if i == 0 else 2.2), labels[i], ha="center", fontsize=9, fontweight="bold")

    fig.text(
        0.5, -0.05,
        "Sources: ONS Business Insights and Conditions Survey (BICS, 2022, 2024a); ONS Opinions and Lifestyle Survey (OPN, 2022–2024).\n"
        "*Feb–May 2022 OPN plotted at midpoint of reported 13%–24% transition range; Sec. M Apr 2022 BICS figure omitted where not directly tabulated.",
        ha="center", fontsize=8, color="#444444"
    )
    plt.tight_layout()
    plt.savefig("figures/fig2_uk_hybrid_adoption.png")
    plt.close()


def make_fig3_retention():
    """Figure 3: CIPD (2023) Hybrid Policy Prevalence (Horizontal) & ONS LFS Job-to-Job Move Peaks."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.2, 4.6))

    # Panel A: Horizontal bar chart to guarantee zero x-axis label collision
    categories = [
        "Unaware of Apr 2024\nDay-One Statutory Right",
        "Report Higher WFH /\nHybrid Productivity",
        "Operate Formal\nHybrid Policy",
        "Rely on Informal /\nAd-hoc Approach",
    ]
    values = [49, 46, 45, 24]
    colors = [OKABE_ORANGE, OKABE_GREEN, OKABE_BLUE, OKABE_SKY]

    y1 = np.arange(len(categories))
    bars1 = ax1.barh(y1, values, color=colors, height=0.52)
    ax1.set_yticks(y1)
    ax1.set_yticklabels(categories, fontsize=8.8)
    ax1.invert_yaxis()
    ax1.set_xlim(0, 60)
    ax1.set_xlabel("Percentage of UK Organisations (%)")
    ax1.set_title("A. UK Employer Hybrid Governance (CIPD, 2023)")
    ax1.grid(axis="x", linestyle="--", alpha=0.35)

    for bar, val in zip(bars1, values):
        ax1.text(val + 1.0, bar.get_y() + bar.get_height() / 2, f"{val}%", va="center", fontsize=9, fontweight="bold")

    # Panel B: ONS LFS Peak Job-to-Job Moves & CIPD Flexibility Attrition
    metrics = [
        "ONS LFS Job-to-Job\nMoves (Q4 2021)",
        "ONS LFS Peak Job-to-Job\nMoves (Q1 2022)",
        "CIPD Est. Left Job Due\nto No Flexibility (2023)",
        "CIPD Est. Changed Career\nDue to No Flexibility",
    ]
    millions = [0.988, 0.994, 2.0, 4.0]
    m_colors = [OKABE_BLUE, OKABE_BLUE, OKABE_ORANGE, OKABE_PURPLE]

    y2 = np.arange(len(metrics))
    hbars = ax2.barh(y2, millions, color=m_colors, height=0.52)
    ax2.set_yticks(y2)
    ax2.set_yticklabels(metrics, fontsize=8.8)
    ax2.invert_yaxis()
    ax2.set_xlabel("Workers (Millions)")
    ax2.set_xlim(0, 4.85)
    ax2.set_title("B. UK Mobility Peaks & Inflexibility Attrition")
    ax2.grid(axis="x", linestyle="--", alpha=0.35)

    for bar, val in zip(hbars, millions):
        label = f"{int(val * 1000):,}k" if val < 1.5 else f"~{val:.1f}M"
        ax2.text(val + 0.08, bar.get_y() + bar.get_height() / 2, label, va="center", fontsize=9, fontweight="bold")

    fig.text(
        0.5, -0.04,
        "Sources: CIPD Flexible and Hybrid Working Practices in 2023 (CIPD, 2023); ONS Labour Force Survey Flows Estimates (ONS, 2024c).",
        ha="center", fontsize=8, color="#444444"
    )
    plt.tight_layout(w_pad=3.0)
    plt.savefig("figures/fig3_retention_and_policy.png")
    plt.close()


def make_fig4_productivity():
    """Figure 4: ONS Whole-Economy Output per Hour Worked Annual % Change (2021-2024)."""
    fig, ax = plt.subplots(figsize=(8.4, 4.3))

    years = ["2021", "2022", "2023", "2024"]
    yoy_growth = [1.4, 0.8, -0.4, -0.8]
    colors = [OKABE_BLUE if v >= 0 else OKABE_ORANGE for v in yoy_growth]

    bars = ax.bar(years, yoy_growth, color=colors, width=0.46, zorder=3)
    ax.axhline(0, color="#333333", linewidth=1.0, zorder=2)
    ax.set_ylim(-1.45, 2.0)
    ax.set_ylabel("Annual Output per Hour Growth (%)")
    ax.set_xlabel("Calendar Year")
    ax.set_title("UK Whole-Economy Labour Productivity Growth (ONS PRDY, 2021–2024)")
    ax.grid(axis="y", linestyle="--", alpha=0.35, zorder=0)

    for bar, val in zip(bars, yoy_growth):
        offset = 0.08 if val >= 0 else -0.15
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            val + offset,
            f"{val:+.1f}%",
            ha="center",
            fontsize=9.5,
            fontweight="bold",
        )

    ax.annotate(
        "Post-lockdown rebound\n(services reopening)",
        xy=(0.15, 1.4), xytext=(0.55, 1.55),
        arrowprops=dict(arrowstyle="->", color="#555555", lw=0.8),
        fontsize=8.2, color="#333333"
    )
    ax.annotate(
        "Hours worked outpaced GVA;\nmacro inflation/energy drag\n(Sec. J resilient vs. Sec. I lag)",
        xy=(2.75, -0.65), xytext=(1.55, -1.25),
        arrowprops=dict(arrowstyle="->", color="#555555", lw=0.8),
        fontsize=8.2, color="#333333"
    )

    fig.text(
        0.5, -0.04,
        "Source: Office for National Statistics (ONS) Labour Productivity Time Series (PRDY), Output per Hour Worked, UK (2024b).",
        ha="center", fontsize=8, color="#444444"
    )
    plt.tight_layout()
    plt.savefig("figures/fig4_uk_productivity_trends.png")
    plt.close()


if __name__ == "__main__":
    make_fig1_conceptual()
    make_fig2_adoption()
    make_fig3_retention()
    make_fig4_productivity()
    print("Generated fig1_conceptual_framework.png, fig2_uk_hybrid_adoption.png, fig3_retention_and_policy.png, fig4_uk_productivity_trends.png")
