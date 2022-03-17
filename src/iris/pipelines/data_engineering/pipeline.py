"""Example code for the nodes in the example pipeline. This code is meant
just for illustrating basic Kedro features.

Delete this when you start working on your own Kedro project.
"""

from kedro.pipeline import node, pipeline

from .nodes import split_data, make_scatter_plot


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                make_scatter_plot,
                inputs="example_iris_data",
                outputs="iris_scatter_plot@matplotlib",
                name="plot",
            ),
            node(
                lambda x: x,
                inputs="iris_scatter_plot@bytes",
                outputs="iris_scatter_plot_base64",
                name="encode",
            ),
            node(
                split_data,
                inputs=["example_iris_data", "params:example_test_data_ratio"],
                outputs=dict(
                    train_x="example_train_x",
                    train_y="example_train_y",
                    test_x="example_test_x",
                    test_y="example_test_y",
                ),
                name="split",
            )
        ]
    )


