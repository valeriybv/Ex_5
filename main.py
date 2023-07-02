import purchaselog
import visits


purchases_path = "data/purchase_log.txt"
visits_path = "data/visit_log.csv"

result = purchaselog.create_dict_from_log(purchases_path)
visits.funnel(purchases_path, visits_path)