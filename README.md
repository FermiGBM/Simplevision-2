# simplevision2 - Enhanced Image Analysis with Moondream2

A powerful Python tool for detailed image analysis using Moondream2, an advanced multimodal AI model. Supports custom prompting and GPU acceleration for enhanced performance.

## Features

- **Advanced AI**: Uses Moondream2 model for sophisticated image understanding
- **Custom Prompts**: Ask specific questions about images
- **GPU Acceleration**: Automatic CUDA detection for faster processing
- **Detailed Analysis**: Comprehensive image understanding and description
- **Flexible**: Works with various image formats and sizes

## Installation

### Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/FermiGBM/simplevision2-heavy.git
cd simplevision2-heavy

# Run the installer
chmod +x install.sh
sudo ./install.sh
```

### Manual Installation

```bash
# Make the script executable
chmod +x simplevision2.py

# Copy to system path
sudo cp simplevision2.py /usr/local/bin/simplevision2
```

### Requirements

- Python 3.6+
- Required Python packages:
  ```bash
  pip3 install transformers Pillow torch
  ```

### Optional (Recommended)

For GPU acceleration:
```bash
# Install PyTorch with CUDA support
# Visit https://pytorch.org/get-started/locally/ for specific commands
# Example for CUDA 11.8:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## Usage

### Basic Usage

```bash
# Generate detailed image analysis
simplevision2 /path/to/image.jpg

# Example
simplevision2 photo.jpg
```

### With Custom Prompts

```bash
# Ask specific questions about the image
simplevision2 image.jpg "What objects are visible in this scene?"
simplevision2 photo.jpg "Describe the visual style and composition"
simplevision2 screenshot.png "What text is visible in this image?"
simplevision2 artwork.jpg "What artistic techniques are used here?"
```

### Command Line

```bash
simplevision2 <image_path> [prompt]
```

**Arguments:**
- `image_path`: Path to the image file (required)
- `prompt`: Optional custom question (default: "Describe this image in detail")

**Examples:**
```bash
# Default analysis
simplevision2 ./my_photo.jpg

# Custom prompt
simplevision2 ./my_photo.jpg "What emotions are conveyed in this image?"

# Analysis of specific elements
simplevision2 ./screenshot.png "What text is visible in this image?"

# Artistic analysis
simplevision2 ./painting.jpg "What artistic style does this represent?"
```

## Model Details

- **Model**: vikhyatk/moondream2
- **Type**: Multimodal LLM with vision capabilities
- **Size**: ~4.7GB (downloaded on first run)
- **Speed**: Slower but more detailed than BLIP
- **Language**: English
- **Capabilities**: Complex reasoning, detailed descriptions, object recognition

## Performance

- **Download Time**: ~2-3 minutes (first run)
- **Inference Time**: ~5-15 seconds per image (CPU), ~1-3 seconds (GPU)
- **Memory Usage**: ~4-8GB RAM (CPU), ~6-12GB (GPU)
- **Storage**: ~4.7GB model cache
- **GPU Support**: Automatic CUDA detection

## GPU Acceleration

The tool automatically detects and uses GPU if available:

```bash
# First run with GPU
simplevision2 photo.jpg
# Output: "Using GPU (CUDA) - faster processing"

# First run without GPU
simplevision2 photo.jpg  
# Output: "GPU not found - using CPU (slower)"
```

## Examples

### Image Description
```bash
simplevision2 landscape.jpg
# Output: "A beautiful mountain landscape with snow-capped peaks, a blue lake in the foreground, and pine trees along the shoreline. The sky is clear with scattered clouds."
```

### Object Recognition
```bash
simplevision2 living_room.jpg "What furniture items are visible?"
# Output: "The living room contains a sofa, coffee table, armchair, bookshelf, television stand, and several lamps. There are also curtains covering large windows."
```

### Text Extraction
```bash
simplevision2 document.jpg "What text is visible in this document?"
# Output: "The document contains a formal letter with the header 'CONFIDENTIAL', addressed to 'John Doe', and discusses quarterly financial results and performance metrics."
```

## Troubleshooting

### Common Issues

1. **"ModuleNotFoundError"**
   ```bash
   pip3 install transformers Pillow torch
   ```

2. **"CUDA not available"**
   - Install PyTorch with CUDA support
   - Visit https://pytorch.org/get-started/locally/ for installation instructions

3. **"Model download failed"**
   - Check internet connection
   - Model is ~4.7GB, ensure sufficient disk space
   - Try running again (model cache is persistent)

4. **"Out of memory"**
   - Close other memory-intensive applications
   - Use smaller images
   - Consider using CPU mode if GPU memory is insufficient

### First Run

The first time you run simplevision2, it will automatically download the Moondream2 model (~4.7GB). This may take several minutes.

```bash
# First run - downloads model
simplevision2 photo.jpg

# Subsequent runs - uses cached model
simplevision2 photo.jpg
```

## Comparison with simplevision-light

| Feature | simplevision-light | simplevision2-heavy |
|---------|-------------------|-------------------|
| Model | BLIP base | Moondream2 |
| Size | ~1.3GB | ~4.7GB |
| Speed | Fast | Slower (but GPU supported) |
| Prompting | Fixed | Custom prompts |
| Detail Level | Basic | Detailed, complex reasoning |
| GPU Support | CPU only | GPU/CPU auto |
| Memory | 2-4GB | 4-12GB |
| Use Case | Quick captions | Deep analysis |

## License

MIT License - see LICENSE file for details.

## Changelog

### v1.0.0
- Initial release
- Moondream2 model integration
- Custom prompting support
- GPU/CPU auto-detection
- Enhanced error handling
