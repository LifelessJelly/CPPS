import csv  # for reading csv files
import matplotlib.pyplot as plt  # for pyplot.subplot and other functions
import matplotlib.ticker as tkr  # for ticker.MultipleLocator()
from typing import List  # type hinting for List

# create a class for all static variables (so that these variables' lifetime last through the whole program)

attrData: List[List[int]] = []
attrNames: [List[str]] = []


# anything with a SV. prefix refers to the class holding static variables


def displayDivider() -> None:
    print("-" * 119)


# function for displaying bus statistics
def displayBuses() -> None:
    print()
    print("The statistics for buses crossing the border each year are:")
    displayDivider()
    for yearPassed, num in enumerate(attrData[1]):
        print(f"{2000 + yearPassed}: {num}")
    displayDivider()
    return


# function for displaying user's input statistics
def displayUserInput(userInput: str) -> None:
    print()
    if userInput == '\n':
        return
    # convert option to index supported value A -> 0, B -> 1, C -> 2, D -> 3
    userIn: int = ord(userInput) - ord('A')
    # make a list reference to the StaticVariables class object to the user's selected option
    selected: List[int] = attrData[userIn]
    # use sum() to sum from index 0 to 7 for calculating average
    sumSelection: int = sum(selected[0:7])
    displayDivider()

    # print the mean number of the user's chosen variable
    print(f"The mean number of {attrNames[userIn]} crossing the border each year is "
          f"{sumSelection / len(selected[0:7]):.0f}")

    # use max to return max value in the index range 0 to 7
    print(f"In {2000 + selected.index(max(selected[0:7]))} crossed the highest number of "
          f"{attrNames[userIn]} from the year 2000 to 2007 with "
          f"{max(selected[0:7])} {attrNames[userIn]}")

    displayDivider()
    return


def displayYrOnYr(userInput: str) -> None:
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
        # Display all the stats
        percentageChange: float = (selected[i + 1] - selected[i]) / selected[i] * 100
        print(
            f"{2000 + i}-{2000 + i + 1}: "
            f"{'increase' if selected[i + 1] > selected[i] else 'decrease'}"
            f" of {percentageChange:.2f}%")
        if percentageChange > 5:
            moreThan5.append(2000 + i + 1)

    # Display years that have 5% or more increase in traffic
    if len(moreThan5) != 0:
        print(f"\nThe following {'years' if len(moreThan5) > 1 else 'year'} have shown an increase of 5% of "
              f"{attrNames[userIn]} crossing the border year on year:")
        for i in moreThan5:
            print(f"{i - 1}-{i}")

    displayDivider()
    return


def displayPlot() -> None:
    # 2 subplots, using constrained layout (scales plot to fit every element on the figure)
    fig, axis = plt.subplots(2, layout="constrained")
    busPerPerson: List[float] = [passenger / attrData[1][index]
                                 for index, passenger in enumerate(attrData[0])]
    personalVehiclesThousands: List[float] = [vehicles / 1000 for vehicles in attrData[2]]
    # The following code below was written with reference to documentation on matplotlib.org
    # Plot the graph for first subplot
    axis[0].plot(range(2000, 2013), busPerPerson, label="Bus passengers per bus")
    axis[0].set_title("Traffic data of bus passengers per bus from 2000 to 2012")
    axis[0].grid()
    axis[0].set(xlabel="year", ylabel="Bus passengers per bus")
    axis[0].xaxis.set_major_locator(tkr.MultipleLocator(1))
    axis[0].yaxis.set_minor_locator(tkr.MultipleLocator(1))
    axis[0].legend()
    axis[1].bar(range(2000, 2013), personalVehiclesThousands, linewidth=1, label="Number of personal "
                                                                                 "vehicles (1k intervals)")
    # Plot the graph for second subplot
    axis[1].set_title(f"Traffic data of every 1000 personal vehicles from 2000 to 2012")
    axis[1].grid()
    axis[1].set(xlabel="year", ylabel="Number of personal vehicles")
    axis[1].xaxis.set_major_locator(tkr.MultipleLocator(1))
    axis[1].yaxis.set_minor_locator(tkr.MultipleLocator(125))
    axis[1].set_xlim(2000 - 0.5, 2012 + 0.5)
    axis[1].legend(loc='lower left')

    plt.show()
    return


def getUserSubInput() -> str:
    print(f"{'-' * 43} List of available option inputs {'-' * 43}")
    print("Options:")
    for i, name in enumerate(attrNames):
        print(f"{chr(ord('A') + i)}: {name}")
    print("Select an option above to view the data")
    print("Or press enter to go back")
    # keep prompting the user for input until they give valid input
    while True:
        userInput: str = input("Please enter your selection: ").upper()
        for c in attrNames:
            char: str = chr(attrNames.index(c) + ord('A'))
            if userInput == c.upper() or userInput == char:
                return char
        if len(userInput) == 0:
            return '\n'
        print("invalid selection input, please try again")


def showMenu() -> None:
    print(f"{'-' * 45} Border Crossing Vehicles 2 {'-' * 46}")
    print("Options:")
    print(f"A: Display the number of Buses crossing the border for each year, for the 13-year period\n"
          f"B: Display user-selected input's mean number of vehicles from 2000 to 2007 and the maximum traffic in the "
          f"8 years \n"
          f"C: Display user-selected input's year on year growth and list down years that have an increase of >5% \n"
          f"D: Show a graph of bus passengers per bus vs year and number of personal vehicles vs year")
    print("Select an option above to view the data, or type 'Q' or 'Quit' to exit the program")


def getUserInput() -> str:
    # keep prompting the user for input until they give valid input
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
        else:
            print("invalid selection input, please try again")


def readCSV() -> None:
    # read CSV file
    with open(r".\brdrxingusc_dataset.csv", newline='') as loadCSV:
        getCSVContent = csv.reader(loadCSV)
        # this next line removes the dates as a list
        next(getCSVContent)
        i: int = 0
        # Dictionaries are disallowed, so we'll just copy data from CSV to a 2D list
        for eachRow in getCSVContent:
            attrNames.append(eachRow[0])
            attrData.append([])
            # map function maps iterable variables to a new type
            attrData[i] = list(map(int, eachRow[1:len(eachRow)]))
            i += 1

    return


def main() -> int:
    readCSV()

    while True:
        showMenu()
        userSelection = getUserInput()
        if userSelection == "QUIT":
            print("EXITING PROGRAM")
            return 0
        print()
        input("Press Enter to continue")


if __name__ == '__main__':
    main()
