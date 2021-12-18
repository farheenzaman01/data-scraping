import requests
from bs4 import BeautifulSoup


def get_heights(url: str) -> list:
    """
    scrapes the url passed. finds all span tags with class sidearm-roster-player-height
    :param url: site to scrape
    :type url: string
    :return: list of heights
    :rtype: list
    """
    # initializing BeautifulSoup and passing url
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    # get heights from span.sidearm-roster-player-height and append to list heights
    height_strings = [tag.text for tag in soup.find_all("span", {"class": "sidearm-roster-player-height"})]
    heights = []
    # converting scraped data from strings to floats
    for height in height_strings:
        # changing height to feet
        heights.append(int(height[0:height.index('\'')]) + (float(height[height.index('\'') + 1:-1]) / 12))
    return heights


def average(heights: list) -> float:
    """
    calculates the average of passed heights
    :param heights: scraped heights for a given team:
    :type heights: list
    :return average height
    :rtype float
    """
    return sum(heights) / len(heights)


def main() -> None:
    # scraping heights for men's swimming team
    print("Scraping heights for men's swimming team")
    men_swimming_heights = get_heights("https://athletics.baruch.cuny.edu/sports/mens-swimming-and-diving/roster")
    men_swimming_heights_avg = average(men_swimming_heights)
    print("Average height is {:.2f} ft.".format(men_swimming_heights_avg))

    # scraping heights for men's volleyball team
    print("Scraping heights for men's volleyball team")
    men_volleyball_heights = get_heights("https://athletics.baruch.cuny.edu/sports/mens-volleyball/roster")
    men_volleyball_heights_avg = average(men_volleyball_heights)
    print("Average height is {:.2f} ft.".format(men_volleyball_heights_avg))

    # scraping heights for women's swimming team
    print("Scraping heights for women's swimming team")
    women_swimming_heights = get_heights("https://athletics.baruch.cuny.edu/sports/womens-swimming-and-diving/roster")
    women_swimming_heights_avg = average(women_swimming_heights)
    print("Average height is {:.2f} ft.".format(women_swimming_heights_avg))

    # scraping heights for mens volleyball team
    print("Scraping heights for women's volleyball team")
    women_volleyball_heights = get_heights("https://athletics.baruch.cuny.edu/sports/womens-volleyball/roster")
    women_volleyball_heights_avg = average(women_volleyball_heights)
    print("Average height is {:.2f} ft.".format(women_volleyball_heights_avg))

    # finding difference between men's swimming and volleyball height average
    print("\ncomparing average between the two men's teams")
    men_average_difference = abs(men_swimming_heights_avg - men_volleyball_heights_avg)
    print("difference is: {:.2f} ft.".format(men_average_difference))

    # finding difference between men's swimming and volleyball height average
    print("comparing average between the two women's teams")
    women_average_difference = abs(women_swimming_heights_avg - women_volleyball_heights_avg)
    print("difference is: {:.2f} ft.".format(women_average_difference))

    # finding difference between swimming team and volleyball team height average
    print("\ncomparing average for both teams")
    swimming_team_height_average = (sum(men_swimming_heights) + sum(women_swimming_heights)) / (len(men_swimming_heights) + len(women_swimming_heights))
    volleyball_team_height_average = (sum(men_volleyball_heights) + sum(women_volleyball_heights)) /[] (len(men_volleyball_heights) + len(women_volleyball_heights))
    team_average_difference = abs(swimming_team_height_average - volleyball_team_height_average)
    print("difference is: {:.2f} ft.".format(team_average_difference))


if __name__ == '__main__':
    main()
