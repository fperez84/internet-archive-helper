# Internet Archive Helper

This script is done literally for education purpose and also fun. I knew old
Club Nintendo Chile magazines are available at [Archive.org](https://archive.org),
but there are so many to do click-ops so I thought of automating this using python
(Plus, I'm looking to refine my python skills so this seems like the perfect
opportunity).

The script will perform a search on [Archive.org](https://archive.org) for
'Club Nintendo' and filter the results for Chilean issues only. Then it will
download them in a given directory.

For the above, the script is using internetarchive library and to prevent ban
is taking a two seconds delay between downloads.

## Features

- Searches Archive.org using the `internetarchive` library.
- Filters results by identifiers containing "chile" (case-insensitive).
- Downloads only PDF files, excluding those with the suffix `_text.pdf`.
- Allows configuring the destination directory for downloaded files.
- Implements a delay between downloads to avoid API rate limits.

---

## Installation

### Prerequisites

- Python 3.7 or higher.
- Internet access.

### Installing dependencies

1. Clone this repository:

   ```bash
   git clone https://github.com/fperez84/internet-archive-helper.git
   cd internet-archive-helper
    ```

1. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set the destination directory in the project's main file (main.py):

    ```python
    output_dir = Path("/your/destination/path")
    ```

1. Run the script

    ```bash
    python main.py
    ```

1. All downloaded files will be on output_dir

## Dependencies

- internetarchive: For interacting with Archive.org's API.
- pathlib: Advanced handling of paths and directories.
- time: Adds delays between downloads.

## Future Improvements

- Add automatic handling of HTTP errors.
- Implement configuration options via a .env file or command-line arguments.

## License

This project is licensed under the BSD 3-Clause License. See the LICENSE file
for more details.

## Note

This project is for educational purposes only and has no commercial intent.
Please respect copyright laws and Archive.org's usage policies.
