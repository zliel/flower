# Copyright 2020 Adap GmbH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Generate plots for Fashion-MNIST results."""


import numpy as np

from flower_benchmark.plot import bar_chart, line_chart


def accuracy() -> None:
    """Generate plots."""
    # Raw data
    fedavg = [
        (0, 0.03759999945759773),
        (1, 0.03759999945759773),
        (2, 0.03759999945759773),
        (3, 0.03759999945759773),
        (4, 0.03759999945759773),
        (5, 0.03759999945759773),
        (6, 0.03759999945759773),
        (7, 0.03759999945759773),
        (8, 0.03759999945759773),
        (9, 0.03759999945759773),
        (10, 0.03759999945759773),
        (11, 0.03759999945759773),
        (12, 0.03759999945759773),
        (13, 0.03759999945759773),
        (14, 0.03759999945759773),
        (15, 0.03759999945759773),
        (16, 0.03759999945759773),
        (17, 0.03759999945759773),
        (18, 0.03759999945759773),
        (19, 0.03759999945759773),
        (20, 0.03759999945759773),
    ]
    fedfs_v0 = [
        (0, 0.03759999945759773),
        (1, 0.6328999996185303),
        (2, 0.7515000104904175),
        (3, 0.7832000255584717),
        (4, 0.8004999756813049),
        (5, 0.8141999840736389),
        (6, 0.821399986743927),
        (7, 0.8331999778747559),
        (8, 0.8378999829292297),
        (9, 0.8418999910354614),
        (10, 0.8536999821662903),
        (11, 0.8414999842643738),
        (12, 0.8521999716758728),
        (13, 0.8618999719619751),
        (14, 0.8629000186920166),
        (15, 0.8565999865531921),
        (16, 0.8691999912261963),
        (17, 0.8709999918937683),
        (18, 0.8690999746322632),
        (19, 0.8640999794006348),
        (20, 0.8712999820709229),
    ]
    fedfs_v1 = [
        (0, 0.03759999945759773),
        (1, 0.6732000112533569),
        (2, 0.7724999785423279),
        (3, 0.7961999773979187),
        (4, 0.8220000267028809),
        (5, 0.8258000016212463),
        (6, 0.8418999910354614),
        (7, 0.8409000039100647),
        (8, 0.8593000173568726),
        (9, 0.8464999794960022),
        (10, 0.864799976348877),
        (11, 0.8633000254631042),
        (12, 0.8718000054359436),
        (13, 0.8669000267982483),
        (14, 0.8743000030517578),
        (15, 0.8730999827384949),
        (16, 0.8780999779701233),
        (17, 0.8766999840736389),
        (18, 0.8773000240325928),
        (19, 0.8769000172615051),
        (20, 0.8791000247001648),
    ]

    # Configure labels and data
    lines = [("FedAvg", fedavg), ("FedFSv0", fedfs_v0), ("FedFSv1", fedfs_v1)]

    # Plot
    values = [np.array([x * 100 for _, x in val]) for _, val in lines]
    labels = [label for label, _ in lines]
    line_chart(values, labels, "Round", "Accuracy (centralized test set)")


def accuracy_fedavg_vs_fedfs() -> None:
    """Comparision of FedAvg vs FedFS."""
    bar_chart(
        y_values=[
            np.array([40.5, 85.3, 86.1, 87.2]),
            np.array([80.5, 84.3, 86.5, 89.2]),
        ],
        bar_labels=["FedAvg", "FedFS"],
        x_label="Timeout",
        x_tick_labels=["T=10", "T=20", "T=30", "T=40"],
        y_label="Final Accuracy",
        filename="accuracy_fedavg_vs_fedfs",
    )


def wall_clock_time_fedavg_vs_fedfs() -> None:
    """Comparision of FedAvg vs FedFS."""
    bar_chart(
        y_values=[np.array([0, 1600, 1750, 2000]), np.array([650, 750, 900, 1100])],
        bar_labels=["FedAvg", "FedFS"],
        x_label="Timeout",
        x_tick_labels=["T=10", "T=20", "T=30", "T=40"],
        y_label="Completion time",
        filename="wall_clock_time_fedavg_vs_fedfs",
    )


def main() -> None:
    """Call all plot functions."""
    accuracy()
    accuracy_fedavg_vs_fedfs()
    wall_clock_time_fedavg_vs_fedfs()


if __name__ == "__main__":
    main()