"""
Importing Libraries
"""
import csv
import matplotlib.pyplot as plt

# Read the dataset using DictReader
# with open("deliveries.csv", "r", encoding="utf8") as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     data = list(csv_reader)


def total_runs():
    """
    Using this method to find out total runs scored by all the teams over the history of IPL
    """
    with open("deliveries.csv", "r", encoding="utf8") as csv_file:
        deliveries_reader = csv.DictReader(csv_file)

        total_runs_scored = {}

        for deliveries in deliveries_reader:
            team = deliveries["batting_team"]
            team_runs = int(deliveries["total_runs"])
            if team in total_runs_scored:
                total_runs_scored[team] += team_runs
            else:
                total_runs_scored[team] = team_runs

        # Plot the chart
        plt.figure(figsize=(10, 6))
        plt.bar(total_runs_scored.keys(), total_runs_scored.values())
        plt.xticks(rotation=90)
        plt.xlabel("Team")
        plt.ylabel("Total Runs")
        plt.title("Total Runs Scored by Each IPL Team")
        plt.tight_layout()
        plt.show()


def top_10_batsman_rcb():
    """
    Method to find out Top 10 highest run scoring batsman in RCB's history
    """
    with open("deliveries.csv", "r", encoding="utf8") as csv_file:
        deliveries_reader = csv.DictReader(csv_file)
        batsman_list = {}
        team_name = "Royal Challengers Bangalore"
        for deliveries in deliveries_reader:
            team = deliveries["batting_team"]
            if team == team_name:
                batsman = deliveries["batsman"]
                batsman_runs = int(deliveries["batsman_runs"])
                if batsman in batsman_list:
                    batsman_list[batsman] += batsman_runs
                else:
                    batsman_list[batsman] = batsman_runs
        # Find top 10 batsman
        top_10_batsman_rcb_ipl = dict(
            sorted(batsman_list.items(), key=lambda item: item[1], reverse=True)[:10]
        )

        plt.bar(top_10_batsman_rcb_ipl.keys(), top_10_batsman_rcb_ipl.values())
        plt.xlabel("Batsman")
        plt.ylabel("Runs")
        plt.title("Top 10 Batsman of RCB in IPL History")
        plt.tight_layout()
        plt.show()


def foreign_umpires():
    """
    Method to find the percentage of foreign umpires by country. Ignoring the Indian Umpires.
    """
    with open("umpires.csv", "r", encoding="utf8") as csvfile:
        reader = csvfile.read()
        reader = reader.replace(", ", ",")
        csvfile = open("umpires_fixed_delimiter.csv", "w", encoding="utf8")
        csvfile.write(reader)
        csvfile.close()

    with open("umpires_fixed_delimiter.csv", "r", encoding="utf8") as csvfile:
        umpires_list = csv.DictReader(csvfile, delimiter=",")
        countries_list = {}
        for data in umpires_list:
            country = data["country"]
            if country == "India":
                continue
            elif country in countries_list:
                countries_list[country] += 1
            else:
                countries_list[country] = 1

        countries = list(countries_list.keys())
        counts = list(countries_list.values())

        # pie chart
        plt.pie(counts, labels=countries, autopct="%1.1f%%", startangle=90)
        plt.axis("equal")
        plt.title("Number of Umpires by Country")
        plt.tight_layout()
        plt.show()


def matchesplayed_byteam_perseason():
    """
    Method is used to find out a stacked bar chart for matches played by teams per season
    """
    with open("matches.csv", "r", encoding="utf8") as csvfile:
        ipl_matches = csv.DictReader(csvfile)
        matchplayed_perseason = {}
        all_team_set = set()
        for matches in ipl_matches:
            season = int(matches["season"])
            team1 = matches["team1"]
            team2 = matches["team2"]
            all_team_set.add(team1)
            all_team_set.add(team2)
            if season not in matchplayed_perseason:
                matchplayed_perseason[season] = {}
                matchplayed_perseason[season][team1] = 1
                matchplayed_perseason[season][team2] = 1
            else:
                if team1 not in matchplayed_perseason[season]:
                    matchplayed_perseason[season][team1] = 1
                else:
                    matchplayed_perseason[season][team1] += 1

                if team2 not in matchplayed_perseason[season]:
                    matchplayed_perseason[season][team2] = 1
                else:
                    matchplayed_perseason[season][team2] += 1

        all_team_list = list(sorted(all_team_set))

        season_years = list(matchplayed_perseason.keys())
        season_years.sort()
        bottom = [0] * len(season_years)
        for team in all_team_list:
            matches_all_season_list = []
            for year in season_years:
                if team not in matchplayed_perseason[year]:
                    matches_all_season_list.append(0)
                else:
                    matches_all_season_list.append(matchplayed_perseason[year][team])

            # print(team, matches_all_season_list)
            plt.bar(season_years, matches_all_season_list, bottom=bottom)
            # Updating bottom
            for i in range(len(bottom)):
                bottom[i] += matches_all_season_list[i]
            print(bottom)
        plt.xlabel("Years")
        plt.ylabel("Matches played per season per team")
        plt.title("Matches played per team per season")
        plt.tight_layout()
        plt.legend(all_team_list)
        plt.show()


def matches_played_per_year():
    """
    Method to plot bar chart which shows number of matches played in a season
    """
    with open("all_season_details.csv", "r", encoding="utf8") as csvfile:
        season_reader = csv.DictReader(csvfile)

        matches_per_year = {}
        season_matches_ids = {}
        for season_list in season_reader:
            season_year = int(season_list["season"])
            match_id = int(season_list["match_id"])
            if season_year in season_matches_ids:
                if match_id in season_matches_ids[season_year]:
                    continue
                else:
                    season_matches_ids[season_year].append(match_id)
            else:
                season_matches_ids[season_year] = [match_id]

        for year, matches in season_matches_ids.items():
            matches_per_year[year] = len(matches)

        # plot the bar chart
        plt.bar(matches_per_year.keys(), matches_per_year.values())
        plt.xticks(rotation=90)
        plt.xlabel("Year")
        plt.ylabel("Matches Played")
        plt.title("Matches Played Per Year")
        plt.tight_layout()
        plt.show()


def matcheswon_per_team_per_year():
    """
    Stacked bar chart used to find matches won by team per season
    """
    with open("matches.csv", "r", encoding="utf8") as csvfile:
        matches_reader = csv.DictReader(csvfile)

        # matchesWon_per_team_per_year_list = {}
        season_wins_by_teams = {}
        for matches_list in matches_reader:
            season_year = int(matches_list["season"])
            winning_team = matches_list["winner"]
            if season_year not in season_wins_by_teams:
                season_wins_by_teams[season_year] = {}

            if winning_team not in season_wins_by_teams[season_year]:
                season_wins_by_teams[season_year][winning_team] = 0

            season_wins_by_teams[season_year][winning_team] += 1

        print(season_wins_by_teams)

        # plot stacked bar chart
        teams = []
        for year, season_detail in season_wins_by_teams.items():
            for winning_team in season_detail.keys():
                if winning_team not in teams:
                    teams.append(winning_team)

        # print(teams)

        # Create a stacked bar chart
        counts = []
        for team in teams:
            team_counts = []
            for year, season_detail in season_wins_by_teams.items():
                if team in season_detail:
                    team_counts.append(season_wins_by_teams[year][team])
                else:
                    team_counts.append(0)
            counts.append(team_counts)

        # print(counts)
        years = list(season_wins_by_teams.keys())
        years.sort()
        # print(years)
        bottom = [0] * len(years)
        for i in range(len(teams)):
            plt.bar(
                list(season_wins_by_teams.keys()),
                counts[i],
                bottom=bottom,
                label=teams[i],
            )

            for j in range(len(bottom)):
                bottom[j] += counts[i][j]

        plt.legend(bbox_to_anchor=(1, 1), loc="upper left")
        plt.tight_layout()
        plt.xlabel("Year")
        plt.show()


def extra_runs_conceded_2016():
    """
    Extra runs conceded by individual teams in 2016 season
    """
    with open("all_season_bowling_card.csv", "r", encoding="utf8") as csvfile:
        bowling_reader = csv.DictReader(csvfile)

        teams_extra_runs = {}
        for bowling_card_list in bowling_reader:
            team = bowling_card_list["bowling_team"]
            season = bowling_card_list["season"]
            if season == "2016":
                wides = int(bowling_card_list["wides"])
                no_ball = int(bowling_card_list["noballs"])
                if team not in teams_extra_runs:
                    teams_extra_runs[team] = wides + no_ball
                else:
                    teams_extra_runs[team] += wides + no_ball

        # plot the bar chart
        plt.bar(teams_extra_runs.keys(), teams_extra_runs.values())
        plt.xticks(rotation=90)
        plt.xlabel("Team")
        plt.ylabel("Extra Runs Conceded")
        plt.tight_layout()
        plt.title("Extra Runs Conceded by Team")
        plt.show()


def top_10_economical_bowlers_2015():
    """
    Top 10 economical bowlers of 2015 season
    """
    with open("all_season_bowling_card.csv", "r", encoding="utf8") as csvfile:
        bowling_reader = csv.DictReader(csvfile)

        bowlers_list = {}
        for bowling_card_list in bowling_reader:
            season_year = int(bowling_card_list["season"])
            bowler = bowling_card_list["fullName"]
            if season_year == 2015:
                if bowler not in bowlers_list:
                    bowlers_list[bowler] = []
                    bowlers_list[bowler].append(float(bowling_card_list["economyRate"]))
                else:
                    bowlers_list[bowler].append(float(bowling_card_list["economyRate"]))

        season_average_economyrate_bowlers_list = {}
        # print(bowlers_list)
        for bowler, economy_list in bowlers_list.items():
            average_economy_rate = 0
            for economy_rate_of_bowler in economy_list:
                average_economy_rate += economy_rate_of_bowler

            average_economy_rate /= len(bowlers_list[bowler])
            season_average_economyrate_bowlers_list[bowler] = average_economy_rate

        top_10_economical_bowlers_of_2015 = dict(
            sorted(
                season_average_economyrate_bowlers_list.items(),
                key=lambda item: item[1],
            )[:10]
        )
        # plot the bar chart
        plt.figure(figsize=(12, 6))
        plt.bar(
            top_10_economical_bowlers_of_2015.keys(),
            top_10_economical_bowlers_of_2015.values(),
        )
        plt.xticks(rotation=90)
        plt.xlabel("Bowler")
        plt.ylabel("Average Economy Rate")
        plt.title("Average Economy Rate by Bowler")
        plt.show()


def execute():
    """
    Main function which calls respective plots
    """
    print("1. A chart of the total runs scored by each teams over the history of IPL")
    print(
        "2. The total runs scored by top 10 batsman playing for Royal Challengers",
        "Bangalore over the history of IPL.",
    )
    print(
        "3. A chart of number of umpires by in IPL by country. Indian umpires are ignored"
    )
    print("4. Matches played by team by season")
    print("5. Number of matches played per year for all the years in IPL")
    print("6. Number of matches won per team per year in IPL")
    print("7. Extra runs conceded per team in the year 2016")
    print("8. Top 10 economical bowlers in the year 2015")
    print("")
    print("Select your choice ")
    print("")
    user_input = input()
    user_input = int(user_input)
    print("")
    print("")

    if user_input == 1:
        total_runs()
    elif user_input == 2:
        top_10_batsman_rcb()
    elif user_input == 3:
        foreign_umpires()
    elif user_input == 4:
        matchesplayed_byteam_perseason()
    elif user_input == 5:
        matches_played_per_year()
    elif user_input == 6:
        matcheswon_per_team_per_year()
    elif user_input == 7:
        extra_runs_conceded_2016()
    elif user_input == 8:
        top_10_economical_bowlers_2015()
    else:
        print("Wrong Input")


execute()
