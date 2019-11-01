import re
def get_year_date(text =""):
    """

    :param text: рядок, вводиться користувачем, 29 вересня 2019
    :return: рядок,дата 29
            рядок, рік, 2019
    """
    date = re.findall(r'^\d{1,2}', text)
    year = re.findall(r"\d+$",text)
    return date + year
if __name__= "__main__":
     get_year_date("1 вересня 2019")