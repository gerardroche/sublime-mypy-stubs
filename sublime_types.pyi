from typing import Any
from typing import Dict
from typing import List
from typing import Tuple
from typing import Union

DIP = float
Location = Tuple[str, str, Tuple[int, int]]
Point = int

# Recursive type hinting is not supported, so the List and Dict data structures
# are only properly defined up to two levels deep then they are set explicitly
# to accept Any.
ValueType = Union[
    str,
    int,
    float,
    bool,
    List[Union[
        str,
        int,
        float,
        bool,
        List[Any],
        Dict[str, Any]
    ]],
    Dict[
        str,
        Union[
            str,
            int,
            float,
            bool,
            List[Union[
                str,
                int,
                float,
                bool,
                List[Any],
                Dict[str, Any]
            ]],
            Dict[str, Any]
        ]
    ]
]

DictValueType = Dict[str, ValueType]

Vector = Tuple[DIP, DIP]
