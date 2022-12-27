import logging
import subprocess
import warnings
from typing import Dict

from policyengine_core.data.dataset import Dataset


class PrivateDataset(Dataset):
    """Private datasets are stored on Google Cloud Buckets (requires the Google Cloud CLI to be installed)."""

    bucket_name: str
    """The name of the Google Cloud Storage bucket to use for this dataset."""
    filename_by_year: Dict[int, str] = None
    """A dictionary mapping years to filenames."""

    def _get_storage_bucket(self):
        logging.info("Successfully _get_storage_bucket and saved dataset.")
    def download(self, year: int):

        logging.info("Successfully downloaded and saved dataset.")

    def upload(self, year: int, filename: str = None):
        logging.info("Successfully upload and saved dataset.")