# FreeCAD Python Models

A collection of Python scripts for generating 3D models using FreeCAD.

## Overview

This repository contains Python scripts that use the FreeCAD Python API to generate 3D models of electronic components.

## Requirements

- FreeCAD 0.19 or later
- Python 3.x (bundled with FreeCAD)

## Installation

1. Install FreeCAD
   - Official website: https://www.freecad.org/downloads.php

2. Clone this repository
```bash
git clone <repository-url>
cd freecad-py
```

## Usage

### Running in FreeCAD GUI

1. Launch FreeCAD
2. Select "Macro" → "Macros..." from the menu
3. Select and execute the script file

### Running from Command Line

```bash
freecad Jack/RCA/aitendo-AV2-8.4-10GA.py
```

or

```bash
freecadcmd Jack/RCA/aitendo-AV2-8.4-10GA.py
```

## Export

Generated models can be exported from FreeCAD in various formats:

- STEP (.step, .stp)
- IGES (.iges, .igs)
- STL (.stl) - for 3D printing
- OBJ (.obj)
- Many other formats

### Export Method

In FreeCAD GUI:
1. Select "File" → "Export..."
2. Choose desired format and save

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## References

- [FreeCAD Official Website](https://www.freecad.org/)
- [FreeCAD Python API Documentation](https://wiki.freecad.org/Python_scripting_tutorial)
- [FreeCAD Part Module](https://wiki.freecad.org/Part_Module)
