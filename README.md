![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Strike and Dip Calculator
 
*For field geologists and structural geology students: enter the coordinates and elevations of three points on a planar surface to instantly compute the strike, dip direction, and dip angle.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geology
 
A web tool that solves the classic three-point problem in structural geology. Inputs: three points, each with Easting (X, meters), Northing (Y, meters), and Elevation (Z, meters) as numeric fields (nine total). The user enters these via gr.Number components labeled 'Point A: X, Y, Z', etc. The core logic: 1. Compute vectors v1 = (x2-x1, y2-y1, z2-z1) and v2 = (x3-x1, y3-y1, z3-z1). 2. Compute the normal n = (a,b,c) = v1 × v2. If n is (0,0,0), show an error 'Points are collinear – cannot define a plane'. 3. Calculate dip angle = arctan(sqrt(a²+b²)/|c|) in degrees (0–90). 4. Calculate dip direction azimuth = atan2(b, a) * 180/π, normalized to 0–360; this is the downdip direction. 5. Compute strike = (dip_direction + 90) mod 360, then if strike ≥ 180, subtract 180 so it lies in [0,180). 6. Convert strike to a compass quadrant string (e.g., N45E, N45W, S45E, S45W) using conventional rules. Outputs: (a) text block showing strike azimuth, compass quadrant, dip direction azimuth and quadrant, and dip angle in degrees; (b) a Matplotlib 3D scatter plot of the three points with a fitted plane surface (wireframe), annotated with strike and dip symbols. The plot uses plt.subplot with projection='3d'. The UI layout is a single-column Gradio interface with three groups of three number inputs, a 'Calculate' button, and two output areas: a textbox and a plot.
 
## Run it
 
```bash
docker build -t strike-and-dip-calculator .
docker run -p 7860:7860 strike-and-dip-calculator
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-22.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
