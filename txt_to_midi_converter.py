import os
import pretty_midi
import tkinter as tk
from tkinter import filedialog
import time

def convert_txt_to_midi(txt_file, output_midi_file, output_folder):
    # Create a PrettyMIDI object
    midi_data = pretty_midi.PrettyMIDI()

    # Create an Instrument
    instrument = pretty_midi.Instrument(0)

    # Read note data from the text file and add notes to the instrument
    with open(txt_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith("Note: "):
                parts = line.strip().split(", ")
                note_info = parts[0].split(": ")[1].split("/")
                pitch = int(note_info[0])
                start_time = float(parts[1].split(": ")[1])
                end_time = float(parts[2].split(": ")[1])
                velocity = int(parts[3].split(": ")[1])
                note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start_time, end=end_time)
                instrument.notes.append(note)

    # Add the instrument to the MIDI data
    midi_data.instruments.append(instrument)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Write the MIDI data to a file within the output folder
    midi_data.write(os.path.join(output_folder, output_midi_file))

def select_folder_and_file():
    # Create the main GUI window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Display a message to select a folder and wait for 5 seconds
    print("Please select a folder...")
    time.sleep(1)

    # Ask the user to select a folder from the "Analyzed" directory
    folder_selected = filedialog.askdirectory(initialdir="Analyzed", title="Select a folder from 'Analyzed'")
    if not folder_selected:
        print("No folder selected. Exiting.")
        return

    # List files in the selected folder
    files_in_folder = os.listdir(folder_selected)

    # Display a message to select a file and wait for 5 seconds
    print("Please select a file...")
    time.sleep(1)

    # Ask the user to select a file to process
    file_selected = filedialog.askopenfilename(initialdir=folder_selected, title="Select a file to process", filetypes=[("Text files", "*.txt")])
    if not file_selected:
        print("No file selected. Exiting.")
        return

    # Process the selected file
    txt_file_name = os.path.basename(file_selected)
    output_folder = os.path.join("Processed Midi", os.path.basename(folder_selected))
    midi_output_file = os.path.splitext(txt_file_name)[0] + ".mid"
    convert_txt_to_midi(file_selected, midi_output_file, output_folder)
    print(f"Conversion complete. MIDI file saved as '{output_folder}/{midi_output_file}'.")

if __name__ == '__main__':
    select_folder_and_file()
