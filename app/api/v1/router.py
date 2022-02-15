from _csv import reader

from fastapi import APIRouter, File

from app.service import convert_temperature

router = APIRouter()


@router.post("/upload-csv")
async def upload_csv(csv_file: bytes = File(...)):
    """
    Upload a CSV file to the server.
    """
    # convert csv_file to dict using pandas
    my_dict = []
    for row in reader(csv_file.decode("utf-8").splitlines()):
        # skip header
        if row[0] == "value":
            continue
        my_dict.append({
            "value": row[0],
            "input_unit": row[1],
            "target_unit": row[2],
            "s_response": row[3]
        })

    for row in my_dict:
        # check row["value"] is a float
        try:
            float(row["value"])
        except ValueError:
            row["output"] = "Invalid input"
            continue
        # check row["target_unit"] is a float
        try:
            float(row["s_response"])
        except ValueError:
            row["output"] = "incorrect"
            continue

        response = convert_temperature(temperature_input=float(row["value"]), input_temperature_type=row["input_unit"],
                                       target_temperature_type=row["target_unit"])

        if response == -1:
            row["output"] = "Invalid input"
            continue
        if response == float(row["s_response"]):
            row["expected_output"] = response
            row["output"] = "correct"
        else:
            row["expected_output"] = response
            row["output"] = "incorrect"

    # my_dict to csv and return
    return my_dict
