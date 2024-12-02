import numpy as np
from scipy.io import wavfile

def snr_noise_reduction(input_file, output_file, snr_threshold=10):
    # Read the input audio file
    fs, audio_data = wavfile.read(input_file)

    # Estimate noise by using a simple assumption (first 10% as noise)
    noise_data = audio_data[:len(audio_data)//10]
    noise_power = np.mean(noise_data**2)
    
    # Compute signal power (assuming remaining part of the audio)
    signal_data = audio_data[len(audio_data)//10:]
    signal_power = np.mean(signal_data**2)
    
    # Calculate the SNR (in dB)
    snr = 10 * np.log10(signal_power / noise_power)

    if snr < snr_threshold:
        # Apply simple noise suppression based on SNR threshold
        noise_estimate = np.mean(audio_data[:len(audio_data)//10])
        audio_data = np.maximum(audio_data - noise_estimate, 0)  # Remove noise
    
    # Write the output audio file
    wavfile.write(output_file, fs, audio_data.astype(np.int16))

# Example usage
snr_noise_reduction('input.wav', 'output.wav', snr_threshold=15)
