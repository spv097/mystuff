import numpy as np
from numpy.typing import _128Bit
V = float(input('Velocity:'))   # freestream velocity (m/s)
y = float(input('Overall Spoiler Height:')) #m
x= float(input('Overall Spoiler Length:'))  #m
L = float(input('Distance from leading edge to spoiler hinge:'))   #m
Cd = float(input('Spoiler Drag Coeficient:'))    
theta =  np.arange(1,91,)  #Deployment Angle
n = 6      # Based on flat plate approximation
VBl = np.sqrt((n/(n+2))*(V**2))   # Velocity in Boundary Layer (m/s)
rho =  1.225    #Density ((kg/m3)
mu = 1.81e-5    # Dynamic Viscosity (kg/ms)
Re = ((rho*V*L)/mu)  # Reynolds Number
delta = (5*(L/Re))   # BL height (Delta 0.99)
Heff = y - delta     # Effective spoiler height outside BL
FT= (0.5 * Cd * rho * (V**2) * (Heff*x)) + ((delta*x) *(n/(n+2)) *0.5 *(V**2)*rho)   # N  Force on spoiler when perpendicular to surface
alpha = 90 -theta   #Effective angle
import math
thetaI= np.radians(alpha)   #Degrees to radians conversion
U= np.cos(thetaI)  # Value of cos(θI)
F = FT*U     # Actual Force on plate
print ('Spoiler Drag:', F , 'N') 
import plotly.graph_objects as go
fig =go.Figure(data=go.Scatter(x= theta, y= F))
fig.update_layout(title='Force Against Deployment Angle Θ', xaxis_title='Deployment Angle Θ', yaxis_title='Force N')
fig.show()