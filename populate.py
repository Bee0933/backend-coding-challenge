#!/usr/bin/env python

from app import SessionLocal, initialize_db, Plan
from datetime import datetime
import fire, ijson, os


def populate_db(json_filename: str):

    # check if file exists
    if os.path.exists(os.path.join(os.getcwd(), json_filename)):

        # open/read json file
        f = open(os.path.join(os.getcwd(), json_filename), "rb")

        # initialize database
        initialize_db()

        # create DB session
        session = SessionLocal()

        # populate database with json data semples
        for record in ijson.items(f, "item"):
            data_sample = Plan(
                id=record["id"],
                originalId=record["originalId"],
                talentId=record["talentId"],
                talentName=record["talentName"],
                talentGrade=record["talentGrade"],
                bookingGrade=record["bookingGrade"],
                operatingUnit=record["operatingUnit"],
                officeCity=record["officeCity"],
                officePostalCode=record["officePostalCode"],
                jobManagerName=record["jobManagerName"],
                jobManagerId=record["jobManagerId"],
                totalHours=record["totalHours"],
                startDate=datetime.strptime(record["startDate"], "%m/%d/%Y %I:%M %p"),
                endDate=datetime.strptime(record["endDate"], "%m/%d/%Y %I:%M %p"),
                clientName=record["clientName"],
                clientId=record["clientId"],
                industry=record["industry"],
                isUnassigned=record["isUnassigned"],
                requiredSkills=record["requiredSkills"],
                optionalSkills=record["optionalSkills"],
            )
            session.add(data_sample)

            session.commit()
    else:
        print("file does not exist !")


if __name__ == "__main__":
    fire.Fire(populate_db)
