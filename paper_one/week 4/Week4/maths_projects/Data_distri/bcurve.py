import numpy as np
import plotly.graph_objects as go

# Create X and Y grid
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# 3D bell shape
Z = np.exp(-(X**2 + Y**2))

# Draw 3D surface
fig = go.Figure(
    data=[
        go.Surface(
            x=X,
            y=Y,
            z=Z
        )
    ]
)

fig.update_layout(
    title="3D Bell Curve",
    scene=dict(
        xaxis_title="X",
        yaxis_title="Y",
        zaxis_title="Height"
    )
)

fig.show()