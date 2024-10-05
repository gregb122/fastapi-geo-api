"""fastapi_geo_api models."""

from typing import Sequence, Type

from beanie import Document

from fastapi_geo_api.db.models.dummy_model import DummyModel


def load_all_models() -> Sequence[Type[Document]]:
    """Load all models from this folder."""
    return [
        DummyModel,
    ]
