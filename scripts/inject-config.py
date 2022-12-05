import os, configparser, argparse

# Define the command line arguments.
parser = argparse.ArgumentParser(description='Inject configuration into a ini type file')
parser.add_argument('config', help='The configuration file to inject into')
parser.add_argument('section', help='The section to inject into')
parser.add_argument('key', help='The key to inject')
parser.add_argument('value', help='The value to inject')
parser.add_argument('-a', '--append', action='store_true', help='Append to the value instead of replacing it')
parser.add_argument('-n', '--newline', action='store_true', help='The newline to use when appending')

# Parse the command line arguments.
args = parser.parse_args()

# Setup the config parser.
config = configparser.RawConfigParser()

# Read the config file.
config.read(args.config)

# Check if we want to append to the value.
if args.append:

    # Get the current value.
    value = config.get(args.section, args.key)

    # Check if we want to append a newline.
    if args.newline:
        value += '\r\n'

    # Append the new value.
    value += args.value
else:
    # Set the value.
    value = args.value

# Set the value.
config.set(args.section, args.key, value)

# Write the config file.
with open(args.config, 'w') as configfile:
    config.write(configfile)
    configfile.close()
    print('Config injected successfully')
    exit(0)

# If we get here, something went wrong.
print('Failed to inject config')
exit(1)