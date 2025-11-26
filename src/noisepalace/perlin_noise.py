from __future__ import annotations

from typing import TYPE_CHECKING

import numpy

if TYPE_CHECKING:
    from typing import List, Optional, Tuple

    from numpy import float64, int8, int64
    from numpy.random import Generator
    from numpy.typing import NDArray


class PerlinNoise:
    def __init__(self, seed: Optional[int] = None) -> None:
        self.seed: Optional[int] = seed
        self.rng: Generator = numpy.random.default_rng(seed=seed)

        permutation = self.rng.integers(0, 256, size=256)
        self.permutation_table: NDArray[int64] = numpy.concatenate(
            [permutation, permutation]
        )

        angles = self.rng.integers(0, 361, size=360)
        gradient_forms: List[Tuple[float64, float64]] = [
            (
                numpy.sin(angle * numpy.pi / 180),
                numpy.cos(angle * numpy.pi / 180),
            )
            for angle in angles
        ]
        self.gradient_vectors: NDArray[float64] = numpy.array(
            gradient_forms,
            dtype=numpy.float64,
        )

        self.offsets: NDArray[int8] = numpy.array(
            ((-1, 1), (1, 1), (-1, -1), (1, -1)), dtype=numpy.int8
        )

    def _hash(self, x: int, y: int) -> int64:
        return self.permutation_table[  # pyright: ignore[reportReturnType]
            (self.permutation_table[x & 255] + y) & 255
        ]

    def _gradient(self, hash_value: int64) -> Tuple[int, int]:
        return self.gradient_vectors[hash_value % 360]

    def simple_2d(
        self,
        x: int,
        y: int,
        octave: int = 1,
        x_offset: float = 0.0,
        y_offset: float = 0.0,
        gradient_vec_offset: int = 0,
    ) -> None:
        center_point = numpy.array((x, y), numpy.int64)
        vertices: List[NDArray[int64]] = []

        for point in self.offsets:
            point: numpy.ndarray[Tuple[int, int]]
            vertices.append(center_point + point)

        for x, y in vertices:
            print(self._gradient(self._hash(x, y)))


if __name__ == "__main__":

    def func(x: int, y: int) -> float: ...

    # p = PerlinNoise(None, func)
    p = PerlinNoise(10)
    p.simple_2d(20, 30)
