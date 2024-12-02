from knowledge_base import LensKnowledgeBase, Fact


class LensExpertSystem:
    def __init__(self):
        self.engine = LensKnowledgeBase()

    def run_expert_system(self, focal_length, aperture, material):
        self.engine.reset()
        self.engine.declare(Fact(focal_length=focal_length,
                            aperture=aperture, material=material))
        self.engine.run()
        return "\n".join([str(fact["recommendation"]) for fact in self.engine.facts.values() if "recommendation" in fact])
