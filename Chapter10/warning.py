import warnings

def month_warning(m:int):
    if not 1 <= m <= 12:
        msg = f"month {m} is not between 1 and 12\n"
        warnings.warn(msg,RuntimeWarning)
    else: 
        print("input is okay.\n")

warnings.filterwarnings(action = 'ignore', category = RuntimeWarning)

month_warning(13)