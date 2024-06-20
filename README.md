# ROpen
Open bulk Tab using domain list on chrome tab.

#Ruturaj Script for RTool ROpen


### Explanation

1. **`parser.add_argument('-f', '--file', type=str, required=True, help='Path to file containing list of websites')`**:
   - This line makes the file path argument required. The user must provide the path to `websites.txt`.

2. **Handling Browser Path for Chrome**:
   - The script uses a hard-coded path to the Chrome executable. Adjust this path if Chrome is installed in a different location on your system.
  
###installation
 **`Install Vie Git`**
 ```sh
git clone https://github.com/RuturajS/ROpen.git & cd Ropen
mkdir +7 search.py
pip install -r requirements.txt
python3 search.py -h
```
 

### Running the Script

1. **Save the Python Script**:
   - Save the above Python script as `search.py`.

2. **Run the Script with Different Options**:
   - **Specify the path to `websites.txt` and open the first 10 domains**:
     ```sh
     python search.py -f "path/to/websites.txt" -s "YOUR_SEARCH_QUERY" -o 10
     ```
   - **Open all domains**:
     ```sh
     python search.py -f "path/to/websites.txt" -s "YOUR_SEARCH_QUERY" -o all
     ```
   - **Open only `http://` domains**:
     ```sh
     python search.py -f "path/to/websites.txt" -s "YOUR_SEARCH_QUERY" -p http
     ```
   - **Open only `https://` domains**:
     ```sh
     python search.py -f "path/to/websites.txt" -s "YOUR_SEARCH_QUERY" -p https
     ```
   - **Open only IP addresses**:
     ```sh
     python search.py -f "path/to/websites.txt" -s "YOUR_SEARCH_QUERY" -ip
     ```
   - **Open in Chrome**:
     ```sh
     python search.py -f "path/to/websites.txt" -s "YOUR_SEARCH_QUERY" -b chrome
     ```

### Help Text

You can view the help text for all available commands and options by running:

```sh
python search.py -h
```

This will display:

```plaintext
usage: search.py [-h] -f FILE [-o OPEN] -s SEARCH [-p {http,https}] [-ip] [-b {default,chrome}]

Open websites with search query in browser tabs.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Path to file containing list of websites
  -o OPEN, --open OPEN  Number of websites to open or "all"
  -s SEARCH, --search SEARCH
                        Search query text (required)
  -p {http,https}, --protocol {http,https}
                        Filter by protocol (http or https)
  -ip, --ip             Filter by IP addresses only
  -b {default,chrome}, --browser {default,chrome}
                        Browser to use (default or chrome)
```

### Notes

- Ensure the path to `websites.txt` is correct when you run the script.
- Replace `"YOUR_SEARCH_QUERY"` with the actual search text you want to use.
- Adjust the Chrome executable path if needed.
- This script assumes that the `webbrowser` module can open Chrome directly. If it doesn't work, you might need to configure the `webbrowser` module to locate the Chrome executable on your system.
