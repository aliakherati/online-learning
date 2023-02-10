import json
import helper

def load_nobel_prizes(filename='prize.json'):
    with open(filename) as f:
        data = json.load(f)
    return data

def main(year, category, filename='./prize.json'):
    data = load_nobel_prizes(filename)
    # Add more here!
    for prize in data['prizes']:
        if 'laureates' not in prize:
            continue
        if year and prize['year'] != year:
            continue
        if category and prize['category'].lower() != category.lower():
            continue

        print_string = f"{prize['year']} nobel prize in {prize['category']}"
        print('-'*len(print_string))
        print(print_string)
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            lastname = laureate.get('surename', '')
            motivation = laureate['motivation']
            print(f"{firstname} {lastname}: {motivation}")
    
if __name__ == '__main__':
    parser = helper.build_parser()
    args = parser.parse_args()
    main(args.year, args.category)

