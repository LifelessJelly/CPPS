import csv  # for reading csv files
import matplotlib.pyplot as plt  # for pyplot.subplot and other functions
import matplotlib.ticker as tkr  # for ticker.MultipleLocator()
from typing import List  # type hinting for List
from pathlib import Path  # for Path.cwd()

attrData: List[List[int]] = []
attrNames: [List[str]] = []


def displayDivider() -> None:
    """Prints a line divider
    :return:
    """
    print("-" * 119)


# function for displaying bus statistics
def displayBuses() -> None:
    """Displays info for task 1

    :return:
    """
    print()
    print(f"The statistics for {attrNames[1].lower()} crossing the border each year are:")

    displayDivider()

    busData: List[int] = attrData[1]
    for yearPassed, num in enumerate(busData):
        year = 2000 + yearPassed
        print(f"{year}: {num}")

    displayDivider()
    input("Press Enter to continue \n")
    return


# function for displaying user's input statistics
def displayUserInput(userInput: str) -> None:
    """Displays user selected input for task 2

    :param userInput: the user's input
    :return:
    """
    print()
    if userInput == '\n':
        return
    # convert option to index supported value A -> 0, B -> 1, C -> 2, D -> 3
    userIn: int = (ord(userInput) - ord('A'))
    selected: List[int] = attrData[userIn][0:8]
    sumSelection: int = sum(selected)
    maxSelection: int = max(selected)
    nameSelection: str = attrNames[userIn]

    displayDivider()

    # print the mean number of the user's chosen variable
    print(f"The mean number of {nameSelection} crossing the border each year is "
          f"{sumSelection / len(selected):.0f} (Truncated down to nearest whole number)")

    print(f"In {2000 + selected.index(maxSelection)} crossed the highest number of "
          f"{attrNames[userIn]} from the year 2000 to 2007 with "
          f"{maxSelection} {nameSelection}")

    displayDivider()
    input("Press Enter to continue \n")
    return


def displayYrOnYr(userInput: str) -> None:
    """Displays user selected input for task 3

    :param userInput: the user's input
    :return:
    """
    print()
    if userInput == '\n':
        return
    userIn: int = ord(userInput) - ord('A')
    selected: List[int] = attrData[userIn]

    displayDivider()

    print(f"The changes in {attrNames[userIn]} crossing the border year on year are:")

    # Store the years that have a growth of 5% or more
    moreThan5: List[int] = []
    for i in range(len(selected) - 1):
        percentageChange: float = (selected[i + 1] - selected[i]) / selected[i] * 100
        year: int = 2000 + i
        # Display all the stats

        print(
            f"{year}-{year + 1}: "
            f"{'increase' if selected[i + 1] > selected[i] else 'decrease'}"
            f" of {percentageChange:.2f}%")
        if percentageChange > 5:
            moreThan5.append(year + 1)

    # Display years that have 5% or more increase in traffic
    if len(moreThan5) != 0:
        print(f"\nThe following years have shown an increase of 5% of "
              f"{attrNames[userIn]} crossing the border year on year:")
        for eachYear in moreThan5:
            print(f"{eachYear - 1}-{eachYear}")

    displayDivider()
    input("Press Enter to continue \n")
    return


def displayPlot() -> None:
    """ Displays custom plots for graph plotting

    See https://matplotlib.org/stable/users/index for matplotlib function documentation \n
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html#matplotlib.pyplot.subplot \n
    https://matplotlib.org/stable/api/ticker_api.html#module-matplotlib.ticker \n
    :return:
    """
    # 2 subplots, using constrained layout (scales plot to fit every element on the figure)
    fig, axis = plt.subplots(2, layout="constrained")
    busPerPerson: List[float] = [passenger / bus for passenger, bus in zip(attrData[0], attrData[1])]
    personalVehiclesThousands: List[float] = attrData[2]
    axis[0].plot(range(2000, 2013), busPerPerson, label=f"{attrNames[0].capitalize()} per {attrNames[1].lower()}")
    axis[0].set_title(f"Traffic data of {attrNames[0].lower()} per {attrNames[1].lower()} from 2000 to 2012")
    axis[0].grid()
    axis[0].set(xlabel="year", ylabel=f"{attrNames[0].capitalize()} per {attrNames[1].lower()}")
    axis[0].xaxis.set_major_locator(tkr.MultipleLocator(1))
    axis[0].yaxis.set_minor_locator(tkr.MultipleLocator(1))
    axis[0].legend()
    axis[1].bar(range(2000, 2013), personalVehiclesThousands, linewidth=1, label=f"Number of {attrNames[2].lower()}",
                color="red")
    # Plot the graph for second subplot
    axis[1].set_title(f"Traffic data of {attrNames[2].lower()} from 2000 to 2012")
    axis[1].grid()
    axis[1].set(xlabel="year", ylabel=f"Number of {attrNames[2].lower()}")
    axis[1].xaxis.set_major_locator(tkr.MultipleLocator(1))
    axis[1].yaxis.set_minor_locator(tkr.MultipleLocator(50000))
    axis[1].set_xlim(2000 - 0.5, 2012 + 0.5)
    axis[1].legend(loc='lower left')

    # turn off scientific notation
    plt.ticklabel_format(style='plain')

    plt.show()
    input("Press Enter to continue \n")
    return


def getUserSubInput() -> str:
    """ Retrieves the user input for the set of available data

    Using a for-each loop, the function prints out both the alphabetical index and the name of the data.
    To iteratively print the alphabetical index, the function uses chr() function call to convert numerical
    data to readable ASCII characters using an ASCII table, with the number 65 for ASCII 'A' being the first
    in the index \n
    >> ord('A') -> 65 \n
    >> i = 1 \n
    >> chr(i + ord('A')) -> chr(1 + 65) -> 'B' \n
    >> i = 2 \n
    >> chr(i + ord('A')) -> chr(2 + 65) -> 'C' \n
    * Pressing 'Enter' with no character input will take you back to the first menu \n
    To determine and correctly output the data chosen by the user, the function performs a similar operation as to where
    it displays the available data options. \n
    The function gets the user input, then attempt to match the user's input with either the non-case sensitive data
    identifier or the alphabetical index, by using a .index() method to get the position that the data identifier is in
    >? Please enter your selection: b \n
    >> userInput = "b".upper() -> "B" \n
    >> name = "BUS PASSENGERS" \n
    >> attrNames.index(name) -> 0 \n
    >> charIndex = chr(0 + 65) -> 'A' \n
    >> if userInput == name or userInput == charIndex -> 'B' != "BUS PASSENGERS" || 'B' != "A" // Evaluates to false \n
    >> name = "BUSES" \n
    >> attrNames.index(name) -> 1 \n
    >> charIndex = chr(1 + 65) -> 'B' \n
    >> if userInput == name or userInput == charIndex -> 'B' != "BUSES" || 'B' == "B" // Evaluates to true \n


    :return: the user's input
    """
    print(f"{'-' * 43} List of available option inputs {'-' * 43}")
    print("Options:")
    asciiA = ord('A')
    for i, name in enumerate(attrNames):
        selectionOption: str = chr(asciiA + i)
        print(f"{selectionOption}: {name}")
    print("Select an option above to view the data")
    print("Or press Enter to go back")
    # keep prompting the user for input until they give valid input
    while True:
        userInput: str = input("Please enter your selection: ").upper()
        for name in attrNames:
            charIndex: str = chr(attrNames.index(name) + asciiA)
            if userInput == name.upper() or userInput == charIndex:
                return charIndex
        if len(userInput) == 0:
            return '\n'
        print("invalid selection input, please try again")


def showMenu() -> None:
    """Shows the main menu with the four options for the user to select from.

    Displays the name of the scenario, followed by the options as outlined by the criteria from the scenario,
    and finally prompt the user to select an option.

    :return:
    """
    print(f"{'-' * 45} Border Crossing Vehicles 2 {'-' * 46}")
    print("Options:")
    print(f"A: Display the number of {attrNames[1].lower()} crossing the border for each year, for the 13-year period\n"
          f"B: Display user-selected input's mean number of vehicles from 2000 to 2007 and the maximum traffic in the "
          f"8 years \n"
          f"C: Display user-selected input's year on year growth and list down years that have an increase of >5% \n"
          f"D: Show a graph of {attrNames[0].lower()} per {attrNames[1].lower()} vs year and "
          f"number of {attrNames[2].lower()} vs year")
    print("Select an option above to view the data, or type 'Quit' to exit the program")


def getUserInput() -> str:
    """ Fetches the user's input with respect to the main menu's given selections

    Keeps prompting the user to give valid input. If the user selects a valid input, then one of the four functions
    will execute depending on which option they select, or exit the program if 'Quit' is entered

    :return:

    """
    while True:
        userInput: str = input("Please enter your selection: ").upper()
        if userInput == 'A' or userInput == "1":
            displayBuses()
            return 'A'
        if userInput == 'B' or userInput == "2":
            displayUserInput(getUserSubInput())
            return 'B'
        if userInput == 'C' or userInput == "3":
            displayYrOnYr(getUserSubInput())
            return 'C'
        if userInput == 'D' or userInput == "4":
            displayPlot()
            return 'D'
        if userInput == "QUIT":
            return "QUIT"
        print("invalid selection input, please try again")


def readCSV(fp: Path) -> None:
    """Reads the csv file passed into this function

    csv files passed into this function should follow the table format where the data is pivoted such that the
    vehicle types are the index, and the columns are the months. \n
    e.g.: \n
    \+--------+--------+--------+--------+\n
    \|  Type  |  2000  |  2001  |  2002  |\n
    \+--------+--------+--------+--------+\n
    \|  Cars  |  1234  |  5678  |  9012  |\n
    \+--------+--------+--------+--------+\n

    Where months reside at the top of the table representing columns, and the type of vehicles on the left of the
    table representing indexes.

    Not following this format will result in an undefined behaviour in the creation of the list of elements.

    This function then reads the entire .csv file and reads the lines row by row, delimited by a comma.

    The function then retrieves the name of the index (by indexing the first element in the line) and puts it into a
    list, then puts the rest of the variables in another list.

    Since the values gathered from the .csv file are in str format, it will be unusable in arithmetic operations
    unless it is converted to an int or float type. Using a for-each loop would be exhausting and slow for very large
    sets of data, so the function uses the map() function instead.

    :param fp: the filepath location as a pathlib.Path type
    :return:
    """
    # read CSV file
    with fp.open(mode="r", encoding="UTF-8", newline="") as loadCSV:
        getCSVContent = csv.reader(loadCSV)
        # skip metadata
        next(getCSVContent)
        # Dictionaries are disallowed, so we'll just copy data from CSV to a 2D list
        for eachRow in getCSVContent:
            attrNames.append(eachRow[0])
            attrData.append([])
            # map function maps iterable variables to a new type
            attrData[len(attrData) - 1] = list(map(int, eachRow[1:len(eachRow)]))

    return


#  program starts here
def main() -> int:
    filePath = Path.cwd() / "brdrxingusc_dataset.csv"
    readCSV(filePath)

    while True:
        showMenu()
        userSelection = getUserInput()
        if userSelection == "QUIT":
            print("EXITING PROGRAM")
            return 0
        print()


if __name__ == '__main__':
    main()
