import gradio as gr
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from strike_and_dip_calculator import calculate_strike_and_dip

def run_calculation(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    try:
        result = calculate_strike_and_dip(x1, y1, z1, x2, y2, z2, x3, y3, z3)
        
        # Create 3D plot
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Points
        points = np.array([[x1, y1, z1], [x2, y2, z2], [x3, y3, z3]])
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='red', s=100, label='Input Points')
        
        # Plane visualization
        # Define a grid for the plane
        min_x, max_x = min(points[:, 0]), max(points[:, 0])
        min_y, max_y = min(points[:, 1]), max(points[:, 1])
        
        # Create a meshgrid
        xx, yy = np.meshgrid(np.linspace(min_x, max_x, 10), np.linspace(min_y, max_y, 10))
        
        # Plane equation: ax + by + cz + d = 0 => z = (-ax - by - d)/c
        a, b, c, d = result['plane_coeffs']
        zz = (-a*xx - b*yy - d) / c
        
        ax.plot_surface(xx, yy, zz, alpha=0.3, color='blue')
        
        # Labels
        ax.set_xlabel('Easting (X)')
        ax.set_ylabel('Northing (Y)')
        ax.set_zlabel('Elevation (Z)')
        ax.set_title(f'Strike: {result["strike_azimuth"]:.1f}° ({result["strike_compass"]}), '
                     f'Dip: {result["dip_angle"]:.1f}°\nDip Direction: {result["dip_direction_azimuth"]:.1f}°')
        
        plt.tight_layout()
        
        # Format output text
        output_text = (
            f"Strike Azimuth: {result['strike_azimuth']:.2f}°\n"
            f"Strike Compass: {result['strike_compass']}\n"
            f"Dip Direction Azimuth: {result['dip_direction_azimuth']:.2f}°\n"
            f"Dip Direction Compass: {result['dip_direction_compass']}\n"
            f"Dip Angle: {result['dip_angle']:.2f}°"
        )
        
        return output_text, fig
    
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        return error_msg, None

with gr.Blocks() as demo:
    gr.Markdown("## Strike and Dip Calculator")
    gr.Markdown("Enter three points (X=Easting, Y=Northing, Z=Elevation) to calculate geological strike and dip.")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Point A")
            ax = gr.Number(label="X (Easting)")
            ay = gr.Number(label="Y (Northing)")
            az = gr.Number(label="Z (Elevation)")
            
        with gr.Column():
            gr.Markdown("### Point B")
            bx = gr.Number(label="X (Easting)")
            by = gr.Number(label="Y (Northing)")
            bz = gr.Number(label="Z (Elevation)")
            
        with gr.Column():
            gr.Markdown("### Point C")
            cx = gr.Number(label="X (Easting)")
            cy = gr.Number(label="Y (Northing)")
            cz = gr.Number(label="Z (Elevation)")
    
    btn = gr.Button("Calculate")
    
    with gr.Row():
        output_text = gr.Textbox(label="Results", interactive=False)
        output_plot = gr.Plot(label="3D Visualization")
    
    btn.click(
        fn=run_calculation,
        inputs=[ax, ay, az, bx, by, bz, cx, cy, cz],
        outputs=[output_text, output_plot]
    )

demo.launch(server_name="0.0.0.0", server_port=7860)
