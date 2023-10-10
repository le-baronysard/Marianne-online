import requests
import os
print(os.environ.get("API_KEY"))
cards = ",".join(['created_at',"fields"])
                 # ,'press_references', 'event_appearances', 'participated_investments', 'headquarters_address', 'child_organizations', 'raised_investments', 'participated_funds', 'raised_funding_rounds', 'child_ownerships', 'founders', 'ipos', 'raised_funds', 'parent_organization', 'acquirer_acquisitions', 'parent_ownership', 'fields', 'investors', 'acquiree_acquisitions', 'participated_funding_rounds'])
print(cards)

company_name = "doctolib"
url = f"https://api.crunchbase.com/api/v4/entities/organizations/{company_name}?&card_ids={cards}&user_key={os.environ.get('API_KEY')}"
#url = f"https://api.crunchbase.com/api/v4/entities/organizations/doctolib/cards/card_id=raised_funds&user_key={os.environ.get('API_KEY')}"
#url = f"https://api.crunchbase.com/api/v4/entities/organizations/sequoia-capital/cards/participated_investments?card_field_ids=announced_on%2Cfunding_round_money_raised%2Corganization_identifier%2Cpartner_identifiers&order=funding_round_money_raised%20desc&user_key={os.environ.get('API_KEY')}"

answer = requests.get(url)

print(answer.status_code)

print(answer.json())

print(answer.json()["cards"]["fields"].keys())
