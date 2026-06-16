from datetime import datetime
class ConcreteEstimator:
    MIXES = {
    "M15": (1, 2, 4),
    "M20": (1, 1.5, 3),
    "M25": (1, 1, 2)
}

    def __init__(
    self,
    length,
    width,
    depth,
    grade
):
    
        if length <= 0:
            raise ValueError(
            "Length must be positive")
        if width <= 0:
            raise ValueError(
            "width must be positive")
        if depth <= 0:
            raise ValueError(
            "depth must be positive")
        if grade not in self.MIXES:
            raise ValueError(
             "Invalid Grade"
    )
        self.length = length
        self.width = width
        self.depth = depth
        self.grade = grade
    
    def wet_volume(self):

     return (
        self.length
        * self.width
        * self.depth
    )
    def dry_volume(self):

     return (
        self.wet_volume()
        * 1.54
    )
    def material_estimate(self):
        dry = self.dry_volume()

        c, s, a = self.MIXES[self.grade]

        total_parts = c + s + a
        cement_volume = (
        dry * c
        / total_parts
    )

        sand_volume = (
        dry * s
        / total_parts
    )

        aggregate_volume = (
        dry * a
        / total_parts
    )

        cement_bags = (
        cement_volume
        / 0.035
    )

        return {
        "cement_bags":
            round(cement_bags, 2),

        "sand_m3":
            round(sand_volume, 2),

        "aggregate_m3":
            round(aggregate_volume, 2)
    }

    def cost_breakdown(
        self,
        cement_rate,
        sand_rate,
        aggregate_rate
    ):

        materials = self.material_estimate()

        cement_cost = (
        materials["cement_bags"]
        * cement_rate
    )

        sand_cost = (
        materials["sand_m3"]
        * sand_rate
    )

        aggregate_cost = (
        materials["aggregate_m3"]
        * aggregate_rate
    )

        total_cost = (
        cement_cost
        + sand_cost
        + aggregate_cost
    )

        return {
        "cement_cost": round(cement_cost, 2),
        "sand_cost": round(sand_cost, 2),
        "aggregate_cost": round(aggregate_cost, 2),
        "total_cost": round(total_cost, 2)
    }
    
    def generate_report(
    self,
    project_name,
    client_name,
    estimate_id,
    cement_rate,
    sand_rate,
    aggregate_rate
    ):

        materials = self.material_estimate()

        costs = self.cost_breakdown(
        cement_rate,
        sand_rate,
        aggregate_rate
        
        )
        total_cost=costs["total_cost"]

        today = datetime.now()
        current_date = today.strftime(
        "%d-%b-%Y"
        )
        return f"""
========================================
CONCRETE ESTIMATION REPORT
========================================

Project Name: {project_name}
Client Name: {client_name}
Estimate ID: {estimate_id}
Date: {current_date}

Grade: {self.grade}

Wet Volume: {self.wet_volume():.2f} m³
Dry Volume: {self.dry_volume():.2f} m³

Cement: {materials['cement_bags']:.2f} bags
Cement Cost: ₹{costs["cement_cost"]}

Sand: {materials['sand_m3']:.2f} m³
Sand Cost: ₹{costs["sand_cost"]}

Aggregate: {materials['aggregate_m3']:.2f} m³
Aggregate Cost: ₹{costs["aggregate_cost"]}

Material Rates:
    
Cement rate:₹{cement_rate}/bag
Sand rate:₹{sand_rate}/m³
Aggregate:{aggregate_rate}/m³

Estimated Cost: ₹{total_cost:,.2f}
"""

