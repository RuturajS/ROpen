import argparse
import webbrowser
import re

def read_websites(filename):
    with open(filename, 'r') as file:
        websites = file.read().splitlines()
    return websites

def filter_websites(websites, protocol=None, is_ip=False):
    filtered_sites = []
    for site in websites:
        if protocol and not site.startswith(protocol):
            continue
        if is_ip:
            ip_pattern = re.compile(r'^(http://|https://)?(\d{1,3}\.){3}\d{1,3}')
            if not ip_pattern.match(site):
                continue
        filtered_sites.append(site)
    return filtered_sites

def open_search_tabs(websites, search_text, browser='default'):
    for site in websites:
        search_url = f"{site}/search?q={search_text}"
        if browser == 'chrome':
            chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open_new_tab(search_url)
        else:
            webbrowser.open_new_tab(search_url)

def main():
    parser = argparse.ArgumentParser(description='Open websites with search query in browser tabs.')
    parser.add_argument('-f', '--file', type=str, required=True, help='Path to file containing list of websites')
    parser.add_argument('-o', '--open', type=str, help='Number of websites to open or "all"')
    parser.add_argument('-s', '--search', type=str, required=True, help='Search query text')
    parser.add_argument('-p', '--protocol', type=str, choices=['http', 'https'], help='Filter by protocol (http or https)')
    parser.add_argument('-ip', '--ip', action='store_true', help='Filter by IP addresses only')
    parser.add_argument('-b', '--browser', type=str, default='default', choices=['default', 'chrome'], help='Browser to use (default or chrome)')

    args = parser.parse_args()

    websites = read_websites(args.file)
    if args.protocol:
        protocol = f"{args.protocol}://"
        websites = filter_websites(websites, protocol=protocol)
    if args.ip:
        websites = filter_websites(websites, is_ip=True)

    if args.open and args.open != 'all':
        websites = websites[:int(args.open)]

    if not websites:
        print("No websites to open based on the provided criteria.")
        return

    open_search_tabs(websites, args.search, args.browser)

if __name__ == "__main__":
    main()
