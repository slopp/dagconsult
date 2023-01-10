from shared_asset_package import my_shared_asset, my_shared_configurable_resource
from dagster import Definitions 

defs = Definitions(
    assets=[my_shared_asset],
    resources={"my_configurable_shared_resource": my_shared_configurable_resource.configured({
        "configuration": "tenant1"
    })}
)