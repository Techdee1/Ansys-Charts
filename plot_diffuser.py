"""
GET 205: Fluid Mechanics – CFD Diffuser Analysis
Plots:
  1. Reynolds Number (Re) vs Mass Flow Rate at inlet
  2. Pressure Drop (ΔP) vs Mass Flow Rate at inlet
"""

import matplotlib
matplotlib.use("Agg")           # non-interactive backend (works everywhere)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

# ── Raw data from ANSYS Fluent simulation ─────────────────────────────────────
# Laminar flow  (Re = 100, 500, 1000, 1500)
lam_Re     = [100,    500,    1000,    1500   ]
lam_Qm_in  = [0.002753953, 0.013769764, 0.027539529, 0.041296937]   # kg/s (abs)
lam_dP     = [0.0072428777, 0.048178601, 0.14408629,  0.28402376 ]   # Pa

# Turbulent flow  (Re = 5×10³, 10⁴, 5×10⁴, 10⁵)
turb_Re    = [5000,   10000,  50000,   100000 ]
turb_Qm_in = [0.13769765, 0.2753953,  1.3769765,  2.753953   ]       # kg/s (abs)
turb_dP    = [2.248299,   6.1993086,  89.834099,  309.36771  ]       # Pa

# ── Styling helpers ───────────────────────────────────────────────────────────
LAM_COLOR  = "#1f77b4"   # blue
TURB_COLOR = "#d62728"   # red
MARKER_KW  = dict(markersize=8, linewidth=1.8)

def add_value_labels(ax, xs, ys, fmt="{:.4f}", offset=(0, 6)):
    """Annotate each data-point with its y-value."""
    for x, y in zip(xs, ys):
        ax.annotate(fmt.format(y),
                    xy=(x, y),
                    xytext=offset,
                    textcoords="offset points",
                    fontsize=7.5, ha="center")

# ═══════════════════════════════════════════════════════════════════════════════
#  FIGURE 1 – Re vs Mass Flow Rate
# ═══════════════════════════════════════════════════════════════════════════════
fig1, ax1 = plt.subplots(figsize=(9, 5.5))

ax1.plot(lam_Re, lam_Qm_in,
         color=LAM_COLOR, marker="o", label="Laminar Flow", **MARKER_KW)
ax1.plot(turb_Re, turb_Qm_in,
         color=TURB_COLOR, marker="s", label="Turbulent Flow", **MARKER_KW)

add_value_labels(ax1, lam_Re,  lam_Qm_in,  fmt="{:.5f}")
add_value_labels(ax1, turb_Re, turb_Qm_in, fmt="{:.4f}")

ax1.set_xscale("log")
ax1.set_xlabel("Reynolds Number (Re)", fontsize=12)
ax1.set_ylabel("Mass Flow Rate at Inlet  $\\dot{m}$ (kg/s)", fontsize=12)
ax1.set_title("Reynolds Number vs Mass Flow Rate at Diffuser Inlet\n"
              "GET 205 – CFD Steady Simulation of Diffuser", fontsize=13)
ax1.legend(fontsize=11)
ax1.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
ax1.xaxis.set_major_formatter(ticker.FuncFormatter(
    lambda v, _: f"{int(v):,}"))
ax1.tick_params(axis="both", labelsize=10)

# Separate region shading
ax1.axvspan(50, 2500,   alpha=0.06, color=LAM_COLOR,  label="_Laminar region")
ax1.axvspan(2500, 2e5,  alpha=0.06, color=TURB_COLOR, label="_Turbulent region")

plt.tight_layout()
fig1.savefig("graph1_Re_vs_massflowrate.png", dpi=150)
print("Saved → graph1_Re_vs_massflowrate.png")

# ═══════════════════════════════════════════════════════════════════════════════
#  FIGURE 2 – Pressure Drop vs Mass Flow Rate
# ═══════════════════════════════════════════════════════════════════════════════
fig2, ax2 = plt.subplots(figsize=(9, 5.5))

ax2.plot(lam_Qm_in, lam_dP,
         color=LAM_COLOR, marker="o", label="Laminar Flow", **MARKER_KW)
ax2.plot(turb_Qm_in, turb_dP,
         color=TURB_COLOR, marker="s", label="Turbulent Flow", **MARKER_KW)

add_value_labels(ax2, lam_Qm_in,  lam_dP,  fmt="{:.5f}")
add_value_labels(ax2, turb_Qm_in, turb_dP, fmt="{:.3f}")

ax2.set_xscale("log")
ax2.set_yscale("log")
ax2.set_xlabel("Mass Flow Rate at Inlet  $\\dot{m}$ (kg/s)", fontsize=12)
ax2.set_ylabel("Pressure Drop  $\\Delta P$ (Pa)", fontsize=12)
ax2.set_title("Pressure Drop vs Mass Flow Rate at Diffuser Inlet\n"
              "GET 205 – CFD Steady Simulation of Diffuser", fontsize=13)
ax2.legend(fontsize=11)
ax2.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
ax2.tick_params(axis="both", labelsize=10)

plt.tight_layout()
fig2.savefig("graph2_dP_vs_massflowrate.png", dpi=150)
print("Saved → graph2_dP_vs_massflowrate.png")

print("\nDone. Both graphs saved to the workspace folder.")
