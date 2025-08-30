from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    for key, value in data.items():
        table_id = f'model-command-466515-q6.uber_dataset_project.{key}'
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            value,   # ici value est déjà un DataFrame.head(100)
            table_id,
            if_exists='replace',
        )
