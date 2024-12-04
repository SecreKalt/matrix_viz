import plotly.graph_objects as go
import numpy as np
import ipywidgets as widgets
import plotly.graph_objects as go

def add_vectors(v1, v2):
    return [v1[0] + v2[0], v1[1] + v2[1]]

def create_vector_plot(vectors, dim='2d'):
    if dim == '2d':
        fig = go.Figure()
        for v in vectors:
            fig.add_trace(go.Scatter(
                x=[0, v[0]], 
                y=[0, v[1]],
                mode='lines+markers',
                name=f'Vektor ({v[0]:.1f}, {v[1]:.1f})'
            ))
        fig.add_trace(go.Scatter(
            x=[-5, 5], 
            y=[0, 0],
            mode='lines',
            line=dict(color='gray', dash='dash'),
            showlegend=False
        ))
        fig.add_trace(go.Scatter(
            x=[0, 0], 
            y=[-5, 5],
            mode='lines',
            line=dict(color='gray', dash='dash'),
            showlegend=False
        ))
        fig.update_layout(
            title='2D Vektor Visualisierung',
            xaxis_title='X',
            yaxis_title='Y',
            xaxis=dict(range=[-5, 5], zerolinecolor='gray'),
            yaxis=dict(range=[-5, 5], zerolinecolor='gray'),
            showlegend=True
        )
    return fig

def update_vector(magnitude, angle):
    x = magnitude * np.cos(np.radians(angle))
    y = magnitude * np.sin(np.radians(angle))
    return create_vector_plot([[x, y]])

def plot_vector_addition(v1, v2):
    result = add_vectors(v1, v2)
    fig = create_vector_plot([v1, v2, result])
    return fig

def create_3d_vector_plot(vectors, dim='3d'):
    fig = go.Figure()
    
    # Vektoren zeichnen
    for v in vectors:
        fig.add_trace(go.Scatter3d(
            x=[0, v[0]], 
            y=[0, v[1]], 
            z=[0, v[2]],
            mode='lines+markers',
            name=f'Vektor ({v[0]:.1f}, {v[1]:.1f}, {v[2]:.1f})'
        ))
    
    # Koordinatenachsen
    axis_length = 5
    fig.add_trace(go.Scatter3d(x=[-axis_length, axis_length], y=[0, 0], z=[0, 0],
                              mode='lines', line=dict(color='red', dash='dash'),
                              name='X-Achse'))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[-axis_length, axis_length], z=[0, 0],
                              mode='lines', line=dict(color='green', dash='dash'),
                              name='Y-Achse'))
    fig.add_trace(go.Scatter3d(x=[0, 0], y=[0, 0], z=[-axis_length, axis_length],
                              mode='lines', line=dict(color='blue', dash='dash'),
                              name='Z-Achse'))
    
    fig.update_layout(
        title='3D Vektor Visualisierung',
        scene = dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            camera=dict(
                up=dict(x=0, y=0, z=1),
                center=dict(x=0, y=0, z=0),
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        )
    )
    return fig

def create_matrix_transformation_plot(matrix, vector):
    transformed_vector = np.dot(matrix, vector)
    vectors = [vector, transformed_vector]
    
    fig = go.Figure()
    colors = ['blue', 'red']
    names = ['Original', 'Transformiert']
    
    for v, color, name in zip(vectors, colors, names):
        fig.add_trace(go.Scatter(
            x=[0, v[0]], 
            y=[0, v[1]],
            mode='lines+markers',
            line=dict(color=color),
            name=name
        ))
    
    max_range = max(abs(np.array(vectors).flatten())) * 1.2
    fig.update_layout(
        title='Matrix Transformation',
        xaxis=dict(range=[-max_range, max_range]),
        yaxis=dict(range=[-max_range, max_range]),
        showlegend=True
    )
    return fig