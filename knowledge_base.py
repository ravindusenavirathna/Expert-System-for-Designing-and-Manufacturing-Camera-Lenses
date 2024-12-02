from experta import KnowledgeEngine, Rule, Fact, W


class LensKnowledgeBase(KnowledgeEngine):
    @Rule(Fact(focal_length=W(), aperture=W(), material=W()))
    def suggest_design(self, focal_length, aperture, material):
        # Simplified decision rules
        if material.lower() == "bk7":
            self.declare(
                Fact(recommendation="Use BK7 glass for high clarity."))
        elif material.lower() == "sf11":
            self.declare(
                Fact(recommendation="Use SF11 for better chromatic aberration correction."))

        # Example rule for focal length and aperture
        if float(focal_length) < 50 and float(aperture) < 2.0:
            self.declare(Fact(recommendation="Use a wide-angle lens design."))
        elif float(focal_length) > 100:
            self.declare(Fact(recommendation="Consider a telephoto lens."))
