from datetime import datetime
class BrickworkEstimator:
    def __init__(
    self,
    length,
    height,
    thickness
):
        self.length=length
        self.height=height
        self.thickness=thickness
    def wall_volume(self):
        return(
            self.length*self.height*self.thickness
        )
    
    def brick_count(self):

        wall_volume = self.wall_volume()

        # Standard brick size: 190 mm × 90 mm × 90 mm
        brick_volume = 0.19 * 0.09 * 0.09

        bricks = wall_volume / brick_volume
        return round(bricks)
    
    def mortar_volume(self):
        return (
        self.wall_volume()
        * 0.30
    )

    def materials(self):
        mortar = self.mortar_volume()
        cement_volume = mortar * 1 / 7
        sand_volume = mortar * 6 / 7
        cement_bags =cement_volume/ 0.035
        bricks = self.brick_count()*1.05
        
        return {
    "bricks":round(bricks),
    "cement_bags": round(cement_bags),
    "sand_m3": round(sand_volume, 2)
    }
    
    def cost_breakdown(
    self,
    brick_rate,
    cement_rate,
    sand_rate
    ):
        materials = self.materials()
        bricks = materials["bricks"]
        brick_cost = bricks * brick_rate


        

        cement_cost = (
    materials["cement_bags"]*
    cement_rate
    )

        sand_cost = (
    materials["sand_m3"]
    * sand_rate
    )

        total_cost = (
    brick_cost
    + cement_cost
    + sand_cost
    )

        return {
        "brick_cost": round(brick_cost, 2),
        "cement_cost": round(cement_cost, 2),
        "sand_cost": round(sand_cost, 2),
        "total_cost": round(total_cost, 2)
        }
    
    def generate_report(
    self,
    project_name,
    cleint_name,
    estimate_id,
    brick_rate,
    cement_rate,
    sand_rate
    ):
        materials = self.materials()
        costs=self.cost_breakdown(
             brick_rate,
            cement_rate,
            sand_rate
        )
        today = datetime.now()
        current_date = today.strftime(
        "%d-%b-%Y"
        )
        return(
        f"""
========================================
BRICKWORK ESTIMATION REPORT
========================================

Project Name: {project_name}
Client Name: {cleint_name}
Estimate ID: {estimate_id}
Date: {current_date}

Wall Volume: {self.wall_volume():.2f} m³
Mortar Volume: {self.mortar_volume():.2f} m³

Bricks Required: {self.brick_count()}
Bricks With Wastage: {materials["bricks"]}
Brick Rate: {brick_rate}
Brick Cost: ₹{ costs["brick_cost"]}

Cement: {materials['cement_bags']} bags
Cement Rate: {cement_rate}
Cement Cost: ₹{costs["cement_cost"]}


Sand: {materials['sand_m3']:.2f} m³
Sand Rate: {sand_rate}
Sand Cost: ₹{costs["sand_cost"]}

Total Cost: ₹{costs["total_cost"]}    
"""
    )

