# Data

The recorded point cloud bag is about 400 MB, which is over GitHub's file size limit, so only its [`metadata.yaml`](metadata.yaml) is kept here.

| | |
|---|---|
| Format | rosbag2, SQLite3 storage (`my_pointcloud_data_0.db3`) |
| Topic | `/rslidar_points` (`sensor_msgs/msg/PointCloud2`, CDR) |
| Messages | 898 |
| Duration | about 89.7 s |
| Recorded | 28 June 2024 |

To run the scripts, either record your own bag (see [docs/SETUP.md](../docs/SETUP.md#5-record-a-bag)) or ask the team for the original recording, then place the folder here:

```
data/my_pointcloud_data/
├── metadata.yaml
└── my_pointcloud_data_0.db3
```

`*.db3` files are ignored by git, so they will not be committed by accident.
