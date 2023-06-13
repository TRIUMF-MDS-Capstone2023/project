import matplotlib.pyplot as plt
import polars as pl


def display_ring(composite_event_id, events, hits, cut_off_time=0.5):
    event = (
        events
        .filter(pl.col("composite_event_id") == composite_event_id)
        .first()
        .collect()
    )
    event_hits = (
        hits
        .filter(pl.col("composite_event_id") == composite_event_id)
        .select(["x_adjusted", "y_adjusted", "chod_delta"])
    )

    track_pos_x = event[0, 'track_pos_x']
    track_pos_y = event[0, 'track_pos_y']
    track_momentum = event[0, 'track_momentum']

    reco_ring_centre_pos_x = event[0, 'ring_centre_pos_x']
    reco_ring_centre_pos_y = event[0, 'ring_centre_pos_y']
    reco_ring_radius = event[0, 'ring_radius']
    reco_ring_likelihood_pion = event[0, 'ring_likelihood_pion']
    reco_ring_likelihood_muon = event[0, 'ring_likelihood_muon']
    reco_ring_likelihood_positron = event[0, 'ring_likelihood_positron']
    reco_ring_likelihood_kaon = event[0, 'ring_likelihood_kaon']
    reco_ring_likelihood_background = event[0, 'ring_likelihood_background']

    run_id = event[0, 'run_id']
    burst_id = event[0, 'burst_id']
    event_id = event[0, 'event_id']
    track_id = event[0, 'track_id']

    in_time_hits = (
        event_hits
        .filter(pl.col("chod_delta").abs() < cut_off_time)
        .collect()
    )
    out_of_time_hits = (
        event_hits
        .filter(pl.col("chod_delta").abs() >= cut_off_time)
        .collect()
    )

    # We use Matplotlib to plot
    fig = plt.figure()
    ax = fig.subplots()

    # First, we mark the track positions and hits
    ax.plot(out_of_time_hits.to_series(0), out_of_time_hits.to_series(1),
            '.', label='Out-of-time hit', color='tab:orange')
    ax.plot(in_time_hits.to_series(0), in_time_hits.to_series(1),
            '.', label='In-time hit', color='tab:cyan')
    ax.plot(track_pos_x, track_pos_y,
            '*', label='Track impact point', color='tab:red')

    # Ring fitting
    ring_fits = (
        abs(reco_ring_centre_pos_x) < 999999. and
        abs(reco_ring_centre_pos_y) < 999999.
    )

    if ring_fits:
        ring = plt.Circle((reco_ring_centre_pos_x, reco_ring_centre_pos_y),
                          reco_ring_radius, color='k', fill=False, ls=':', lw=0.5)
        ax.add_patch(ring)
        ax.plot(reco_ring_centre_pos_x, reco_ring_centre_pos_y,
                '.', label='Fitted ring pos.', color='k')
        ax.text(reco_ring_centre_pos_x + 10, reco_ring_centre_pos_y - 10,
                f'({reco_ring_centre_pos_x:.2f}, {reco_ring_centre_pos_y:.2f})')
        ax.text(reco_ring_centre_pos_x + np.cos(1) * reco_ring_radius,
                reco_ring_centre_pos_y + np.sin(1) * reco_ring_radius,
                f'r = {reco_ring_radius:.2f}')
    else:
        ax.text(0, 0, 'No ring', fontsize=14, ha='center')

    # Set the scene
    ax.set_aspect('equal')
    ax.set_xlim(-350, 350)  # mm
    ax.set_ylim(-350, 350)  # mm
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.legend()

    # And title
    likelihood_str = (
        f'$L_{{\pi}}$ = {reco_ring_likelihood_pion:.2f}' +
        f', $L_{{\mu}}$ = {reco_ring_likelihood_muon:.2f}' +
        f', $L_{{e}}$ = {reco_ring_likelihood_positron:.2f}' +
        f', $L_{{K}}$ = {reco_ring_likelihood_kaon:.2f}' +
        f', $L_{{bkg}}$ = {reco_ring_likelihood_background:.2f}'
    )

    plt.suptitle(f'Run {run_id}, Burst {burst_id}, Event {event_id}, Track {track_id} (Tcut = {cut_off_time} ns)' +
                 f'\n{likelihood_str}', y=1.05, fontsize=12)
    plt.title(f'p = {track_momentum:.2f} GeV/c' +
              f'\nComposite event ID: {composite_event_id}', fontsize=10)

    # And done!
    return fig
