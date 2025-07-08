# 🗣️ Speech Recognition Tool

A powerful and user-friendly speech-to-text application built with Streamlit and OpenAI's Whisper model. Transform your audio files and voice recordings into accurate text transcriptions with just a few clicks.

## ✨ Features

- **Multiple Input Methods**: Upload audio files or record directly in your browser
- **Format Support**: Works with MP3 and WAV audio files
- **Real-time Recording**: Built-in voice recording functionality
- **Accurate Transcription**: Powered by OpenAI's Whisper-small model
- **Download Transcripts**: Save your transcriptions as text files
- **Clean Interface**: Intuitive tabbed layout with modern styling

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. Clone or download this repository

2. Install FFmpeg (required for audio processing):
   - **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use `winget install ffmpeg`
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt install ffmpeg` (Ubuntu/Debian) or `sudo yum install ffmpeg` (CentOS/RHEL)

3. Install Python dependencies:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

### Requirements File

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit>=1.28.0
transformers>=4.35.0
pydub>=0.25.1
torch>=2.0.0
```

4. Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

### Python Packages
- **streamlit**: Web application framework
- **transformers**: Hugging Face transformers library for AI models
- **pydub**: Audio file processing and format conversion
- **torch**: PyTorch for model inference

### System Dependencies
- **FFmpeg**: Required for audio format conversion and processing

## 🎯 How to Use

### Upload Audio Files
1. Click on the "🎧 Upload Audio File" tab
2. Upload your MP3 or WAV file using the file uploader
3. Wait for the transcription to complete
4. View your transcript and download it as a text file

### Record Your Voice
1. Switch to the "🎤 Record Your Voice" tab
2. Click the record button and speak into your microphone
3. Stop recording when finished
4. The app will automatically transcribe your recording
5. Download your transcript as needed

## 🔧 Technical Details

### Model Information
- **ASR Model**: OpenAI Whisper-small
- **Language Support**: Multilingual (99 languages)
- **Accuracy**: High-quality transcription for clear audio

### Audio Processing
- Automatic format conversion to WAV for optimal processing
- Temporary file handling for security and performance
- Support for various audio formats through pydub

### Performance Features
- Model caching for faster subsequent usage
- Efficient temporary file management
- Real-time processing indicators

## 🎨 Interface Features

- **Responsive Design**: Works on desktop and mobile devices
- **Progress Indicators**: Visual feedback during transcription
- **Clean Layout**: Modern, user-friendly interface
- **Download Functionality**: Easy transcript export

## 🛠️ Customization

You can modify the application by:

- Changing the Whisper model (e.g., `whisper-base`, `whisper-large`)
- Adding support for additional audio formats
- Customizing the UI styling in the CSS section
- Implementing additional export formats

## 📋 System Requirements

- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: 1GB free space for model files
- **Internet**: Required for initial model download
- **Browser**: Modern web browser with microphone support

## 🔍 Troubleshooting

### Common Issues

**Model Loading Issues**
- Ensure stable internet connection for initial download
- Check available disk space for model files

**Audio Upload Problems**
- Verify file format is MP3 or WAV
- Check file size (very large files may cause timeouts)

**Audio Processing Dependencies**
- Verify FFmpeg is installed and accessible in your PATH
- Check audio file integrity and format compatibility

**Recording Issues**
- Grant microphone permissions in your browser
- Ensure microphone is working properly

**Performance Issues**
- Close other applications to free up RAM
- Consider using a smaller Whisper model for faster processing

## 🤝 Contributing

Feel free to contribute to this project by:
- Reporting bugs or issues
- Suggesting new features
- Submitting pull requests
- Improving documentation

## 🙏 Acknowledgments

- OpenAI for the Whisper model
- Hugging Face for the transformers library
- Streamlit team for the excellent web framework
- pydub developers for audio processing capabilities

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section above
2. Review the error messages carefully
3. Ensure all dependencies are properly installed
4. Verify your system meets the minimum requirements

---

**Built with using Streamlit and OpenAI Whisper**

## ⚠️ Disclaimer:
This project was developed during an internship. It is intended for personal portfolio purposes only.
All rights reserved. Please do not reuse or redistribute without permission.
