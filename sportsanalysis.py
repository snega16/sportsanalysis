import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
plt.rcParams['figure.figsize'] = (14, 8)
matches = pd.read_csv('matches.csv')

def display_menu():
    print("Which of the following analysis you want to see?")
    print("------------------------------------------------")
    print("1. Toss Winner")
    print("2. Toss Decision")
    print("3. Top players")
    print("4. Win by runs")
    print("5. Win by wickets")
    print("------------------------------------------------")


def toss_winner():
    sns.countplot(x='toss_winner', data=matches)
    plt.show()

def toss_decision():
    sns.countplot(x='toss_winner', data=matches)
    plt.show()

def top_players():
    top_players = matches.player_of_match.value_counts()[:10]
    fig, ax = plt.subplots()
    ax.set_ylim([0,20])
    ax.set_ylabel("Count")
    ax.set_title("Top player of the match Winners")
    #top_players.plot.bar()
    sns.barplot(x = top_players.index, y = top_players, orient='v');
    plt.show()

def win_by_runs():
    fig, ax = plt.subplots()
    ax.set_title("Winning by Runs - Team Performance")
    #top_players.plot.bar()
    sns.boxplot(y = 'winner', x = 'win_by_runs', data=matches[matches['win_by_runs']>0], orient = 'h'); #palette="Blues");
    plt.show()


def win_by_wickets():
    fig, ax = plt.subplots()
    ax.set_title("Winning by Wickets - Team Performance")
    #top_players.plot.bar()
    sns.boxplot(y = 'winner', x = 'win_by_wickets', data=matches[matches['win_by_wickets']>0], orient = 'h'); #palette="Blues");
    plt.show()

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        toss_winner()
    elif choice == '2':
        toss_decision()
    elif choice == '3':
        top_players()
    elif choice == '4':
        win_by_runs()
    elif choice == '5':
        win_by_wickets()
    else:
        break
