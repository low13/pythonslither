# Python Slither
This is an attempt I had at making a snake game in just a few hours.

The game itself is very basic, as it doesn't use any sprites. Instead, it relies on color and sound effects.

## Build
To build the game into a `.exe` file, follow these steps:

1. Install `pyinstaller` if it's not already installed:
   
   ```
   pip install pyinstaller
   ```
2. Use `pyinstaller` to generate the `.exe` file:

   ```
   pyinstaller PythonSlither.spec
   ```
3. Once that's done, the executable will be located in the `dist` folder.

Alternatively, you may download the final executable from the [Releases](https://github.com/low13/pythonslither/releases) page.
