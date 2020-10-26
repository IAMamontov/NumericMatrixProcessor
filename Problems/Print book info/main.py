def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author is None and year is None:
        print("\"{}\"".format(title))
    elif author is None:
        print("\"{}\" was written in {}".format(title, year))
    elif year is None:
        print("\"{}\" was written by {}".format(title, author))
    else:
        print("\"{}\" was written by {} in {}".format(title, author, year))