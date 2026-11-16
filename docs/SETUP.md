# Setup: Helios 16P on ROS 2 Galactic

These are the steps we followed on Ubuntu 20.04. They follow our [short manual](short_manual.odt) and [project report](project_report.pdf).

## 1. Install ROS 2 Galactic

Follow the official guide: https://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Debians.html

In short: add the ROS 2 apt sources, install `ros-galactic-desktop`, initialise `rosdep`, then source the environment in every new shell:

```bash
source /opt/ros/galactic/setup.bash
```

## 2. Build the RoboSense driver

Clone the driver packages into a workspace and build with `colcon`:

```bash
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone --recursive https://github.com/RoboSense-LiDAR/rslidar_sdk.git
git clone https://github.com/RoboSense-LiDAR/rslidar_msg.git
cd ~/ros2_ws
colcon build
source install/setup.bash
```

Check the `rslidar_sdk` README for its build dependencies (`libyaml-cpp-dev`, `libpcap-dev`) and for selecting the ROS 2 build in its `CMakeLists.txt`.

## 3. Configure the Helios 16P

Connect the LiDAR to the PC over Ethernet and put the PC's network interface on the same subnet as the sensor.

Copy our [config.yaml](../config/rslidar_sdk/config.yaml) over `rslidar_sdk/config/config.yaml`. The settings that matter:

| Key | Value |
|---|---|
| `msg_source` | `1` (live LiDAR) |
| `lidar_type` | `RSHELIOS_16P` |
| `msop_port` / `difop_port` | `6699` / `7788` |
| `ros_send_point_cloud_topic` | `/rslidar_points` |

Rebuild after changing the config.

## 4. Run the driver and check in RViz2

```bash
ros2 launch rslidar_sdk start.py
```

This starts the driver node and RViz2. Set the fixed frame to `rslidar` and add a PointCloud2 display on `/rslidar_points`. A live point cloud means the sensor works.

## 5. Record a bag

In a second terminal (with the workspace sourced):

```bash
ros2 bag record /rslidar_points -o my_pointcloud_data
```

Stop with `Ctrl+C`. You get a folder with `metadata.yaml` and `my_pointcloud_data_0.db3`.

## 6. Build the map

Point `db_path` in [`src/slam.py`](../src/slam.py) at the `.db3` file and run it. See the main [README](../README.md#quick-start).

## Troubleshooting we ran into

- Version mismatches between the driver, Ubuntu and ROS 2 releases. Stick to Ubuntu 20.04 with Galactic.
- No points in RViz2: usually the network interface is on the wrong subnet, or a firewall blocks UDP ports 6699/7788.
- RViz2 shows nothing even though the topic publishes: the fixed frame does not match `ros_frame_id` (`rslidar`).
