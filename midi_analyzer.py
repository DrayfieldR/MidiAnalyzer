import argparse
import os
import pretty_midi

def analyze_midi(input_file, output_folder):
    try:
        # Check if the input file exists
        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        # Load the input MIDI file
        midi_file = pretty_midi.PrettyMIDI(input_file)

        # Create an output directory
        os.makedirs(output_folder, exist_ok=True)

        # Create a subdirectory for the input file's name
        input_file_name = os.path.splitext(os.path.basename(input_file))[0]
        output_dir = os.path.join(output_folder, input_file_name)
        os.makedirs(output_dir, exist_ok=True)

        # Get the list of instruments in the MIDI file
        instruments = midi_file.instruments

        # Create a file to combine all instrument notes
        combined_output_file = os.path.join(output_dir, "combined.txt")
        with open(combined_output_file, 'w') as combined_file:
            for instrument in instruments:
                combined_file.write(f"Instrument Name: {instrument.name}\n")
                for note in instrument.notes:
                    combined_file.write(f"Note: {note.pitch}, Start Time: {note.start}, End Time: {note.end}, Velocity: {note.velocity}\n")

        # Loop through the instruments and analyze their notes individually
        for instrument in instruments:
            instrument_output_file = os.path.join(output_dir, f"{instrument.name}.txt")
            with open(instrument_output_file, 'w') as f:
                f.write(f"Instrument Name: {instrument.name}\n")
                for note in instrument.notes:
                    f.write(f"Note: {note.pitch}, Start Time: {note.start}, End Time: {note.end}, Velocity: {note.velocity}\n")

        # Get the tempo
        tempo = midi_file.get_tempo()
        tempo_output_file = os.path.join(output_dir, "tempo.txt")
        with open(tempo_output_file, 'w') as f:
            f.write(f"Tempo: {tempo} BPM\n")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MIDI File Analyzer")
    parser.add_argument("input_file", help="Input MIDI file to analyze")
    parser.add_argument("--output-folder", help="Output folder", default="Analyzed")
    args = parser.parse_args()

    analyze_midi(args.input_file, args.output_folder)
    print(f"Analysis results saved in the '{os.path.basename(args.input_file)}' directory within 'Analyzed'.")
