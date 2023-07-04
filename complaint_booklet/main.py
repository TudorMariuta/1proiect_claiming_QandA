from lib.interface import ListUnsolved, MenuUserChoice, AddItem, ExitItem, SolveOne
from lib.complaint import Complaint, Booklet
from pathlib import Path
import json
from lib import data_store

ROOT = Path(__file__).parent
DATA_STORE_PATH = ROOT / "complaints.json"

b1 = Booklet(DATA_STORE_PATH)
# Load persistance
try:
    b1.load_json()
except (OSError, json.JSONDecodeError) as err:
    print(err)


main_menu = MenuUserChoice("Caiet de reclamarii")
main_menu.add_choice(ListUnsolved("Vezi reclamatii nerezolvate", b1))
main_menu.add_choice(AddItem("Adauga reclamatie", b1))
main_menu.add_choice(SolveOne("Rezolva reclamatie", b1))
main_menu.add_choice(ExitItem("Iesire"))

while True:
    main_menu.execute()