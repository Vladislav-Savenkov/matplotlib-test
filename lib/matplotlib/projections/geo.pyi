from matplotlib.axes import Axes as Axes
from matplotlib.patches import Circle as Circle
from matplotlib.path import Path as Path
from matplotlib.ticker import (
    FixedLocator as FixedLocator,
    Formatter as Formatter,
    NullFormatter as NullFormatter,
    NullLocator as NullLocator,
)
from matplotlib.transforms import (
    Affine2D as Affine2D,
    BboxTransformTo as BboxTransformTo,
    Transform as Transform,
)

from typing import Any, Literal

class GeoAxes(Axes):
    class ThetaFormatter(Formatter):
        def __init__(self, round_to: float = ...) -> None: ...
        def __call__(self, x: float, pos: Any | None = ...): ...
    RESOLUTION: float
    def get_xaxis_transform(
        self, which: Literal["tick1", "tick2", "grid"] = ...
    ) -> Transform: ...
    def get_xaxis_text1_transform(
        self, pad: float
    ) -> tuple[
        Transform,
        Literal["center", "top", "bottom", "baseline", "center_baseline"],
        Literal["center", "left", "right"],
    ]: ...
    def get_xaxis_text2_transform(
        self, pad: float
    ) -> tuple[
        Transform,
        Literal["center", "top", "bottom", "baseline", "center_baseline"],
        Literal["center", "left", "right"],
    ]: ...
    def get_yaxis_transform(
        self, which: Literal["tick1", "tick2", "grid"] = ...
    ) -> Transform: ...
    def get_yaxis_text1_transform(
        self, pad: float
    ) -> tuple[
        Transform,
        Literal["center", "top", "bottom", "baseline", "center_baseline"],
        Literal["center", "left", "right"],
    ]: ...
    def get_yaxis_text2_transform(
        self, pad: float
    ) -> tuple[
        Transform,
        Literal["center", "top", "bottom", "baseline", "center_baseline"],
        Literal["center", "left", "right"],
    ]: ...
    # TODO adust set_yscale/set_xscale once Axes stubs written
    def set_yscale(self, *args, **kwargs) -> None: ...  # type: ignore
    def set_xlim(self, *args, **kwargs) -> tuple[float, float]: ...
    def set_ylim(self, *args, **kwargs) -> tuple[float, float]: ...
    def format_coord(self, lon: float, lat: float) -> str: ...
    def set_longitude_grid(self, degrees: float) -> None: ...
    def set_latitude_grid(self, degrees: float) -> None: ...
    def set_longitude_grid_ends(self, degrees: float) -> None: ...
    def get_data_ratio(self) -> float: ...
    def can_zoom(self) -> bool: ...
    def can_pan(self) -> bool: ...
    def start_pan(self, x, y, button) -> None: ...
    def end_pan(self) -> None: ...
    def drag_pan(self, button, key, x, y) -> None: ...

class _GeoTransform(Transform):
    input_dims: int
    output_dims: int
    def __init__(self, resolution: int) -> None: ...

class AitoffAxes(GeoAxes):
    name: str

    class AitoffTransform(_GeoTransform):
        def inverted(self) -> AitoffAxes.InvertedAitoffTransform: ...

    class InvertedAitoffTransform(_GeoTransform):
        def inverted(self) -> AitoffAxes.AitoffTransform: ...

class HammerAxes(GeoAxes):
    name: str

    class HammerTransform(_GeoTransform):
        def inverted(self) -> HammerAxes.InvertedHammerTransform: ...

    class InvertedHammerTransform(_GeoTransform):
        def inverted(self) -> HammerAxes.HammerTransform: ...

class MollweideAxes(GeoAxes):
    name: str

    class MollweideTransform(_GeoTransform):
        def inverted(self) -> MollweideAxes.InvertedMollweideTransform: ...

    class InvertedMollweideTransform(_GeoTransform):
        def inverted(self) -> MollweideAxes.MollweideTransform: ...

class LambertAxes(GeoAxes):
    name: str

    class LambertTransform(_GeoTransform):
        def __init__(
            self, center_longitude: float, center_latitude: float, resolution: int
        ) -> None: ...
        def inverted(self) -> LambertAxes.InvertedLambertTransform: ...

    class InvertedLambertTransform(_GeoTransform):
        def __init__(
            self, center_longitude: float, center_latitude: float, resolution: int
        ) -> None: ...
        def inverted(self) -> LambertAxes.LambertTransform: ...

    def __init__(
        self,
        *args,
        center_longitude: float = ...,
        center_latitude: float = ...,
        **kwargs
    ) -> None: ...
