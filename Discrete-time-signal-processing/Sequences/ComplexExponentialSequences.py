import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.gridspec import GridSpec

A     = 1.0
phi   = 0.0
alpha = 0.9
omega = 0.4
N     = 30

fig = plt.figure(figsize=(10, 10), facecolor="#111")
fig.suptitle(r"$x[n] = |A|\,|\alpha|^n e^{j(\omega_0 n+\phi)}$",
             color="white", fontsize=13)

gs = GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35)
ax_plane  = fig.add_subplot(gs[0, 0])
ax_env    = fig.add_subplot(gs[0, 1])
ax_sig    = fig.add_subplot(gs[1, :])
ax_total  = fig.add_subplot(gs[2, :])

BLUE, GREEN, AMBER, PURPLE = "#3987e5", "#1baf7a", "#eda100", "#9085e9"

for ax in [ax_plane, ax_env, ax_sig, ax_total]:
    ax.set_facecolor("#1a1a1a")
    ax.tick_params(colors="#666", labelsize=8)
    for sp in ax.spines.values():
        sp.set_edgecolor("#333")

ax_plane.set_title("Piano complesso",                    color="#aaa", fontsize=9, loc="left")
ax_env.set_title("Inviluppo |A|·|α|ⁿ",                  color="#aaa", fontsize=9, loc="left")
ax_sig.set_title("Parte reale (blu) e immaginaria (verde)", color="#aaa", fontsize=9, loc="left")
ax_total.set_title("|x[n]| — modulo totale",             color="#aaa", fontsize=9, loc="left")

ns = np.arange(N + 1)

# --- Piano complesso ---
ax_plane.set_xlim(-1.5, 1.5)
ax_plane.set_ylim(-1.5, 1.5)
ax_plane.axhline(0, color="#333", lw=0.8)
ax_plane.axvline(0, color="#333", lw=0.8)
circle = plt.Circle((0, 0), 1, color="#333", fill=False, lw=0.8, linestyle="--")
ax_plane.add_patch(circle)
ax_plane.set_aspect("equal")
ax_plane.set_xlabel("Re", color="#666", fontsize=8)
ax_plane.set_ylabel("Im", color="#666", fontsize=8)
plane_line, = ax_plane.plot([], [], color=BLUE, lw=2)
plane_dot,  = ax_plane.plot([], [], "o", color=BLUE, ms=7, mec="#111", mew=1.2)
plane_text  = ax_plane.text(0.05, 0.92, "", transform=ax_plane.transAxes,
                             color="#aaa", fontsize=9)

# --- Inviluppo ---
ax_env.set_xlim(0, N)
ax_env.set_ylim(-A * 1.3, A * 1.3)
ax_env.axhline(0, color="#333", lw=0.8)
env_vals = A * alpha**ns
ax_env.plot(ns,  env_vals,  color=AMBER, lw=1.2, linestyle="--", alpha=0.6)
ax_env.plot(ns, -env_vals,  color=AMBER, lw=1.2, linestyle="--", alpha=0.6)
env_dot, = ax_env.plot([], [], "o", color=AMBER, ms=7, mec="#111", mew=1.2)
env_text  = ax_env.text(0.5, 0.88, "", transform=ax_env.transAxes,
                         color=AMBER, fontsize=9, ha="center")

# --- Parte reale e immaginaria ---
ax_sig.set_xlim(0, N)
ax_sig.set_ylim(-A * 1.3, A * 1.3)
ax_sig.axhline(0, color="#333", lw=0.8)
# Preallochiamo stem-like artists: una LineCollection per Re e una per Im
re_dots, = ax_sig.plot([], [], "o", color=BLUE,  ms=5, mec="#111", mew=1)
im_dots, = ax_sig.plot([], [], "o", color=GREEN, ms=5, mec="#111", mew=1)
sig_vline = ax_sig.axvline(0, color="#555", lw=1, linestyle=":")
ax_sig.legend(
    [plt.Line2D([], [], color=BLUE), plt.Line2D([], [], color=GREEN)],
    ["Re", "Im"],
    fontsize=8, facecolor="#222", labelcolor="white", loc="upper right"
)

# --- Modulo totale ---
ax_total.set_xlim(0, N)
ax_total.set_ylim(0, A * 1.3)
# BUG FIX 1: salviamo il riferimento alla linea statica dell'inviluppo
#             così non viene persa quando facciamo collections.clear()
envelope_line, = ax_total.plot(ns, env_vals, color=AMBER, lw=1.2,
                                linestyle="--", alpha=0.6, label="inviluppo")
tot_dots, = ax_total.plot([], [], "o", color=PURPLE, ms=5, mec="#111", mew=1)
tot_vline  = ax_total.axvline(0, color="#555", lw=1, linestyle=":")
tot_text   = ax_total.text(0.5, 0.85, "", transform=ax_total.transAxes,
                            color=PURPLE, fontsize=9, ha="center")
ax_total.legend(fontsize=8, facecolor="#222", labelcolor="white", loc="upper right")

# Teniamo traccia delle LineCollection dinamiche per poterle rimuovere
# senza toccare quelle statiche  (BUG FIX 2)
sig_collections   = []
total_collections = []


def update(frame):
    global sig_collections, total_collections

    n = frame % (N + 1)
    ns_shown = np.arange(n + 1)

    env  = A * alpha**n
    re_n = env * np.cos(omega * n + phi)
    im_n = env * np.sin(omega * n + phi)

    # --- Piano complesso ---
    plane_line.set_data([0, re_n], [0, im_n])
    plane_dot.set_data(np.array([re_n]), np.array([im_n]))   # BUG FIX 3
    plane_text.set_text(f"n={n}")

    # --- Inviluppo ---
    env_dot.set_data(np.array([n]), np.array([env]))          # BUG FIX 3
    env_text.set_text(f"|A||α|ⁿ = {env:.2f}")

    # --- Re / Im: rimuoviamo solo le vlines dinamiche ---          # BUG FIX 2
    for coll in sig_collections:
        coll.remove()
    sig_collections = []

    re_vals = A * alpha**ns_shown * np.cos(omega * ns_shown + phi)
    im_vals = A * alpha**ns_shown * np.sin(omega * ns_shown + phi)

    sig_collections.append(
        ax_sig.vlines(ns_shown,       0, re_vals, colors=BLUE,  lw=2, alpha=0.9)
    )
    sig_collections.append(
        ax_sig.vlines(ns_shown + 0.2, 0, im_vals, colors=GREEN, lw=2, alpha=0.9)
    )
    re_dots.set_data(ns_shown,       re_vals)
    im_dots.set_data(ns_shown + 0.2, im_vals)
    sig_vline.set_xdata([n])                                  # BUG FIX 4

    # --- Modulo totale: rimuoviamo solo le vlines dinamiche ---    # BUG FIX 2
    for coll in total_collections:
        coll.remove()
    total_collections = []

    mod_vals = A * alpha**ns_shown
    total_collections.append(
        ax_total.vlines(ns_shown, 0, mod_vals, colors=PURPLE, lw=2, alpha=0.9)
    )
    tot_dots.set_data(ns_shown, mod_vals)
    tot_vline.set_xdata([n])                                  # BUG FIX 4
    tot_text.set_text(f"|x[{n}]| = {env:.2f}")

    return (plane_line, plane_dot, env_dot,
            re_dots, im_dots, tot_dots,
            sig_vline, tot_vline)


# BUG FIX 5: frames=N+1 (da 0 a N), repeat=True gestisce il loop
ani = animation.FuncAnimation(
    fig, update,
    frames=N + 1,
    interval=100,
    repeat=True,
    blit=False   # blit=True è incompatibile con vlines dinamiche
)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()