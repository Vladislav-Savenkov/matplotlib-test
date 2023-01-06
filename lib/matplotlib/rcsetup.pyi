import ast
from matplotlib import cbook
from matplotlib._enums import CapStyle, JoinStyle
from matplotlib._fontconfig_pattern import parse_fontconfig_pattern
from matplotlib.cbook import ls_mapper
from matplotlib.colors import Colormap, is_color_like
from matplotlib._typing import Color, LineStyleType, MarkEveryType

from cycler import Cycler

from typing import Any, Callable, Iterable, Literal, TypeVar

interactive_bk: list[str]
non_interactive_bk: list[str]
all_backends: list[str]

T = TypeVar("T")

def _listify_validator(s: Callable[[Any], T]) -> Callable[[Any], list[T]]: ...

class ValidateInStrings:
    key: str
    ignorecase: bool
    valid: dict[str, str]
    def __init__(
        self,
        key: str,
        valid: Iterable[str],
        ignorecase: bool = ...,
        *,
        _deprecated_since: str | None = ...
    ) -> None: ...
    def __call__(self, s: Any) -> str: ...

def validate_any(s: Any) -> Any: ...
def validate_anylist(s: Any) -> list[Any]: ...
def validate_bool(b: Any) -> bool: ...
def validate_axisbelow(s: Any) -> bool | Literal["line"]: ...
def validate_dpi(s: Any) -> Literal["figure"] | float: ...
def validate_string(s: Any) -> str: ...
def validate_string_or_None(s: Any) -> str | None: ...
def validate_stringlist(s: Any) -> list[str]: ...
def validate_int(s: Any) -> int: ...
def validate_int_or_None(s: Any) -> int | None: ...
def validate_float(s: Any) -> float: ...
def validate_float_or_None(s: Any) -> float | None: ...
def validate_floatlist(s: Any) -> list[float]: ...
def validate_fonttype(s: Any) -> int: ...
def validate_backend(s: Any) -> str: ...
def validate_color_or_inherit(s: Any) -> Literal["inherit"] | Color: ...
def validate_color_or_auto(s: Any) -> Color | Literal["auto"]: ...
def validate_color_for_prop_cycle(s: Any) -> Color: ...
def validate_color(s: Any) -> Color: ...
def validate_colorlist(s: Any) -> list[Color]: ...
def _validate_color_or_linecolor(
    s: Any,
) -> Color | Literal["linecolor", "markerfacecolor", "markeredgecolor"] | None: ...
def validate_aspect(s: Any) -> Literal["auto", "equal"] | float: ...
def validate_fontsize_None(
    s: Any,
) -> Literal[
    "xx-small",
    "x-small",
    "small",
    "medium",
    "large",
    "x-large",
    "xx-large",
    "smaller",
    "larger",
] | float | None: ...
def validate_fontsize(
    s: Any,
) -> Literal[
    "xx-small",
    "x-small",
    "small",
    "medium",
    "large",
    "x-large",
    "xx-large",
    "smaller",
    "larger",
] | float: ...
def validate_fontsizelist(
    s: Any,
) -> list[
    Literal[
        "xx-small",
        "x-small",
        "small",
        "medium",
        "large",
        "x-large",
        "xx-large",
        "smaller",
        "larger",
    ]
    | float
]: ...
def validate_fontweight(
    s: Any,
) -> Literal[
    "ultralight",
    "light",
    "normal",
    "regular",
    "book",
    "medium",
    "roman",
    "semibold",
    "demibold",
    "demi",
    "bold",
    "heavy",
    "extra bold",
    "black",
] | int: ...
def validate_fontstretch(
    s: Any,
) -> Literal[
    "ultra-condensed",
    "extra-condensed",
    "condensed",
    "semi-condensed",
    "normal",
    "semi-expanded",
    "expanded",
    "extra-expanded",
    "ultra-expanded",
] | int: ...
def validate_font_properties(s: Any) -> dict[str, Any]: ...
def validate_whiskers(s: Any) -> list[float] | float: ...
def validate_ps_distiller(s: Any) -> None | Literal["ghostscript", "xpdf"]: ...
def validate_fillstyle(
    s: Any,
) -> Literal["full", "left", "right", "bottom", "top", "none"]: ...
def validate_fillstylelist(
    s: Any,
) -> list[Literal["full", "left", "right", "bottom", "top", "none"]]: ...
def validate_markevery(s: Any) -> MarkEveryType: ...
def _validate_linestyle(s: Any) -> LineStyleType: ...
def validate_markeverylist(s: Any) -> list[MarkEveryType]: ...
def validate_bbox(s: Any) -> Literal["tight", "standard"] | None: ...
def validate_sketch(s: Any) -> None | tuple[float, float, float]: ...
def validate_hatch(s: Any) -> str: ...
def validate_hatchlist(s: Any):
    list[str]

def validate_dashlist(s: Any):
    list[list[float]]

# TODO: copy cycler overloads?
def cycler(*args, **kwargs) -> Cycler: ...
def validate_cycler(s: Any) -> Cycler: ...
def validate_hist_bins(
    s: Any,
) -> Literal["auto", "sturges", "fd", "doane", "scott", "rice", "sqrt"] | int | list[
    float
]: ...
