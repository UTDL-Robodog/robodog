# Robodog

Welcome to the UTDL Robodog repository (2021-). This repository hosts the open-source code for the autonomous robotic quadruped (including a manipulator) created by the UTDL Robodog team.

## Cloning 

To clone the repository: `git clone https://github.com/UTDL-Robodog/robodog.git`

## Contributor Guidelines

Here we will outline the guidelines for contributions to the repository.

### Development Branches

To contribute a feature, branch from main with: `git checkout -b "feature_name"`

Proceed to make your changes in the branch. When complete, submit a merge request to main with testing documented (if possible).

### Merge Requests

Merge requests must be submitted for development branches to be merged into `main`. Each merge request **must be reviewed by an approved reviewer.** Please **do not** approve your own merge request (generally). Merge requests can be submitted via the web application. Please include:
- Feature description
- Summary of changes
- Any relevant testing

## Basic Coding Guidelines

This section will serve to outline some basic coding rules for this repository to keep things consistent. Please follow the following guidelines to the best of your ability.

- **Files:** files will follow a `snake_case` format. Ex. `gripper_kinematics.py`
- **Objects/Classes:** classes will follow the `PascalCase` format. Ex. `CameraInstance()`
- **Functions:** functions will follow a `camelCase` format. Ex. `produceBoundingBoxes()`

## Dependencies

This section will cover the main dependencies required to run the project, as well as provide links or instructions on how to install them.

### Programming Languages

- `Python 3`
- `C++`

### Packages

- `ROS`
