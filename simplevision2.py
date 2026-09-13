#!/usr/bin/env python3
"""
simplevision2 - Enhanced image analysis using Moondream2

Usage:
    simplevision2 /path/to/image.jpg [prompt]

Example:
    simplevision2 photo.jpg
    simplevision2 video_frame.jpg "Describe the visual style and composition"
"""

import sys
from PIL import Image
import torch

torch.set_num_threads(8)  # Use 4 CPU threads for faster inference

from transformers import AutoModelForCausalLM

def main():
    if len(sys.argv) < 2:
        print("Usage: simplevision2 /path/to/image.jpg [prompt]")
        print("  prompt: optional custom question (default: 'Describe this image in detail')")
        sys.exit(1)

    try:
        # Auto-detect GPU, fallback to CPU
        if torch.cuda.is_available():
            print("Using GPU (CUDA) - faster processing")
        else:
            print("GPU not found - using CPU (slower)")

        print("Loading Moondream2 model (first run may take a moment)...")
        model = AutoModelForCausalLM.from_pretrained(
            "vikhyatk/moondream2",
            trust_remote_code=True,
            dtype=torch.float32,
        )
        if torch.cuda.is_available():
            model = model.to("cuda")

        # Default or custom prompt
        prompt = sys.argv[2] if len(sys.argv) > 2 else "Describe this image in detail."

        # Process image (native Moondream API accepts a PIL image directly)
        print(f"Processing: {sys.argv[1]}")
        image = Image.open(sys.argv[1]).convert("RGB")

        answer = model.query(question=prompt, image=image)

        print("\nAnalysis Result:")
        print(answer["answer"].strip())

    except FileNotFoundError:
        print(f"Error: Image file '{sys.argv[1]}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
