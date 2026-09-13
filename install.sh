#!/bin/bash

# simplevision2-heavy installer script
# Installs the enhanced Moondream2 image analysis tool

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INSTALL_DIR="/usr/local/bin"

echo "Installing simplevision2-heavy (Moondream2 model)..."

# Check if running as root
if [[ $EUID -eq 0 ]]; then
   echo "This script should not be run as root. Use sudo if needed."
   exit 1
fi

# Check Python 3 availability
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    exit 1
fi

# Check PyTorch availability (optional but recommended)
if ! python3 -c "import torch" &> /dev/null; then
    echo "Warning: PyTorch not found. Installing CPU version..."
    pip3 install torch
fi

# Copy the script to /usr/local/bin
echo "Installing to $INSTALL_DIR/simplevision2..."
sudo cp "$SCRIPT_DIR/simplevision2.py" "$INSTALL_DIR/simplevision2"
sudo chmod +x "$INSTALL_DIR/simplevision2"

echo "Installation complete!"
echo ""
echo "Usage examples:"
echo "  simplevision2 /path/to/image.jpg"
echo "  simplevision2 photo.jpg \"Describe the visual style and composition\""
echo ""
echo "Requirements:"
echo "  - Python 3.6+"
echo "  - pip3 install transformers Pillow torch"
echo "  - Optional: CUDA for GPU acceleration"
echo ""
echo "Run 'simplevision2 --help' for more information."
echo ""
echo "Binary location: $INSTALL_DIR/simplevision2"