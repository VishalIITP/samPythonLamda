import json
from db import connectMasterDb, connectUserDb


# import requests


def lambda_handler(event, context):
 
    conn_user = connectUserDb()
    cur_user = conn_user.cursor()

    query = "SELECT email FROM user_db.tbl_users;"
    print(query)
    cur_user.execute(query)
    user_res = cur_user.fetchall()
    firstName = user_res["first_name"]
    lastName = user_res["last_name"]
    phone = user_res["mobile"]
    nationalId = user_res["national_id"]
    gender = user_res["gender"]
    crn = user_res["crn"]
    id = user_res["id"]
    
    
    
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

 