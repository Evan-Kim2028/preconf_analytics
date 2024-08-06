import asyncio
import nest_asyncio
import polars as pl
from mev_commit_sdk_py.hypersync_client import Hypersync

# expand polars df output
pl.Config.set_fmt_str_lengths(200)
pl.Config.set_fmt_float("full")

# to run asyncio loop in notebook
nest_asyncio.apply()

holesky: str = 'https://holesky.hypersync.xyz'

client = Hypersync(holesky)

asyncio.run(client.get_blocks_txs(
    block_range=(7200 * 3), save_data=True))
