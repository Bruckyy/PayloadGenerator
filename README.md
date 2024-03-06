# Payload Generator

The Payload Generator is a Python script that allows you to generate shellcode payloads targeting Linux and Windows operating systems for reverse connections.

## Installation

1. Clone the repository:

    ```
    git clone https://github.com/Bruckyy/PayloadGenerator.git
    ```

2. Navigate to the project directory:

    ```
    cd PayloadGenerator
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

The main script `main.py` accepts the following command-line arguments:

- `--linux`: Generate payload targeting Linux.
- `--windows`: Generate payload targeting Windows (not implemented yet).
- `-p`, `--port`: Specify the reverse connection port (required).
- `--ip`: Specify the reverse connection IPv4 (required).

To generate a payload targeting Linux:

```
python main.py --linux -p <port> --ip <IPv4>
```

Replace `<port>` with the desired port number and `<IPv4>` with the IPv4 address.

## Examples

Generating a payload targeting Linux:

```
python main.py --linux -p 4444 --ip 192.168.1.100
```
