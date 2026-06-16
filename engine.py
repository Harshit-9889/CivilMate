
project_name = input(
    "Project Name: "
    )

client_name = input(
    "Client Name: "
    )

estimate_id = input(
    "Estimate ID: "
    )
safe_project_name = (
        project_name
        .replace(" ", "_")
        .replace("/", "_")
    )



from exports.Excel.concrete_export import export_concrete_report

from exports.Excel.brickwork_export import export_brickwork_report

from exports.Excel.steelwork_export import export_steelwork_report

from exports.TXT.TXT_EXPORT import save_report

from exports.Pdf.concrete_export_pdf import export_concrete_pdf

from exports.Pdf.brickwork_export_pdf import export_brickwork_pdf

from exports.Pdf.steel_export_pdf import export_steel_pdf

from data.rates import (
    CEMENT_RATE,
    SAND_RATE,
    AGGREGATE_RATE,
    BRICK_RATE,
    STEEL_RATE
)

print("=" * 40)
print("CIVILMATE ESTIMATOR")
print("=" * 40)

print()
print("1. Concrete Estimator")
print("2. Brickwork Estimator")
print("3. Steel Estimator")

choice = input(
    "\nChoose option: "
)
from calculators.concrete import ConcreteEstimator

from calculators.brickwork import BrickworkEstimator

from calculators.steel import SteelEstimator    

if choice == "1":

    length = float(
        input("Length(m): ")
    )

    width = float(
        input("Width(m): ")
    )

    depth = float(
        input("Depth(m): ")
    )

    grade = input(
        "Grade (M15/M20/M25): "
    )

    estimator = ConcreteEstimator(
        length,
        width,
        depth,
        grade
    )
    materials = estimator.material_estimate()
    
    report=estimator.generate_report(
            project_name,
            client_name,
            estimate_id,
            CEMENT_RATE,
            SAND_RATE,
            AGGREGATE_RATE
    )
    costs =estimator.cost_breakdown(
    CEMENT_RATE,
    SAND_RATE,
    AGGREGATE_RATE
    )

    print(report)

    export_concrete_pdf(
        project_name,
    safe_project_name,
    client_name,
    estimate_id,
    materials,
    costs,
    CEMENT_RATE,
    SAND_RATE,
    AGGREGATE_RATE,
    )


    excel = input(
    "Export to Excel? (y/n): "
    )
    if excel.lower()=="y":
        export_concrete_report(
    project_name,
    safe_project_name,
    client_name,
    estimate_id,
    materials["cement_bags"],
    materials["sand_m3"],
    materials["aggregate_m3"],
    CEMENT_RATE,
    SAND_RATE,
    AGGREGATE_RATE,
    costs
    )
    elif excel.lower()=="n":
        print("THANKYOU FOR USING CIVILMATE") 
    else:
         print("invalid choice")
    save = input(
    "Save report? (y/n): "
    )
    if save.lower() == "y":

        save_report(
                 report,
                 safe_project_name,
                 estimate_id,
            )
    elif save.lower()=="n":
        print("THANKYOU FOR USING CIVILMATE") 
    else:
         print("invalid choice")

    
elif choice== "2":
    length = float(
        input("Length(m): ")
    )

    height = float(
        input("Width(m): ")
    )

    thickness= float(
        input("Depth(m): ")
    )

    estimator=BrickworkEstimator(
        length,
        height,
        thickness
    )

    materials =estimator.materials()
    costs=estimator.cost_breakdown(
        BRICK_RATE,
        CEMENT_RATE,
        SAND_RATE
    )
    
    report=estimator.generate_report(
            project_name,
            client_name,
            estimate_id,
            BRICK_RATE,
            CEMENT_RATE,
            SAND_RATE
    )
    print(report)

    export_brickwork_pdf(
        project_name,
    safe_project_name,
    client_name,
    estimate_id,
    materials,
    costs,
    CEMENT_RATE,
    SAND_RATE,
    AGGREGATE_RATE,
    )
    excel = input(
    "Export to Excel? (y/n): "
    )
    if excel.lower()=="y":
        export_brickwork_report(
    project_name,
    safe_project_name,
    client_name,
    estimate_id,
    materials["bricks"],
    materials["cement_bags"],
    materials["sand_m3"],
    BRICK_RATE,
    CEMENT_RATE,
    SAND_RATE,
    costs
    )
    elif excel.lower()=="n":
        print("THANKYOU FOR USING CIVILMATE") 
    else:
         print("invalid choice")
    save = input(
    "Save report? (y/n): "
    )
    if save.lower() == "y":
       
        save_report(
                 report,
                 safe_project_name,
                 estimate_id,
            )
        
    elif save.lower()=="n":
        print("THANKYOU FOR USING CIVILMATE") 
    else:
         print("invalid choice")

elif choice=="3":
    
    bar_type =input(
        "Bar Type(TMT/HYSD): "
    )
    Diameter = float(
        input("Diameter(mm): ")
    )

    length = float(
        input("length(m): ")
    )

    number_of_bars= float(
        input("Number of bars: ")
    )
    estimator=SteelEstimator(
        bar_type,
        Diameter,
        length,
        number_of_bars
    )

    steel_weight=estimator.weight_with_wastage()
    steel_cost=estimator.cost_breakdown(STEEL_RATE)

    report=(
        estimator.generate_report(
            project_name,
            client_name,
            estimate_id,
            STEEL_RATE
        )
    )
    print(report)

    export_steel_pdf(
        project_name,
    safe_project_name,
    client_name,
    estimate_id,
    steel_weight,
    steel_cost,
    STEEL_RATE,
    )

    excel = input(
    "Export to Excel? (y/n): "
    )
    if excel.lower()=="y":
        export_steelwork_report(
           project_name,
           safe_project_name,
           client_name,
           estimate_id,
           steel_weight,
           bar_type,
           STEEL_RATE,
           steel_cost,
           
    )
        

    elif excel.lower()=="n":
        print("THANKYOU FOR USING CIVILMATE") 
    else:
         print("invalid choice")
    save = input(
    "Save report? (y/n): "
    )
    if save.lower() == "y":
      
        save_report(
                 report,
                 safe_project_name,
                 estimate_id,
            )
        
    elif save.lower()=="n":
        print("THANKYOU FOR USING CIVILMATE") 
    else:
         print("invalid choice")
else:
    print("Invalid Choice") 

