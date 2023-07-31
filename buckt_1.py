# Save data to an AWS bucket

from typing import Dict

import aws_lib


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAVD32IN6IH3ED7JBO", "dDgPnb57+BaorxKT0QxTlLaI3FKu8fFf2Mpczw3g")
    database.push(data)