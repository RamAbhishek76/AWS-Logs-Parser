# Read and store the lookup table provided as a dictionary, for counting tags and combination occurences.
def load_lookup_table(filename):
    try:
        with open(filename, mode='r') as file:
            lines = file.readlines()
            lookup_dict = {}
            for line in lines[1:]:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    port = int(parts[0])
                    protocol = parts[1].strip().lower()
                    tag = parts[2].strip()
                    lookup_dict[(port, protocol)] = tag
        return lookup_dict
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")
    except ValueError:
        print("Error converting data types in the lookup table.")

# Create a dictionary of the most commonly used protocols with their corresponding values, as mentioned in the documentation shared as part of the task.
PROTOCOL_MAP = {
    '1': 'icmp',
    '2': 'igmp',
    '6': 'tcp',
    '17': 'udp',
    '41': 'ipv6',
    '46': 'rsvp',
    '47': 'gre',
    '50': 'esp',
    '51': 'ah',
    '58': 'icmpv6',
    '88': 'eigrp',
    '89': 'ospf',
    '94': 'ipip',
    '132': 'sctp'
}

# Parse the given flow_logs file and create a list, with the count for each combination and also, the tags.
def parse_flow_logs(flow_log_filename, lookup_table):
    tag_counts = {}
    port_protocol_counts = {}

    # Open the flow_logs file, parse it, strip and fetch the various fields from each listed log.
    try:
        with open(flow_log_filename, mode='r') as file:
            flow_logs = [line.strip().split() for line in file.readlines()]
    except FileNotFoundError:
        print("The file was not found.")
    except IOError:
        print("An error occurred while reading the file.")

    # Map the stored flow_logs to get the protocol value, which is the eighth field in every log. In case of non-int values or non-formatted log, skip them.
    processed_entries = [
        ((int(fields[6]), PROTOCOL_MAP.get(fields[7], 'unknown')),
        lookup_table.get((int(fields[6]), PROTOCOL_MAP.get(fields[7], 'unknown'))))
        for fields in flow_logs
        if len(fields) > 8 and fields[6].isdigit()
    ]

    # Count the port/protocol combination occurrences and tag occurrences and keep track of the values.
    port_protocol_counts = {key: processed_entries.count((key, tag))
                            for key, tag in set((entry[0], entry[1]) for entry in processed_entries)}
    tag_counts = {tag if tag else 'Untagged': sum(1 for entry in processed_entries if entry[1] == tag)
                  for tag in set(tag for _, tag in processed_entries)}

    # Return the tag counts and the port protocol counts.
    return tag_counts, port_protocol_counts

# As requested in the requirement, write the output to a txt file.
def write_output(tag_counts, port_protocol_counts, output_filename):
    with open(output_filename, mode='w') as file:
        # Write the tag counts which is calculated using parse_flow_logs methods.
        file.write("Tag Counts:\n")
        file.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")

        # Write the port/protocol combination counts which is also calculated in the parse_flow_logs method.
        file.write("\nPort/Protocol Combination Counts:\n")
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

def main():
    lookup_table = load_lookup_table('lookup_table.txt')
    tag_counts, port_protocol_counts = parse_flow_logs('flow_logs.txt', lookup_table)
    write_output(tag_counts, port_protocol_counts, 'output.txt')

if __name__ == "__main__":
    main()
