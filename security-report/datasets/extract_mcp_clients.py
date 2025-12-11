#!/usr/bin/env python3
"""
Script to extract MCP client information from two HTML source files:
1. punkpeye-awesome-mcp-clients-refs-heads-main-README.md (GitHub HTML page)
2. modelcontextprotocol.io-clients.html (official MCP clients page)

Output: CSV file with columns: MCP Client Name, MCP Client Main URL, MCP Client Source Code URL
"""

import re
import csv
import json
from bs4 import BeautifulSoup
from pathlib import Path


def extract_from_punkpeye(filepath: str) -> list[dict]:
    """
    Extract MCP client info from the punkpeye awesome-mcp-clients GitHub page.
    The README content is embedded in a JSON blob within a script tag.
    """
    clients = []

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the embedded JSON data with the README content
    script_tag = soup.find('script', {'type': 'application/json', 'data-target': 'react-app.embeddedData'})
    if not script_tag:
        print("Warning: Could not find embedded JSON data in punkpeye file")
        return clients

    try:
        data = json.loads(script_tag.string)
        payload = data.get('payload', {})
        blob = payload.get('blob', {})

        # Get the table of contents - level 3 headings are the client names
        header_info = blob.get('headerInfo', {})
        toc = header_info.get('toc', [])

        # Get all client names from level 3 headings (these are the clients)
        client_names = [item['text'].strip() for item in toc if item.get('level') == 3]

        # Also try to get the rich text content to extract URLs
        rich_text = blob.get('richText', '')

        # Parse the rich text HTML to extract URLs for each client
        if rich_text:
            rich_soup = BeautifulSoup(rich_text, 'html.parser')

            # Find all h3 headings - each represents a client
            for h3 in rich_soup.find_all('h3', class_='heading-element'):
                name = h3.get_text(strip=True)
                if not name:
                    continue

                main_url = ""
                source_url = ""

                # Find the next table which contains client info
                # Look through siblings and their children for the info table
                parent = h3.parent
                current = parent.find_next_sibling() if parent else h3.find_next_sibling()

                while current and current.name != 'div':  # div typically contains next h3
                    # Check for markdown-accessiblity-table or table
                    tables = []
                    if current.name == 'markdown-accessiblity-table':
                        tables = current.find_all('table')
                    elif current.name == 'table':
                        tables = [current]
                    elif hasattr(current, 'find_all'):
                        tables = current.find_all('table')

                    for table in tables:
                        rows = table.find_all('tr')
                        for row in rows:
                            th = row.find('th')
                            td = row.find('td')
                            if th and td:
                                header = th.get_text(strip=True).lower()
                                link = td.find('a')
                                cell_text = td.get_text(strip=True)

                                if header == 'github' and link:
                                    href = link.get('href', '')
                                    if href and not href.startswith('#'):
                                        source_url = href
                                        if not main_url:
                                            main_url = href
                                elif header == 'website' and link:
                                    href = link.get('href', '')
                                    if href and not href.startswith('#') and cell_text != '-':
                                        main_url = href
                                elif header == 'gitlab' and link:
                                    href = link.get('href', '')
                                    if href and not href.startswith('#'):
                                        if not source_url:
                                            source_url = href
                                        if not main_url:
                                            main_url = href

                    current = current.find_next_sibling()

                if name and (main_url or source_url):
                    # If only source_url found, use it as main_url too
                    if not main_url:
                        main_url = source_url
                    clients.append({
                        'name': name,
                        'main_url': main_url,
                        'source_url': source_url
                    })

        # If we couldn't get URLs from richText, use client names with placeholder
        if not clients and client_names:
            print(f"  Using client names from TOC (URLs not extracted from richText)")
            for name in client_names:
                clients.append({
                    'name': name,
                    'main_url': '',
                    'source_url': ''
                })

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")

    return clients


def extract_from_modelcontextprotocol(filepath: str) -> tuple[list[dict], set[str]]:
    """
    Extract MCP client info from the modelcontextprotocol.io clients page.
    This page has a main table with client information (first column has client name + link).

    Returns:
        tuple: (list of client dicts, set of normalized client names for lookup)
    """
    clients = []
    client_names_normalized = set()

    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # Find the main clients table - it has columns:
    # Client, Resources, Prompts, Tools, Discovery, Sampling, Roots, Elicitation, Instructions
    tables = soup.find_all('table')

    for table in tables:
        rows = table.find_all('tr')

        # Check if this is the clients table by looking at header
        header_row = rows[0] if rows else None
        if header_row:
            headers = [th.get_text(strip=True).lower() for th in header_row.find_all(['th', 'td'])]
            # Look for the clients table signature
            if 'client' not in headers:
                continue

        # Process data rows (skip header)
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])
            if not cells:
                continue

            # First cell has the client name with a link
            first_cell = cells[0]
            link = first_cell.find('a')

            if link and link.get('href'):
                href = link.get('href')
                name = link.get_text(strip=True)

                if not name or len(name) < 2:
                    continue

                source_url = ""
                main_url = href

                if 'github.com' in href or 'gitlab.com' in href:
                    source_url = href

                clients.append({
                    'name': name,
                    'main_url': main_url,
                    'source_url': source_url
                })

                # Track normalized name for lookup
                client_names_normalized.add(normalize_name(name))

    return clients, client_names_normalized


def normalize_name(name: str) -> str:
    """
    Normalize a client name for deduplication.
    Handles variations like spaces vs hyphens, different casing, etc.
    """
    # Convert to lowercase
    result = name.lower().strip()
    # Normalize spaces and hyphens
    result = result.replace('-', ' ').replace('_', ' ')
    # Remove multiple spaces
    while '  ' in result:
        result = result.replace('  ', ' ')
    return result


def merge_clients(list1: list[dict], list2: list[dict], mcp_official_names: set[str]) -> list[dict]:
    """
    Merge two lists of clients, avoiding duplicates based on normalized name.
    Tracks whether each client is listed on modelcontextprotocol.io.

    Args:
        list1: First list of clients (e.g., from punkpeye)
        list2: Second list of clients (e.g., from modelcontextprotocol.io)
        mcp_official_names: Set of normalized names that appear on modelcontextprotocol.io
    """
    merged = {}

    for client in list1 + list2:
        name = client['name'].strip()
        name_normalized = normalize_name(name)

        if name_normalized not in merged:
            merged[name_normalized] = {
                'name': name,
                'main_url': client['main_url'],
                'source_url': client['source_url'],
                'listed_on_mcp_official': name_normalized in mcp_official_names
            }
        else:
            # Update if we have better info
            existing = merged[name_normalized]
            if not existing['main_url'] and client['main_url']:
                existing['main_url'] = client['main_url']
            if not existing['source_url'] and client['source_url']:
                existing['source_url'] = client['source_url']

    return sorted(merged.values(), key=lambda x: x['name'].lower())


def write_csv(clients: list[dict], output_path: str):
    """Write clients to CSV file."""
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['MCP Client Name', 'MCP Client Main URL', 'MCP Client Source Code URL', 'Listed In modelcontextprotocol.io'])
        for client in clients:
            writer.writerow([
                client['name'],
                client['main_url'],
                client['source_url'],
                'Yes' if client.get('listed_on_mcp_official', False) else 'No'
            ])


def sanitize_filename(name: str) -> str:
    """
    Convert a client name to a safe filename.
    Replaces problematic characters and normalizes spacing.
    """
    # Replace characters that are problematic in filenames
    replacements = {
        '/': '-',
        '\\': '-',
        ':': '-',
        '*': '',
        '?': '',
        '"': '',
        '<': '',
        '>': '',
        '|': '',
        ' ': '-',
    }
    result = name
    for char, replacement in replacements.items():
        result = result.replace(char, replacement)

    # Remove multiple consecutive dashes
    while '--' in result:
        result = result.replace('--', '-')

    # Remove leading/trailing dashes
    result = result.strip('-')

    return result


def write_markdown_files(clients: list[dict], output_dir: str):
    """
    Write individual markdown files for each client with YAML frontmatter.
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for client in clients:
        name = client['name']
        main_url = client['main_url']
        source_url = client['source_url']

        # Create safe filename
        filename = sanitize_filename(name) + '.md'
        filepath = output_path / filename

        # Build YAML frontmatter
        yaml_lines = [
            '---',
            f'title: "{name}"',
        ]

        if main_url:
            yaml_lines.append(f'main_url: "{main_url}"')
        else:
            yaml_lines.append('main_url: ""')

        if source_url:
            yaml_lines.append(f'source_code_url: "{source_url}"')
        else:
            yaml_lines.append('source_code_url: ""')

        yaml_lines.append('---')
        yaml_lines.append('')
        yaml_lines.append(f'# {name}')
        yaml_lines.append('')
        yaml_lines.append('## Notes')
        yaml_lines.append('')
        yaml_lines.append('<!-- Add notes and information about this MCP client here -->')
        yaml_lines.append('')

        content = '\n'.join(yaml_lines)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return len(clients)


def main():
    base_dir = Path(__file__).parent

    punkpeye_file = base_dir / "punkpeye-awesome-mcp-clients-refs-heads-main-README.md"
    mcp_official_file = base_dir / "modelcontextprotocol.io-clients.html"
    output_file = base_dir / "mcp-clients.csv"
    markdown_dir = base_dir / "mcp-client-dataset"

    print("Extracting clients from punkpeye awesome-mcp-clients...")
    punkpeye_clients = extract_from_punkpeye(str(punkpeye_file))
    print(f"  Found {len(punkpeye_clients)} entries")

    print("\nExtracted clients from punkpeye:")
    for c in punkpeye_clients[:10]:
        print(f"  - {c['name']}: {c['main_url']}")
    if len(punkpeye_clients) > 10:
        print(f"  ... and {len(punkpeye_clients) - 10} more")

    print("\nExtracting clients from modelcontextprotocol.io...")
    mcp_clients, mcp_official_names = extract_from_modelcontextprotocol(str(mcp_official_file))
    print(f"  Found {len(mcp_clients)} entries")
    print(f"  (Tracking {len(mcp_official_names)} unique normalized names)")

    print("\nExtracted clients from modelcontextprotocol.io:")
    for c in mcp_clients[:10]:
        print(f"  - {c['name']}: {c['main_url']}")
    if len(mcp_clients) > 10:
        print(f"  ... and {len(mcp_clients) - 10} more")

    print("\nMerging datasets...")
    merged = merge_clients(punkpeye_clients, mcp_clients, mcp_official_names)
    print(f"  Total unique clients: {len(merged)}")

    # Count how many are listed on official site
    official_count = sum(1 for c in merged if c.get('listed_on_mcp_official', False))
    print(f"  Listed on modelcontextprotocol.io: {official_count}")

    print(f"\nWriting CSV to {output_file}...")
    write_csv(merged, str(output_file))

    print(f"\nWriting markdown files to {markdown_dir}/...")
    count = write_markdown_files(merged, str(markdown_dir))
    print(f"  Created {count} markdown files")

    print("\nDone!")

    return merged


if __name__ == "__main__":
    main()
