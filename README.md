# Implementation of SLAM Using Helios 16P LiDAR

This repository contains the project implementation, documentation, and algorithms for Simultaneous Localization and Mapping (SLAM) using the **Helios 16P LiDAR** sensor.

## Project Structure

- **slam_implementation/**: Python scripts for reading sensor rosbag/database point cloud data and performing 2D SLAM mapping (Slam.py, Database.py, Topics.py).
- **Implementation of SLAM Using Helios 16P LiDAR.pdf**: Project documentation and research report.
- **Lidar based slam.pptx / Lidar based slam (2).pdf**: Project presentation slides.
- **SHORT MANUAL.odt**: Hardware setup and operational instructions.

## Prerequisites

- Python 3.8+
- NumPy
- Matplotlib
- SQLite3

`ash
pip install numpy matplotlib
`

## Running SLAM

`ash
cd slam_implementation
python Slam.py
`

> **Note**: Large rosbag raw data files (.db3) and hardware SDK driver packages are excluded from this repository to stay within GitHub file size limits.
