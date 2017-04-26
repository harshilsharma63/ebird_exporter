import string


def format_filename(s):
    """Take a string and return a valid filename constructed from the string.
        Uses a whitelist approach: any characters not present in valid_chars are
        removed. Also spaces are replaced with underscores.
        
        Note: this method may produce invalid filename such as ``, `.` or `..`
        When I use this method I prepend a date string like '2009_01_15_19_46_32_'
        and append a file extension like '.txt', so I avoid the potential of using
        an invalid filename.
 
    """
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in s if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filename.
    return filename
