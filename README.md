# FactorioPrints
Blueprint library for Factorio.


## These don't look like blueprint strings...
Blueprint strings are base64 encoded, compressed, JSON. https://wiki.factorio.com/Blueprint_string_format

This repo contains an unpacking script that looks in a "strings" directory for text files containing blueprint strings and decodes them to JSON and stores them in the "raw blueprints" directory.

Similarly there is also a script which does the opposite operation to produce usable blueprint strings.