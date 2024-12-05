# modules/decision_support/supplier_selection.py

from utils.inference_engine import RuleEngine
import os


class SupplierSelection:
    @staticmethod
    def select_supplier(criteria):
        rule_file = os.path.join("knowledge_base", "supplier_rules.json")
        engine = RuleEngine(rule_file)
        return engine.evaluate(criteria)
