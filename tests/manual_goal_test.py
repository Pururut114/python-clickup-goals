import argparse
from goal_methods import get_goals, get_goal_by_id, create_goal, update_goal, delete_goal

parser = argparse.ArgumentParser(description="Run manual ClickUp goal tests.")
parser.add_argument("--get", action="store_true", help="Get all goals")
parser.add_argument("--get-by-id", metavar="GOAL_ID", help="Get a goal by ID")
parser.add_argument("--create", action="store_true", help="Create a goal")
parser.add_argument("--update", metavar="GOAL_ID", help="Update a goal by ID")
parser.add_argument("--delete", metavar="GOAL_ID", help="Delete a goal by ID")

args = parser.parse_args()

print("Запусти одну из функций ниже, указав goal_id при необходимости.")

if args.get:
    get_goals()
elif args.get_by_id:
    get_goal_by_id(args.get_by_id)
elif args.create:
    create_goal()
elif args.update:
    update_goal(args.update)
elif args.delete:
    delete_goal(args.delete)