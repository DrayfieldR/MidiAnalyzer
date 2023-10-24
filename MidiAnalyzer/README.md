# MIDI Analyzer and Converter

## Introduction

The MIDI Analyzer and Converter is a versatile tool designed to help you work with MIDI files. Whether you want to analyze MIDI files and generate text reports or convert text files into MIDI, this tool provides an efficient and user-friendly solution.

### Why Use This Tool

The world of MIDI files is vast, encompassing a variety of musical compositions and instrument arrangements. This tool empowers you to gain insights into the structure and content of MIDI files, allowing you to:

- Study and analyze the composition of MIDI tracks and instruments.
- Create your custom text annotations of MIDI files.
- Convert your textual music compositions into MIDI format.

This documentation will guide you through the installation, usage, and features of the tool.

## Installation

Before you can start using the MIDI Analyzer and Converter, make sure you have Python 3.x installed on your system. If you haven't already installed Python, you can download it from the official website: [https://www.python.org/](https://www.python.org/).

To install the required Python library `pretty_midi`, open your terminal or command prompt and enter the following command:

pip install pretty_midi

## Directory Structure

- Midi Analyzer (root directory) contains the main Python scripts and log files.
- Analyzed is where the tool stores the analyzed data of MIDI files.
- Processed Midi is where the tool saves the converted MIDI files.
- The two Python scripts, midi_analyzer.py and txt_to_midi_converter.py, are essential components of the tool.

## Using the Tool

The tool provides both a Graphical User Interface (GUI) and a Command-Line Interface (CLI) to meet your MIDI analysis and conversion needs.

### Graphical User Interface (GUI)

MIDI Analyzer (Drag-and-Drop)

1. Drag and drop MIDI files onto the onto midi_analyzer.py file to analyze them.
2. The analyzed results are saved in the 'Analyzed' directory.

![image](https://github.com/DrayfieldR/MidiAnalyzer/assets/148846964/837f77fd-9f84-4cc8-b91e-6e2c314e9b0c)

### Command-Line Interface (CLI)

Convert a text file to MIDI:

1. run the py file

python txt_to_midi_converter.py

2. You will be prompted to select a folder
3. You will be prompted to select a file
4. The converted txt to midi file will be in the 'Processed Midi' direcotry.

## License

This tool is distributed under the MIT License, which grants you the freedom to modify and distribute it according to your needs. Please see the LICENSE file in your project's root directory for detailed license terms.

## Contact

For additional assistance or questions, please contact the developer, Daniel Robinson, at Robinson.D.Rayfield@gmail.com
