# OlympicCoder-7B UI

A simple web interface for interacting with the OlympicCoder-7B model, a 7B parameter code generation model.

## Features

- User-friendly web interface built with Streamlit
- Adjustable parameters (temperature, max tokens)
- Syntax-highlighted code output
- Raw API response viewer

## Requirements

- Python 3.12+
- CUDA 12.4+ compatible GPU
- vLLM
- Streamlit
- OlympicCoder-7B model files

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/2Rebfl/olympic-coder-ui.git
   cd olympic-coder-ui
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv olympic-env
   source olympic-env/bin/activate
   pip install -r requirements.txt
   ```

3. Download the OlympicCoder-7B model:
   ```bash
   # Using Hugging Face CLI
   huggingface-cli download open-r1/OlympicCoder-7B --local-dir ~/olympic-coder-7b
   
   # Or using Git LFS
   git lfs install
   git clone https://huggingface.co/open-r1/OlympicCoder-7B ~/olympic-coder-7b
   ```

## Usage

1. Start the vLLM API server:
   ```bash
   export LD_LIBRARY_PATH=/usr/local/cuda-12.4/targets/x86_64-linux/lib:$LD_LIBRARY_PATH
   python -m vllm.entrypoints.api_server --model ~/olympic-coder-7b --port 8000 --max-model-len 4096 --gpu-memory-utilization 0.95
   ```

2. Start the Streamlit UI:
   ```bash
   streamlit run olympic_ui.py --server.port 8501
   ```

3. Access the UI in your browser:
   - Local: http://localhost:8501
   - Remote: Set up port forwarding with `ssh -L 8501:localhost:8501 user@server`

## Troubleshooting

- **CUDA library not found**: Ensure the CUDA libraries are in your LD_LIBRARY_PATH
- **Out of memory errors**: Reduce the `max-model-len` parameter
- **API connection errors**: Make sure the vLLM server is running on port 8000

## License

This project is licensed under the MIT License - see the LICENSE file for details.
