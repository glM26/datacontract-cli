from google.cloud import bigquery
import logging
import os
import pytest

from datacontract.data_contract import DataContract

logging.basicConfig(level=logging.INFO, force=True)

datacontract = "examples/bigquery/datacontract.yaml"

@pytest.mark.skipif(os.environ.get("DATACONTRACT_BIGQUERY_ACCOUNT_INFO_JSON_PATH") is None, reason="Requires DATACONTRACT_BIGQUERY_ACCOUNT_INFO_JSON_PATH to be set")
def test_examples_bigquery():
    data_contract = DataContract(data_contract_file=datacontract)

    run = data_contract.test()

    print(run)
    assert run.result == "passed"
    assert all(check.result == "passed" for check in run.checks)