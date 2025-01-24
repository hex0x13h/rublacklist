import os
from ipaddress import ip_network

def read_files(directory):
    """Read all files in the specified directory and return unique lines."""
    unique_entries = set()

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".list"):
                with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if line and not line.startswith("#"):  # Ignore comments and empty lines
                            unique_entries.add(line)
    return unique_entries

def deduplicate(entries):
    """Remove duplicate IPs, domains, and overlapping IP ranges."""
    ip_ranges = set()
    domains = set()

    for entry in entries:
        try:
            # Check if it's an IP or CIDR range
            ip_range = ip_network(entry, strict=False)
            ip_ranges.add(ip_range)
        except ValueError:
            # Otherwise, treat it as a domain
            domains.add(entry)

    # Remove overlapping IP ranges
    deduplicated_ips = set()
    for ip in sorted(ip_ranges, key=lambda x: (x.prefixlen, x)):
        if not any(ip.subnet_of(existing) for existing in deduplicated_ips):
            deduplicated_ips.add(ip)

    # Convert IP ranges back to strings
    deduplicated_ips = {str(ip) for ip in deduplicated_ips}

    return deduplicated_ips.union(domains)

def save_to_file(entries, output_file):
    """Save entries to a file."""
    with open(output_file, "w", encoding="utf-8") as f:
        for entry in sorted(entries):
            f.write(entry + "\n")

if __name__ == "__main__":
    input_dir = "."  # Current directory
    output_file = "full.list"

    print("Reading list files...")
    entries = read_files(input_dir)

    print(f"Found {len(entries)} entries. Deduplicating...")
    unique_entries = deduplicate(entries)

    print(f"{len(unique_entries)} unique entries remain. Saving to {output_file}...")
    save_to_file(unique_entries, output_file)

    print("Done!")
