# Save data to an AWS bucket

from typing import Dict

import aws_lib


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAVAGUQ5JEZC5D4FQG", "MhgmJTQly+nIgAPeN0+kx6Mx/8Elpos5UzqK3zj")
    database.push(data)

# aws_access_key_id = AKIAWY56YWJJZRJDL2N4
# aws_secret_access_key = 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
