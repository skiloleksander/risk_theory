import os
import json
from classes import Event, Investment

directory = os.path.dirname(os.path.abspath(__file__)) + '/saves'

investments = {}

def save_investments(filename: str):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename), 'w') as f:
        json.dump({id: {
            "success_events": [{"rate": event.rate, "revenue": event.revenue} for event in investment.success_events],
            "failure_events": [{"rate": event.rate, "revenue": event.revenue} for event in investment.failure_events]
        } for id, investment in investments.items()}, f, indent=2)

def load_investments(filename: str):
    global investments
    with open(os.path.join(directory, filename), 'r') as f:
        data = json.load(f)
        investments = {}
        for id, investment_data in data.items():
            success_events = [Event(event["rate"], event["revenue"]) for event in investment_data["success_events"]]
            failure_events = [Event(event["rate"], event["revenue"]) for event in investment_data["failure_events"]]
            investments[id] = Investment(id, success_events, failure_events)

def check_investment_exists(id: str) -> bool:
    return id in investments

def add_investment(id: str, success_events: list[Event], failure_events: list[Event]):
    investments[id] = Investment(id, success_events, failure_events)

def delete_investment(id: str):
    del investments[id]
    print(f"Investment with ID '{id}' has been deleted.")

def output_investment(id: str):
    investment = investments[id]
    print(investment)

def list_investments():
    if not investments:
        print("No investments available.")
    else:
        print("Available investments:")
        for id in investments.keys():
            print(f"- {id}")

def investment_analysis(id: str):
    investment = investments[id]
    print(f"Analysis for Investment ID: {id}")
    print(f"Mathematical Expectation: {investment.math_expect()}")
    print(f"Variance: {investment.variance()}")
    print(f"RMS Deviation: {investment.rms_deviation()}")
    print(f"Variation Coefficient: {investment.variation_coefficient()}")
    print(f"Semi-Quadratic Deviation: {investment.semiquadratic_deviation()}")
    print(f"Semi-Variation Coefficient: {investment.semivariation_coefficient()}")

def compare_investments(id1: str, id2: str):
    investment1 = investments[id1]
    investment2 = investments[id2]
    results = {
        id1: {
            "Variance": investment1.variance(),
            "RMS Deviation": investment1.rms_deviation(),
            "Variation Coefficient": investment1.variation_coefficient(),
            "Semi-Quadratic Deviation": investment1.semiquadratic_deviation(),
            "Semi-Variation Coefficient": investment1.semivariation_coefficient()
        },
        id2: {
            "Variance": investment2.variance(),
            "RMS Deviation": investment2.rms_deviation(),
            "Variation Coefficient": investment2.variation_coefficient(),
            "Semi-Quadratic Deviation": investment2.semiquadratic_deviation(),
            "Semi-Variation Coefficient": investment2.semivariation_coefficient()
        }
    }
    print(f"Comparison between Investment: {id1} and Investment: {id2}")
    for metric in results[id1].keys():
        print(f"{metric}: {id1} = {results[id1][metric]}, {id2} = {results[id2][metric]}")
    score1, score2 = 0, 0
    for metric in results[id1].keys():
        if results[id1][metric] < results[id2][metric]:
            score1 += 1
        elif results[id1][metric] > results[id2][metric]:
            score2 += 1
    
    print("Overall Comparison:")

    max_expectation = max(investment1.math_expect(), investment2.math_expect())
    if investment1.math_expect() == max_expectation:
        print(f"Investment: {id1} is better based on mathematical expectation ({max_expectation}) (choose it if you like to risk).")
    elif investment2.math_expect() == max_expectation:
        print(f"Investment: {id2} is better based on mathematical expectation ({max_expectation}) (choose it if you like to risk).")
    elif investment1.math_expect() == investment2.math_expect():
        print("Both investments have the same mathematical expectation.")

    if score1 > score2:
        print(f"Investment: {id1} is better based on overall metrics. ({id1}: {score1} vs {id2}: {score2}) (choose it if you not like to risk).")
    elif score2 > score1:
        print(f"Investment: {id2} is better based on overall metrics. ({id1}: {score1} vs {id2}: {score2}) (choose it if you not like to risk).")
    elif score1 == score2:
        print(f"Both investments are equal based on overall metrics. ({id1}: {score1} vs {id2}: {score2}) (choose either one if you are indifferent to risk).")

def compare_all_investments():
    if len(investments) < 2:
        print("Not enough investments to compare.")
        return
    max_expectation = max(investment.math_expect() for investment in investments.values())
    results = {
        id: {
            "Variance": investment.variance(),
            "RMS Deviation": investment.rms_deviation(),
            "Variation Coefficient": investment.variation_coefficient(),
            "Semi-Quadratic Deviation": investment.semiquadratic_deviation(),
            "Semi-Variation Coefficient": investment.semivariation_coefficient()
        } for id, investment in investments.items()
    }
    scores = {id: 0 for id in investments.keys()}
    for metric in results[next(iter(results))].keys():
        best_value = min(results[id][metric] for id in results.keys())
        for id in results.keys():
            if results[id][metric] == best_value:
                scores[id] += 1
    print("Overall Comparison of All Investments:")
    for id, investment in investments.items():
        if investment.math_expect() == max_expectation:
            print(f"Investment: {id} is the best based on mathematical expectation ({max_expectation}) (choose it if you like to risk).")
    for id, score in scores.items():
        print(f"Investment: {id}, Score: {score}")
    print("Best Investment(s) based on overall metrics:")
    max_score = max(scores.values())
    for id, score in scores.items():
        if score == max_score:
            print(f"- {id} (choose it if you not like to risk).")
            