from usdm_excel.usdm_excel import USDMExcel
import os

#study = "Roche Phase 3 NCT04320615"
#study = "cycles_1_v2"
study = "simple_1"
#study = "simple_2"

program_path = os.path.abspath("import_excel.py")
file_path = os.path.join(os.path.dirname(program_path), "source_data/%s.xlsx" % (study))
x = USDMExcel(file_path)
json = x.to_json()
nodes, edges = x.to_nodes_and_edges()
#print("JSON:", json)
print("NODES:", nodes)
print("EDGES:", edges)