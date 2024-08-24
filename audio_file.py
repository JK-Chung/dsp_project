import scipy.io.wavfile as wavf

def read_wav_file(wav_file_path):
  return wavf.read(wav_file_path)