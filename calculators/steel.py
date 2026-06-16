from datetime import datetime
class SteelEstimator:
    def __init__(
    self,
    bar_type,
    diameter,
    length,
    number_of_bars
    ):
        self.bar_type=bar_type
        self.diameter=diameter
        self.length=length
        self.number_of_bars=number_of_bars
        if diameter <= 0:
             raise ValueError(
        "Diameter must be positive" )
        if length <= 0:
            raise ValueError(
        "Diameter must be positive")
        if number_of_bars <= 0:
            raise ValueError(
        "Diameter must be positive")
    def single_bar_weight(self):
        weight = (
    self.diameter ** 2
    * self.length
    ) / 162
        return( round(weight, 2))
    def total_weight(self):
       t_weight=self.single_bar_weight() *self.number_of_bars
       return(round(t_weight,2))
    def weight_with_wastage(self):
        weight = self.total_weight()
        return round(
    weight * 1.05,
    2
    )
    def cost_breakdown(
    self,
    steel_rate
):
        cost=self.weight_with_wastage()*steel_rate
        return (round(cost,2))
    def generate_report(
    self,
    project_name,
    client_name,
    estimate_id,
    steel_rate
    ):
        bar_weight=self.single_bar_weight()
        t_weight=self.total_weight()
        w_wastage=self.weight_with_wastage()
        cost=self.cost_breakdown(steel_rate)
        today = datetime.now()
        current_date = today.strftime(
        "%d-%b-%Y"
        )
        return(
        f"""
========================================
STEEL ESTIMATION REPORT
========================================

Project Name: {project_name}
Client Name: {client_name}
Estimate ID: {estimate_id}
Date: {current_date}

Diameter: {self.diameter} mm

Length: {self.length} m

Number of Bars: {self.number_of_bars}

Single Bar Weight: {bar_weight:.2f} kg

Total Weight: {t_weight} kg

Weight with Wastage: {w_wastage} kg

Steel Rate: ₹{steel_rate}

Steel Cost: ₹{cost:,.2f}
"""
    )
